---
description: >-
  Install, upgrade, and remove MariaDB Shell on Windows with the install.ps1
  PowerShell script.
---

# Windows

The `install.ps1` script installs MariaDB Shell for the current user from a GitHub release. It runs in Windows PowerShell 5.1 and in PowerShell 7, and does not require administrator privileges.

## Requirements

* 64-bit Windows on an x86-64 or ARM64 CPU. 32-bit Windows is not supported.
* Windows 10 version 1803 or later, which includes the `tar` command that the script uses to unpack the package.

## Install the Latest Release

Run the following command in a PowerShell window:

```powershell
irm https://github.com/mariadb-corporation/mariadb-shell/raw/main/install.ps1 | iex
```

The script performs these steps:

1. Detects the CPU architecture. On a 32-bit PowerShell process running on 64-bit Windows, it detects the architecture of the machine, not of the process.
2. Downloads the `SHA256SUMS` file of the release and uses it as the list of available packages.
3. Selects the Windows package for your architecture.
4. Downloads the package and compares its SHA-256 checksum with the value in `SHA256SUMS`. The script stops if the checksums don't match.
5. Unpacks the package into `%LOCALAPPDATA%\Programs\mariadb-shell\<version>`, for example `%LOCALAPPDATA%\Programs\mariadb-shell\26.9.5`.
6. Writes two command files, `mariadb-shell.cmd` and `msh.cmd`, into `%LOCALAPPDATA%\Programs\mariadb-shell\bin`. Both start the installed version's `mariadb-shell.exe`. They use paths relative to their own location, so you can move the whole installation directory.
7. Removes older versions, keeping the new version and one previous version. See [Upgrade and Roll Back](#upgrade-and-roll-back).

{% hint style="info" %}
Without options, the script installs the newest release that is not marked as a prerelease on GitHub. If no such release exists, the script cannot find `SHA256SUMS` and stops with an error. In that case, install the newest prerelease or a specific version as described in the next sections.
{% endhint %}

## Pass Options to the Script

When you pipe the script into `iex`, you cannot pass parameters to it. Each parameter therefore has an equivalent environment variable, which you set before you run the command. For example, to install the newest release and add the command directory to your `PATH`:

```powershell
$env:MARIADB_SHELL_ADDTOPATH = 1
irm https://github.com/mariadb-corporation/mariadb-shell/raw/main/install.ps1 | iex
```

To pass parameters directly, create a script block from the downloaded script and invoke it:

```powershell
& ([scriptblock]::Create((irm https://github.com/mariadb-corporation/mariadb-shell/raw/main/install.ps1))) -AddToPath
```

## Install a Prerelease

To install the newest release even if it is a prerelease, set `MARIADB_SHELL_PRERELEASE`, or use the `-PreRelease` parameter:

```powershell
$env:MARIADB_SHELL_PRERELEASE = 1
irm https://github.com/mariadb-corporation/mariadb-shell/raw/main/install.ps1 | iex
```

## Install a Specific Version

To install a particular release, set `MARIADB_SHELL_TAG` to its tag, or use the `-Tag` parameter. A pinned tag takes precedence over `-PreRelease`:

```powershell
$env:MARIADB_SHELL_TAG = 'v26.9.5'
irm https://github.com/mariadb-corporation/mariadb-shell/raw/main/install.ps1 | iex
```

Environment variables that you set with `$env:` remain set for the rest of the PowerShell session. Remove them with `Remove-Item Env:MARIADB_SHELL_TAG` before you install another version in the same window.

## Add the Command Directory to PATH

The script changes your user `PATH` only when you ask it to with `-AddToPath` or `MARIADB_SHELL_ADDTOPATH`. Otherwise, it prints the command to add the directory yourself:

```powershell
[Environment]::SetEnvironmentVariable('Path', ([Environment]::GetEnvironmentVariable('Path','User') + ";$env:LOCALAPPDATA\Programs\mariadb-shell\bin"), 'User')
```

Open a new terminal so that the change takes effect, then check the installation:

```powershell
mariadb-shell --version
```

## Installation Options

| Parameter | Environment variable | Default | Description |
| --- | --- | --- | --- |
| `-Tag` | `MARIADB_SHELL_TAG` | Newest release | Release tag to install, for example `v26.9.5`. |
| `-PreRelease` | `MARIADB_SHELL_PRERELEASE` | Off | Install the newest release, including prereleases. |
| `-AddToPath` | `MARIADB_SHELL_ADDTOPATH` | Off | Add the command directory to the user `PATH`. |
| `-Prefix` | `MARIADB_SHELL_PREFIX` | `%LOCALAPPDATA%\Programs\mariadb-shell` | Directory that holds the unpacked versions. |
| `-BinDir` | `MARIADB_SHELL_BINDIR` | `<prefix>\bin` | Directory where `mariadb-shell.cmd` and `msh.cmd` are written. |
| `-Repo` | `MARIADB_SHELL_REPO` | `mariadb-corporation/mariadb-shell` | GitHub repository, in `owner/repo` form, to install from. It must be public. |

A parameter takes precedence over its environment variable. For the switch variables `MARIADB_SHELL_PRERELEASE` and `MARIADB_SHELL_ADDTOPATH`, any non-empty value turns the setting on.

## Upgrade and Roll Back

To upgrade, run the installation command again. The script installs the new version next to the existing ones and rewrites `mariadb-shell.cmd` and `msh.cmd` to start it.

After each installation, the script keeps only two versions in the prefix directory: the version it installed and the highest of the other versions. It removes only directories whose names consist of digits and dots.

To roll back, reinstall the earlier release with `MARIADB_SHELL_TAG`. Alternatively, edit the two `.cmd` files and change the version in the path they start.

Upgrading does not change your configuration directory, `%AppData%\MariaDB\mariadb-shell`.

## Uninstall

The script has no uninstall mode. To remove MariaDB Shell:

1. Delete the installation directory:

   ```powershell
   Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Programs\mariadb-shell"
   ```

2. If you added the command directory to your user `PATH`, remove that entry, for example in **Settings** > **System** > **About** > **Advanced system settings** > **Environment Variables**.
3. Optionally, delete your configuration directory, `%AppData%\MariaDB\mariadb-shell`, and your sandbox directory, `%USERPROFILE%\MariaDB\mariadb-shell\sandboxes`. Stop any running sandbox instances first. See [Files and Environment Variables](../files-and-environment-variables.md).

## Troubleshooting

| Message | Cause and solution |
| --- | --- |
| `tar was not found` | Your Windows build is older than Windows 10 version 1803. Install manually as described in [Manual Installation](manual-installation.md), using another tool to unpack the package. |
| `32-bit Windows is not supported` | Only 64-bit packages are built. |
| `could not download SHA256SUMS from the latest release` | The release does not exist or is a prerelease. Set `MARIADB_SHELL_PRERELEASE` or `MARIADB_SHELL_TAG`. |
| `checksum mismatch` | The download is corrupt or incomplete. Run the script again. |
| `LOCALAPPDATA is not set` | The default installation directory cannot be determined. Set `MARIADB_SHELL_PREFIX` or pass `-Prefix`. |
