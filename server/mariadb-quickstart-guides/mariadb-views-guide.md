---
description: >-
  Discover how to create and use views to simplify complex queries, restrict
  data access, and present a specific perspective of your data.
---

# Creating & Using Views Guide

This guide introduces SQL Views in MariaDB, virtual tables based on the result-set of a stored query. Learn how views simplify complex queries, enhance data security by restricting access, and provide an abstraction layer over your database tables through practical examples.

### Prerequisites

* A basic understanding of SQL, particularly `JOIN` operations. (You may want to refer to guides like "Basic Joins Guide" or "More Advanced Joins" if available.)
* Access to a MariaDB database.
* Privileges to `CREATE TABLE` and `CREATE VIEW`.

### Setup: Example Employee Database

First, we'll create and populate two tables, `Employees` and `Hours`, to use in our examples. If you have already completed a tutorial using this database structure (e.g., from a "More Advanced Joins" guide), you might be able to skip this setup.

**Employees Table:**

{% code expandable="true" %}
```sql
CREATE TABLE `Employees` (
  `ID` TINYINT(3) UNSIGNED NOT NULL AUTO_INCREMENT,
  `First_Name` VARCHAR(25) NOT NULL,
  `Last_Name` VARCHAR(25) NOT NULL,
  `Position` VARCHAR(25) NOT NULL,
  `Home_Address` VARCHAR(50) NOT NULL,
  `Home_Phone` VARCHAR(12) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM;

INSERT INTO `Employees` (`First_Name`, `Last_Name`, `Position`, `Home_Address`, `Home_Phone`)
VALUES
  ('Mustapha', 'Mond', 'Chief Executive Officer', '692 Promiscuous Plaza', '326-555-3492'),
  ('Henry', 'Foster', 'Store Manager', '314 Savage Circle', '326-555-3847'),
  ('Bernard', 'Marx', 'Cashier', '1240 Ambient Avenue', '326-555-8456'),
  ('Lenina', 'Crowne', 'Cashier', '281 Bumblepuppy Boulevard', '328-555-2349'),
  ('Fanny', 'Crowne', 'Restocker', '1023 Bokanovsky Lane', '326-555-6329'),
  ('Helmholtz', 'Watson', 'Janitor', '944 Soma Court', '329-555-2478');
```
{% endcode %}

**Hours Table:**

{% code expandable="true" %}
```sql
CREATE TABLE `Hours` (
  `ID` TINYINT(3) UNSIGNED NOT NULL,
  `Clock_In` DATETIME NOT NULL,
  `Clock_Out` DATETIME NOT NULL
) ENGINE=MyISAM;

INSERT INTO `Hours`
VALUES ('1', '2005-08-08 07:00:42', '2005-08-08 17:01:36'),
  ('1', '2005-08-09 07:01:34', '2005-08-09 17:10:11'),
  ('1', '2005-08-10 06:59:56', '2005-08-10 17:09:29'),
  ('1', '2005-08-11 07:00:17', '2005-08-11 17:00:47'),
  ('1', '2005-08-12 07:02:29', '2005-08-12 16:59:12'),
  ('2', '2005-08-08 07:00:25', '2005-08-08 17:03:13'),
  ('2', '2005-08-09 07:00:57', '2005-08-09 17:05:09'),
  ('2', '2005-08-10 06:58:43', '2005-08-10 16:58:24'),
  ('2', '2005-08-11 07:01:58', '2005-08-11 17:00:45'),
  ('2', '2005-08-12 07:02:12', '2005-08-12 16:58:57'),
  ('3', '2005-08-08 07:00:12', '2005-08-08 17:01:32'),
  ('3', '2005-08-09 07:01:10', '2005-08-09 17:00:26'),
  ('3', '2005-08-10 06:59:53', '2005-08-10 17:02:53'),
  ('3', '2005-08-11 07:01:15', '2005-08-11 17:04:23'),
  ('3', '2005-08-12 07:00:51', '2005-08-12 16:57:52'),
  ('4', '2005-08-08 06:54:37', '2005-08-08 17:01:23'),
  ('4', '2005-08-09 06:58:23', '2005-08-09 17:00:54'),
  ('4', '2005-08-10 06:59:14', '2005-08-10 17:00:12'),
  ('4', '2005-08-11 07:00:49', '2005-08-11 17:00:34'),
  ('4', '2005-08-12 07:01:09', '2005-08-12 16:58:29'),
  ('5', '2005-08-08 07:00:04', '2005-08-08 17:01:43'),
  ('5', '2005-08-09 07:02:12', '2005-08-09 17:02:13'),
  ('5', '2005-08-10 06:59:39', '2005-08-10 17:03:37'),
  ('5', '2005-08-11 07:01:26', '2005-08-11 17:00:03'),
  ('5', '2005-08-12 07:02:15', '2005-08-12 16:59:02'),
  ('6', '2005-08-08 07:00:12', '2005-08-08 17:01:02'),
  ('6', '2005-08-09 07:03:44', '2005-08-09 17:00:00'),
  ('6', '2005-08-10 06:54:19', '2005-08-10 17:03:31'),
  ('6', '2005-08-11 07:00:05', '2005-08-11 17:02:57'),
  ('6', '2005-08-12 07:02:07', '2005-08-12 16:58:23');
```
{% endcode %}

### Building a Complex Query (Example: Employee Tardiness)

Let's say Human Resources needs a report on employees who are late (clock in after 7:00:59 AM) and do not make up the time at the end of their shift (work less than 10 hours and 1 minute).

Initial Query (Helmholtz's Lateness):

This query finds instances where Helmholtz was late within a specific week:

```sql
SELECT
  `Employees`.`First_Name`,
  `Employees`.`Last_Name`,
  `Hours`.`Clock_In`,
  `Hours`.`Clock_Out`
FROM `Employees`
INNER JOIN `Hours` ON `Employees`.`ID` = `Hours`.`ID`
WHERE `Employees`.`First_Name` = 'Helmholtz'
AND DATE_FORMAT(`Hours`.`Clock_In`, '%Y-%m-%d') >= '2005-08-08'
AND DATE_FORMAT(`Hours`.`Clock_In`, '%Y-%m-%d') <= '2005-08-12'
AND DATE_FORMAT(`Hours`.`Clock_In`, '%H:%i:%S') > '07:00:59';
```

**Output:**

```
+------------+-----------+---------------------+---------------------+
| First_Name | Last_Name | Clock_In            | Clock_Out           |
+------------+-----------+---------------------+---------------------+
| Helmholtz  | Watson    | 2005-08-09 07:03:44 | 2005-08-09 17:00:00 |
| Helmholtz  | Watson    | 2005-08-12 07:02:07 | 2005-08-12 16:58:23 |
+------------+-----------+---------------------+---------------------+
```

Refined Query (Policy Violators):

This query identifies all employees who were late and whose shift duration was less than 10 hours and 1 minute (601 minutes).

```sql
SELECT
  `Employees`.`First_Name`,
  `Employees`.`Last_Name`,
  `Hours`.`Clock_In`,
  `Hours`.`Clock_Out`,
  (601 - TIMESTAMPDIFF(MINUTE, `Hours`.`Clock_In`, `Hours`.`Clock_Out`)) AS Difference -- Corrected Difference Calculation
FROM `Employees`
INNER JOIN `Hours` USING (`ID`) -- Simplified JOIN condition
WHERE DATE_FORMAT(`Hours`.`Clock_In`, '%Y-%m-%d') BETWEEN '2005-08-08' AND '2005-08-12'
  AND TIME(`Hours`.`Clock_In`) > '07:00:59'
  AND TIMESTAMPDIFF(MINUTE, `Hours`.`Clock_In`, `Hours`.`Clock_Out`) < 601;
```

**Output of Refined Query (example structure):**

```
+------------+-----------+---------------------+---------------------+------------+
| First_Name | Last_Name | Clock_In            | Clock_Out           | Difference |
+------------+-----------+---------------------+---------------------+------------+
| Mustapha   | Mond      | 2005-08-12 07:02:29 | 2005-08-12 16:59:12 |          4 |
... (other rows matching the criteria)
+------------+-----------+---------------------+---------------------+------------+
```

### Creating and Using a View

The refined query is becoming complex. Storing this query logic in application code makes it harder to manage and means changes to table structures require application code changes. Views can simplify this.

A view is a virtual table based on the result-set of a stored query.

Creating the Employee\_Tardiness View:

We use the refined query to create a view. SQL SECURITY INVOKER means the view runs with the permissions of the user querying it.

```sql
CREATE SQL SECURITY INVOKER VIEW Employee_Tardiness AS
SELECT
  `Employees`.`First_Name`,
  `Employees`.`Last_Name`,
  `Hours`.`Clock_In`,
  `Hours`.`Clock_Out`,
  (601 - TIMESTAMPDIFF(MINUTE, `Hours`.`Clock_In`, `Hours`.`Clock_Out`)) AS Difference
FROM `Employees`
INNER JOIN `Hours` USING (`ID`)
WHERE DATE_FORMAT(`Hours`.`Clock_In`, '%Y-%m-%d') BETWEEN '2005-08-08' AND '2005-08-12'
  AND TIME(`Hours`.`Clock_In`) > '07:00:59'
  AND TIMESTAMPDIFF(MINUTE, `Hours`.`Clock_In`, `Hours`.`Clock_Out`) < 601;
```

Querying the View:

Now, retrieving the tardiness data is much simpler:

```sql
SELECT * FROM Employee_Tardiness;
```

This will produce the same results as the complex "Refined Query" above.

You can also apply further conditions when querying the view:

```sql
SELECT * FROM Employee_Tardiness WHERE Difference >= 5;
```

**Output (example structure, showing those at least 5 minutes short):**

```
+------------+-----------+---------------------+---------------------+------------+
| First_Name | Last_Name | Clock_In            | Clock_Out           | Difference |
+------------+-----------+---------------------+---------------------+------------+
| Mustapha   | Mond      | 2005-08-12 07:02:29 | 2005-08-12 16:59:12 |          5 |
... (other rows where Difference >= 5)
+------------+-----------+---------------------+---------------------+------------+
```

### Other Benefits and Uses of Views

* **Simplifying Complex Queries:** As demonstrated, views hide complex joins and calculations.
* **Restricting Data Access (Column-Level Security):** Views can expose only a subset of columns from underlying tables, preventing users or applications from seeing sensitive information (e.g., `Home_Address`, `Home_Phone` were not included in our `Employee_Tardiness` view).
* **Implementing Row-Level Security:** A view can include a `WHERE` clause that filters rows based on the user querying it or other criteria, effectively providing row-level access control. For updatable views, defining them with `WITH CHECK OPTION` (or the similar effect of a `CASCADE` clause mentioned in original text, usually `WITH CASCADED CHECK OPTION`) can ensure that `INSERT`s or `UPDATE`s through the view adhere to the view's `WHERE` clause conditions.
* **Pre-emptive Optimization:** Complex, frequently used queries can be defined as views with optimal join strategies and indexing considerations. Other users or applications query the already optimized view, reducing the risk of running inefficient ad-hoc queries.
* **Abstracting Table Structures:** Views provide a consistent interface to applications even if the underlying table structures change (e.g., tables are normalized, split, or merged). The view definition can be updated to map to the new structure, while applications continue to query the unchanged view.

### Summary of View Advantages

Views offer a powerful way to:

* **Simplify data access:** Make complex queries easier to write and understand.
* **Abstract database logic:** Separate application code from the complexities of the database schema.
* **Enhance security:** Control access to specific rows and columns.
* **Improve maintainability:** Changes to underlying tables can often be managed by updating the view definition without altering application queries.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
