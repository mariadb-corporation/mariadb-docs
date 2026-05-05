---
description: >-
  MariaDB ColumnStore does not support recursive Common Table Expressions on
  ColumnStore tables; the page documents three workarounds for cases requiring
  recursive query patterns.
---

# ColumnStore and Recursive CTE Limitations

The ColumnStore engine does not fully support recursive `Common Table Expressions (CTEs)`. Attempting to use recursive CTEs directly against ColumnStore tables typically results in an error.

The purpose of the following examples is to demonstrate three potential workarounds for this issue. The best fit for your organization will depend on your specific needs and ability to refactor queries and adjust your approach.

### Setup: Simulating an Org Chart

It simulates a simple organizational chart with employees and managers to illustrate the problem and the workarounds.

First, an InnoDB table for comparison:

```sql
CREATE TABLE employees_innodb (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    manager_id INT  -- references employees.id (nullable for top-level)
);

INSERT INTO employees_innodb (id, name, manager_id) VALUES
(1, 'CEO', NULL),
(2, 'VP of Sales', 1),
(3, 'Sales Rep A', 2),
(4, 'VP of Eng', 1),
(5, 'Eng A', 4),
(6, 'Eng B', 4);

```

Next, the ColumnStore table, which is where the CTE issue arises:

```sql
CREATE TABLE employees (
    id INT,
    name VARCHAR(100),
    manager_id INT  -- references employees.id (nullable for top-level)
) engine=columnstore;

INSERT INTO employees (id, name, manager_id) VALUES
(1, 'CEO', NULL),
(2, 'VP of Sales', 1),
(3, 'Sales Rep A', 2),
(4, 'VP of Eng', 1),
(5, 'Eng A', 4),
(6, 'Eng B', 4);

```

Attempting to run a recursive CTE directly on the `employees` (ColumnStore) table:

```sql
WITH RECURSIVE org_chart AS (
    -- Anchor: start with the top-level manager (CEO)
    SELECT id, name, manager_id, 0 AS level
    FROM employees
    WHERE id = 1

    UNION ALL

    -- Recursive step: find employees who report to the previous level
    SELECT e.id, e.name, e.manager_id, oc.level + 1
    FROM employees e
    JOIN org_chart oc ON e.manager_id = oc.id
)
SELECT * FROM org_chart;

```

This will result in the aforementioned error:

```sql
ERROR 1178 (42000): The storage engine for the table doesn't support Recursive CTE
```

### Workarounds

Here are three potential workarounds to address the recursive CTE limitation with MariaDB ColumnStore.

#### Option 1: Toggle ColumnStore Select Handler

You can temporarily bypass ColumnStore's `SELECT` handler by disabling it at the session level before executing your recursive CTE and then re-enabling it afterwards.

```sql
SET SESSION columnstore_select_handler=OFF;

WITH RECURSIVE org_chart AS (
    -- Anchor: start with the top-level manager (CEO)
    SELECT id, name, manager_id, 0 AS level
    FROM employees
    WHERE id = 1

    UNION ALL

    -- Recursive step: find employees who report to the previous level
    SELECT e.id, e.name, e.manager_id, oc.level + 1
    FROM employees e
    JOIN org_chart oc ON e.manager_id = oc.id
)
SELECT * FROM org_chart;

SET SESSION columnstore_select_handler=ON;

```

**Note:** This workaround may not always be effective, as its success can depend on the specific MariaDB server version and table definitions.

#### Option 2: Use Procedural Simulation via Temporary Table

If direct recursive CTEs fail or cause server crashes, you can simulate the recursive logic using a stored procedure and a temporary table. This approach iteratively populates the hierarchy.

First, create a temporary table to store the hierarchical data:

```sql
CREATE TABLE temp_org_chart (
    id INT,
    name VARCHAR(100),
    manager_id INT,
    level INT
);

-- Initialize the temporary table with the top-level employees
INSERT INTO temp_org_chart (id, name, manager_id, level)
SELECT id, name, manager_id, 0 AS level FROM employees WHERE manager_id IS NULL;
```

Next, create a stored procedure to iteratively populate the `temp_org_chart` table:

```sql
DELIMITER //

CREATE OR REPLACE PROCEDURE populate_org_chart()
BEGIN
  DECLARE v_level INT DEFAULT 1;
  DECLARE rows_inserted INT DEFAULT 1;

  -- Loop until no more rows are inserted, indicating the hierarchy is fully traversed
  WHILE rows_inserted > 0 DO

    -- Insert employees who report to the previous level
    INSERT INTO temp_org_chart (id, name, manager_id, level)
    SELECT e.id, e.name, e.manager_id, v_level
    FROM employees e
    JOIN temp_org_chart t ON e.manager_id = t.id
    WHERE t.level = v_level - 1
      AND NOT EXISTS (
          SELECT 1 FROM temp_org_chart x WHERE x.id = e.id
      );

    -- Get the number of rows inserted in the current iteration
    SET rows_inserted = ROW_COUNT();
    -- Increment the level for the next iteration
    SET v_level = v_level + 1;

  END WHILE;
END //

DELIMITER ;
```

Finally, call the stored procedure and then select from the populated temporary table:

```sql
CALL populate_org_chart();
SELECT * FROM temp_org_chart;
```

#### Option 3: Clone Data into InnoDB

Another robust workaround is to clone the structure and data of the ColumnStore table into an InnoDB table. Once the data resides in an InnoDB table, you can execute the recursive CTE as usual, as InnoDB fully supports them.

This approach involves a few steps, often executed via shell commands interacting with the MariaDB client:

1. **Extract and Modify `CREATE TABLE` Statement:** Use `SHOW CREATE TABLE` to get the definition of your ColumnStore table, then modify it to change the engine to `InnoDB` and give the new table a different name (e.g., `employees2`).

```sql
mariadb test -qsNe "SHOW CREATE TABLE employees" \
  | awk -F '\t' '{print $2}' \
  | sed -e 's/ENGINE=Columnstore/ENGINE=InnoDB/' \
        -e 's/CREATE TABLE `employees`/CREATE TABLE `employees2`/' \
  > create_employees2.sql

```

2. **Create New Table and Copy Data:** Execute the modified `CREATE TABLE` script to create the new InnoDB table, then insert all data from the original ColumnStore table into it.

```sql
mariadb test < create_employees2.sql
mariadb test -e "INSERT INTO employees2 SELECT * FROM employees"
```

3. **Run Recursive CTE on the InnoDB Table:** Now, with the data in `employees2` (an InnoDB table), you can run your recursive CTE without issues.

```sql
WITH RECURSIVE org_chart AS (
    -- Anchor: start with the top-level manager (CEO)
    SELECT id, name, manager_id, 0 AS level
    FROM employees2
    WHERE id = 1

    UNION ALL

    -- Recursive step: find employees who report to the previous level
    SELECT e.id, e.name, e.manager_id, oc.level + 1
    FROM employees2 e
    JOIN org_chart oc ON e.manager_id = oc.id
)
SELECT * FROM org_chart;
```

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
