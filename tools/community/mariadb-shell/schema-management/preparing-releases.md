---
description: >-
  Release a version of an MSM schema project, write the update script from the
  previous release, and generate the deployment script that creates or
  upgrades the schema.
---

# Preparing Releases

A release turns the current development script into a numbered version that you can deploy. It takes three steps, in this order:

1. **Prepare the release** with `msm.prepare_release()`. MSM saves a snapshot of the development script under the version number and, from the second release on, creates an empty update script.
2. **Write the update script**, which changes the tables of the previous release to those of the new one.
3. **Generate the deployment script** with `msm.generate_deployment_script()`.

The first release of a project has no update script, so it needs only steps 1 and 3.

{% hint style="warning" %}
Write the update script before you generate the deployment script. The deployment script contains the update scripts. If you generate it while the update script is still empty, it creates the new version correctly on an empty server, but it upgrades existing schemas without changing their tables.
{% endhint %}

## Prepare a Release

```python
msm.prepare_release(schema_project_path=project, version="1.1.0", next_version="1.2.0")
```

The function does the following:

1. It replaces the `SOURCE` statements of the development script with the content of their files. See [Split Sections into Files](developing-a-schema.md#split-sections-into-files).
2. It writes the snapshot `releases/versions/<schema>_<version>.sql`, with the sections of the development script and the version number in section 910. Sections without statements are left out.
3. If an earlier release exists, it creates the update script `releases/updates/<schema>_<previous>_to_<version>.sql` from a template. The script contains the section banners, comments, and commented-out examples, but no statements.
4. It sets the development version in the development script to `next_version`.

It returns the paths of the files it wrote.

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `schema_project_path` | string | The [MSM working directory](schema-projects.md#the-msm-working-directory) | The project folder. |
| `version` | string | | The version to release. It must not be lower than the last released version. |
| `next_version` | string | | The development version after the release. It must be higher than `version`. |
| `allow_to_stay_on_same_version` | Boolean | `false` | Allow `next_version` to be the same as `version`, for example to release a version again after a correction. |
| `overwrite_existing` | Boolean | `false` | Replace an existing snapshot of the same version. |

In interactive mode, the function prompts for `version`, suggesting the current development version, and for `next_version`, suggesting the next patch version.

The function refuses a version that is lower than the last released one:

```text
ValueError: The given version 1.0.5 is lower than the last released version 1.1.0.
```

## Write the Update Script

The update script `releases/updates/<schema>_<previous>_to_<version>.sql` describes how to change a schema of the previous release into one of the new release. MSM can't derive these changes from the two snapshots; you write them. Compare the snapshots of both versions in `releases/versions/` to see what changed.

Write the statements into these sections of the update script:

| Section | What to write |
| --- | --- |
| 240 | `ALTER TABLE` statements, new `CREATE TABLE` statements, data changes with `INSERT`, `UPDATE`, or `DELETE`, and `DROP … IF EXISTS` for every object that the new version no longer has. Order matters, because each statement changes the state that the next one works on. |
| 270 | `REVOKE` for privileges and `DROP ROLE` for roles that the new version no longer has. |
| 230 | Helper routines for the update, with names starting with `msm_`. |
| 290 | `DROP … IF EXISTS` for the helpers of section 230. |

Leave out everything that sections 150 and 170 of the development script already define. New and changed views, routines, triggers, and events reach the server through section 150 of the new version, and new roles and privileges through section 170; both run on every deployment, after the table changes. The update script only needs what these sections can't express: table changes, and the removal of objects, privileges, and roles. Section 250 of the update script isn't used. See [MSM Sections](msm-sections.md#update-script).

Sections 240 and 270 become the bodies of stored procedures, so end each statement with `;`, don't use `DELIMITER`, and qualify names with the schema. See [Statements Inside Stored Procedures](msm-sections.md#statements-inside-stored-procedures).

```python
update_script = project + "/releases/updates/shop_1.0.0_to_1.1.0.sql"

msm.set.section_sql_content(update_script, "240", """
ALTER TABLE `shop`.`product` ADD COLUMN `price` DECIMAL(10,2);
UPDATE `shop`.`product` SET `price` = 9.99 WHERE `price` IS NULL;""")
```

If the new version takes a privilege away, for example `DELETE` from a role `shop_writer`, remove it from section 170 of the development script, and revoke it from existing schemas in section 270:

```python
msm.set.section_sql_content(update_script, "270", """
REVOKE DELETE ON `shop`.* FROM `shop_writer`;""")
```

Don't grant privileges in section 270. On an upgrade, it runs before section 170, so a role that is new in this version doesn't exist yet, and the `GRANT` fails the deployment with error 1133. See [Server Variables](msm-sections.md#server-variables).

The table definitions in the new snapshot and the result of the update script must match: a schema upgraded from the previous release must end up with the same tables as one created fresh with the new release. Test both paths before you deploy to production, as described in [Test a Release](#test-a-release).

## Generate the Deployment Script

```python
msm.generate_deployment_script(schema_project_path=project, version="1.1.0")
```

```text
/home/dev/projects/shop.msm.project/releases/deployment/shop_deployment_1.1.0.sql
```

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `schema_project_path` | string | The MSM working directory | The project folder. |
| `version` | string | | The released version to generate the script for. In interactive mode, the function prompts for it and suggests the last released version. |
| `overwrite_existing` | Boolean | `false` | Replace an existing deployment script of the same version. |

The deployment script creates the schema at the target version on a server that doesn't have it, and upgrades it from any earlier release on a server that has it. For the first release of a project, the deployment script is a copy of the release snapshot. From the second release on, MSM builds it from the snapshot of the target version and the update scripts of all earlier releases, as described in [MSM Sections](msm-sections.md#deployment-script).

Each pair of consecutive releases needs an update script. If one is missing, the generation fails, either with a message that names the missing upgrade step or with one that names the update script file that couldn't be found.

Deployment scripts are generated files. To change one, change the snapshot or the update scripts and generate it again with `overwrite_existing`. `msm.deploy_schema()` requires a deployment script for every released version, so generate one after each release.

## Test a Release

Before you deploy a release to production, check both ways that a server can reach it, for example on a [sandbox](../sandbox-instances.md):

1. Deploy the previous release, then the new one, and check that the upgrade works and keeps the data.
2. Drop the schema and deploy the new release on its own, and check that it creates the same schema.

```python
msm.deploy_schema(schema_project_path=project, version="1.0.0")
msm.deploy_schema(schema_project_path=project, version="1.1.0")
session.run_sql("DROP SCHEMA `shop`")
msm.deploy_schema(schema_project_path=project, version="1.1.0")
```

## Correct a Release

Released files are meant to stay unchanged once a release is deployed anywhere. Before that, you can correct a release:

* To change an update script, edit it and generate the deployment script again with `overwrite_existing`.
* To change the snapshot, correct the development script, set the development version back with `msm.set.development_version()`, and prepare the release again with `overwrite_existing`. Set `allow_to_stay_on_same_version` if `next_version` is the same as `version`.

After a release is deployed, make corrections in a new release instead.
