---
description: >-
  Reference of all functions of the msm global object, with their Python and
  command line names, parameters, options, and return values.
---

# Function Reference

The `msm` global object and its sub-objects `msm.get` and `msm.set` provide the functions below. In Python mode, call them with snake_case names and pass options as keyword arguments. On the command line, use the kebab-case names shown in the tables and pass options as `--name=value`, in camelCase or kebab-case. See [Command Line Integration](../using-mariadb-shell/command-line-integration.md).

```python
msm.prepare_release(schema_project_path="/home/dev/projects/shop.msm.project", version="1.1.0", next_version="1.2.0")
```

```bash
mariadb-shell -- msm prepare-release --schema-project-path=/home/dev/projects/shop.msm.project --version=1.1.0 --next-version=1.2.0
```

Every function that takes `schema_project_path` uses the [MSM working directory](schema-projects.md#the-msm-working-directory) when you leave it out.

In interactive mode, which includes the command line, functions print their results and return nothing; with `useWizards` off, they return the values described below. See [Interactive and Non-Interactive Use](README.md#interactive-and-non-interactive-use).

## Projects

| Python | Command line | Description |
| --- | --- | --- |
| `msm.create_new_project_folder(schema_name, target_path, copyright_holder[, options])` | `msm create-new-project-folder` | Creates a project folder and returns its path. Options: `license`, `copyrights`, `overwrite_existing`, `enforce_target_path`, `allow_special_chars`. See [Create a Project](schema-projects.md#create-a-project). |
| `msm.get.project_settings([options])` | `msm get project-settings` | Returns the content of `msm.project.json` as a dictionary. |
| `msm.get.project_information([options])` | `msm get project-information` | Returns the project settings plus `currentDevelopmentVersion`, `lastReleasedVersion`, and `schemaDevelopmentFilePath`. |
| `msm.get.available_licenses()` | `msm get available-licenses` | Returns the names of the included license headers. |

## Sections and Versions

| Python | Command line | Description |
| --- | --- | --- |
| `msm.get.sql_content_from_section(file_path, section_id)` | `msm get sql-content-from-section` | Returns the content of a section of a script, without its banner. `section_id` is the number as a string, for example `"140"`. |
| `msm.set.section_sql_content(file_path, section_id, sql_content)` | `msm set section-sql-content` | Replaces the content of a section of a script and writes the file. Fails if the section doesn't exist. |
| `msm.set.development_version([options])` | `msm set development-version` | Sets the development version in section 910 of the development script. Option: `version`, in the form `major.minor.patch`. |
| `msm.get.released_versions([options])` | `msm get released-versions` | Returns the released versions, sorted, each as a list of three integers, for example `[[1, 0, 0], [1, 1, 0]]`. |
| `msm.get.last_released_version([options])` | `msm get last-released-version` | Returns the highest released version as a list of three integers, or `None`. |
| `msm.get.deployment_script_versions([options])` | `msm get deployment-script-versions` | Returns the versions that have a deployment script, as lists of three integers. |
| `msm.get.last_deployment_version([options])` | `msm get last-deployment-version` | Returns the highest version that has a deployment script, or `None`. |

## Releases

| Python | Command line | Description |
| --- | --- | --- |
| `msm.prepare_release([options])` | `msm prepare-release` | Writes the snapshot of a release and, from the second release on, an empty update script, and sets the next development version. Returns the paths of the files it wrote. Options: `version`, `next_version`, `allow_to_stay_on_same_version`, `overwrite_existing`. See [Prepare a Release](preparing-releases.md#prepare-a-release). |
| `msm.generate_deployment_script([options])` | `msm generate-deployment-script` | Generates the deployment script of a release and returns its path. Options: `version`, `overwrite_existing`. See [Generate the Deployment Script](preparing-releases.md#generate-the-deployment-script). |

## Deployment

These functions use the global session, or the session passed with the `session` option. On the command line, pass a connection URI before the `--`.

| Python | Command line | Description |
| --- | --- | --- |
| `msm.deploy_schema([options])` | `msm deploy-schema` | Creates or upgrades the schema on the server and returns a message about the result. Options: `version`, `backup`, `backup_directory`, `session`. See [Deploying Schemas](deploying-schemas.md). |
| `msm.get.schema_exists([options])` | `msm get schema-exists` | Returns whether the schema of the project exists on the server. |
| `msm.get.schema_is_managed([options])` | `msm get schema-is-managed` | Returns whether the schema has the `msm_schema_version` view. |
| `msm.get.schema_version([options])` | `msm get schema-version` | Returns the deployed version as a string, or `None` if the schema doesn't exist. |

## Working Directory

| Python | Command line | Description |
| --- | --- | --- |
| `msm.cd(directory)` | `msm cd` | Sets the MSM working directory. |
| `msm.pwd()` | `msm pwd` | Returns the MSM working directory. |
| `msm.ls([path])` | `msm ls` | Lists the folders and files of the MSM working directory, or of a path relative to it. |

## Plugin Information

| Python | Command line | Description |
| --- | --- | --- |
| `msm.info()` | `msm info` | Returns a short description of the plugin. |
| `msm.version()` | `msm version` | Returns the version of the plugin. |

`msm.get_schema_diagram()` is reserved for a future schema modeler. It returns an empty diagram model and fails when you pass a project path.
