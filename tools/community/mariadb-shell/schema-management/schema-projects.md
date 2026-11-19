---
description: >-
  Create an MSM schema project, also from a schema on a server, understand
  its folders and files, change its settings, license and copyright notices,
  and use the MSM working directory.
---

# Schema Projects

<!--
  SYNCED: this page is maintained in mariadb-corporation/mariadb-shell, under docs-ref/content/,
  and copied one way into mariadb-docs (tools/community/mariadb-shell/).
  Make every change in mariadb-corporation/mariadb-shell. A change made in mariadb-docs or in the
  GitBook editor is overwritten by the next sync.
-->

An MSM schema project is a folder that holds everything about one database schema: the development script, a snapshot of every released version, the update scripts between releases, and the generated deployment scripts. It consists of plain text files, so you can keep it in version control together with the application that uses the schema.

## Create a Project

```python
msm.create_new_project_folder(schema_name, target_path, copyright_holder[, options])
```

The function creates the folder `<schema>.msm.project` inside `target_path` and returns its path. For example:

```python
msm.create_new_project_folder("shop", "~/projects", "Example Corp", license="MIT")
```

```text
/home/dev/projects/shop.msm.project
```

| Parameter | Description |
| --- | --- |
| `schema_name` | The name of the database schema. It is used in the SQL scripts and, with spaces and characters that aren't allowed in file names removed, in the file names. |
| `target_path` | The directory in which the project folder is created. It must exist, unless you set `enforce_target_path`. |
| `copyright_holder` | The holder named in the copyright notice of the generated scripts and documents, exactly as you give it. MSM adds no period at the end; include one if you want it. |

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `license` | string | `None` | The license header of the generated scripts: `BSD`, `GPL-2.0`, `MIT`, or `None`. See [Licenses](#licenses). |
| `copyrights` | list | | Copyright notices for a project with more than one holder. Replaces `copyright_holder`. See [Copyright Notices](#copyright-notices). |
| `year_of_creation` | string | The current year | The first year of the copyright notice, for a schema that existed before it became an MSM project. Four digits, not in the future. |
| `overwrite_existing` | Boolean | `false` | Replace a project folder of the same name. Its previous content is deleted. |
| `enforce_target_path` | Boolean | `false` | Create `target_path` if it doesn't exist. |
| `allow_special_chars` | Boolean | `false` | Accept any schema name. See below. |

In interactive mode, the function prompts for any of the three parameters that you leave out. When it prompts for the copyright holder, it also prompts for the year of creation.

By default, the schema name must be usable without quotes: it may consist of basic Latin letters, digits, `_`, and `$`, must not start with `$`, and must not consist of digits only. Set `allow_special_chars` to `true` to use any other name.

## Create a Project from a Schema on a Server

To put a schema that already exists on a server under MSM, create the project from it. `msm.import_live_schema()` reads the schema on the global session, or on the one passed with the `session` option, and creates a project whose development script creates the same objects:

```python
shell.connect("mariadb://admin@db.example.com:3306")
msm.import_live_schema("shop", "~/projects", copyright_holder="Example Corp", license="MIT")
```

The development script gets the `CREATE` statements that the server returns with `SHOW CREATE`:

* tables and sequences in section 140, the tables ordered by their foreign keys
* views, stored procedures and functions, triggers, and events in section 150, written so that they can run again, the views ordered by the objects that they read
* in files under `development/sections/` instead, for a section larger than `maxInlineSectionSize`

So that the project deploys on any server and under any schema name, the statements have no `DEFINER` clause, no `AUTO_INCREMENT=<n>` table option, and no schema name in front of the schema's own objects. Objects of other schemas keep their schema name. The import doesn't take data, users, roles, or privileges, and leaves out MSM's own views and routines, whose names start with `msm_`. Then MSM makes the schema snapshot of section 160.

| Parameter or option | Description |
| --- | --- |
| `schema` | The schema on the server. The project gets its name. |
| `target_path` | The directory in which the project folder is created. |
| `objects` | The objects to import, as a dictionary with a list of names for each kind: `tables`, `views`, `procedures`, `functions`, `triggers`, `events`, and `sequences`. A kind that you leave out isn't imported. Without `triggers`, the selected tables bring their triggers; a trigger needs its table. The default is every object. |
| `copyright_holder`, `copyrights`, `license`, `year_of_creation`, `overwrite_existing`, `enforce_target_path` | As for [`msm.create_new_project_folder()`](#create-a-project). |
| `session` | The session to read the schema with. The default is the global session. |

The function returns the project's path, the numbers of imported objects, the version that MSM deployed of the schema if it has the `msm_schema_version` view, warnings about what it left out, and the files it wrote. It refuses the import before it writes anything when a check of `msm.create_new_project_folder()` fails, when `objects` names an object that the schema doesn't have, or when two selected objects have names that differ only in case, such as a table `Customer` and a view `customer`. A project can't keep such names apart. Tables, views, and sequences count as one kind for this check.

A foreign key that references a table of the schema that you didn't select is left out, with a warning; its index stays. A selected view that reads an object that you didn't select gets a warning too.

To see what the import can take, use `msm.list_live_schema_objects()`. It returns the tables with their comments and triggers, the views, procedures, functions, triggers with their tables, events, and sequences of the schema. Each view has `reads`, the tables, views, sequences, and functions of the schema that it reads, or `None` when they can't be worked out. The result also has `project_folder_name`, `schema_version`, and `left_out`, MSM's own objects.

{% hint style="info" %}
The import needs `mariadb-lsp`, the MariaDB SQL language server, and the list uses it to find what each view reads. MSM looks for it next to `mariadb-shell`, where the release packages of MariaDB Shell install it, then on the `PATH` and in `~/.local/bin`; pass `lsp_path` to use another binary. To import views, the binary must report what a view reads. With one that doesn't, `reads` is `None` for every view, and an import that selects views is refused.
{% endhint %}

## Project Layout

```text
shop.msm.project/
├── msm.project.json                       Project settings
├── README.md                              Description of the workflow
├── CHANGELOG.md                           Change log of the schema, for you to maintain
├── development/
│   ├── README.md
│   ├── shop_next.sql                      The development script
│   └── sections/                          Optional files included with SOURCE (you create it)
└── releases/
    ├── versions/
    │   ├── README.md
    │   └── shop_1.0.0.sql                 Complete create script of each release
    ├── updates/
    │   ├── README.md
    │   └── shop_1.0.0_to_1.1.0.sql        Update script between consecutive releases
    └── deployment/
        ├── README.md
        └── shop_deployment_1.1.0.sql      Generated deployment script of each release
```

| File | Created by | Description |
| --- | --- | --- |
| `development/<schema>_next.sql` | `create_new_project_folder()` | The complete definition of the next version. The suffix `_next` stands for the version under development; the version number itself is stored inside the script. See [Developing a Schema](developing-a-schema.md). |
| `releases/versions/<schema>_<version>.sql` | `prepare_release()` | A snapshot of the development script at the time of the release. MSM derives the list of released versions from these file names. |
| `releases/updates/<schema>_<from>_to_<to>.sql` | `prepare_release()` | The update script from one release to the next. MSM creates it from a template, and you add the statements. See [Preparing Releases](preparing-releases.md#write-the-update-script). |
| `releases/deployment/<schema>_deployment_<version>.sql` | `generate_deployment_script()` | The script that creates or upgrades the schema to this version. Regenerate it instead of editing it. |

Version numbers have the form `major.minor.patch`, for example `1.4.2`. The README files recommend [semantic versioning](https://semver.org/).

## Project Settings

`msm.project.json` holds the settings of the project:

{% code title="msm.project.json" %}
```json
{
    "copyrights": [
        {
            "holder": "Example Corp",
            "yearOfCreation": "2026",
            "tracksUpdates": true
        }
    ],
    "copyrightHolder": "Example Corp",
    "customLicense": "",
    "license": "MIT",
    "onlineAlter": {
        "enabled": true
    },
    "schemaDependencies": [],
    "schemaName": "shop",
    "schemaFileName": "shop",
    "yearOfCreation": "2026"
}
```
{% endcode %}

| Key | Description |
| --- | --- |
| `schemaName` | The name of the database schema. |
| `schemaFileName` | The schema name as it is used in file names. |
| `license` | The license header: `BSD`, `GPL-2.0`, `MIT`, `None`, or `CUSTOM`. |
| `customLicense` | The license text when `license` is `CUSTOM`. |
| `copyrights` | The copyright notices. See [Copyright Notices](#copyright-notices). |
| `copyrightHolder` | The first copyright holder, kept for tools that read the older single-holder format. `copyrights` takes precedence. |
| `yearOfCreation` | The first year of the first copyright notice. |
| `onlineAlter` | Optional. How deployments run the `ALTER TABLE` statements of the update scripts. On when missing. See [Online ALTER TABLE Settings](deploying-schemas.md#online-alter-table-settings). |
| `substitutions` | Optional. The placeholders that the scripts and the schema name can use as `/*<msm:name>*/`, each with a `default` value and an optional `pattern`, a regular expression that a value must match. `msm.deploy_schema()` replaces them before the scripts run; see its `substitutions` option in [Deploying Schemas](deploying-schemas.md#deploy-a-release). |
| `maxInlineSectionSize` | Optional. The largest section, in characters, that MSM keeps in the development script when it writes a whole section, as the imports do; a larger one goes into files under `development/sections/`. The default is 16384. |
| `schemaDependencies` | Reserved; always empty. |

To read the settings, use `msm.get.project_settings()`. `msm.get.project_information()` returns the same settings plus the current development version, the last released version, and the path of the development script:

```python
msm.get.project_information(schema_project_path=project)
```

```text
{
    ...
    "currentDevelopmentVersion": "1.1.0",
    "lastReleasedVersion": "1.0.0",
    "schemaDevelopmentFilePath": "/home/dev/projects/shop.msm.project/development/shop_next.sql",
    ...
}
```

## Change Project Settings

To change settings, pass the keys to change to `msm.set.project_settings()`:

```python
msm.set.project_settings({"license": "GPL-2.0"}, schema_project_path=project)
msm.set.project_settings({"onlineAlter": {"enabled": True, "maxRebuildBytes": 1073741824}}, schema_project_path=project)
```

The function returns the files it wrote, or an empty list when nothing changed.

* Only the keys that you pass change. Each value replaces the stored one as a whole: `copyrights` is the full list of holders, and `onlineAlter` is the whole setting, with its values for tables.
* `None` removes an optional key, so that MSM uses its default again: `customLicense`, `onlineAlter`, `substitutions`, `maxInlineSectionSize`, and `schemaDependencies`.
* The keys that you can set are `copyrights`, `license`, `customLicense`, `onlineAlter`, `substitutions`, `maxInlineSectionSize`, and `schemaDependencies`. `schemaName` and `schemaFileName` can't change, and `copyrightHolder` and `yearOfCreation` follow the first entry of `copyrights`. The function refuses these keys and unknown ones.
* MSM checks every value before it writes anything, and writes nothing when it refuses one. A `CUSTOM` license needs a `customLicense` text that uses only the placeholders described in [Licenses](#licenses).
* The files of the project follow the settings. When only the years change, MSM updates them in the existing notices. When a holder, the license, or the custom license text changes, MSM writes the license header of the development script again, and replaces the notices in the files under `development/sections/` and in the README and CHANGELOG files that it created. Released files keep the notices they were released with.

## Licenses

The license header is written at the top of every script that MSM generates. MSM includes the headers `BSD`, `GPL-2.0`, `MIT`, and `None`; `None` contains only the copyright notices. To list them, run `msm.get.available_licenses()`.

To use a license of your own, create the project with one of the included headers, then set `license` to `CUSTOM` and put the header text into `customLicense` with [`msm.set.project_settings()`](#change-project-settings). `msm.create_new_project_folder()` refuses `CUSTOM`. The text must be a valid SQL comment, because it is placed in front of the SQL statements, and it can contain only these placeholders:

| Placeholder | Replaced with |
| --- | --- |
| `${copyright_notices}` | One `Copyright (c) <years>, <holder>` line for each holder, each starting with ` * ` so that it fits into a `/* */` comment. |
| `${copyright_holder}` | The first holder. |
| `${year}` | The years of the first holder. |

## Copyright Notices

For a project with several copyright holders, pass `copyrights` instead of `copyright_holder`. In Python, pass it as a keyword argument and leave `copyright_holder` out. Each entry is a dictionary with these keys:

| Key | Description |
| --- | --- |
| `holder` | The name of the holder. |
| `yearOfCreation` | The first year of the notice. |
| `yearOfLastUpdate` | Optional. The last year of the notice. It must not be before `yearOfCreation`. |
| `tracksUpdates` | Optional. When `true`, MSM keeps `yearOfLastUpdate` up to date; see below. A project created with `copyright_holder` has it set. |

```python
msm.create_new_project_folder("shop", "~/projects", copyrights=[
    {"holder": "Example Corp", "yearOfCreation": "2024", "yearOfLastUpdate": "2025"},
    {"holder": "Example Services Ltd", "yearOfCreation": "2026", "tracksUpdates": True},
])
```

A notice reads `Copyright (c) 2024, 2025, Example Corp`, or `Copyright (c) 2026, Example Services Ltd` when there is no later year. MSM writes the holder exactly as stored and adds no period; a period at the end is part of the holder's name, for example `"holder": "Example Corp."`.

MSM stores the years and never computes them when it writes a notice. On the first change that MSM makes to a project in a new year, it sets `yearOfLastUpdate` of every holder that tracks updates to the current year, writes `msm.project.json`, and updates the years in the notices of the development script, the files under `development/sections/`, and the README and CHANGELOG files that it created. Only the years change, so the files keep their line count. The changes that count are those of `msm.set.section_sql_content()`, `msm.set.development_version()`, `msm.prepare_release()`, `msm.generate_deployment_script()`, `msm.set.project_settings()`, and the functions that edit the schema or its diagrams. The creation of a project counts too, so a project created with a `year_of_creation` in the past starts with a notice such as `Copyright (c) 2024, 2026, Example Corp`. Released snapshots, update scripts, and deployment scripts keep the notices they were written with.

## The MSM Working Directory

Every function that works on a project takes the option `schema_project_path`. When you leave it out, the function uses the MSM working directory, which you set with `msm.cd()`. This saves typing the path in interactive sessions:

```python
msm.cd("~/projects/shop.msm.project")
msm.get.released_versions()
```

| Function | Description |
| --- | --- |
| `msm.cd(directory)` | Sets the working directory. An absolute path, a path starting with `~`, a path relative to the MSM working directory, or `..`. |
| `msm.pwd()` | Returns the working directory. The default is your home directory. |
| `msm.ls([path])` | Lists the folders and files of the working directory, or of a path relative to it. |

MSM stores the working directory in `config.json` in its plugin data directory, so it persists across sessions. It is independent of the current directory of the process.

{% hint style="info" %}
A function that runs on a working directory that isn't a project folder fails with `StopIteration: User-defined function threw an exception`. Change to the project folder with `msm.cd()`, or pass `schema_project_path`.
{% endhint %}

## Where MSM Stores Its Own Files

MSM keeps its own files in the plugin data directory, `plugin_data/msm_plugin/` in the [user configuration directory](../files-and-environment-variables.md#user-configuration-directory):

| File | Contents |
| --- | --- |
| `config.json` | The MSM working directory. |
| `msm_schema_update_log.txt` | The log of all deployments. See [Deploying Schemas](deploying-schemas.md#the-deployment-log). |
| `backups/` | Default location of the backups taken before an upgrade. |

<sub>_This page is licensed: GPLv2_</sub>
