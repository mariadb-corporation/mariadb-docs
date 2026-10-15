---
description: >-
  Create an MSM schema project, understand its folders and files, choose a
  license and copyright notices, and use the MSM working directory.
---

# Schema Projects

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
| `copyright_holder` | The holder named in the copyright notice of the generated scripts and documents. |

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `license` | string | `None` | The license header of the generated scripts: `BSD`, `GPL-2.0`, `MIT`, or `None`. See [Licenses](#licenses). |
| `copyrights` | list | | Copyright notices for a project with more than one holder. Replaces `copyright_holder`. See [Copyright Notices](#copyright-notices). |
| `overwrite_existing` | Boolean | `false` | Replace a project folder of the same name. Its previous content is deleted. |
| `enforce_target_path` | Boolean | `false` | Create `target_path` if it doesn't exist. |
| `allow_special_chars` | Boolean | `false` | Controls the check of the schema name; see the warning below. |

In interactive mode, the function prompts for any of the three parameters that you leave out.

{% hint style="warning" %}
Use a schema name that consists of letters, digits, `_`, and `$`, and doesn't consist of digits only, so that it can be used without quotes. In the current release, the check of the name is reversed: by default, MSM accepts any name, and `allow_special_chars` set to `true` enforces these rules.
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
| `copyrights` | The copyright notices. |
| `copyrightHolder` | The first copyright holder, kept for tools that read the older single-holder format. `copyrights` takes precedence. |
| `yearOfCreation` | The year in which the project was created. |
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

## Licenses

The license header is written at the top of every script that MSM generates. MSM includes the headers `BSD`, `GPL-2.0`, `MIT`, and `None`; `None` contains only the copyright notices. To list them, run `msm.get.available_licenses()`.

To use a license of your own, set `license` to `CUSTOM` in `msm.project.json`, and put the header text into `customLicense`. The text must be a valid SQL comment, because it is placed in front of the SQL statements, and it can contain these placeholders:

| Placeholder | Replaced with |
| --- | --- |
| `${copyright_notices}` | One `Copyright (c) <years>, <holder>.` line for each holder, each starting with ` * ` so that it fits into a `/* */` comment. |
| `${copyright_holder}` | The first holder. |
| `${year}` | The years of the first holder. |

## Copyright Notices

For a project with several copyright holders, pass `copyrights` instead of `copyright_holder`. In Python, pass it as a keyword argument and leave `copyright_holder` out. Each entry is a dictionary with these keys:

| Key | Description |
| --- | --- |
| `holder` | The name of the holder. |
| `yearOfCreation` | The first year of the notice. |
| `yearOfLastUpdate` | Optional. The last year of the notice. |
| `tracksUpdates` | Optional. When `true`, the notice always ends with the current year, so that it is up to date in every newly generated script. |

```python
msm.create_new_project_folder("shop", "~/projects", copyrights=[
    {"holder": "Example Corp", "yearOfCreation": "2024", "yearOfLastUpdate": "2025"},
    {"holder": "Example Services Ltd", "yearOfCreation": "2026", "tracksUpdates": True},
])
```

A notice reads `Copyright (c) 2024, 2025, Example Corp.`, or `Copyright (c) 2026, Example Services Ltd.` when both years are the same.

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
