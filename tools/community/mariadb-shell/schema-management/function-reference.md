---
description: >-
  Reference of all functions of the msm global object, with their Python and
  command line names, parameters, options, and return values.
---

# Function Reference

<!--
  SYNCED: this page is maintained in mariadb-corporation/mariadb-shell, under docs-ref/content/,
  and copied one way into mariadb-docs (tools/community/mariadb-shell/).
  Make every change in mariadb-corporation/mariadb-shell. A change made in mariadb-docs or in the
  GitBook editor is overwritten by the next sync.
-->

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
| `msm.create_new_project_folder(schema_name, target_path, copyright_holder[, options])` | `msm create-new-project-folder` | Creates a project folder and returns its path. Options: `license`, `copyrights`, `year_of_creation`, `overwrite_existing`, `enforce_target_path`, `allow_special_chars`. See [Create a Project](schema-projects.md#create-a-project). |
| `msm.import_live_schema(schema, target_path[, options])` | `msm import-live-schema` | Creates a project from a schema on the server of the global session, or of the one passed with `session`, and returns what it imported. Options: `objects`, `copyright_holder`, `copyrights`, `license`, `year_of_creation`, `overwrite_existing`, `enforce_target_path`, `session`, `lsp_path`. See [Create a Project from a Schema on a Server](schema-projects.md#create-a-project-from-a-schema-on-a-server). |
| `msm.list_live_schema_objects(schema[, options])` | `msm list-live-schema-objects` | Returns the objects of a schema on the server that `msm.import_live_schema()` can import, with what each view reads. Options: `session`, `lsp_path`. |
| `msm.import_workbench_model(model_path, target_path[, options])` | `msm import-workbench-model` | Creates a project from a schema of a MySQL Workbench model (`.mwb`), with its EER diagrams. Options: `schema`, `copyright_holder`, `copyrights`, `license`, `year_of_creation`, `overwrite_existing`, `enforce_target_path`, `lsp_path`. |
| `msm.get.project_settings([options])` | `msm get project-settings` | Returns the content of `msm.project.json` as a dictionary. |
| `msm.set.project_settings(settings[, options])` | `msm set project-settings` | Changes the given keys of `msm.project.json`, brings the project's files in line, and returns the files it wrote. See [Change Project Settings](schema-projects.md#change-project-settings). |
| `msm.get.project_information([options])` | `msm get project-information` | Returns the project settings plus `currentDevelopmentVersion`, `lastReleasedVersion`, and `schemaDevelopmentFilePath`. |
| `msm.get.available_licenses()` | `msm get available-licenses` | Returns the names of the included license headers. |

## Sections and Versions

| Python | Command line | Description |
| --- | --- | --- |
| `msm.get.sql_content_from_section(file_path, section_id)` | `msm get sql-content-from-section` | Returns the content of a section of a script, without its banner. `section_id` is the number as a string, for example `"140"`. |
| `msm.set.section_sql_content(file_path, section_id, sql_content)` | `msm set section-sql-content` | Replaces the content of a section of a script and writes the file. Fails if the section doesn't exist. |
| `msm.split_sections([options])` | `msm split-sections` | Moves the statements of sections 140, 150, and 170 of the development script into files by object kind. Options: `sections`, `lsp_path`. See [Split Sections into Files](developing-a-schema.md#split-sections-into-files). |
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
| `msm.deploy_schema([options])` | `msm deploy-schema` | Creates or upgrades the schema on the server and returns a message about the result. Options: `version`, `backup`, `backup_directory`, `online_alter`, `substitutions`, `session`. See [Deploying Schemas](deploying-schemas.md). |
| `msm.online_alter_table(schema, table, spec[, options])` | `msm online-alter-table` | Runs one `ALTER TABLE` on the server the least disruptive way that it accepts, and returns which step applied it. Options: `options`, `session`. See [Run One ALTER TABLE Online](deploying-schemas.md#run-one-alter-table-online). |
| `msm.get.schema_exists([options])` | `msm get schema-exists` | Returns whether the schema of the project exists on the server. |
| `msm.get.schema_is_managed([options])` | `msm get schema-is-managed` | Returns whether the schema has the `msm_schema_version` view. |
| `msm.get.schema_version([options])` | `msm get schema-version` | Returns the deployed version as a string, or `None` if the schema doesn't exist. |

## Online ALTER TABLE Settings

| Python | Command line | Description |
| --- | --- | --- |
| `msm.get_online_alter_settings([options])` | `msm get-online-alter-settings` | Returns the defaults, the project's `onlineAlter` setting, and, with the option `table`, whether online `ALTER TABLE` is on for that table and its values. See [Online ALTER TABLE Settings](deploying-schemas.md#online-alter-table-settings). |
| `msm.get_online_alter_defaults()` | `msm get-online-alter-defaults` | Returns the values that MSM uses where nothing is set. |

To change the setting, use `msm.set.project_settings()`.

## Schema Diagrams and Schema Edits

Section 160 of the development script holds a snapshot of the schema objects and the schema diagrams of the project. These functions read and change them. Those that read the SQL need `mariadb-lsp`, the MariaDB SQL language server, and take the option `lsp_path`.

| Python | Command line | Description |
| --- | --- | --- |
| `msm.list_schema_diagrams([options])` | `msm list-schema-diagrams` | Lists the diagrams, and says whether the schema snapshot matches the development script. |
| `msm.get_schema_diagrams([options])` | `msm get-schema-diagrams` | Returns the rows of the `msm_schema_diagrams` view: the schema snapshot `schema_definition` and one row per diagram. Option: `diagram`. |
| `msm.get_schema_diagram_image(diagram, figure_id[, options])` | `msm get-schema-diagram-image` | Returns the picture of an image figure of a diagram, as a data URL. |
| `msm.update_schema_definition([options])` | `msm update-schema-definition` | Makes the schema snapshot again from the development script. `msm.prepare_release()` does this too. |
| `msm.create_schema_diagram(name[, options])` | `msm create-schema-diagram` | Adds a diagram of the schema's tables, laid out. |
| `msm.layout_schema_diagram(name[, options])` | `msm layout-schema-diagram` | Adds objects to a diagram and lays out its figures. |
| `msm.set_schema_diagram([document][, options])` | `msm set-schema-diagram` | Adds a diagram, or replaces the one of the same name. Option: `document_file`. |
| `msm.rename_schema_diagram(name, new_name[, options])` | `msm rename-schema-diagram` | Renames a diagram and keeps its figures, pictures, and place among the diagrams. Refuses an empty name, `schema_definition`, and a name that another diagram has, in any case. Returns the files it wrote, or an empty list for the same name. |
| `msm.remove_schema_diagram(name[, options])` | `msm remove-schema-diagram` | Removes a diagram. |
| `msm.edit_schema(edits, base_hash[, options])` | `msm edit-schema` | Changes tables, columns, indexes, keys, views, and routines in the `CREATE` statements of the development script. `base_hash` is the `source_hash` of the schema snapshot that the edits were made against. Option: `edits_file`. |
| `msm.get_object_templates()` | `msm get-object-templates` | Returns the `CREATE` statements that `msm.add_schema_object()` fills in, for each kind, and the placeholders that each kind takes: `${name}` and `${schema}`, and `${table}` for a trigger. |
| `msm.add_schema_object(kind, name, base_hash[, options])` | `msm add-schema-object` | Adds a `view`, `procedure`, `function`, `trigger`, `event`, or `sequence` from a template through `msm.edit_schema()`: a sequence to section 140 before the first table, every other kind to section 150. Returns what `msm.edit_schema()` returns, plus the `file` and the `line` where the new statement starts. Options: `template`, `table` (for a trigger), `lsp_path`. |

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

<sub>_This page is licensed: GPLv2_</sub>
