---
description: >-
  This guide provides a conceptual overview of database indexes, explaining
  their purpose, different types, and when to use them for optimization.
---

# Essentials of an Index Guide

_An index on `Last_Name` organizes the records by surname, enhancing search efficiency without altering the original table order. Indices can be created for any column, such as ID or first name, to enable quick lookups based on different criteria._

Imagine you've created a table with the following rows:

```
+----+------------+-----------+-------------------------+---------------------------+--------------+
| ID | First_Name | Last_Name | Position                | Home_Address              | Home_Phone   |
+----+------------+-----------+-------------------------+---------------------------+--------------+
|  1 | Mustapha   | Mond      | Chief Executive Officer | 692 Promiscuous Plaza     | 326-555-3492 |
|  2 | Henry      | Foster    | Store Manager           | 314 Savage Circle         | 326-555-3847 |
|  3 | Bernard    | Marx      | Cashier                 | 1240 Ambient Avenue       | 326-555-8456 |
|  4 | Lenina     | Crowne    | Cashier                 | 281 Bumblepuppy Boulevard | 328-555-2349 |
|  5 | Fanny      | Crowne    | Restocker               | 1023 Bokanovsky Lane      | 326-555-6329 |
|  6 | Helmholtz  | Watson    | Janitor                 | 944 Soma Court            | 329-555-2478 |
+----+------------+-----------+-------------------------+---------------------------+--------------+
```

Now, imagine you've been asked to return the home phone of Fanny Crowne. Without indexes, the only way to do it is to go through every row until you find the matching first name and surname. Now imagine there are millions of records and you can see that, even for a speedy database server, this is highly inefficient.

The answer is to sort the records. If they were stored in alphabetical order by surname, even a human could quickly find a record amongst a large number. But we can't sort the entire record by surname. What if we want to also look a record by ID, or by first name? The answer is to create separate indexes for each column we wish to sort by. An index simply contains the sorted data (such as surname), and a link to the original record.

For example, an index on Last\_Name:

```
+-----------+----+
| Last_Name | ID |
+-----------+----+
| Crowne    |  4 |
| Crowne    |  5 |
| Foster    |  2 |
| Marx      |  3 |
| Mond      |  1 |
| Watson    |  6 |
+-----------+----+
```

and an index on Position

```
+-------------------------+----+
| Position                | ID |
+-------------------------+----+
| Cashier                 |  3 |
| Cashier                 |  4 |
| Chief Executive Officer |  1 |
| Janitor                 |  6 |
| Restocker               |  5 |
| Store Manager           |  2 |
+-------------------------+----+
```

would allow you to quickly find the phone numbers of all the cashiers, or the phone number of the employee with the surname Marx, very quickly.

Where possible, you should create an index for each column that you search for records by, to avoid having the server read every row of a table.

See [CREATE INDEX](../reference/sql-statements/data-definition/create/create-index.md) and [Getting Started with Indexes](mariadb-indexes-guide.md) for more information.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
