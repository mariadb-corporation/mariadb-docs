---
description: >-
  Spring Data R2DBC applications with MariaDB Connector/R2DBC require Maven,
  Entity classes for object mapping, and the spring-boot-starter-data-r2dbc
  dependency.
---

# Application Development with MariaDB/Connector/R2DBC (Spring Data)

## Overview

Development with MariaDB Connector/R2DBC (Spring) involves building (compiling), and running applications. An Entity class also needs to be created.

## Building Applications

When using Maven to manage your Java builds, running build downloads and installs the relevant JAR dependencies and compiles your project:

## Build the package:

```bash
$ mvn package
```

Run the application:

```bash
$ java -jar target/app.jar
```

## Code Example: Create an Entity

Spring Data R2DBC supports object mapping, which allows Java objects to map to rows in the database. This feature can be used to persist objects in the database and read objects from the database.

Before using object mapping, the entity class that models the database table must be defined. The entity class consists of fields matching the database table columns.

For example, entity class is shown below for the test.contact table defined in the [Setup for Examples](setup-for-connector-r2dbc-examples-spring-data.md), which contains the _id, first\_name, last\_name, and email columns_:

```java
// Imports the @Id annotation type, which demarcates an identifier.
import org.springframework.data.annotation.Id;

// This is an Entity class
// It has the same name as the text.contact table
public class Contact {

      // The class members correspond to columns
      // in the test.contact table
      private int id;
      private String first_name;
      private String last_name;
      private String email;

      // Constructor
      public Contact(int id, String first_name, String last_name, String email) {
         this.id = id;
         this.first_name = first_name;
         this.last_name = last_name;
         this.email = email;
      }

      // The @Id annotation indicates that this field
      // is the primary key column
      @Id
      public int getId() {
         return id;
      }

      public String getFirst_name() {
         return first_name;
      }

      public String getLast_name() {
         return last_name;
      }

      public String getEmail() {
         return email;
      }

      @Override
      public String toString() {
         return "Contact [id=" + id + ", first_name=" + first_name + ", last_name=" + last_name + ", email=" + email + "]";
      }
   }
```

* The entity class must have the same name as the database table it models.
* For the test.contact table, the entity class is called Contact.
* The entity class must declare an identifier (i.e., primary key) field by annotating the field declaration or its getter method declaration with @Id.

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>


{% @marketo/form formId="4316" %}
