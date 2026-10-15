---
description: >-
  Download a MariaDB Shell release package, verify its checksum, and unpack it
  without the installation scripts.
---

# Manual Installation

Install MariaDB Shell manually when you cannot pipe a script from the internet into a shell, when you deploy to systems without internet access, or when you want to choose the installation directory and the package yourself.

## Choose a Package

Each release on the [GitHub releases page](https://github.com/mariadb-corporation/mariadb-shell/releases) provides one `.tar.gz` package per platform and a `SHA256SUMS` file with the checksum of every package. Package names follow the pattern `mariadb-shell-<version>-<platform>-<architecture>.tar.gz`. For version 26.9.5, the packages are:

| Package | Platform |
| --- | --- |
| `mariadb-shell-26.9.5-linux-glibc2.34-x86-64bit.tar.gz` | Linux, x86-64, glibc 2.34 or later |
| `mariadb-shell-26.9.5-linux-glibc2.34-arm-64bit.tar.gz` | Linux, ARM64, glibc 2.34 or later |
| `mariadb-shell-26.9.5-macos15-x86-64bit.tar.gz` | macOS 15 or later, Intel |
| `mariadb-shell-26.9.5-macos26-arm-64bit.tar.gz` | macOS 26 or later, Apple silicon |
| `mariadb-shell-26.9.5-windows-x86-64bit.tar.gz` | Windows, x86-64 |
| `mariadb-shell-26.9.5-windows-arm-64bit.tar.gz` | Windows, ARM64 |

A Linux or macOS package runs on the platform version in its name and on any later version. To check the glibc version of a Linux system, run `getconf GNU_LIBC_VERSION`.

{% hint style="info" %}
The release also contains `mariadb-<version>-...-sandbox.tar.gz` packages and a `SERVER_SHA256SUMS` file. These are MariaDB Server builds for [sandbox instances](../sandbox-instances.md), not part of MariaDB Shell.
{% endhint %}

## Download and Verify

Download the package for your platform and the `SHA256SUMS` file into the same directory, then verify the package.

{% tabs %}
{% tab title="Linux" %}
```sh
curl -fLO https://github.com/mariadb-corporation/mariadb-shell/releases/download/v26.9.5/mariadb-shell-26.9.5-linux-glibc2.34-x86-64bit.tar.gz
curl -fLO https://github.com/mariadb-corporation/mariadb-shell/releases/download/v26.9.5/SHA256SUMS
sha256sum -c SHA256SUMS --ignore-missing
```
{% endtab %}

{% tab title="macOS" %}
macOS provides `shasum` instead of `sha256sum`:

```sh
curl -fLO https://github.com/mariadb-corporation/mariadb-shell/releases/download/v26.9.5/mariadb-shell-26.9.5-macos26-arm-64bit.tar.gz
curl -fLO https://github.com/mariadb-corporation/mariadb-shell/releases/download/v26.9.5/SHA256SUMS
shasum -a 256 -c SHA256SUMS --ignore-missing
```
{% endtab %}

{% tab title="Windows" %}
PowerShell has no checksum-file verifier, so compare the hash yourself:

```powershell
$pkg  = 'mariadb-shell-26.9.5-windows-x86-64bit.tar.gz'
$base = 'https://github.com/mariadb-corporation/mariadb-shell/releases/download/v26.9.5'
Invoke-WebRequest "$base/$pkg" -OutFile $pkg
Invoke-WebRequest "$base/SHA256SUMS" -OutFile SHA256SUMS

$expected = (Get-Content SHA256SUMS | Where-Object { $_ -like "*  $pkg" }).Split(' ')[0]
$actual   = (Get-FileHash $pkg -Algorithm SHA256).Hash
if ($actual -eq $expected) { 'Checksum OK' } else { 'Checksum MISMATCH' }
```
{% endtab %}
{% endtabs %}

The `--ignore-missing` option makes `sha256sum` and `shasum` check only the packages that are present, instead of failing on the packages you didn't download. A correct download reports `OK` for the package. Don't install a package whose checksum doesn't match.

## Unpack the Package

Each package contains a single top-level directory, `mariadb-shell-<version>-<platform>-<architecture>`, with the following layout:

| Directory | Contents |
| --- | --- |
| `bin/` | The `mariadb-shell` executable, the `msh` alias (`msh.cmd` on Windows), and the credential store helpers (`mariadb-secret-store-*`). On Windows, also the required DLLs. |
| `lib/` | Private libraries, the bundled Python runtime, and the built-in plugins. On Linux and macOS, client authentication plugins are in `lib/mariadb/plugins/`. |
| `share/mariadb-shell/` | Data files, such as the sample prompt themes. |
| `share/man/man1/` | The `mariadb-shell(1)` and `msh(1)` manual pages (Linux and macOS). |

Keep this layout intact: the shell finds its libraries and data files relative to the parent of its `bin` directory.

{% tabs %}
{% tab title="Linux and macOS" %}
The following commands use the same locations as `install.sh`:

```sh
mkdir -p ~/.local/share/mariadb-shell ~/.local/bin
tar -xzf mariadb-shell-26.9.5-linux-glibc2.34-x86-64bit.tar.gz -C ~/.local/share/mariadb-shell
mv ~/.local/share/mariadb-shell/mariadb-shell-26.9.5-linux-glibc2.34-x86-64bit ~/.local/share/mariadb-shell/26.9.5
ln -sfn ~/.local/share/mariadb-shell/26.9.5/bin/mariadb-shell ~/.local/bin/mariadb-shell
ln -sfn ~/.local/share/mariadb-shell/26.9.5/bin/msh ~/.local/bin/msh
```

Make sure that `~/.local/bin` is on your `PATH`. For a system-wide installation, unpack into a directory such as `/opt` and create the links in `/usr/local/bin` instead.
{% endtab %}

{% tab title="Windows" %}
The following commands use the same location as `install.ps1`:

```powershell
$prefix = "$env:LOCALAPPDATA\Programs\mariadb-shell"
New-Item -ItemType Directory -Force $prefix | Out-Null
tar -xzf mariadb-shell-26.9.5-windows-x86-64bit.tar.gz -C $prefix
Rename-Item "$prefix\mariadb-shell-26.9.5-windows-x86-64bit" '26.9.5'
```

Then add `%LOCALAPPDATA%\Programs\mariadb-shell\26.9.5\bin` to your user `PATH`, or start `mariadb-shell.exe` with its full path.
{% endtab %}
{% endtabs %}

Check the installation:

```sh
mariadb-shell --version
```

## Upgrade and Uninstall

To upgrade, unpack the new version next to the old one and point the links (or your `PATH`) at the new `bin` directory. Remove old version directories when you no longer need them.

To uninstall, delete the version directories and the links you created. Your configuration directory is separate from the installation; see [Files and Environment Variables](../files-and-environment-variables.md).
