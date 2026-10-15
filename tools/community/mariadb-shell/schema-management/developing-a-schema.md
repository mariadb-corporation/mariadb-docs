---
description: >-
  Write and evolve the development script of an MSM project, set the
  development version, try the script on a test server, and split large
  sections into files with SOURCE statements.
---

# Developing a Schema

All development happens in one file, the development script `development/<schema>_next.sql`. It always contains the complete definition of the next version of the schema, not a list of changes: when a table gets a new column, you change its `CREATE TABLE` statement. The changes from one release to the next are written separately, in the update script that MSM creates when you prepare a release. See [Preparing Releases](preparing-releases.md).

## Edit the Development Script

Write each kind of statement into its section, as described in [MSM Sections](msm-sections.md):

| What | Section |
| --- | --- |
| Tables and base data | 140 |
| Views, stored procedures and functions, triggers, events | 150 |
| Roles and privileges | 170 |
| REST endpoints | 180 |
| Helpers for the creation of the schema | 130, removed in 190 |

You can edit the file in any editor. In scripts, or from an AI agent, use the section functions, which replace the content of one section and leave the banners alone. Both take the path of the script file:

```python
dev_script = "/home/dev/projects/shop.msm.project/development/shop_next.sql"

msm.set.section_sql_content(dev_script, "140", """
CREATE TABLE `shop`.`product`(
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(100) NOT NULL,
    `price` DECIMAL(10,2)
);

INSERT INTO `shop`.`product`(`name`, `price`) VALUES ('Widget', 9.99);""")

print(msm.get.sql_content_from_section(dev_script, "140"))
```

`msm.set.section_sql_content()` fails if the section doesn't exist in the file, and `msm.get.sql_content_from_section()` returns the content without the banner and without the comment lines that directly follow it.

### Example

A development script for version 1.1.0 of the `shop` schema could contain the following in its main sections:

{% code title="Section 140" %}
```sql
CREATE TABLE `shop`.`product`(
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(100) NOT NULL,
    `price` DECIMAL(10,2)
);
```
{% endcode %}

{% code title="Section 150" %}
```sql
DELIMITER %%

CREATE OR REPLACE SQL SECURITY INVOKER VIEW `shop`.`product_names` AS
    SELECT `name` FROM `shop`.`product`%%

DELIMITER ;
```
{% endcode %}

{% code title="Section 170" %}
```sql
CREATE ROLE IF NOT EXISTS `shop_reader`;
GRANT SELECT ON `shop`.* TO `shop_reader`;
```
{% endcode %}

{% code title="Section 180" %}
```sql
CREATE OR REPLACE REST SERVICE /shop;
CREATE OR REPLACE REST SCHEMA /shop ON SERVICE /shop FROM `shop`;
CREATE OR REPLACE REST VIEW /product ON SERVICE /shop SCHEMA /shop AS `shop`.`product` {
    id: id @KEY,
    name: name,
    price: price
};
```
{% endcode %}

Sections 140 and 170 end up inside stored procedures in the deployment script, so they use plain statements ending in `;`. Section 150 runs at the top level and switches the delimiter to define its objects. REST statements require the REST metadata on the server; see [Deploying Schemas](deploying-schemas.md#rest-endpoints).

## Set the Development Version

The development version is stored in section 910 of the development script. A new project starts at `0.0.1`, and each release sets the version for the next round of development. To change it, for example to plan a bigger version step:

```python
msm.set.development_version(schema_project_path=project, version="2.0.0")
```

To read it, use `msm.get.project_information()`, which returns it as `currentDevelopmentVersion`.

## Try the Development Script

The development script is a complete create script, so you can run it on a test server to check it before a release, for example on a [sandbox](../sandbox-instances.md):

```bash
mariadb-shell root@localhost:3310 --sql -f ~/projects/shop.msm.project/development/shop_next.sql
```

The script creates the tables with `CREATE TABLE`, so it only runs on a server where the schema doesn't exist yet. Drop the test schema before you run it again. It doesn't work with [`SOURCE` statements](#split-sections-into-files), which only `msm.prepare_release()` resolves.

## Split Sections into Files

When a section grows large, move its statements into separate files and include them with `SOURCE` statements. When you prepare a release, MSM replaces each `SOURCE` statement with the content of the file, so the release snapshot and the deployment script are complete and don't depend on the files.

The syntax is:

```sql
SOURCE '<path>'[<start>:<end>];
```

* **`<path>`** is the path of the file, absolute or relative to the `development` folder.
* **`[<start>:<end>]`** selects the characters of the file to include, in the notation of Python slices. It is required. `[0:]` includes the whole file; `[53:]` leaves out the first 53 characters, for example a copyright header; `[53:-20]` also leaves out the last 20.
* The indentation of the `SOURCE` line is added to every included line.

Put the files into `development/sections/`, and name them after their section, so that their order is clear:

```text
development/
├── shop_next.sql
└── sections/
    ├── 140-10_tables.sql
    ├── 140-20_base_data.sql
    ├── 150-10_views.sql
    └── 150-20_procedures.sql
```

{% code title="Section 140 of shop_next.sql" %}
```sql
SOURCE './sections/140-10_tables.sql'[37:];
SOURCE './sections/140-20_base_data.sql'[37:];
```
{% endcode %}

The files follow the rules of the section that includes them: a file included in section 140 contains plain statements ending in `;`, and a file included in section 150 switches the delimiter for routine definitions.

{% hint style="warning" %}
Always write the slice. A `SOURCE` statement without one, or with `[:]`, isn't resolved: without a slice, it is copied into the release unchanged and the deployment fails with a syntax error, and `[:]` makes `msm.prepare_release()` fail with `invalid literal for int()`. Use `[0:]` to include a whole file.
{% endhint %}

## Next Step

When the development script has everything for the next version, prepare a release, as described in [Preparing Releases](preparing-releases.md).
