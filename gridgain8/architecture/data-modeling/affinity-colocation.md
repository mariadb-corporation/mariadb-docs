---
description: >-
  How affinity colocation stores related cache entries together on the same node
  so multi-entry queries run locally, and how to configure a custom affinity key.
---

# Affinity Colocation

In many cases it is beneficial to colocate different entries if they are often accessed together.
In this way, multi-entry queries are executed on one node (where the objects are stored).
This concept is known as _affinity colocation_.

Entries are assigned to partitions by the affinity function.
The objects that have the same affinity keys go to the same partitions.
This allows you to design your data model in such a way that related entries are stored together.
"Related" here refers to the objects that are in a parent-child relationship or objects that are often queried together.

For example, let's say you have `Person` and `Company` objects, and each person has the `companyId` field that indicates the company the person works for.
By specifying the `Person.companyId` and `Company.ID` as affinity keys, you ensure that all the persons working for the same company are stored on the same node, where the company object is stored as well.
Queries that request persons working for a specific company are processed on a single node.

You can also colocate a computation task with the data. See [Colocating Computations With Data](../../gridgain8-usage/colocating-computations.md).

## Configuring Affinity Key

If you do not specify the affinity key explicitly, the cache key is used as the default affinity key.
If you create your caches as SQL tables using SQL statements, the PRIMARY KEY is the default affinity key.

If you want to colocate data from two caches by a different field, you have to use a complex object as the key. That object usually contains a field that uniquely identifies the object in that cache and a field that you want to use for colocation.

There are several ways to configure a custom affinity field within the custom key, which are described below.

The following example illustrates how you can colocate the person objects with the company objects using a custom key class and the `@AffinityKeyMapped` annotation.

{% tabs %}
{% tab title="Java" %}
```java
public class AffinityCollocationExample {

    static class Person {
        private int id;
        private String companyId;
        private String name;

        public Person(int id, String companyId, String name) {
            this.id = id;
            this.companyId = companyId;
            this.name = name;
        }

        public int getId() {
            return id;
        }
    }

    static class PersonKey {
        private int id;

        @AffinityKeyMapped
        private String companyId;

        public PersonKey(int id, String companyId) {
            this.id = id;
            this.companyId = companyId;
        }
    }

    static class Company {
        private String id;
        private String name;

        public Company(String id, String name) {
            this.id = id;
            this.name = name;
        }

        public String getId() {
            return id;
        }
    }

    public void configureAffinityKeyWithAnnotation() {
        CacheConfiguration<PersonKey, Person> personCfg = new CacheConfiguration<PersonKey, Person>("persons");
        personCfg.setBackups(1);

        CacheConfiguration<String, Company> companyCfg = new CacheConfiguration<>("companies");
        companyCfg.setBackups(1);

        try (Ignite ignite = Ignition.start()) {
            IgniteCache<PersonKey, Person> personCache = ignite.getOrCreateCache(personCfg);
            IgniteCache<String, Company> companyCache = ignite.getOrCreateCache(companyCfg);

            Company c1 = new Company("company1", "My company");
            Person p1 = new Person(1, c1.getId(), "John");

            // Both the p1 and c1 objects will be cached on the same node
            personCache.put(new PersonKey(p1.getId(), c1.getId()), p1);
            companyCache.put("company1", c1);

            // Get the person object
            p1 = personCache.get(new PersonKey(1, "company1"));
        }
    }

    public void configureAffinitKeyWithAffinityKeyClass() {
        CacheConfiguration<AffinityKey<Integer>, Person> personCfg = new CacheConfiguration<AffinityKey<Integer>, Person>(
                "persons");
        personCfg.setBackups(1);

        CacheConfiguration<String, Company> companyCfg = new CacheConfiguration<String, Company>("companies");
        companyCfg.setBackups(1);

        Ignite ignite = Ignition.start();

        IgniteCache<AffinityKey<Integer>, Person> personCache = ignite.getOrCreateCache(personCfg);
        IgniteCache<String, Company> companyCache = ignite.getOrCreateCache(companyCfg);

        Company c1 = new Company("company1", "My company");
        Person p1 = new Person(1, c1.getId(), "John");

        // Both the p1 and c1 objects will be cached on the same node
        personCache.put(new AffinityKey<Integer>(p1.getId(), c1.getId()), p1);
        companyCache.put(c1.getId(), c1);

        // Get the person object
        p1 = personCache.get(new AffinityKey(1, "company1"));
    }

    public void configureAffinityKeyWithCacheKeyConfiguration() {
        CacheConfiguration<PersonKey, Person> personCfg = new CacheConfiguration<PersonKey, Person>("persons");
        personCfg.setBackups(1);

        // Configure the affinity key
        personCfg.setKeyConfiguration(new CacheKeyConfiguration("Person", "companyId"));

        CacheConfiguration<String, Company> companyCfg = new CacheConfiguration<String, Company>("companies");
        companyCfg.setBackups(1);

        Ignite ignite = Ignition.start();

        IgniteCache<PersonKey, Person> personCache = ignite.getOrCreateCache(personCfg);
        IgniteCache<String, Company> companyCache = ignite.getOrCreateCache(companyCfg);

        Company c1 = new Company("company1", "My company");
        Person p1 = new Person(1, c1.getId(), "John");

        // Both the p1 and c1 objects will be cached on the same node
        personCache.put(new PersonKey(1, c1.getId()), p1);
        companyCache.put(c1.getId(), c1);

        // Get the person object
        p1 = personCache.get(new PersonKey(1, "company1"));
    }
}
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
class Person
{
    public int Id { get; set; }
    public string Name { get; set; }
    public int CityId { get; set; }
    public string CompanyId { get; set; }
}

class PersonKey
{
    public int Id { get; set; }

    [AffinityKeyMapped] public string CompanyId { get; set; }
}

class Company
{
    public string Name { get; set; }
}

class AffinityCollocation
{
    public static void Example()
    {
        var personCfg = new CacheConfiguration
        {
            Name = "persons",
            Backups = 1,
            CacheMode = CacheMode.Partitioned
        };

        var companyCfg = new CacheConfiguration
        {
            Name = "companies",
            Backups = 1,
            CacheMode = CacheMode.Partitioned
        };

        using (var ignite = Ignition.Start())
        {
            var personCache = ignite.GetOrCreateCache<PersonKey, Person>(personCfg);
            var companyCache = ignite.GetOrCreateCache<string, Company>(companyCfg);

            var person = new Person {Name = "Vasya"};

            var company = new Company {Name = "Company1"};

            personCache.Put(new PersonKey {Id = 1, CompanyId = "company1_key"}, person);
            companyCache.Put("company1_key", company);
        }
    }
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
struct Person
{
    int32_t id;
    std::string name;
    int32_t cityId;
    std::string companyId;
};

struct PersonKey
{
    int32_t id;
    std::string companyId;
};

struct Company
{
    std::string name;
};

namespace ignite { namespace binary {
template<> struct BinaryType<Person> : BinaryTypeDefaultAll<Person>
{
    static void GetTypeName(std::string& dst)
    {
        dst = "Person";
    }

    static void Write(BinaryWriter& writer, const Person& obj)
    {
        writer.WriteInt32("id", obj.id);
        writer.WriteString("name", obj.name);
        writer.WriteInt32("cityId", obj.cityId);
        writer.WriteString("companyId", obj.companyId);
    }

    static void Read(BinaryReader& reader, Person& dst)
    {
        dst.id = reader.ReadInt32("id");
        dst.name = reader.ReadString("name");
        dst.cityId = reader.ReadInt32("cityId");
        dst.companyId = reader.ReadString("companyId");
    }
};

template<> struct BinaryType<PersonKey> : BinaryTypeDefaultAll<PersonKey>
{
    static void GetTypeName(std::string& dst)
    {
        dst = "PersonKey";
    }

    static void GetAffinityFieldName(std::string& dst)
    {
        dst = "companyId";
    }

    static void Write(BinaryWriter& writer, const PersonKey& obj)
    {
        writer.WriteInt32("id", obj.id);
        writer.WriteString("companyId", obj.companyId);
    }

    static void Read(BinaryReader& reader, PersonKey& dst)
    {
        dst.id = reader.ReadInt32("id");
        dst.companyId = reader.ReadString("companyId");
    }
};

template<> struct BinaryType<Company> : BinaryTypeDefaultAll<Company>
{
    static void GetTypeName(std::string& dst)
    {
        dst = "Company";
    }

    static void Write(BinaryWriter& writer, const Company& obj)
    {
        writer.WriteString("name", obj.name);
    }

    static void Read(BinaryReader& reader, Company& dst)
    {
        dst.name = reader.ReadString("name");
    }
};
}};  // namespace ignite::binary

int main()
{
    using namespace ignite;
    using namespace cache;

    IgniteConfiguration cfg;
    Ignite ignite = Ignition::Start(cfg);

    Cache<PersonKey, Person> personCache = ignite.GetOrCreateCache<PersonKey, Person>("person");
    Cache<std::string, Company> companyCache = ignite.GetOrCreateCache<std::string, Company>("company");

    Person person{};
    person.name = "Vasya";

    Company company{};
    company.name = "Company1";

    personCache.Put(PersonKey{1, "company1_key"}, person);
    companyCache.Put("company1_key", company);

    return 0;
}
```
{% endtab %}
{% tab title="SQL" %}
```sql
CREATE TABLE IF NOT EXISTS Person (
  id int,
  city_id int,
  name varchar,
  company_id varchar,
  PRIMARY KEY (id, company_id)
) WITH "template=partitioned,backups=1,affinity_key=company_id";

CREATE TABLE IF NOT EXISTS Company (
  id int,
  name varchar,
  PRIMARY KEY (id)
) WITH "template=partitioned,backups=1";
```
{% endtab %}
{% endtabs %}

You can also configure the affinity key field in the cache configuration by using the `CacheKeyConfiguration` class.

{% tabs %}
{% tab title="Java" %}
```java
public void configureAffinityKeyWithCacheKeyConfiguration() {
    CacheConfiguration<PersonKey, Person> personCfg = new CacheConfiguration<PersonKey, Person>("persons");
    personCfg.setBackups(1);

    // Configure the affinity key
    personCfg.setKeyConfiguration(new CacheKeyConfiguration("Person", "companyId"));

    CacheConfiguration<String, Company> companyCfg = new CacheConfiguration<String, Company>("companies");
    companyCfg.setBackups(1);

    Ignite ignite = Ignition.start();

    IgniteCache<PersonKey, Person> personCache = ignite.getOrCreateCache(personCfg);
    IgniteCache<String, Company> companyCache = ignite.getOrCreateCache(companyCfg);

    Company c1 = new Company("company1", "My company");
    Person p1 = new Person(1, c1.getId(), "John");

    // Both the p1 and c1 objects will be cached on the same node
    personCache.put(new PersonKey(1, c1.getId()), p1);
    companyCache.put(c1.getId(), c1);

    // Get the person object
    p1 = personCache.get(new PersonKey(1, "company1"));
}
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
var personCfg = new CacheConfiguration("persons")
{
    KeyConfiguration = new[]
    {
        new CacheKeyConfiguration
        {
            TypeName = nameof(Person),
            AffinityKeyFieldName = nameof(Person.CompanyId)
        } 
    }
};

var companyCfg = new CacheConfiguration("companies");

IIgnite ignite = Ignition.Start();

ICache<PersonKey, Person> personCache = ignite.GetOrCreateCache<PersonKey, Person>(personCfg);
ICache<string, Company> companyCache = ignite.GetOrCreateCache<string, Company>(companyCfg);

var companyId = "company_1";
Company c1 = new Company {Name = "My company"};
Person p1 = new Person {Id = 1, Name = "John", CompanyId = companyId};

// Both the p1 and c1 objects will be cached on the same node
personCache.Put(new PersonKey {Id = 1, CompanyId = companyId}, p1);
companyCache.Put(companyId, c1);

// Get the person object
p1 = personCache.Get(new PersonKey {Id = 1, CompanyId = companyId});
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

Instead of defining a custom key class, you can use the `AffinityKey` class, which is designed specifically for the purpose of using custom affinity mapping.

{% tabs %}
{% tab title="Java" %}
```java
public void configureAffinitKeyWithAffinityKeyClass() {
    CacheConfiguration<AffinityKey<Integer>, Person> personCfg = new CacheConfiguration<AffinityKey<Integer>, Person>(
            "persons");
    personCfg.setBackups(1);

    CacheConfiguration<String, Company> companyCfg = new CacheConfiguration<String, Company>("companies");
    companyCfg.setBackups(1);

    Ignite ignite = Ignition.start();

    IgniteCache<AffinityKey<Integer>, Person> personCache = ignite.getOrCreateCache(personCfg);
    IgniteCache<String, Company> companyCache = ignite.getOrCreateCache(companyCfg);

    Company c1 = new Company("company1", "My company");
    Person p1 = new Person(1, c1.getId(), "John");

    // Both the p1 and c1 objects will be cached on the same node
    personCache.put(new AffinityKey<Integer>(p1.getId(), c1.getId()), p1);
    companyCache.put(c1.getId(), c1);

    // Get the person object
    p1 = personCache.get(new AffinityKey(1, "company1"));
}
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
var personCfg = new CacheConfiguration("persons");
var companyCfg = new CacheConfiguration("companies");

IIgnite ignite = Ignition.Start();

ICache<AffinityKey, Person> personCache = ignite.GetOrCreateCache<AffinityKey, Person>(personCfg);
ICache<string, Company> companyCache = ignite.GetOrCreateCache<string, Company>(companyCfg);

var companyId = "company_1";
Company c1 = new Company {Name = "My company"};
Person p1 = new Person {Id = 1, Name = "John", CompanyId = companyId};

// Both the p1 and c1 objects will be cached on the same node
personCache.Put(new AffinityKey(1, companyId), p1);
companyCache.Put(companyId, c1);

// Get the person object
p1 = personCache.Get(new AffinityKey(1, companyId));
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
