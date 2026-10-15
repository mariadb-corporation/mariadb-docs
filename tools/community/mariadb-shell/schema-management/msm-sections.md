---
description: >-
  Reference of the numbered MSM sections in development, update, and
  deployment scripts, which statements belong in each, and how the deployment
  script runs them.
---

# MSM Sections

MSM scripts are plain SQL files divided into numbered sections. Each section starts with a banner:

```sql
-- #############################################################################
-- MSM Section 140: Non-idempotent Schema Objects
-- -----------------------------------------------------------------------------
-- This section contains creation of schema TABLEs and the initialization of
-- base data (standard INSERTs).
-- #############################################################################
```

The section that a statement is in decides how the generated deployment script uses it: whether it runs only when the schema is created, only during an upgrade from a certain version, or on every deployment, and whether it runs inside a stored procedure. Put every statement into the section that matches its kind.

Edit sections with `msm.set.section_sql_content()` and read them with `msm.get.sql_content_from_section()`. These functions replace only the content below the banner, so the banners stay intact. You can also edit the files in an editor, as long as you keep the banners unchanged.

## Idempotent and Non-Idempotent Objects

The section model is built on one distinction:

* **Non-idempotent** changes alter state that can't simply be created again: the structure of tables and the data in them. `CREATE TABLE` can run only once, and an `ALTER TABLE` only on the version it was written for. The deployment script therefore runs these statements depending on the version that the server has.
* **Idempotent** objects can be created again at any time without loss: views, stored procedures and functions, triggers, events, and REST endpoints. They are written with `CREATE OR REPLACE` or with a `DROP … IF EXISTS` before the `CREATE`. The deployment script runs their complete definition for the target version on every deployment.

Because the idempotent objects are always created from the target version's definition, they never need version-specific update statements. Only tables, data, and authorization changes need them.

## Development Script

The development script `development/<schema>_next.sql` and the release snapshots in `releases/versions/` have the following sections. Sections marked as provided contain statements that MSM manages; leave them as they are.

| Section | Name | Contents |
| --- | --- | --- |
| 000 | Database Schema Development Script | A description of the script. In release snapshots, section 001. |
| 010 | Server Variable Settings | Provided. Saves `UNIQUE_CHECKS`, `FOREIGN_KEY_CHECKS`, and `SQL_MODE`, and sets them for the script. |
| 110 | Database Schema Creation | Provided. `CREATE SCHEMA IF NOT EXISTS` and `USE`. |
| 120 | Database Schema Version Creation Indication | Provided. Sets the `msm_schema_version` view to `0.0.0` while the schema is being created. |
| 130 | Creation of Helpers | Stored procedures and functions that the creation of the schema needs. Their names must start with `msm_`. |
| 140 | Non-idempotent Schema Objects | `CREATE TABLE` statements and `INSERT` statements for base data. |
| 150 | Idempotent Schema Objects | All other schema objects: views, stored procedures and functions, triggers, and events. |
| 170 | Authorization | `CREATE ROLE` and `GRANT` statements. |
| 180 | REST Service Definition | Optional. MariaDB REST Service endpoints. |
| 190 | Removal of Helpers | `DROP … IF EXISTS` for the helpers of section 130. |
| 910 | Database Schema Version | Provided. Sets the `msm_schema_version` view to the development version. |
| 920 | Server Variable Restoration | Provided. Restores the variables saved in section 010. |

## Update Script

The update scripts in `releases/updates/` describe the changes from one release to the next. They have the following sections:

| Section | Name | Contents |
| --- | --- | --- |
| 002 | Database Schema Update Script | A description of the script. |
| 010 | Server Variable Settings | Provided. |
| 220 | Database Schema Version Update Indication | Provided. |
| 230 | Creation of Update Helpers | Stored procedures and functions that the update needs. Their names must start with `msm_`, and they must be created with `CREATE OR REPLACE` or after a `DROP … IF EXISTS`. |
| 240 | Non-idempotent Schema Object Changes and All DROPs | `ALTER TABLE`, new tables, data changes, and every `DROP` of an object that the new version no longer has, including views, routines, triggers, and events. |
| 250 | Idempotent Schema Object Additions And Changes | Not used by the deployment script; see the note below. |
| 270 | Authorization | `REVOKE` and `DROP ROLE` for privileges and roles that the new version no longer has. New roles and privileges come from section 170, which runs on every deployment. |
| 290 | Removal of Update Helpers | `DROP … IF EXISTS` for the helpers of section 230. |
| 910 | Database Schema Version Definition | Provided. |
| 920 | Server Variable Restoration | Provided. |

{% hint style="info" %}
The deployment script doesn't include section 250. New and changed views, routines, triggers, and events reach the server through section 150 of the target version, which runs in full on every deployment. Define them in section 150 of the development script, not in section 250. A removed object is the only change that section 150 can't express, so put its `DROP … IF EXISTS` into section 240.
{% endhint %}

## Deployment Script

`msm.generate_deployment_script()` combines the release snapshot of the target version and the update scripts of all earlier releases into one deployment script. For the first release of a project, the deployment script is a copy of the release snapshot. From the second release on, it has the following structure:

| Section | Contents | Runs |
| --- | --- | --- |
| 003 | A description of the script. | |
| 010 | Server variable settings. | Always |
| 110 | `CREATE SCHEMA IF NOT EXISTS`. | Always |
| 330 | The helpers of section 130 of the target version and of section 230 of every update script. | Always |
| 340 | Stored procedures for the tables: `msm_create_<version>` with section 140 of the target version, and `msm_update_<from>_to_<to>` with section 240 of each update script. Then `msm_create_or_update`, which checks the schema and calls either the create procedure or the update procedures from the deployed version up to the target, one release after the other. The procedures are called and dropped. | Depends on the deployed version |
| 150 | Section 150 of the target version. | Always |
| 370 | Stored procedures for authorization: `msm_auth_<version>` with section 170 of the target version, and `msm_auth_<from>_to_<to>` with section 270 of each update script. On a new schema, only `msm_auth_<version>` runs. On an upgrade, the procedures for each step run first, then `msm_auth_<version>`. | Always |
| 180 | Section 180 of the target version. | Always |
| 390 | Section 290 of every update script, and section 190 of the target version. | Always |
| 910 | Sets the `msm_schema_version` view to the target version. | Always |
| 920 | Restores the server variables. | Always |

Empty sections are left out of the generated script.

This structure has the following consequences for the statements you write:

* **Section 170 runs on every deployment**, including upgrades, after the authorization changes of section 270. Write it so that it can run again: `CREATE ROLE IF NOT EXISTS`, and `GRANT` statements, which don't fail if the privilege exists. Because it runs on upgrades too, new roles and privileges reach existing schemas through it, just as new views reach them through section 150. Section 270 is needed only for what section 170 can't express: `REVOKE` and `DROP ROLE`. During a deployment, the session variable `@msm_schema_init` is `1` when the schema is created and `0` when it is upgraded, so that you can make statements depend on it.
* **Section 180 runs on every deployment.** Use `CREATE OR REPLACE REST …` statements.
* **While the update procedures run, the views and routines are still those of the deployed version.** Section 150 of the target version runs only after all table changes. An update step can't call a routine that only an intermediate version introduced; define what it needs as a helper in section 230.

## Statements Inside Stored Procedures

In the deployment script, sections 140 and 170 of the development script and sections 240 and 270 of the update scripts become the bodies of stored procedures. Statements in these sections must therefore follow the rules for stored procedures:

* End every statement with `;`. Don't use `DELIMITER`.
* Qualify object names with the schema name, for example `` `shop`.`product` ``. `USE` isn't allowed inside a stored procedure.
* Don't create stored procedures, functions, triggers, or events here. Put them into section 150, or into the helper sections.
* For DDL that depends on a condition, use `PREPARE` and `EXECUTE`.

The other sections run at the top level of the script. To create a stored procedure, function, trigger, or event there, switch the delimiter, as the templates do:

```sql
DELIMITER %%

CREATE OR REPLACE VIEW `shop`.`product_names` AS
    SELECT `name` FROM `shop`.`product`%%

DROP PROCEDURE IF EXISTS `shop`.`add_product`%%
CREATE PROCEDURE `shop`.`add_product`(IN product_name VARCHAR(100))
BEGIN
    INSERT INTO `shop`.`product`(`name`) VALUES (product_name);
END%%

DELIMITER ;
```

## Server Variables

Section 010 sets the following variables for the duration of the script, and section 920 restores them:

```sql
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,'
    'NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,'
    'NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION';
```

With `ONLY_FULL_GROUP_BY`, every column in the select list of a query with `GROUP BY` must be grouped or aggregated. MariaDB applies this rule more strictly than MySQL, because it doesn't accept columns that only depend on a grouped key. Write the views in section 150 accordingly.

`NO_AUTO_CREATE_USER` makes a `GRANT` to a role or user that doesn't exist fail with error 1133, so the deployment stops with an error instead of creating an account of that name. Create every role with `CREATE ROLE IF NOT EXISTS` in section 170 before you grant privileges to it.

## The Schema Version

MSM stores the version of a deployed schema in the view `msm_schema_version` inside the schema:

```sql
SELECT * FROM `shop`.`msm_schema_version`;
```

```text
+-------+-------+-------+
| major | minor | patch |
+-------+-------+-------+
|     1 |     1 |     0 |
+-------+-------+-------+
```

* A schema with this view is managed by MSM. MSM refuses to deploy to an existing schema of the same name without it.
* While a deployment creates or upgrades the schema, the view reports `0.0.0`. A schema that still reports `0.0.0` after a deployment ended was left behind by a deployment that failed.
* In the development script, the view's definition in section 910 holds the development version. Change it with `msm.set.development_version()` rather than by editing the file.

## Helper Routines

Sections 130 and 230 define stored procedures and functions that are needed only while the schema is created or upgraded, for example to move data between tables. Their names must start with `msm_`. Drop them again in sections 190 and 290 with `DROP … IF EXISTS`. The deployment script uses the `msm_` prefix as well: when it checks whether a schema is empty, it ignores routines whose names start with `msm_`.
