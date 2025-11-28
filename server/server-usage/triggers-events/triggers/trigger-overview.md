# Trigger Overview

A trigger is a set of statements that run when, or are triggered by, an event that occurs on a table.

## Events

The event can be an `INSERT`, an `UPDATE`, or a `DELETE`. The trigger can be executed `BEFORE` or `AFTER` the event. A table can have multiple triggers defined for the same event and timing combination.

The [LOAD DATA INFILE](../../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) and [LOAD XML](../../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-xml.md) statements invoke `INSERT` triggers for each row that is being inserted.

The [REPLACE](../../../reference/sql-statements/data-manipulation/changing-deleting-data/replace.md) statement is executed with the following workflow:

* `BEFORE INSERT`;
* `BEFORE DELETE` (only if a row is being deleted);
* `AFTER DELETE` (only if a row is being deleted);
* `AFTER INSERT`.

The [INSERT ... ON DUPLICATE KEY UPDATE](../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert-on-duplicate-key-update.md) statement, when a row already exists, follows the following workflow:

* `BEFORE INSERT`;
* `BEFORE UPDATE`;
* `AFTER UPDATE`.

Otherwise, it works like a normal `INSERT` statement.

Note that [TRUNCATE TABLE](../../../reference/sql-statements/table-statements/truncate-table.md) does not activate any triggers.

## Triggers and Errors

With non-transactional storage engines, if a `BEFORE` statement produces an error, the statement isn't executed. Statements that affect multiple rows fail before inserting the current row.

With transactional engines, triggers are executed in the same transaction as the statement that invoked them.

If a warning is issued with the `SIGNAL` or `RESIGNAL` statement (that is, an error with an `SQLSTATE` starting with `'01'`), it is treated like an error.

## Creating a Trigger

Here's a simple example to demonstrate a trigger in action. Using these two tables as an example:

```sql
CREATE TABLE animals (id MEDIUMINT(9) 
NOT NULL AUTO_INCREMENT, 
name CHAR(30) NOT NULL, 
PRIMARY KEY (`id`));

CREATE TABLE animal_count (animals INT);

INSERT INTO animal_count (animals) VALUES(0);
```

We want to increment a counter each time a new animal is added. Here's what the trigger looks like:

```sql
CREATE TRIGGER increment_animal 
AFTER INSERT ON animals 
FOR EACH ROW 
UPDATE animal_count SET animal_count.animals = animal_count.animals+1;
```

The trigger has:

* a name (in this case, `increment_animal`),
* a trigger time (in this case, after the specified trigger event),
* a trigger event (an `INSERT`),
* a table with which it is associated (`animals`),
* a set of statements to run (here, just the one `UPDATE` statement).

`AFTER INSERT` specifies that the trigger runs _after_ an `INSERT`. The trigger could also be set to run _before_, and the statement causing the trigger could be a `DELETE` or an `UPDATE` as well. You can also have multiple triggers for an action. In this case, you can use `FOLLOWS | PRECEDES`` `_`other_trigger_name`_ to specify the order of the triggers.

The set of statements to run are the statements on the table of the trigger; therefore, columns/values that change are always just a column name or an expression like `NEW.`_`column_name`_. Table references of other tables must come from explicit table references.

Now, if we insert a record into the `animals` table, the trigger runs, incrementing the _`animal_count`_ table.

```sql
SELECT * FROM animal_count;
+---------+
| animals |
+---------+
|       0 |
+---------+

INSERT INTO animals (name) VALUES('aardvark');
INSERT INTO animals (name) VALUES('baboon');

SELECT * FROM animal_count;
+---------+
| animals |
+---------+
|       2 |
+---------+
```

For more details on the syntax, see [CREATE TRIGGER](create-trigger.md).

## Dropping Triggers

To drop a trigger, use the [DROP TRIGGER](../../../reference/sql-statements/data-definition/drop/drop-trigger.md) statement. Triggers are also dropped if the table with which they are associated is also dropped.

```sql
DROP TRIGGER increment_animal;
```

## Triggers Metadata

The [Information Schema TRIGGERS Table](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-triggers-table.md) stores information about triggers.

The [SHOW TRIGGERS](../../../reference/sql-statements/administrative-sql-statements/show/show-triggers.md) statement returns similar information.

The [SHOW CREATE TRIGGER](../../../reference/sql-statements/administrative-sql-statements/show/show-create-trigger.md) statement returns a `CREATE TRIGGER` statement that creates the given trigger.

## More Complex Triggers

Triggers can consist of multiple statements enclosed by a [BEGIN and END](../../../reference/sql-statements/programmatic-compound-statements/begin-end.md). If you're entering multiple statements on the command line, temporarily set a new delimiter so that you can use a semicolon to delimit the statements inside your trigger. See [Delimiters in the mariadb client](../../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md#delimiters) for more.

```sql
DROP TABLE animals;

UPDATE animal_count SET animals=0;

CREATE TABLE animals (id MEDIUMINT(9) NOT NULL AUTO_INCREMENT, 
name CHAR(30) NOT NULL, 
PRIMARY KEY (`id`)) 
ENGINE=InnoDB;

DELIMITER //
CREATE TRIGGER the_mooses_are_loose
AFTER INSERT ON animals
FOR EACH ROW
BEGIN
 IF NEW.name = 'Moose' THEN
  UPDATE animal_count SET animal_count.animals = animal_count.animals+100;
 ELSE 
  UPDATE animal_count SET animal_count.animals = animal_count.animals+1;
 END IF;
END; //

DELIMITER ;

INSERT INTO animals (name) VALUES('Aardvark');

SELECT * FROM animal_count;
+---------+
| animals |
+---------+
|       1 |
+---------+

INSERT INTO animals (name) VALUES('Moose');

SELECT * FROM animal_count;
+---------+
| animals |
+---------+
|     101 |
+---------+
```

## Trigger Errors

If a trigger contains an error and the engine is transactional, or it is a `BEFORE` trigger, the trigger will not run, and will prevent the original statement from running as well. If the engine is non-transactional, and it is an `AFTER` trigger, the trigger will not run, but the original statement will.

Here, we'll drop the above examples and then recreate the trigger with an error, a field that doesn't exist, first using the default [InnoDB](../../storage-engines/innodb/), a transactional engine, and then again using [MyISAM](../../storage-engines/myisam-storage-engine/), a non-transactional engine.

```sql
DROP TABLE animals;

CREATE TABLE animals (id MEDIUMINT(9) NOT NULL AUTO_INCREMENT, 
name CHAR(30) NOT NULL, 
PRIMARY KEY (`id`)) 
ENGINE=InnoDB;

CREATE TRIGGER increment_animal 
AFTER INSERT ON animals 
FOR EACH ROW 
UPDATE animal_count SET animal_count.id = animal_count_id+1;

INSERT INTO animals (name) VALUES('aardvark');
ERROR 1054 (42S22): Unknown column 'animal_count.id' in 'field list'

SELECT * FROM animals;
Empty set (0.00 sec)
```

And now the identical procedure, but with a MyISAM table.

```sql
DROP TABLE animals;

CREATE TABLE animals (id MEDIUMINT(9) NOT NULL AUTO_INCREMENT, 
name CHAR(30) NOT NULL, 
PRIMARY KEY (`id`)) 
ENGINE=MyISAM;

CREATE TRIGGER increment_animal 
AFTER INSERT ON animals 
FOR EACH ROW 
UPDATE animal_count SET animal_count.id = animal_count_id+1;

INSERT INTO animals (name) VALUES('aardvark');
ERROR 1054 (42S22): Unknown column 'animal_count.id' in 'field list'

SELECT * FROM animals;
+----+----------+
| id | name     |
+----+----------+
|  1 | aardvark |
+----+----------+
```

The following example shows how to use a trigger to validate data. The [SIGNAL](../../../reference/sql-statements/programmatic-compound-statements/signal.md) statement is used to intentionally produce an error if the email field is not a valid email. As the example shows, in that case, the new row is not inserted (because it is a `BEFORE` trigger).

```sql
CREATE TABLE user (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	first_name CHAR(20),
	last_name CHAR(20),
	email CHAR(100)
)
	ENGINE = MyISAM;

DELIMITER //
CREATE TRIGGER bi_user
  BEFORE INSERT ON user
  FOR EACH ROW
BEGIN
  IF NEW.email NOT LIKE '_%@_%.__%' THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Email field IS NOT valid';
  END IF;
END; //
DELIMITER ;

INSERT INTO user (first_name, last_name, email) VALUES ('John', 'Doe', 'john_doe.example.net');
ERROR 1644 (45000): Email field is not valid

SELECT * FROM user;
Empty set (0.00 sec)
```

## See Also

* [CREATE TRIGGER](create-trigger.md)
* [DROP TRIGGER](../../../reference/sql-statements/data-definition/drop/drop-trigger.md)
* [Information Schema TRIGGERS Table](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-triggers-table.md)
* [SHOW TRIGGERS](../../../reference/sql-statements/administrative-sql-statements/show/show-triggers.md)
* [SHOW CREATE TRIGGER](../../../reference/sql-statements/administrative-sql-statements/show/show-create-trigger.md)
* [Trigger Limitations](trigger-limitations.md)
* [Creative uses of triggers: Things you people wouldn't believe](https://www.youtube.com/watch?v=-O2up6Fr9M0) (video)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
