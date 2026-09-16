---
description: >-
  Reference for GridGain 9 CLI configuration parameters, including color themes,
  pager settings, and how to manage parameters and configuration profiles.
---

# CLI Configuration Parameters

```properties
ignite.jdbc.key-store.path=
ignite.cluster-endpoint-url=http://localhost:10300
ignite.jdbc.client-auth=
ignite.rest.key-store.password=
ignite.jdbc.key-store.password=
ignite.cli.sql.multiline=true
ignite.cli.sql.display-page-size=1000
ignite.cli.syntax-highlighting=true
ignite.cli.color-scheme=solarized-dark
ignite.cli.pager.enabled=true
ignite.cli.pager.command=less -RFX
ignite.rest.trust-store.path=
ignite.jdbc.trust-store.password=
ignite.auth.basic.username=
ignite.jdbc-url=jdbc:ignite:thin://127.0.0.1:10800
ignite.rest.key-store.path=
ignite.rest.trust-store.password=
ignite.jdbc.trust-store.path=
ignite.auth.basic.password=
```

|Property|Default|Description|
|---|---|---|
|ignite.jdbc.key-store.path||Path to the JDBC keystore file for SSL/TLS client authentication.|
|ignite.cluster-endpoint-url|`http://localhost:10300`|URL endpoint for connecting to the Ignite cluster REST API.|
|ignite.jdbc.client-auth||If JDBC client authorization is enabled in CLI.|
|ignite.rest.key-store.password||Password for the REST API keystore file.|
|ignite.jdbc.key-store.password||Password for the JDBC keystore file.|
|ignite.cli.sql.multiline|`true`|Enables multiline input mode for SQL commands in the CLI.|
|ignite.cli.sql.display-page-size|1000|The number of rows fetched and displayed per page when executing SQL queries in the REPL.|
|ignite.cli.syntax-highlighting|`true`|Enables syntax highlighting in CLI output.|
|ignite.cli.color-scheme|`solarized-dark`|Color theme for CLI output. See the [Color Themes](#color-themes) section for more information.|
|ignite.cli.pager.enabled|`true` on UNIX, `false` on Windows|Enables pager for long output in CLI.|
|ignite.cli.pager.command|`less -RFX` on UNIX, `more` on Windows|Command used for paging output.|
|ignite.rest.trust-store.path||Path to the REST API truststore file for SSL/TLS server verification.|
|ignite.jdbc.trust-store.password||Password for the JDBC truststore file.|
|ignite.auth.basic.username||Username for basic authentication when connecting to the cluster.|
|ignite.jdbc-url|`jdbc:ignite:thin://127.0.0.1:10800`|JDBC connection URL for connecting to the Ignite cluster.|
|ignite.rest.key-store.path||Path to the REST API keystore file for SSL/TLS client authentication.|
|ignite.rest.trust-store.password||Password for the REST API truststore file.|
|ignite.jdbc.trust-store.path||Path to the JDBC truststore file for SSL/TLS server verification.|
|ignite.auth.basic.password||Password for basic authentication when connecting to the cluster.|

## Color Themes

The CLI tool supports multiple color themes to improve readability in different terminal environments. The following themes are available:

- `solarized-dark` - Default theme, optimized for readability on dark backgrounds.
- `dark` - High-contrast theme for dark backgrounds.
- `solarized-light` - Alternative theme, optimized for readability on light backgrounds.
- `light` - Dark colors theme for light backgrounds.

To change the color theme, use the following command:

```bash
cli config set ignite.cli.color-scheme=solarized-light
```

## Pager Configuration

The CLI tool automatically uses paging for long outputs. The pager mode is enabled by default on UNIX systems and can be configured with the following parameters:

- `ignite.cli.pager.enabled` - Enable or disable the pager functionality.
- `ignite.cli.pager.command` - Specify the command to use for paging (default: `less -RFX` on UNIX, `more` on Windows).
- `ignite.cli.sql.display-page-size` - Set the number of rows fetched per page for SQL results (default: 1000).

To disable the pager:

```bash
cli config set ignite.cli.pager.enabled=false
```

You can also use a custom pager command by setting it in the configuration:

```bash
cli config set ignite.cli.pager.command="less -S"
```

## Managing Configuration Parameters

Use the `cli config` commands to read and change CLI configuration parameters. Unless you specify otherwise, these commands operate on the active profile.

- Display all parameters of the active profile:

  ```bash
  cli config show
  ```
- Get the value of a single parameter:

  ```bash
  cli config get ignite.jdbc-url
  ```
- Set one or more parameters:

  ```bash
  cli config set ignite.cli.pager.enabled=false ignite.cli.color-scheme=light
  ```
- Remove a parameter from the profile:

  ```bash
  cli config remove ignite.cli.pager.command
  ```

All of these commands accept the `--profile` option, which applies the operation to the specified profile instead of the active one:

```bash
cli config show --profile myprofile
```

For the full syntax of every command, see [CLI Configuration Commands](../../ignite-cli-tool.md#cli-configuration-commands).

## Configuration Profiles

GridGain [CLI](../../ignite-cli-tool.md#interactive-cli-mode) supports configuration profiles to manage different sets of settings.
Each profile stores its own CLI-specific settings.

The first time you run the CLI, it creates a profile named `default` and makes it active. Profiles are stored in the `ignitecli/defaults` file under your configuration directory. Keystore, truststore, and authentication settings are kept separately in `ignitecli/secrets`.

Use the following commands to create and manage profiles:

- Create a new configuration profile:

  ```bash
  cli config profile create <profile_name>
  ```

  To copy the settings of an existing profile into the new one, add `--copy-from`. To make the new profile active immediately, add `--activate`:

  ```bash
  cli config profile create --copy-from default --activate myprofile
  ```
- Switch to an existing profile:

  ```bash
  cli config profile activate <profile_name>
  ```
- Display all available profiles:

  ```bash
  cli config profile list
  ```
- Display the name of the active profile:

  ```bash
  cli config profile show
  ```

To see the settings stored in a profile, use `cli config show`, as described in [Managing Configuration Parameters](#managing-configuration-parameters).
