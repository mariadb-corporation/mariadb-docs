---
description: >-
  Install, upgrade, and remove MariaDB Shell on Linux and macOS with the
  install.sh script.
---

# Linux and macOS

The `install.sh` script installs MariaDB Shell into your home directory from a GitHub release. It runs under any POSIX shell, including minimal container images that have no `bash`.

## Requirements

* Linux with glibc 2.34 or later, or macOS 15 or later (macOS 26 or later on Apple silicon). Linux distributions based on musl libc are not supported.
* An x86-64 or ARM64 CPU.
* `curl`, `tar`, and `awk`.
* `sha256sum` or `shasum`, to verify the download.
* `jq` or `python3`, only when you install a prerelease with `--pre-release`.

## Install the Latest Release

Run the script from the repository:

```sh
curl -fsSL https://github.com/mariadb-corporation/mariadb-shell/raw/main/install.sh | bash
```

The script performs these steps:

1. Detects the operating system, the CPU architecture, and, on Linux, the glibc version (with `getconf GNU_LIBC_VERSION`, or `ldd --version` as a fallback). On macOS, it reads the major version from `sw_vers`.
2. Downloads the `SHA256SUMS` file of the release and uses it as the list of available packages.
3. Selects the package that matches your architecture and has the highest platform version that is not newer than yours. For example, a package built for glibc 2.34 is selected on a system with glibc 2.39.
4. Downloads the package and compares its SHA-256 checksum with the value in `SHA256SUMS`. The script stops if the checksums don't match.
5. Unpacks the package into `~/.local/share/mariadb-shell/<version>`, for example `~/.local/share/mariadb-shell/26.9.5`.
6. Creates the symbolic links `~/.local/bin/mariadb-shell` and `~/.local/bin/msh`, which point to the installed version.
7. Removes older versions, keeping the new version and one previous version. See [Upgrade and Roll Back](#upgrade-and-roll-back).

A successful run ends with output similar to the following:

```text
==> Detected: linux 2.39, x86-64bit
==> Fetching package list from the latest release
==> Selected mariadb-shell-26.9.5-linux-glibc2.34-x86-64bit.tar.gz
==> Downloading
==> Verifying checksum
==> Unpacking into /home/dba/.local/share/mariadb-shell
==> Installed /home/dba/.local/share/mariadb-shell/26.9.5/bin/mariadb-shell   Ver 26.9.5 ...
==> Binary: /home/dba/.local/bin/mariadb-shell -> /home/dba/.local/share/mariadb-shell/26.9.5/bin/mariadb-shell
==>         /home/dba/.local/bin/msh -> /home/dba/.local/share/mariadb-shell/26.9.5/bin/msh
```

{% hint style="info" %}
Without options, the script installs the newest release that is not marked as a prerelease on GitHub. If no such release exists, the script cannot find `SHA256SUMS` and stops with an error. In that case, install the newest prerelease or a specific version as described in the next sections.
{% endhint %}

## Install a Prerelease

To install the newest release even if it is a prerelease, pass `--pre-release` to the script. When you pipe the script into a shell, pass options after `-s --`:

```sh
curl -fsSL https://github.com/mariadb-corporation/mariadb-shell/raw/main/install.sh | bash -s -- --pre-release
```

## Install a Specific Version

To install a particular release, set `MARIADB_SHELL_TAG` to its tag. A pinned tag takes precedence over `--pre-release`:

```sh
curl -fsSL https://github.com/mariadb-corporation/mariadb-shell/raw/main/install.sh | MARIADB_SHELL_TAG=v26.9.5 bash
```

Each release also carries a copy of `install.sh` as a release asset.

## Add the Command Directory to PATH

The script does not edit your shell startup files. If `~/.local/bin` is not on your `PATH`, the script prints a reminder at the end. Add the directory to your shell profile, for example `~/.bashrc` or `~/.zshrc`:

```sh
export PATH="$HOME/.local/bin:$PATH"
```

Open a new terminal, then check the installation:

```sh
mariadb-shell --version
```

## Installation Options

The script reads the following environment variables:

| Variable | Default | Description |
| --- | --- | --- |
| `MARIADB_SHELL_TAG` | Newest release | Release tag to install, for example `v26.9.5`. |
| `MARIADB_SHELL_PREFIX` | `~/.local/share/mariadb-shell` | Directory that holds the unpacked versions. |
| `MARIADB_SHELL_BINDIR` | `~/.local/bin` | Directory where the `mariadb-shell` and `msh` links are created. |
| `MARIADB_SHELL_REPO` | `mariadb-corporation/mariadb-shell` | GitHub repository, in `owner/repo` form, to install from. It must be public. |

The script accepts these options:

| Option | Description |
| --- | --- |
| `--pre-release` | Install the newest release, including prereleases. |
| `-h`, `--help` | Print usage information and exit. |

For example, to install into `/opt/mariadb-shell` and create the links in `/usr/local/bin`, run the script as a user who can write to both directories:

```sh
curl -fsSL https://github.com/mariadb-corporation/mariadb-shell/raw/main/install.sh \
  | MARIADB_SHELL_PREFIX=/opt/mariadb-shell MARIADB_SHELL_BINDIR=/usr/local/bin sh
```

## Upgrade and Roll Back

To upgrade, run the installation command again. The script installs the new version next to the existing ones and points the `mariadb-shell` and `msh` links at it. Running the command for a version that is already installed replaces that version's files.

After each installation, the script keeps only two versions in the prefix directory: the version it installed and the highest of the other versions. It removes only directories whose names consist of digits and dots, and leaves any other files in the prefix directory alone.

To roll back to the previous version, point the links at it:

```sh
ln -sfn ~/.local/share/mariadb-shell/26.9.4/bin/mariadb-shell ~/.local/bin/mariadb-shell
ln -sfn ~/.local/share/mariadb-shell/26.9.4/bin/msh ~/.local/bin/msh
```

Alternatively, reinstall the earlier release with `MARIADB_SHELL_TAG`.

Upgrading does not change your configuration directory, `~/.mariadb-shell`.

## Uninstall

The script has no uninstall mode. To remove MariaDB Shell, delete the links and the installation directory:

```sh
rm -f ~/.local/bin/mariadb-shell ~/.local/bin/msh
rm -rf ~/.local/share/mariadb-shell
```

If you used `MARIADB_SHELL_PREFIX` or `MARIADB_SHELL_BINDIR`, delete those locations instead.

To also remove your history, settings, plugins, log file, and sandbox instances, delete `~/.mariadb-shell`. Stop any running sandbox instances first. See [Files and Environment Variables](../files-and-environment-variables.md).

## Troubleshooting

| Message | Cause and solution |
| --- | --- |
| `could not determine the glibc version (musl is not supported)` | The system does not use glibc. Use a glibc-based distribution or container image. |
| `no compatible package for linux 2.31 / x86-64bit` | The system's glibc is older than any package in the release. The script lists the available packages. Upgrade to a distribution with glibc 2.34 or later. |
| `unsupported CPU architecture` | Only x86-64 and ARM64 packages are built. |
| `could not download SHA256SUMS from the latest release` | The release does not exist or is a prerelease. Use `--pre-release` or set `MARIADB_SHELL_TAG`. |
| `checksum mismatch` | The download is corrupt or incomplete. Run the script again. |
| `this install needs jq or python3 to read the release listing` | Install `jq` or `python3`, which the script needs for `--pre-release`. |
