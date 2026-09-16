---
description: >-
  Execute table operations in GridGain 9 with RecordView and KeyValueView, map
  user objects to table tuples, run criterion queries, and use the partition API.
---

# Table API

To execute table operations on a specific table, you need to get a specific view of the table and use one of its methods. You can only create new tables by using SQL API.

GridGain supports mapping user objects to table tuples. This ensures that objects created in any programming language can be used for key-value operations directly.

{% hint style="info" %}
The Java examples on this page use the thin client, which requires the `ignite-client` module. For repository and dependency configuration, see [Project Setup and Required Modules](project-setup.md).
{% endhint %}

## Table Views in GridGain 9

### Data Representation: Tuples vs POJOs/Records

When working with tables, GridGain offers two approaches: directly handling the data or mapping the data to classes. The direct data handling approach handles data tuples. Alternatively, when mapping data to classes, the data is converted to and from these classes as needed for database interactions.

### View Types: RecordView vs KeyValueView

When creating views, you can create a `RecordView` or `KeyValueView`. The primary difference between these view types is the API used.

In a RecordView, you create a single "record" that includes all the information about a row to be updated or retrieved from the table, and send this record to the server. This record should contain all the fields, including the primary key.

In a KeyValueView, you work with key-value mappings. Think of it as a dictionary where the key object contains the primary key field or fields, and the value object contains the data fields. This approach is useful when primary key is not directly related to the domain object thus you prefer not to add the primary key to it.

## Data Type Support

### Time and Date Data Types

Only JavaTime API is supported for working with table views. The following data types are not supported:

- `java.util.Date`
- `java.sql.Date`
- `java.sql.Time`
- `java.sql.Timestamp`

Use the following data types instead:

- `java.time.LocalDate`
- `java.time.LocalTime`
- `java.time.LocalDateTime`
- `java.time.Instant`

## Getting a Table Instance

First, get an instance of the table. To obtain an instance of table, use the `IgniteTables.table(String)` method. You can also use `IgniteTables.tables()` method to list all existing tables.

{% tabs %}
{% tab title="Java" %}
```java
IgniteTables tableApi = client.tables();
List<Table> existingTables = tableApi.tables();
Table firstTable = existingTables.get(0);
```
{% endtab %}

{% tab title=".NET" %}
```csharp
var existingTables = await Client.Tables.GetTablesAsync();
var firstTable = existingTables[0];

var myTable = await Client.Tables.GetTableAsync("MY_TABLE");
```
{% endtab %}

{% tab title="C++" %}
```cpp
using namespace ignite;

auto table_api = client.get_tables();
std::vector<table> existing_tables = table_api.get_tables();
table first_table = existing_tables.front();

std::optional<table> my_table = table_api.get_table("MY_TABLE);
```
{% endtab %}
{% endtabs %}

By default, if the schema name is not specified, the `PUBLIC` schema is used. If a qualified name is specified, the table is taken from the specified schema.

### Qualified Table Name Object

Instead of using a string to specify table name, you can create a `QualifiedName` object to hold a fully qualified table name. GridGain provides 2 methods for creating qualified names:

- You can parse the fully qualified table name with the `parse` method:

{% code title="Java" %}
```java
QualifiedName qualifiedTableName = QualifiedName.parse("PUBLIC.Person");
Table myTable = tableApi.table(qualifiedTableName);
```
{% endcode %}

- You can provide schema name and table name separately with the `of` method:

{% code title="Java" %}
```java
QualifiedName qualifiedTableName = QualifiedName.of("PUBLIC", "MY_TABLE");
Table myTable = tableApi.table(qualifiedTableName);
```
{% endcode %}

The provided names must follow SQL syntax rules for identifiers:

- Identifier must start from a character in the "Lu", "Ll", "Lt", "Lm", "Lo", or "Nl" Unicode categories or `U+0331` (underscore);
- Identifier characters (expect for the first one) may be `U+00B7` (middle dot), or any character in the "Mn", "Mc", "Nd", "Pc", or "Cf" Unicode categories;
- Identifiers that contain any other characters must be quoted with `U+2033` (double-quotes);
- Double-quote inside the identifier must be escaped with 2 double-quote characters.

Any unquoted names will be cast to upper case. In this case, `Person` and `PERSON` names are equivalent. To avoid this, add escaped quotes around the name. For example, `"Person"` will be encoded as a case-sensitive `Person` name. If the name contains the `U+2033` (double quote) symbol, it must be escaped as `""` (2 double quote symbols).

Foe example:

```java
// Case-insensitive table `MY_TABLE` in a case-insensitive `PUBLIC` schema.
QualifiedName.parse("public.my_table"))

// Case-sensitive table `my_table` in a case-sensitive `public` schema.
QualifiedName.parse("\"public\".\"my_table\""))

// Same as above, but with comma as separator that needs to be surrounded by quote characters.
QualifiedName.of("\"public\"","\"my_table\""))

// Case-sensitive name my"table.
QualifiedName.parse("\"my\"\"table\""));

// Case-sensitive table name `public.my_table` in a default schema.
QualifiedName.parse("\"public.my_table\""));
```

## Basic Table Operations

Once you've got a table you need to get a specific view to choose how you want to operate table records.

### Tuple Record View

A tuple record view. It can be used to operate table tuples directly. When retrieving data from tuple views, you can use a wide variety of methods to retrieve type-specific data stored in tuples. A full list of methods is available in the Tuple object [javadoc](https://www.gridgain.com/sdk/gridgain9/latest/javadoc/org/apache/ignite/table/Tuple.html).

{% tabs %}
{% tab title="Java" %}
```java
RecordView<Tuple> accounts = client.tables().table("accounts").recordView();

System.out.println("\nInserting a record into the 'accounts' table...");

Tuple newAccountTuple = Tuple.create()
        .set("accountNumber", 123456)
        .set("firstName", "John")
        .set("lastName", "Smith")
        .set("balance", 100.00d);

accounts.insert(null, newAccountTuple);

System.out.println("\nRetrieving a record using RecordView API...");

Tuple accountNumberTuple = Tuple.create().set("accountNumber", 123456);

Tuple accountTuple = accounts.get(null, accountNumberTuple);

System.out.println(
        "\nRetrieved record:\n"
                + "    Account Number: " + accountTuple.intValue("accountNumber") + '\n'
                + "    Owner: " + accountTuple.stringValue("firstName") + " " + accountTuple.stringValue("lastName") + '\n'
                + "    Balance: $" + accountTuple.doubleValue("balance"));
```
{% endtab %}

{% tab title=".NET" %}
```csharp
IRecordView<IIgniteTuple> view = table.RecordBinaryView;

IIgniteTuple fullRecord = new IgniteTuple
{
  ["id"] = 42,
  ["name"] = "John Doe"
};

await view.UpsertAsync(transaction: null, fullRecord);

IIgniteTuple keyRecord = new IgniteTuple { ["id"] = 42 };
(IIgniteTuple value, bool hasValue) = await view.GetAsync(transaction: null, keyRecord);

Debug.Assert(hasValue);
Debug.Assert(value.FieldCount == 2);
Debug.Assert(value["id"] as int? == 42);
Debug.Assert(value["name"] as string == "John Doe");
```
{% endtab %}

{% tab title="C++" %}
```cpp
record_view<ignite_tuple> view = table.get_record_binary_view();

ignite_tuple record{
  {"id", 42},
  {"name", "John Doe"}
};

view.upsert(nullptr, record);
std::optional<ignite_tuple> res_record = view.get(nullptr, {"id", 42});

assert(res_record.has_value());
assert(res_record->column_count() == 2);
assert(res_record->get<std::int64_t>("id") == 42);
assert(res_record->get<std::string>("name") == "John Doe");
```
{% endtab %}
{% endtabs %}

### Record View

A record view [maps](https://www.gridgain.com/sdk/gridgain9/latest/javadoc/org/apache/ignite/table/mapper/package-summary.html) to a user-defined type and enables table operations on user objects which are mapped to table tuples.

Create the type converter:

```java
static class CityIdConverter implements TypeConverter<String, Integer> {

    @Override
    public String  toObjectType(Integer columnValue) {
        return columnValue.toString();
    }

    @Override
    public Integer toColumnType(String cityId) {
        return Integer.parseInt(cityId);
    }
}
```

Then build the mapper and get the `RecordView`:

```java
public static void main(String[] args) throws Exception {
    var mapper = Mapper.builder(Person.class)
            .automap()
            .map("cityId", "city_id", new CityIdConverter())
            .build();

    try (IgniteClient client = IgniteClient.builder()
            .addresses("127.0.0.1:10800")
            .build()
    ) {
        RecordView<Person> view = client.tables()
                .table("person")
                .recordView(mapper);

        Person myPerson = new Person(2, "2", "John Doe", 40, "Apache");

        view.upsert(null, myPerson);
    }
}
```

Perform table operations on your custom objects mapped to table tuples:

{% tabs %}
{% tab title="Java" %}
```java
RecordView<Account> accounts = client.tables()
        .table("accounts")
        .recordView(Account.class);

System.out.println("\nInserting a record into the 'accounts' table...");

Account newAccount = new Account(
        123456,
        "John",
        "Smith",
        100.00d
);

accounts.insert(null, newAccount);

System.out.println("\nRetrieving a record using RecordView API...");

Account account = accounts.get(null, new Account(123456));

System.out.println(
        "\nRetrieved record:\n"
            + "    Account Number: " + account.accountNumber + '\n'
            + "    Owner: " + account.firstName + " " + account.lastName + '\n'
            + "    Balance: $" + account.balance);
```
{% endtab %}

{% tab title=".NET" %}
```csharp
var pocoView = table.GetRecordView<Poco>();
await pocoView.UpsertAsync(transaction: null, new Poco(42, "John Doe"));
var (value, hasValue) = await pocoView.GetAsync(transaction: null, new Poco(42));

Debug.Assert(hasValue);
Debug.Assert(value.Name == "John Doe");

public record Poco(long Id, string? Name = null);
```
{% endtab %}

{% tab title="C++" %}
```cpp
record_view<person> view = table.get_record_view<person>();

person record(42, "John Doe");

view.upsert(nullptr, record);
std::optional<person> res_record = view.get(nullptr, person{42});

assert(res.has_value());
assert(res->id == 42);
assert(res->name == "John Doe");
```
{% endtab %}
{% endtabs %}

### Key-Value Tuple View

A tuple key-value view. It can be used to operate table using key and value tuples separately. When retrieving data from tuple views, you can use a wide variety of methods to retrieve type-specific data stored in tuples. A full list of methods is available in the Tuple object [javadoc](https://www.gridgain.com/sdk/gridgain9/latest/javadoc/org/apache/ignite/table/Tuple.html).

{% tabs %}
{% tab title="Java" %}
```java
KeyValueView<Tuple, Tuple> kvView = client.tables().table("accounts").keyValueView();

System.out.println("\nInserting a key-value pair into the 'accounts' table...");

Tuple key = Tuple.create()
        .set("accountNumber", 123456);

Tuple value = Tuple.create()
        .set("firstName", "John")
        .set("lastName", "Smith")
        .set("balance", 100.00d);

kvView.put(null, key, value);

System.out.println("\nRetrieving a value using KeyValueView API...");

value = kvView.get(null, key);

System.out.println(
        "\nRetrieved value:\n"
                + "    Account Number: " + key.intValue("accountNumber") + '\n'
                + "    Owner: " + value.stringValue("firstName") + " " + value.stringValue("lastName") + '\n'
                + "    Balance: $" + value.doubleValue("balance"));
```
{% endtab %}

{% tab title=".NET" %}
```csharp
IKeyValueView<IIgniteTuple, IIgniteTuple> kvView = table.KeyValueBinaryView;

IIgniteTuple key = new IgniteTuple { ["id"] = 42 };
IIgniteTuple val = new IgniteTuple { ["name"] = "John Doe" };

await kvView.PutAsync(transaction: null, key, val);
(IIgniteTuple? value, bool hasValue) = await kvView.GetAsync(transaction: null, key);

Debug.Assert(hasValue);
Debug.Assert(value.FieldCount == 1);
Debug.Assert(value["name"] as string == "John Doe");
```
{% endtab %}

{% tab title="C++" %}
```cpp
key_value_view<ignite_tuple, ignite_tuple> kv_view = table.get_key_value_binary_view();

ignite_tuple key_tuple{{"id", 42}};
ignite_tuple val_tuple{{"name", "John Doe"}};

kv_view.put(nullptr, key_tuple, val_tuple);
std::optional<ignite_tuple> res_tuple = kv_view.get(nullptr, key_tuple);

assert(res_tuple.has_value());
assert(res_tuple->column_count() == 2);
assert(res_tuple->get<std::int64_t>("id") == 42);
assert(res_tuple->get<std::string>("name") == "John Doe");
```
{% endtab %}
{% endtabs %}

### Key-Value View

A key-value view with user objects. It can be used to operate table using key and value user objects mapped to table tuples.

{% tabs %}
{% tab title="Java" %}
```java
KeyValueView<AccountKey, Account> kvView = client.tables()
        .table("accounts")
        .keyValueView(AccountKey.class, Account.class);
System.out.println("\nInserting a key-value pair into the 'accounts' table...");

AccountKey key = new AccountKey(123456);

Account value = new Account(
        "John",
        "Smith",
        100.00d
);

kvView.put(null, key, value);

System.out.println("\nRetrieving a value using KeyValueView API...");

value = kvView.get(null, key);

System.out.println(
        "\nRetrieved value:\n"
            + "    Account Number: " + key.accountNumber + '\n'
            + "    Owner: " + value.firstName + " " + value.lastName + '\n'
            + "    Balance: $" + value.balance);
```
{% endtab %}

{% tab title=".NET" %}
```csharp
IKeyValueView<long, Poco> kvView = table.GetKeyValueView<long, Poco>();

await kvView.PutAsync(transaction: null, 42, new Poco(Id: 0, Name: "John Doe"));
(Poco? value, bool hasValue) = await kvView.GetAsync(transaction: null, 42);

Debug.Assert(hasValue);
Debug.Assert(value.Name == "John Doe");

public record Poco(long Id, string? Name = null);
```
{% endtab %}

{% tab title="C++" %}
```cpp
key_value_view<person, person> kv_view = table.get_key_value_view<person, person>();

kv_view.put(nullptr, {42}, {"John Doe"});
std::optional<person> res = kv_view.get(nullptr, {42});

assert(res.has_value());
assert(res->id == 42);
assert(res->name == "John Doe");
```
{% endtab %}
{% endtabs %}

## Working with Mappers

Mappers provide an abstraction layer that converts between your Java objects (POJOs or Records) and GridGain's internal tuple representation. They eliminate the need to manually pack and unpack data, allowing you to work directly with your domain objects.

When you create a `RecordView` or `KeyValueView` with a POJO class, you can use a mapper to handle the conversion between your objects and table data.

There are two types of mappers:

- **PojoMapper**: Maps individual object fields to columns (for POJOs and complex objects)
- **OneColumnMapper**: Maps an entire object to a single column (for simple types)

### Natively Supported Types

The following types are natively supported and can be used without custom type converters:

- **String**
- **Boolean**
- **UUID**
- **byte[]**
- **Numeric types**: **Byte**, **Short**, **Integer**, **Long**, **Float**, **Double**, **BigDecimal**
- **Date/Time types**: **LocalDate**, **LocalTime**, **LocalDateTime**, **Instant**

{% hint style="info" %}
OneColumnMapper does not support primitive types (int, long, boolean, etc.) due to Java Generics limitations. Use wrapper classes (Integer, Long, Boolean, etc.) instead.
{% endhint %}

All other types require a custom type converter.

### Creating Mappers

GridGain provides several ways to create mappers, from simple automatic mapping to fully customized configurations.

#### Automatic Class Mapping

You can use automatic class mapping to pass your POJO class directly to the view. GridGain automatically maps fields to columns by name:

```java
RecordView<Account> accountView = table.recordView(Account.class);

// For KeyValueView
KeyValueView<AccountKey, AccountValue> kvView =
    table.keyValueView(AccountKey.class, AccountValue.class);
```

{% hint style="info" %}
The default mapper copies every non-static, non-transient declared field to the tuple, including primitive zero values and `null` references. This affects how column `DEFAULT` clauses are applied — see [Column Defaults and the Default Mapper](#column-defaults-and-the-default-mapper).
{% endhint %}

#### Factory Mapper Methods

For more advanced scenarios, use the static factory methods on the `Mapper` interface:

```java
// Single column mapping
Mapper<String> nameMapper = Mapper.of(String.class, "name");
RecordView<String> nameView = table.recordView(nameMapper);

// Single column with type converter
Mapper<Status> statusMapper = Mapper.of(
    Status.class,
    "status",
    new StatusConverter()
);

// Explicit field-to-column pairs
Mapper<Person> customMapper = Mapper.of(
    Person.class,
    "id", "person_id",
    "fullName", "full_name",
    "age", "person_age"
);
```

#### Using MapperBuilder for Advanced Configuration

For complex mapping scenarios, use `MapperBuilder`:

```java
Mapper<Person> mapper = Mapper.builder(Person.class)
    .map("fieldName", "column_name")
    .map("age", "person_age")
    .map("cityId", "city_id")
    .build();

RecordView<Person> view = table.recordView(mapper);
```

{% hint style="warning" %}
A `MapperBuilder` instance cannot be reused after calling `build()`. Attempting to use it again will throw an `IllegalStateException`.
{% endhint %}

### Mapping Options

#### Automatic Field Mapping with automap()

The `automap()` method automatically maps all object fields to columns with matching names:

```java
Mapper<Person> mapper = Mapper.builder(Person.class)
    .automap()
    .build();
```

Behavior of `automap()`:

- Maps fields to columns with the same name in uppercase, consistently with SQL API.
- Static and transient fields are automatically excluded.
- Respects manual overriding (via `.map()` calls)

Example with using automap:

```java
public class Person {
    private int id;           // Maps to ID column
    private String name;      // Maps to NAME column
    private int age;          // Maps to AGE column

    public Person() {}
}

Mapper<Person> mapper = Mapper.builder(Person.class)
    .automap()
    .build();
```

#### Explicit Mapping

When field names do not match column names, use explicit mapping:

```java
Mapper<Person> mapper = Mapper.builder(Person.class)
    .map("fieldName", "column_name")
    .map("age", "person_age")
    .map("id", "person_id")
    .build();
```

You can also map multiple fields at once:

```java
Mapper<Person> mapper = Mapper.builder(Person.class)
    .map("id", "person_id",
         "age", "person_age",
         "name", "person_name")
    .build();
```

Explicit mapping supports fields from parent classes, allowing you to map inherited fields when working with class hierarchies:

```java
public class Account {
    private Integer accountId;
    private String accountType;

    public Account() {}
}

public class PremiumAccount extends Account {
    private String premiumLevel;

    public PremiumAccount() {}
}

// Map fields from both parent and child classes using Mapper.of()
Mapper<PremiumAccount> mapper = Mapper.of(
    PremiumAccount.class,
    "accountId", "account_id",        // Field from parent class
    "accountType", "account_type",    // Field from parent class
    "premiumLevel", "premium_level"   // Field from child class
);

// Or use MapperBuilder
Mapper<PremiumAccount> builderMapper = Mapper.builder(PremiumAccount.class)
    .map("accountId", "account_id")
    .map("accountType", "account_type")
    .map("premiumLevel", "premium_level")
    .build();
```

{% hint style="warning" %}
Shadowed fields (fields with the same name in both parent and child classes) are not supported. If a child class declares a field with the same name as a parent field, only the child's field will be accessible for mapping.
{% endhint %}

#### Using @Column Annotation

You can use the `@Column` annotation to specify column names directly in your POJO:

```java
import org.apache.ignite.catalog.annotations.Column;

public class Person {
    @Column("person_id")
    private int id;

    @Column("full_name")
    private String name;

    private int age;  // Maps to AGE by default

    public Person() {}
}

// Automatic mapping respects @Column annotations
Mapper<Person> mapper = Mapper.builder(Person.class)
    .automap()
    .build();
```

When mapped this way, column names specified in the annotation will be used.

### Column Defaults and the Default Mapper

When a table column has a `DEFAULT` value, the default is applied only when the column is missing from the row sent to the server. With the default mapper (used when you pass a POJO class directly to `recordView()` or `keyValueView()`, or when you call `automap()`), every non-static, non-transient field declared on the class is copied to the tuple via reflection, including primitive zero values (`0`, `false`) and `null` references. From the engine's perspective the column was supplied, so the column-level default is not applied.

Consider the following table:

```sql
CREATE TABLE table1 (id INT PRIMARY KEY, name VARCHAR, someInt INT DEFAULT 1);
```

The inserts below all populate `someInt` with the column default `1`, because the column is absent from the row in each case:

```java
// Value class without a field for the column with a default.
class PersonName {
    public String name;
    public PersonName(String name) { this.name = name; }
}

KeyValueView<Integer, PersonName> kvView = client.tables()
        .table("table1")
        .keyValueView(Integer.class, PersonName.class);

// SQL — column omitted from the column list.
client.sql().execute(null, "INSERT INTO table1 (id, name) VALUES (?, ?)", 1, "joe");

// RecordView — column not set on the tuple.
recordView.insert(null, Tuple.create().set("id", 2).set("name", "joe2"));

// KeyValueView — value class does not declare a field for the column.
kvView.put(null, 3, new PersonName("joe3"));
```

The next insert, however, writes `0` to `someInt` — not the column default `1`:

```java
class Person {
    public String name;
    public int someInt;            // declared but never assigned -> 0
    public Person(String name) { this.name = name; }
}

KeyValueView<Integer, Person> kvView = client.tables()
        .table("table1")
        .keyValueView(Integer.class, Person.class);

kvView.put(null, 4, new Person("joe4"));   // someInt = 0; the column default 1 is overridden
```

Because `someInt` is declared on `Person`, the default mapper copies it. Java has no `undefined`, so the mapper cannot distinguish "the user did not set this field" from "the user explicitly set this field to `0`".

The same applies to boxed types: if `someInt` were declared as `Integer` and left `null`, the mapper would write `null` to the column. If the column is nullable, you get `null`; if it is not nullable, the insert fails.

#### Letting the Column Default Apply

To have the engine apply the column default, the column must be absent from the row sent to the server. You have three options:

1. **Omit the field from the POJO.** Define a value class that does not declare the column, or mark the field `transient` — the default mapper skips static and transient fields:

```java
class Person {
    public String name;
    public transient int someInt;  // transient — not mapped to a column
    public Person(String name) { this.name = name; }
}

KeyValueView<Integer, Person> kvView = client.tables()
        .table("table1")
        .keyValueView(Integer.class, Person.class);

kvView.put(null, 5, new Person("joe5"));   // someInt picks up the column default 1
```

2. **Use a `Tuple` instead of a POJO.** With `RecordView<Tuple>` or `KeyValueView<Tuple, Tuple>`, only the columns you call `.set()` on are sent to the server.

3. **Provide a custom mapper.** Use `MapperBuilder` to map only the fields whose columns should be written, omitting columns that should pick up their default.

#### Setting an Explicit `null`

If a column is nullable and you want to write an explicit `null` rather than the column default, set it explicitly in SQL or in a `Tuple`:

```sql
INSERT INTO table1 (id, name, someInt) VALUES (1, 'joe', NULL);
```

```java
recordView.insert(null, Tuple.create()
        .set("id", 6)
        .set("name", "joe6")
        .set("someInt", null));
```

With a POJO, a `null` (or primitive zero) field is always written as that value and never replaced by the column default.

### Type Conversion

Type converters enable you to map fields whose types are incompatible with column types. They transform data when writing to and reading from the database.

The example below shows how you can map an object's field of String type to a column of Integer type:

```java
public class CityIdConverter implements TypeConverter<String, Integer> {
    @Override
    public String toObjectType(Integer columnValue) {
        return columnValue != null ? columnValue.toString() : null;
    }

    @Override
    public Integer toColumnType(String cityId) {
        return cityId != null ? Integer.parseInt(cityId) : null;
    }
}

// Use the converter
Mapper<Person> mapper = Mapper.builder(Person.class)
    .automap()
    .map("cityId", "city_id", new CityIdConverter())
    .build();
```

### Java Records

You can also map tables to Java records.

Records behave identically to traditional classes when mapping to tables, with one key difference: the `@Column` annotation is applied to constructor parameters instead of fields.

#### Requirements

Java records require Java 14 or later.

##### RecordView with Records

The simplest way to use records is with `RecordView`. Annotate the record's canonical constructor parameters with `@Column`:

```java
public record Person(
    @Column("id") Integer id,
    @Column("name") String name,
    @Column("age") Integer age
) {}

public static void main(String[] args) {
    try (IgniteClient client = IgniteClient.builder()
            .addresses("127.0.0.1:10800")
            .build()
    ) {
        RecordView<Person> view = client.tables()
                .table("person")
                .recordView(Person.class);

        Person person = new Person(1, "John Doe", 30);
        view.upsert(null, person);

        Person retrieved = view.get(null, new Person(1, null, null));
        System.out.println("Retrieved: " + retrieved.name());
    }
}
```

##### KeyValueView with Records

You can use records for both keys and values in `KeyValueView`:

```java
public record PersonKey(@Column("id") Integer id) {}

public record PersonValue(
    @Column("name") String name,
    @Column("age") Integer age
) {}

public static void main(String[] args) {
    try (IgniteClient client = IgniteClient.builder()
            .addresses("127.0.0.1:10800")
            .build()
    ) {
        KeyValueView<PersonKey, PersonValue> kvView = client.tables()
                .table("person")
                .keyValueView(PersonKey.class, PersonValue.class);

        PersonKey key = new PersonKey(1);
        PersonValue value = new PersonValue("John Doe", 30);

        kvView.put(null, key, value);

        PersonValue retrieved = kvView.get(null, key);
        System.out.println("Retrieved: " + retrieved.name());
    }
}
```

##### Creating Tables from Annotated Classes

You can create tables directly from annotated classes using the `@Table` annotation. This works for both Java records and POJOs.

###### Records

Create tables from record definitions:

```java
@Table(value = "person_table",
       zone = @Zone(value = "zone_default", replicas = 2, storageProfiles = "default"),
       indexes = @Index(value = "idx_name", columns = @ColumnRef("name")))
public record Person(
    @Id
    @Column("id") Integer id,

    @Column("name") String name,

    @Column(value = "age", nullable = true) Integer age
) {}

public static void main(String[] args) {
    try (IgniteClient client = IgniteClient.builder()
            .addresses("127.0.0.1:10800")
            .build()
    ) {
        org.apache.ignite.table.Table myTable =
            client.catalog().createTable(Person.class);

        RecordView<Person> view = myTable.recordView(Person.class);
        view.upsert(null, new Person(1, "John Doe", 30));
    }
}
```

For `KeyValueView`, provide both key and value record types:

```java
@Table(value = "person_table",
       zone = @Zone(value = "zone_default", replicas = 2, storageProfiles = "default"))
public static class PersonKey {
    @Id
    @Column("id") Integer id;
}

public record PersonKeyRecord(@Column("id") Integer id) {}

public record PersonValueRecord(
    @Column("name") String name,
    @Column("age") Integer age
) {}

public static void main(String[] args) {
    try (IgniteClient client = IgniteClient.builder()
            .addresses("127.0.0.1:10800")
            .build()
    ) {
        // Create table using annotated class for schema definition
        org.apache.ignite.table.Table myTable =
            client.catalog().createTable(PersonKey.class, PersonValueRecord.class);

        // Use records for data operations
        KeyValueView<PersonKeyRecord, PersonValueRecord> kvView =
            myTable.keyValueView(PersonKeyRecord.class, PersonValueRecord.class);

        kvView.put(null,
                   new PersonKeyRecord(1),
                   new PersonValueRecord("John Doe", 30));
    }
}
```

###### POJOs with Inheritance

You can create tables from POJO classes that extend other classes. Fields from both parent and child classes will be included in the table schema:

```java
import org.apache.ignite.catalog.annotations.*;

public class Account {
    @Id
    @Column("account_id")
    private Integer accountId;

    @Column("account_type")
    private String accountType;

    public Account() {}

    // Getters and setters
}

@Table(value = "premium_accounts",
       zone = @Zone(value = "zone_default", storageProfiles = "default"))
public class PremiumAccount extends Account {
    @Column("premium_level")
    private String premiumLevel;

    public PremiumAccount() {}

    // Getters and setters
}

public static void main(String[] args) {
    try (IgniteClient client = IgniteClient.builder()
            .addresses("127.0.0.1:10800")
            .build()
    ) {
        // Create table including fields from both Account and PremiumAccount
        org.apache.ignite.table.Table myTable =
            client.catalog().createTable(PremiumAccount.class);

        RecordView<PremiumAccount> view = myTable.recordView(PremiumAccount.class);

        PremiumAccount account = new PremiumAccount();
        account.setAccountId(1);
        account.setAccountType("business");
        account.setPremiumLevel("gold");

        view.upsert(null, account);
    }
}
```

The resulting table will include all annotated fields: `account_id`, `account_type`, and `premium_level`.

{% hint style="warning" %}
Shadowed fields (fields with the same name in both parent and child classes) are not supported.
{% endhint %}

## Criterion Queries

GridGain 9 provides the criterion queries that can be used to retrieve data from tables. Criterion queries work with any type of view, returning the appropriate data to the query specified.

The example below shows how you can execute a query within an implicit transaction:

{% code title="Java" %}
```java
try (Cursor<Entry<Tuple, Tuple>> cursor = table.keyValueView().query(
        null, // Implicit transaction
        // Query criteria
        and(
                columnValue("name", equalTo("John Doe")),
                columnValue("age", greaterThan(20))
        )
)) {
    // Process query results (keeping original cursor iteration pattern)
    // As an example, println all matched values.
    while (cursor.hasNext()) {
        printRecord(cursor.next());
    }
}
```
{% endcode %}

The comparison query are specified by using the `query()` method, and providing the comparison criteria in the `columnValue` method.

You can also specify the specific transaction to execute the query in to perform the query in that specific transaction.

{% code title="Java" %}
```java
try (Cursor<Entry<Tuple, Tuple>> cursor = table.keyValueView().query(
        transaction,
        // Query criteria
        and(
                columnValue("name", equalTo("John Doe")),
                columnValue("age", greaterThan(20))
        )
)) {
    // Process query results
    // As an example, println all matched values.
    while (cursor.hasNext()) {
        printRecord(cursor.next());
    }

    // Commit transaction if all operations succeed
    transaction.commit();
} catch (Exception e) {
    // Rollback transaction on error
    transaction.rollback();
    throw new RuntimeException("Transaction failed", e);
}
```
{% endcode %}

### Asynchronous Queries

You can also perform the query asynchronously by using the `queryAsync` method. This way the query is executed without blocking the thread. For example, you can execute the above query asynchronously:

{% code title="Java" %}
```java
public static void performQueryAsync(Table table) {
    System.out.println("[ Example 3 ] Performing asynchronous query");

    AsyncCursor<Entry<Tuple, Tuple>> result = table.keyValueView().queryAsync(
                    null, // Implicit transaction
                    and(
                            columnValue("name", equalTo("John Doe")),
                            columnValue("age", greaterThan(20))
                    )
            )
            .join();

    for (Entry<Tuple, Tuple> tupleTupleEntry : result.currentPage()) {
        printRecord(tupleTupleEntry);
    }
}
```
{% endcode %}

This operation uses the `thenCompose()` method to handle the query results asynchronously in the user-defined `fetchAllRowsInto()` method. Here is how this method may look like:

### Table TTL

When inserting values to the table, you can set expiration time for these values if TTL is enabled in the table. You can set the TTL by using the [CREATE TABLE](../sql-reference/ddl.md#create-table) or [ALTER TABLE](../sql-reference/ddl.md#alter-table-if-exists-table-set-expire-at) statements.

When adding data to the table, it is enough to put the desired TTL timestamp in the TTL column.

### Comparison Expressions

The following expressions are supported in criterion queries:

| Expression | Description | Example |
|---|---|---|
| `equalTo` | Checks if the object is equal to the value. | `columnValue("City", equalTo("New York"))` |
| `notEqualTo` | Checks if the object is not equal to the value. | `columnValue("City", notEqualTo("New York"))` |
| `greaterThan` | Checks if the object is greater than the value. | `columnValue("Salary", greaterThan(10000))` |
| `greaterThanOrEqualTo` | Checks if the object is greater than or equal to the value. | `columnValue("Salary", greaterThanOrEqualTo(10000))` |
| `lessThan` | Checks if the object is less than the value. | `columnValue("Salary", lessThan(10000))` |
| `lessThanOrEqualTo` | Checks if the object is less than or equal to the value. | `columnValue("Salary", lessThanOrEqualTo(10000))` |
| `nullValue` | Checks if the object is null. | `columnValue("City", nullValue()` |
| `notNullValue` | Checks if the object is not null. | `columnValue("City", notNullValue())` |
| `in` | Checks if the object is in the collection. | `columnValue("City", in("New York", "Washington"))` |
| `notIn` | Checks if the object is not in the collection. | `columnValue("City", notIn("New York", "Washington"))` |

### Comparison Operators

The following operators are supported in criterion queries:

| Operator | Description | Example |
|---|---|---|
| `not` | Negates the condition. | `not(columnValue("City", equalTo("New York")))` |
| `and` | Used to evaluate multiple conditions at the same time. | `and(columnValue("City", equalTo("New York")), columnValue("Salary", greaterThan(10000)))` |
| `or` | Used to evaluate for at least one matching condition. | `or(columnValue("City", equalTo("New York")), columnValue("Salary", greaterThan(10000)))` |

### Checking Key Existence

You can check if a table has an entry for a key without fetching the value in both `RecordView` and `KeyValueView`.

#### Single Key Check

The example below shows how you can check for an existence of a single key:

{% tabs %}
{% tab title="Java" %}
```java
RecordView<Tuple> accounts = client.tables().table("accounts").recordView();

Tuple accountKey = Tuple.create().set("accountNumber", 123456);
boolean present = accounts.contains(null, accountKey);

KeyValueView<Tuple, Tuple> kvView = client.tables().table("accounts").keyValueView();
boolean presentKv = kvView.contains(null, accountKey);
```
{% endtab %}

{% tab title=".NET" %}
```csharp
IRecordView<IIgniteTuple> view = table.RecordBinaryView;

IIgniteTuple key = new IgniteTuple { ["id"] = 42 };
bool present = await view.ContainsKeyAsync(transaction: null, key);

IKeyValueView<IIgniteTuple, IIgniteTuple> kvView = table.KeyValueBinaryView;
bool presentKv = await kvView.ContainsAsync(transaction: null, key);
```
{% endtab %}

{% tab title="C++" %}
```cpp
key_value_view<ignite_tuple, ignite_tuple> kv_view = table.get_key_value_binary_view();

ignite_tuple key_tuple{{"id", 42}};
bool present = kv_view.contains(nullptr, key_tuple);
```

{% hint style="info" %}
You can only check key existence for key-value views in C++.
{% endhint %}
{% endtab %}
{% endtabs %}

#### Multiple Keys

When checking multiple keys, the operation will only return `true` if all specified keys exist.

{% tabs %}
{% tab title="Java" %}
```java
RecordView<Tuple> accounts = client.tables().table("accounts").recordView();

List<Tuple> keys = List.of(
        Tuple.create().set("accountNumber", 123456),
        Tuple.create().set("accountNumber", 123457));

boolean allPresent = accounts.containsAll(null, keys);

// Asynchronous form.
CompletableFuture<Boolean> future = accounts.containsAllAsync(null, keys);
```
{% endtab %}

{% tab title=".NET" %}
```csharp
IRecordView<IIgniteTuple> view = table.RecordBinaryView;

IIgniteTuple[] keys =
{
    new IgniteTuple { ["id"] = 42 },
    new IgniteTuple { ["id"] = 43 }
};

bool allPresent = await view.ContainsAllKeysAsync(transaction: null, keys);

// Also available on IKeyValueView<TK, TV>.
IKeyValueView<IIgniteTuple, IIgniteTuple> kvView = table.KeyValueBinaryView;
bool allPresentKv = await kvView.ContainsAllKeysAsync(transaction: null, keys);
```
{% endtab %}

{% tab title="C++" %}
Not supported in C++.
{% endtab %}
{% endtabs %}

## Partition API

To retrieve a partition `id`, you need to pass the corresponding `key` value and use the following [method](https://www.gridgain.com/sdk/gridgain9/latest/javadoc/org/apache/ignite/table/partition/PartitionDistribution.html#partition\(org.apache.ignite.table.Tuple\)):

{% tabs %}
{% tab title="Java" %}
```java
Table table = client.tables().table("PUBLIC.Person");
RecordView<Tuple> personTableView = table.recordView();


PartitionDistribution partDistribution = table.partitionDistribution();
Partition partition = partDistribution.partitionAsync(Tuple.create().set("id", 1)).join();

long partitionId = partition.id();
```
{% endtab %}

{% tab title=".NET" %}
```csharp
var table = await Client.Tables.GetTableAsync("PUBLIC.Person");
var partitionDistribution = table!.PartitionDistribution;
IPartition partition = await partitionDistribution.GetPartitionAsync(new IgniteTuple { ["id"] = 1 });
long partitionId = partition.Id;
```
{% endtab %}
{% endtabs %}

As `PartitionManager` API is now deprecated and will be removed in upcoming releases, use `PartitionDistribution` [API](https://www.gridgain.com/sdk/gridgain9/latest/javadoc/org/apache/ignite/table/partition/PartitionDistribution.html) instead.

{% tabs %}
{% tab title="Java" %}
```java
Table table = client.tables().table("PUBLIC.Person");
PartitionDistribution partDistribution = table.partitionDistribution();
```
{% endtab %}

{% tab title=".NET" %}
```csharp
var table = await Client.Tables.GetTableAsync("PUBLIC.Person");
var partitionDistribution = table!.PartitionDistribution;
```
{% endtab %}
{% endtabs %}

For more details on data partitioning, see the following [article](../administrators-guide/storage/data-partitions.md).
