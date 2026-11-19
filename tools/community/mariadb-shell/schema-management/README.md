---
description: >-
  Manage a MariaDB database schema across its lifecycle with the msm global
  object of MariaDB Shell, from the first version through releases to
  deployments that create or upgrade the schema.
icon: code-branch
---

# Schema Management

<!--
  SYNCED: this page is maintained in mariadb-corporation/mariadb-shell, under docs-ref/content/,
  and copied one way into mariadb-docs (tools/community/mariadb-shell/).
  Make every change in mariadb-corporation/mariadb-shell. A change made in mariadb-docs or in the
  GitBook editor is overwritten by the next sync.
-->

MariaDB Schema Management (MSM) manages one database schema as a project on disk. You write the full definition of the schema in a single development script, release it under version numbers, and deploy each release with a generated script that creates the schema on a new server or upgrades it from any earlier release on an existing one.

MSM is included with MariaDB Shell as the built-in `msm` plugin. It works with plain SQL files that you keep in version control, and it needs a database server only for the deployment.

{% hint style="warning" %}
MSM is a preview feature. `msm.info()` reports it as `PREVIEW` and for testing purposes only.
{% endhint %}

## When to Use MSM

Use MSM for a schema that changes over time and is installed on more than one server, for example an application schema that exists on developer machines, in test environments, and in production, each at a different version. A single create script covers a new installation but not the upgrade of an existing one. MSM generates one deployment script per release that handles both cases.

## The Lifecycle

```text
 create project ──► develop ──► prepare release ──► write update script ──► generate deployment script ──► deploy
                       ▲                                                                                     │
                       └────────────────────────── next development version ◄──────────────────────────────┘
```

1. **Create a project.** `msm.create_new_project_folder()` creates the project folder with a development script for version `0.0.1`. See [Schema Projects](schema-projects.md).
2. **Develop.** You write the complete, current definition of the schema into the sections of the development script `development/<schema>_next.sql`: tables, views, routines, roles, and REST endpoints. See [Developing a Schema](developing-a-schema.md).
3. **Prepare a release.** `msm.prepare_release()` takes a snapshot of the development script under a version number. From the second release on, it also creates an empty update script from the previous release to the new one, and it raises the development version for the next round of development.
4. **Write the update script.** You add the statements that change existing tables from the previous release to the new one.
5. **Generate the deployment script.** `msm.generate_deployment_script()` combines the release and all update scripts into one script that creates the schema or upgrades it from any earlier release. See [Preparing Releases](preparing-releases.md).
6. **Deploy.** `msm.deploy_schema()` runs the deployment script on a server, optionally after taking a backup of the existing schema. See [Deploying Schemas](deploying-schemas.md).

The scripts are divided into numbered **MSM sections**. The section that a statement is in decides how the deployment script uses it, for example whether it runs once when a table is created or on every deployment. See [MSM Sections](msm-sections.md).

## Requirements

* A MariaDB Shell release package, installed as described in [Installation](../installation/README.md). The release packages include the `msm` plugin; a MariaDB Shell built from source doesn't.
* For deployments, a MariaDB server and an account that can create the schema and its objects. See [Deploying Schemas](deploying-schemas.md#required-privileges).

## Quick Start

The following example creates a project for a schema named `shop`, releases a first version with one table, and deploys it. Start MariaDB Shell connected to a server and switch to Python mode:

```bash
mariadb-shell mariadb://root@localhost:3306 --py
```

Turn off the interactive prompts, so that the functions return their results instead of printing them:

```python
shell.options.useWizards = False
```

Create the project in the existing directory `~/projects`:

```python
project = msm.create_new_project_folder("shop", "~/projects", "Example Corp", license="MIT")
```

Add a table to section 140 of the development script, and set the version to release:

```python
dev_script = project + "/development/shop_next.sql"
msm.set.section_sql_content(dev_script, "140", """
CREATE TABLE `shop`.`product`(
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(100) NOT NULL
);""")
msm.set.development_version(schema_project_path=project, version="1.0.0")
```

Release version 1.0.0, generate its deployment script, and deploy it:

```python
msm.prepare_release(schema_project_path=project, version="1.0.0", next_version="1.1.0")
msm.generate_deployment_script(schema_project_path=project, version="1.0.0")
msm.deploy_schema(schema_project_path=project)
```

```text
Deployment of `shop` version 1.0.0 completed successfully.
```

The schema `shop` now exists on the server with the table `product` and the view `msm_schema_version`, which reports the deployed version.

## The msm Global Object

The plugin adds the `msm` global object to Python mode, with the sub-objects `msm.get` and `msm.set`. All functions are also available through [command line integration](../using-mariadb-shell/command-line-integration.md), for example `mariadb-shell -- msm prepare-release`. See [Function Reference](function-reference.md).

To show the built-in help, run `\? msm` in Python mode, or `mariadb-shell -- msm --help` on the command line.

### Interactive and Non-Interactive Use

The functions behave differently depending on the `useWizards` shell option:

* **Interactive** (`useWizards` is on, the default in an interactive session, and on the command line). A function prompts for missing values, such as a version number, and prints its result instead of returning it. For example, `msm.get.released_versions()` prints one version per line.
* **Non-interactive** (`useWizards` is off). A function doesn't prompt, returns its result, and raises an error when a required value is missing. Use this mode in scripts.

Set the option for the current session with `shell.options.useWizards = False`, or start MariaDB Shell with `--no-wizard`.

## In This Section

{% content-ref url="schema-projects.md" %}
[schema-projects.md](schema-projects.md)
{% endcontent-ref %}

{% content-ref url="msm-sections.md" %}
[msm-sections.md](msm-sections.md)
{% endcontent-ref %}

{% content-ref url="developing-a-schema.md" %}
[developing-a-schema.md](developing-a-schema.md)
{% endcontent-ref %}

{% content-ref url="preparing-releases.md" %}
[preparing-releases.md](preparing-releases.md)
{% endcontent-ref %}

{% content-ref url="deploying-schemas.md" %}
[deploying-schemas.md](deploying-schemas.md)
{% endcontent-ref %}

{% content-ref url="function-reference.md" %}
[function-reference.md](function-reference.md)
{% endcontent-ref %}

<sub>_This page is licensed: GPLv2_</sub>
