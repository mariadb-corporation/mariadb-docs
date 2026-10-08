# Relational Databases: Basic Terms

The relational database model uses certain terms to describe its components:

* Data are the values kept in the database. On their own, the data means very little. `CA 684-213` is an example of data in a DMV (Division of Motor Vehicles) database.
* Information is processed data. For example, `CA 684-213` is the car registration number of a car belonging to Lyndon Manson, in a DMV database.
* A database is a collection of tables, also called entities.
* Each table is made up of records (the horizontal rows in the table, also called tuples). Each record should be unique, and can be stored in any order in the table.
* Each record is made up of fields (which are the vertical columns of the table, also called attributes). Basically, a record is one fact (for example, one customer or one sale).
* These fields can be of various types. MariaDB has many types (see [Data Types](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types) for a list), but generally types fall into three kinds: character, numeric, and date. For example, a customer name is a character field, a customer's birthday is a date field, and a customer's number of children is a numeric field.
* The range of allowed values for a field is called the domain (also called a field specification). For example, a credit card field may be limited to only the values `Mastercard`, `Visa` and `Amex`.
* A field is said to contain a null value when it contains nothing at all. Null fields can create complexities in calculations and have consequences for data accuracy. For this reason, many fields are specifically set not to contain null values.
* A key accesses specific records in a table.
* An index is a mechanism to improve the performance of a database. Indexes are often confused with keys. Indexes are, strictly speaking, part of the physical structure, and keys are part of the logical structure. You'll often see the terms used interchangeably, however, including throughout this documentation.
* A view is a virtual table made up of a subset of the actual tables.
* A one-to-one (1:1) relationship is where for each instance of the first table in a relationship, only one instance of the second table exists, An example of this would be a case where a chain of stores carries a vending machine. Each vending machine can only be in one store, and each store carries only one vending machine.

```mermaid
erDiagram
    accTitle: Vending machine to store relationship
    accDescr {
        Each vending machine appears in exactly one store, and each store carries
        exactly one vending machine. This is a one-to-one relationship.
    }
    VENDING_MACHINE ||--|| STORE : "appears in"
```

_A vending machine appears in exactly one store (one-to-one)._

* A one-to-many (1:N) relationship is where for each instance of the first table in a relationship, many instances of the second table exist. This is a common kind of relationship. An example is the relationship between a sculptor and their sculptures. Each sculptor may have created many sculptures, but each sculpture has been created by only one sculptor.

```mermaid
erDiagram
    accTitle: Sculptor to sculpture relationship
    accDescr {
        One sculptor sculpts many sculptures; each sculpture is made by exactly one
        sculptor. This is a one-to-many relationship.
    }
    SCULPTOR ||--o{ SCULPTURE : sculpts
```

_A sculptor sculpts many sculptures, but each sculpture has only one sculptor (one-to-many)._

* A many-to-many (M:N) relationship occurs where, for each instance of the first table, there are many instances of the second table, and for each instance of the second table, there are many instances of the first. For example, a student can have many lecturers, and a lecturer can have many students.

```mermaid
erDiagram
    accTitle: Student to lecturer relationship
    accDescr {
        Each student is taught by one or more lecturers, and each lecturer teaches
        one or more students. This is a many-to-many relationship.
    }
    STUDENT }|--|{ LECTURER : "is taught by"
```

_A student is taught by many lecturers, and a lecturer teaches many students (many-to-many)._
* A mandatory relationship exists where for each instance of the first table in a relationship, one or more instances of the second must exist. For example, for a music group to exist, there must exist at least one musician in that group.
* An optional relationship is where for each instance of the first table in a relationship, there may exist instances of the second. For example, if an author can be listed in the database without having written a book (in other words, a prospective author), that relationship is optional. The reverse isn't necessarily true though. For example, for a book to be listed, it must have an author.
* Data integrity refers to the condition where data is accurate, valid, and consistent. An example of poor integrity would be if a customer telephone number is stored differently in two different locations. Another is where a course record contains a reference to a lecturer who is no longer present at the school. [Database normalization](database-normalization/) is a technique that assists you to minimize the risk of these sorts of problems.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
