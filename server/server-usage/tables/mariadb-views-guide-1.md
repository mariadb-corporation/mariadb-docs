---
description: >-
  Discover how to create and manage views in MariaDB to simplify complex
  queries, restrict data access, and provide an abstraction layer over tables.
---

# Views

## A Tutorial Introduction

**Up-front warning:** This is the beginning of a very basic tutorial on views,\
based on my experimentation with them. This tutorial assumes that you've read\
the appropriate tutorials up to and including [More Advanced Joins](../../reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/joins/more-advanced-joins.md) (or that\
you understand the concepts behind them). This page is intended to give you a\
general idea of how views work and what they do, as well as some examples of\
when you could use them.

### Requirements for This Tutorial

In order to perform the SQL statements in this tutorial, you will need access\
to a MariaDB database and you will need the CREATE TABLE\
and CREATE VIEW privileges on this table.

## The Employee Database

First, we need some data we can perform our optimizations on, so we'll recreate\
the tables from the [More Advanced Joins](../../reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/joins/more-advanced-joins.md) tutorial, to\
provide us with a starting point. If you have already completed that tutorial\
and have this database already, you can skip ahead.

First, we create the table that will hold all of the employees and their\
contact information:

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
```

Next, we add a few employees to the table:

```sql
INSERT INTO `Employees` (`First_Name`, `Last_Name`, `Position`, `Home_Address`, `Home_Phone`)
VALUES
  ('Mustapha', 'Mond', 'Chief Executive Officer', '692 Promiscuous Plaza', '326-555-3492'),
  ('Henry', 'Foster', 'Store Manager', '314 Savage Circle', '326-555-3847'),
  ('Bernard', 'Marx', 'Cashier', '1240 Ambient Avenue', '326-555-8456'),
  ('Lenina', 'Crowne', 'Cashier', '281 Bumblepuppy Boulevard', '328-555-2349'),
  ('Fanny', 'Crowne', 'Restocker', '1023 Bokanovsky Lane', '326-555-6329'),
  ('Helmholtz', 'Watson', 'Janitor', '944 Soma Court', '329-555-2478');
```

Now, we create a second table, containing the hours which each employee clocked in and out during the week:

```sql
CREATE TABLE `Hours` (
  `ID` TINYINT(3) UNSIGNED NOT NULL,
  `Clock_In` DATETIME NOT NULL,
  `Clock_Out` DATETIME NOT NULL
) ENGINE=MyISAM;
```

Finally, although it is a lot of information, we add a full week of hours for\
each of the employees into the second table that we created:

```sql
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

## Working with the Employee Database

In this example, we are going to assist Human Resources by simplifying the\
queries that their applications need to perform. At the same time, it's going\
to enable us to abstract their queries from the database, which allows us more\
flexibility in maintaining it.

### Filtering by Name, Date and Time

In the previous tutorial, we looked at a JOIN query that displayed all of the\
lateness instances for a particular employee. In this tutorial, we are going to\
abstract that query somewhat to provide us with all lateness occurrences for\
all employees, and then standardize that query by making it into a view.

Our previous query looked like this:

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

The result:

```sql
+------------+-----------+---------------------+---------------------+
| First_Name | Last_Name | Clock_In            | Clock_Out           |
+------------+-----------+---------------------+---------------------+
| Helmholtz  | Watson    | 2005-08-09 07:03:44 | 2005-08-09 17:00:00 |
| Helmholtz  | Watson    | 2005-08-12 07:02:07 | 2005-08-12 16:58:23 |
+------------+-----------+---------------------+---------------------+
```

### Refining Our Query

The previous example displays to us all of Heimholtz's punch-in times that were\
after seven AM. We can see here that Heimholz has been late twice within this\
reporting period, and we can also see that in both instances, he either left\
exactly on time or he left early. Our company policy, however, dictates that\
late instances must be made up at the end of one's shift, so we want to exclude\
from our report anyone whose clock-out time was greater than 10 hours and one\
minute after their clock-in time.

```sql
SELECT
  `Employees`.`First_Name`,
  `Employees`.`Last_Name`,
  `Hours`.`Clock_In`,
  `Hours`.`Clock_Out`,
  (TIMESTAMPDIFF(MINUTE,`Hours`.`Clock_Out`,`Hours`.`Clock_In`) + 601) AS Difference
FROM `Employees`
INNER JOIN `Hours` USING (`ID`)
WHERE DATE_FORMAT(`Hours`.`Clock_In`, '%Y-%m-%d') >= '2005-08-08'
AND DATE_FORMAT(`Hours`.`Clock_In`, '%Y-%m-%d') <= '2005-08-12'
AND DATE_FORMAT(`Hours`.`Clock_In`, '%H:%i:%S') > '07:00:59'
AND TIMESTAMPDIFF(MINUTE,`Hours`.`Clock_Out`,`Hours`.`Clock_In`) > -601;
```

This gives us the following list of people who have violated our attendance policy:

```sql
+------------+-----------+---------------------+---------------------+------------+
| First_Name | Last_Name | Clock_In            | Clock_Out           | Difference |
+------------+-----------+---------------------+---------------------+------------+
| Mustapha   | Mond      | 2005-08-12 07:02:29 | 2005-08-12 16:59:12 |          4 |
| Henry      | Foster    | 2005-08-11 07:01:58 | 2005-08-11 17:00:45 |          2 |
| Henry      | Foster    | 2005-08-12 07:02:12 | 2005-08-12 16:58:57 |          4 |
| Bernard    | Marx      | 2005-08-09 07:01:10 | 2005-08-09 17:00:26 |          1 |
| Lenina     | Crowne    | 2005-08-12 07:01:09 | 2005-08-12 16:58:29 |          3 |
| Fanny      | Crowne    | 2005-08-11 07:01:26 | 2005-08-11 17:00:03 |          2 |
| Fanny      | Crowne    | 2005-08-12 07:02:15 | 2005-08-12 16:59:02 |          4 |
| Helmholtz  | Watson    | 2005-08-09 07:03:44 | 2005-08-09 17:00:00 |          4 |
| Helmholtz  | Watson    | 2005-08-12 07:02:07 | 2005-08-12 16:58:23 |          4 |
+------------+-----------+---------------------+---------------------+------------+
```

## The Utility of Views

We can see in the previous example that there have been several instances of\
employees coming in late and leaving early. Unfortunately, we can also see that\
this query is getting needlessly complex. Having all of this SQL in our\
application not only creates more complex application code, but also means that\
if we ever change the structure of this table we're going to have to change\
what is becoming a somewhat messy query. This is where views begin to show\
their usefulness.

### Creating the Employee Tardiness View

Creating a view is almost exactly the same as creating a SELECT statement, so\
we can use our previous SELECT statement in the creation of our new view:

```sql
CREATE SQL SECURITY INVOKER VIEW Employee_Tardiness AS 
SELECT
  `Employees`.`First_Name`,
  `Employees`.`Last_Name`,
  `Hours`.`Clock_In`,
  `Hours`.`Clock_Out`,
(TIMESTAMPDIFF(MINUTE,`Hours`.`Clock_Out`,`Hours`.`Clock_In`) + 601) as Difference
FROM `Employees`
INNER JOIN `Hours` USING (`ID`)
WHERE DATE_FORMAT(`Hours`.`Clock_In`, '%Y-%m-%d') >= '2005-08-08'
AND DATE_FORMAT(`Hours`.`Clock_In`, '%Y-%m-%d') <= '2005-08-12'
AND DATE_FORMAT(`Hours`.`Clock_In`, '%H:%i:%S') > '07:00:59'
AND TIMESTAMPDIFF(MINUTE,`Hours`.`Clock_Out`,`Hours`.`Clock_In`) > -601;
```

Note that the first line of our query contains the statement 'SQL SECURITY\
INVOKER' - this means that when the view is accessed, it runs with the same\
privileges that the person accessing the view has. Thus, if someone without\
access to our Employees table tries to access this view, they will get an\
error.

Other than the security parameter, the rest of the query is fairly self\
explanatory. We simply run 'CREATE VIEW AS' and then append any\
valid SELECT statement, and our view is created. Now if we do a SELECT from the\
view, we can see we get the same results as before, with much less SQL:

```sql
SELECT * FROM Employee_Tardiness;
```

```sql
+------------+-----------+---------------------+---------------------+------------+
| First_Name | Last_Name | Clock_In            | Clock_Out           | Difference |
+------------+-----------+---------------------+---------------------+------------+
| Mustapha   | Mond      | 2005-08-12 07:02:29 | 2005-08-12 16:59:12 |          5 |
| Henry      | Foster    | 2005-08-11 07:01:58 | 2005-08-11 17:00:45 |          3 |
| Henry      | Foster    | 2005-08-12 07:02:12 | 2005-08-12 16:58:57 |          5 |
| Bernard    | Marx      | 2005-08-09 07:01:10 | 2005-08-09 17:00:26 |          2 |
| Lenina     | Crowne    | 2005-08-12 07:01:09 | 2005-08-12 16:58:29 |          4 |
| Fanny      | Crowne    | 2005-08-09 07:02:12 | 2005-08-09 17:02:13 |          1 |
| Fanny      | Crowne    | 2005-08-11 07:01:26 | 2005-08-11 17:00:03 |          3 |
| Fanny      | Crowne    | 2005-08-12 07:02:15 | 2005-08-12 16:59:02 |          5 |
| Helmholtz  | Watson    | 2005-08-09 07:03:44 | 2005-08-09 17:00:00 |          5 |
| Helmholtz  | Watson    | 2005-08-12 07:02:07 | 2005-08-12 16:58:23 |          5 |
+------------+-----------+---------------------+---------------------+------------+
```

Now we can even perform operations on the table, such as limiting our results\
to just those with a Difference of at least five minutes:

```sql
SELECT * FROM Employee_Tardiness WHERE Difference >=5;
```

```sql
+------------+-----------+---------------------+---------------------+------------+
| First_Name | Last_Name | Clock_In            | Clock_Out           | Difference |
+------------+-----------+---------------------+---------------------+------------+
| Mustapha   | Mond      | 2005-08-12 07:02:29 | 2005-08-12 16:59:12 |          5 |
| Henry      | Foster    | 2005-08-12 07:02:12 | 2005-08-12 16:58:57 |          5 |
| Fanny      | Crowne    | 2005-08-12 07:02:15 | 2005-08-12 16:59:02 |          5 |
| Helmholtz  | Watson    | 2005-08-09 07:03:44 | 2005-08-09 17:00:00 |          5 |
| Helmholtz  | Watson    | 2005-08-12 07:02:07 | 2005-08-12 16:58:23 |          5 |
+------------+-----------+---------------------+---------------------+------------+
```

### Other Uses of Views

Aside from just simplifying our application's SQL queries, there are also other\
benefits that views can provide, some of which are only possible by using\
views.

#### Restricting Data Access

For example, even though our Employees database contains fields for Position,\
Home Address, and Home Phone, our query does not allow for these fields to be\
shown. This means that in the case of a security issue in the application (for\
example, an SQL injection attack, or even a malicious programmer), there is no\
risk of disclosing an employee's personal information.

#### Row-level Security

We can also define separate views to include a specific WHERE clause for\
security; for example, if we wanted to restrict a department head's access to\
only the staff that report to him, we could specify his identity in the view's\
CREATE statement, and he would then be unable to see any other department's\
employees, despite them all being in the same table. If this view is writeable and it is defined with the CASCADE clause, this restriction will also apply to writes. This is actually the only\
way to implement row-level security in MariaDB, so views play an important part\
in that area as well.

#### Pre-emptive Optimization

We can also define our views in such a way as to force the use of indexes, so\
that other, less-experienced developers don't run the risk of running\
un-optimized queries or JOINs that result in full-table scans and extended\
locks. Expensive queries, queries that SELECT \*, and poorly thought-out JOINs\
can not only slow down the database entirely, but can cause inserts to fail,\
clients to time out, and reports to error out. By creating a view that is\
already optimized and letting users perform their queries on that, you can\
ensure that they won't cause a significant performance hit unnecessarily.

#### Abstracting Tables

When we re-engineer our application, we sometimes need to change the database\
to optimize or accommodate new or removed features. We may, for example, want\
to [normalize](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/database-theory/database-normalization) our tables when they start getting too large and queries start\
taking too long. Alternately, we may be installing a new application with\
different requirements alongside a legacy application. Unfortunately, database\
redesign will tend to break backwards-compatibility with previous applications,\
which can cause obvious problems.

Using views, we can change the format of the underlying tables while still\
presenting the same table format to the legacy application. Thus, an\
application which demands username, hostname, and access time in string format\
can access the same data as an application which requires firstname, lastname,\
user@host, and access time in Unix timestamp format.

## Summary

Views are an SQL feature that can provide a lot of versatility in larger\
applications, and can even simplify smaller applications further. Just as\
stored procedures can help us abstract out our database logic, views can\
simplify the way we access data in the database, and can help un-complicate our\
queries to make application debugging easier and more efficient.

_The initial version of this article was copied, with permission, from_ [_Views\_(Basic_](https://hashmysql.org/wiki/Views_\(Basic\)) _on 2012-10-05._

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
