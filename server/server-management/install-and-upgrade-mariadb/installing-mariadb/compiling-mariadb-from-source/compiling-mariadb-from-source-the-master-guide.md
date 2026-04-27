---
description: >-
  Complete step-by-step guide for compiling and building MariaDB from source on
  various flavors of Linux and on macOS.
---

# Compiling MariaDB From Source: The Master Guide

{% hint style="info" %}
This guide covers compiling MariaDB on Unix-like systems, including Linux and macOS. If you are building on Windows, please refer to the dedicated [Building MariaDB on Windows](building_mariadb_on_windows.md) guide.
{% endhint %}

This guide provides the universal workflow for building MariaDB Server from source code. While specific dependencies may vary by operating system, the core build process remains consistent across all modern platforms.

## Major Steps

{% stepper %}
{% step %}
#### Prepare Your Environment

Before you begin, your system must have the necessary compilers, build tools, and library headers.

> For details, see [Install Build Dependencies](compiling-mariadb-from-source-the-master-guide.md#prepare-your-environment-install-build-dependencies).
{% endstep %}

{% step %}
#### Obtain the Source Code

Decide whether you need the latest development branch or a specific stable release.

*   Option A: Git clone (best for developers)

    ```bash
    git clone --branch 11.8 https://github.com/MariaDB/server.git
    cd server
    ```
*   Option B: Source tarball (best for stability)

    Download the `.tar.gz` from the [official MariaDB downloads](https://mariadb.org/download/) and extract it:

    ```bash
    tar -xf mariadb-11.8.x.tar.gz
    cd mariadb-11.8.x
    ```

> For details on both options, see [Obtaining the Source Code](compiling-mariadb-from-source-the-master-guide.md#obtaining-the-source-code).
{% endstep %}

{% step %}
#### Configure the Build (CMake)

MariaDB uses out-of-source builds to keep the source tree clean. This is where you define installation paths and features.

1. Create a build directory: `mkdir build && cd build`
2.  Run CMake:

    ```bash
    cmake .. -DCMAKE_BUILD_TYPE=RelWithDebInfo
    ```

    * _Common flags like `-DCMAKE_INSTALL_PREFIX` or debug options go here._

> For common CMake configuration flags, see [Common CMake Configuration Flags](compiling-mariadb-from-source-the-master-guide.md#common-cmake-configuration-flags).
>
> For a configuration alternative to configuring CMake, see [The Quick Way: Using BUILD Scripts](compiling-mariadb-from-source-the-master-guide.md#the-quick-way-using-build-scripts).
{% endstep %}

{% step %}
#### Compile

Once configured, use the CMake build tool to compile the binaries. Using the `--parallel` flag speeds this up by using multiple CPU cores.

{% tabs %}
{% tab title="Linux" %}
```bash
cmake --build . --parallel $(nproc)
```
{% endtab %}

{% tab title="macOS" %}
{% code overflow="wrap" %}
```bash
cmake --build . --parallel $(sysctl -n hw.logicalcpu)
```
{% endcode %}
{% endtab %}

{% tab title="Universal" %}
For CMake 3.13+, run this:

{% code overflow="wrap" %}
```bash
cmake --build . --parallel 
```
{% endcode %}

Without a number, modern CMake automatically picks an appropriate number of jobs.
{% endtab %}
{% endtabs %}

> If you encounter build errors, see [Troubleshooting Common Build Errors](compiling-mariadb-from-source-the-master-guide.md#troubleshooting-common-build-errors).
{% endstep %}

{% step %}
#### Install and Initialize

After a successful build, you must prepare the data directory and system tables before the server can start.

1. Install: `sudo cmake --install .` (or run directly from the build directory for testing).
2. Create Data Directory: Ensure the `mysql` user exists and has permissions.
3. Initialize System Tables.
   1.  If running from the build directory (use this if you did _not_ run the `cmake` install command – in that case, you must run the script from within your build folder):

       ```bash
       ./scripts/mariadb-install-db --user=mysql --datadir=[path]
       ```
   2.  If you installed to the system (`sudo cmake --install ...`, in which case the `PATH` to `mariadb-install-db` is set):

       ```bash
       mariadb-install-db --user=mysql --datadir=[path]
       ```

> See [this section for conventional locations of the data directory](compiling-mariadb-from-source-the-master-guide.md#conventional-data-directory-locations) (`--datadir`).
{% endstep %}

{% step %}
#### Start and Verify

Launch the server and check that it is responsive.

```bash
./bin/mariadbd-safe --user=mysql &
./bin/mariadb -u root -p
```
{% endstep %}

{% step %}
#### Test the Build

Before putting your fresh build into production, verify it against the official test suite. MariaDB includes [MTR (MariaDB Test Run)](../../../../clients-and-utilities/testing-tools/mariadb-test/) for this purpose.

1.  Run Unit Tests: Quickly check the core logic.

    ```bash
    cmake --build . --target test
    ```
2.  Run Integration Tests (MTR): This launches actual server instances and runs thousands of SQL tests.

    ```bash
    cd mysql-test
    ./mysql-test-run.pl --parallel=$(nproc)
    ```

    * Pro-Tip: If a specific test fails, you can run it individually: `./mysql-test-run.pl alias`.
    * Note: You do not need to install MariaDB to the system to run these tests; they run entirely within the build directory.
{% endstep %}

{% step %}
#### After Building

After successfully building MariaDB from source, additional tasks can be found under [Post-Build](compiling-mariadb-from-source-the-master-guide.md#post-build).
{% endstep %}
{% endstepper %}

## Summary of the Build Workflow

| **Step** | **Action**          | **Primary Tool**       |
| -------- | ------------------- | ---------------------- |
| 1        | Install Build Tools | `apt` / `dnf` / `brew` |
| 2        | Download Source     | `git` / `wget`         |
| 3        | Configure Features  | `cmake`                |
| 4        | Compile Binaries    | `cmake --build`        |
| 5        | Initialize Database | `mariadb-install-db`   |

## Preparing Your Environment: Install Build Dependencies

> This section covers the details of step 1 (Prepare Your Environment).

To compile MariaDB, you need a set of core build tools and development headers for various libraries.

### Setting up the MariaDB Source Repository

{% hint style="info" %}
Setting up the MariaDB source repository is optional but recommended. If you want to build the MariaDB version that comes with your operating system, you can skip this subsection, though.
{% endhint %}

Adding the MariaDB Repository Tool into the workflow ensures that you are getting the dependencies specifically tailored for the version of MariaDB you want to build (for instance, 11.8), rather than whatever outdated version happens to be in your operating system's default upstream repository.

#### Using the MariaDB Repository Tool

While your operating system's default repositories contain many build tools, they may lack the specific library versions required for the latest MariaDB releases. Using the MariaDB Repository Tool ensures your environment is perfectly synced with the version you intend to build.

**1. Configure the Repository**

Use the [MariaDB Repository Configuration Tool](../../mariadb-package-repository-setup-and-usage.md) to generate the setup commands for your specific operating system and desired MariaDB version.

Example for Ubuntu 24.04 and MariaDB 11.8 (**don't copy this blindly** – the example uses the 11.8 release and a specific mirror; adjust these strings based on the output of the Repository Configuration Tool):

```bash
sudo apt-get install software-properties-common dirmngr
sudo apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xF1656F24C74CD1D8
sudo add-apt-repository --update --yes --enable-source \
'deb [arch=amd64] https://mirrors.xtom.com/mariadb/repo/11.8/ubuntu noble main'
```

**2. Install Tailored Dependencies**

Once the repository is active and the `source` lines are enabled, you can use the package manager to pull exactly what that specific MariaDB version requires:

{% tabs %}
{% tab title="Ubuntu / Debian" %}
```bash
sudo apt-get build-dep mariadb-11.8  # Replace with your target version
```
{% endtab %}

{% tab title="RHEL / CentOS / Fedora" %}
```bash
sudo dnf builddep mariadb-server
```
{% endtab %}
{% endtabs %}

**Advantages of Using the Repository Tool**

1. Version Accuracy: If MariaDB 11.x requires a newer `libssl` or `zstd` than what your operating system provides by default, the MariaDB repo often provides the correct headers.
2. Completeness: It automatically handles the "Source Repositories" issue because the `add-apt-repository` command includes the `--enable-source` flag by default.
3. Automation: It reduces the "Manual Package Table" from a primary task to a fallback for users who cannot or will not add external repositories.

### **The "Shortcut" Command**

Most Linux distributions allow you to install all necessary dependencies for the "official" build with a single command.

This requires that "source repositories" are enabled in your package manager. Enable them like this:

{% tabs %}
{% tab title="Ubuntu" %}
Run this command:

{% code overflow="wrap" %}
```bash
sudo add-apt-repository --update --yes --enable-source
```
{% endcode %}
{% endtab %}

{% tab title="Debian" %}
Edit `/etc/apt/sources.list` and uncomment lines starting with `deb-src`.
{% endtab %}

{% tab title="RHEL / Alma" %}
Run `dnf config-manager --set-enabled baseos-source appstream-source` .
{% endtab %}

{% tab title="Fedora" %}
Source repos are usually enabled by default, but check `dnf repolist` to verify.
{% endtab %}
{% endtabs %}

The shortcut command itself varies by operating system:

{% tabs %}
{% tab title="Ubuntu / Debian" %}
`sudo apt build-dep mariadb-server`
{% endtab %}

{% tab title="RHEL / CentOS / Fedora" %}
`sudo dnf builddep mariadb` (or `yum-builddep mariadb-server`)
{% endtab %}

{% tab title="SLES / openSUSE" %}
`sudo zypper source-install -d mariadb`
{% endtab %}

{% tab title="macOS" %}
Homebrew does not have a direct `build-dep` command. You can install the standard MariaDB build stack using:

```bash
brew install cmake git bison flex openssl zlib boost
```
{% endtab %}
{% endtabs %}

### **Manual Package Table**

If you are building a specific version or don't want to use the shortcut, use the list below to install the mandatory packages.

{% tabs %}
{% tab title="Ubuntu / Debian" %}
Use `apt` to install these tools:

* Build tools: `build-essential git cmake`
* Parser tools: `bison flex`
* Terminal/UI: `libncurses-dev`
* Security/SSL: `libssl-dev` or `gnutls-dev`
* Compression: `zlib1g-dev`
* Miscellaneous headers: `libaio-dev libboost-all-dev`
{% endtab %}

{% tab title="RHEL / CentOS / Fedora" %}
Use `dnf` (or `yum`) to install these tools:

* Build tools: `gcc-c++ git cmake`
* Parser tools: `bison flex`
* Terminal/UI: `ncurses-devel`
* Security/SSL: `openssl-devel`
* Compression: `zlib-devel`
* Miscellaneous headers: `libaio-devel boost-devel`
{% endtab %}

{% tab title="SLES / openSUSE" %}
Use `zypper` to install these tools:

* Build tools: `gcc-c++ git cmake`
* Parser tools: `bison flex`
* Terminal/UI: `ncurses-devel`
* Security/SSL: `libopenssl-devel`
* Compression: `libzlib-devel`
* Miscellaneous headers: `libaio-devel boost-devel`
{% endtab %}

{% tab title="macOS" %}
Use `brew` to install these tools:

* Build tools: `cmake git`
* Parser tools: `bison flex`
* Terminal/UI: `ncurses`
* Security/SSL: `openssl`
* Compression: `zlib`
* Miscellaneous headers: `boost`

The system-provided version of `bison` on macOS is often too old. After running `brew install bison`, you may need to add it to your `PATH`:

{% code overflow="wrap" %}
```bash
export PATH="/opt/homebrew/opt/bison/bin:$PATH"
```
{% endcode %}
{% endtab %}
{% endtabs %}

### **Optional Dependencies (Plugins & Features)**

If you plan to enable specific storage engines or features, install these additional packages:

| **Feature**       | **Dependency**      | **Package Name (Generic)**                                                    |
| ----------------- | ------------------- | ----------------------------------------------------------------------------- |
| S3 Storage Engine | `libcurl`           | `libcurl-devel` / `libcurl4-openssl-dev`                                      |
| GSSAPI (Kerberos) | `krb5`              | `krb5-devel` / `libkrb5-dev`                                                  |
| RocksDB / MyRocks | `snappy, lz4, zstd` | <p><code>snappy-devel, lz4-devel,</code></p><p><code>libzstd-devel</code></p> |
| Systemd Support   | `systemd`           | `systemd-devel` / `libsystemd-dev`                                            |
| Authentication    | `pam`               | `pam-devel` / `libpam0g-dev`                                                  |

## Obtaining the Source Code

> This section covers the details of step 2 (Obtain the Source Code).

Depending on your goal, you can either clone the repository using Git or download a stable source tarball.

### Option A: Git Clone (Recommended for Developers)

Using Git allows you to easily switch between versions and contribute patches. MariaDB uses submodules for certain components; you must initialize these for the build to succeed.

1.  Clone the specific branch:

    Choose a branch that matches the major version you need (for instance, `11.8`).

    ```bash
    git clone --branch 11.8 https://github.com/MariaDB/server.git
    cd server
    ```
2.  Initialize Submodules:

    This command downloads the source code for external storage engines and connectors.

    ```bash
    git submodule update --init --recursive
    ```

### Option B: Source Tarball (Best for Stability)

If you do not need version control, downloading a pre-packaged source tarball is simpler. Submodules are already included in the tarball, so no extra steps are required.

1. Download: Visit the [MariaDB Downloads page](https://mariadb.org/download/) and select the "Source" tab.
2.  Extract:

    ```bash
    tar -xf mariadb-11.8.x.tar.gz
    cd mariadb-11.8.x
    ```

### Key Takeaway: Git vs. Tarball

| Feature    | Git Clone                      | Source Tarball                |
| ---------- | ------------------------------ | ----------------------------- |
| Updates    | Easy (`git pull`)              | Manual (download new version) |
| Submodules | Requires manual initialization | Pre-included                  |
| History    | Full commit history available  | No history included           |
| Size       | Larger (includes `.git` data)  | Smaller                       |

## Common CMake Configuration Flags

> This section covers the details of step 3 (Configure the Build).

When running `cmake ..`, you can pass these options (using the `-D` prefix) to customize how MariaDB is built.

<table><thead><tr><th width="150.58984375">Category</th><th width="336.92578125">Flag</th><th>Description</th></tr></thead><tbody><tr><td>Install Path</td><td><code>-DCMAKE_INSTALL_PREFIX=/opt/mariadb</code></td><td>Defines where the server is installed (default: <code>/usr/local</code>).</td></tr><tr><td>Build Type</td><td><code>-DCMAKE_BUILD_TYPE=RelWithDebInfo</code></td><td>Options: <code>Release</code>, <code>Debug</code>, <code>RelWithDebInfo</code> (recommended).</td></tr><tr><td>Features</td><td><code>-DWITH_EMBEDDED_SERVER=ON</code></td><td>Builds the <code>libmariadbd</code> embedded library.</td></tr><tr><td>Storage Engines</td><td><code>-DPLUGIN_ROCKSDB=NO</code></td><td>Explicitly disables a specific storage engine (use <code>YES</code> to force enable).</td></tr><tr><td>Security</td><td><code>-DWITH_SSL=system</code></td><td>Use the system's OpenSSL (default). Options: <code>system</code>, <code>openssl</code>, <code>gnutls</code>.</td></tr><tr><td>Debugging</td><td><code>-DWITH_ASAN=ON</code></td><td>Enables AddressSanitizer to find memory leaks.</td></tr><tr><td>Standardization</td><td><code>-DBUILD_CONFIG=mysql_release</code></td><td>Configures the build to match the official MariaDB release binaries.</td></tr></tbody></table>

### Pro-Tip: Managing Plugins

Most plugins are auto-detected based on the dependencies you installed in [step 1](compiling-mariadb-from-source-the-master-guide.md#preparing-your-environment-install-build-dependencies). To see a full list of available options and their current status, run:

```bash
cmake .. -LH
```

## The Quick Way: Using BUILD Scripts

> This section covers alternative details of step 3 (Configure the Build).

If you don't want to manually toggle CMake flags, MariaDB includes a `BUILD/` directory containing pre-configured scripts for common development environments. These are especially useful for developers who need a specific setup (like a Debug build with Valgrind support) quickly.

### How to Use a BUILD Script

These scripts must be run from the root of the source directory (unlike the manual "out-of-source" CMake method).

```bash
# Example: Build an optimized 64-bit version with debugging symbols
./BUILD/compile-pentium64-debug
```

### Common Script Variants

Most scripts follow a naming convention: `compile-[architecture]-[type]`.

| Script                           | Best For...                                                        |
| -------------------------------- | ------------------------------------------------------------------ |
| `compile-pentium64-debug`        | Standard 64-bit development with debug symbols.                    |
| `compile-pentium64-max`          | Enables almost all features and plugins (highest compatibility).   |
| `compile-pentium64-valgrind-max` | Optimized for memory testing with Valgrind.                        |
| `compile-amd64-debian-build`     | Mimics the configuration used for official Debian/Ubuntu packages. |

### Adding Extra Flags

You can still pass custom CMake flags to these scripts using environment variables or arguments, though most users find the defaults sufficient for testing.

```bash
./BUILD/compile-pentium64-debug --extra-configs="-DCMAKE_INSTALL_PREFIX=/tmp/mariadb"
```

## Troubleshooting Common Build Errors

> This section covers details of step 4 (Compile).

Compiling from source often hits roadblocks. Here are the most common issues and how to fix them.

<table><thead><tr><th width="273.2265625">Error Message</th><th>Likely Cause</th><th>Solution</th></tr></thead><tbody><tr><td><code>CMAKE_CXX_COMPILER not found</code></td><td>Missing C++ compiler.</td><td>Install <code>g++</code> (Linux) or <code>clang</code> (macOS).</td></tr><tr><td><code>Bison version is too old</code></td><td>macOS default <code>bison</code> is outdated.</td><td><code>brew install bison</code> and update your <code>PATH</code>.</td></tr><tr><td><code>Could not find GSSAPI</code></td><td>Missing Kerberos headers.</td><td>Install <code>libkrb5-dev</code> or <code>krb5-devel</code>.</td></tr><tr><td><code>Could not find Curses</code></td><td>Missing terminal headers.</td><td>Install <code>libncurses-dev</code> or <code>ncurses-devel</code>.</td></tr><tr><td><code>No space left on device</code></td><td><code>/tmp</code> or build dir is full.</td><td>MariaDB requires ~5GB to 10GB of disk space for a full build.</td></tr></tbody></table>

### **The "Clean Slate" Command**

If you changed your CMake flags and things are getting weird, the best fix is to wipe the cache and start over.

```bash
# Inside your build directory
rm -rf *
cmake .. [your flags]
```

{% hint style="info" %}
Do not delete the source directory, only the contents of the `build` folder.
{% endhint %}

## Notes

### Conventional Data Directory Locations

This table lists typical locations of `--datadir`.

| Platform             | Conventional Data Directory                         |
| -------------------- | --------------------------------------------------- |
| Linux (General)      | `/var/lib/mysql`                                    |
| macOS (Homebrew)     | `/opt/homebrew/var/mysql`                           |
| macOS (Intel/Legacy) | `/usr/local/var/mysql`                              |
| FreeBSD              | `/var/db/mysql`                                     |
| Custom/Dev Build     | `~/mariadb-data` (or any folder owned by your user) |

## Post-Build

> This section covers optional additional things to do after building MariaDB successfully (step 8 (After Building)).

### Packaging

If you need to deploy MariaDB to multiple servers, you don't have to compile it on every machine. Instead, use MariaDB’s built-in packaging support to create a distributable package.

MariaDB uses [CPack](https://cmake.org/cmake/help/latest/module/CPack.html) (part of the [CMake](https://cmake.org/cmake/help/latest/) suite) to generate these packages.

1.  Configure for Packaging: To ensure the package follows standard filesystem hierarchies, use the `mysql_release` configuration.

    ```bash
    cmake .. -DBUILD_CONFIG=mysql_release
    ```
2.  Generate the Package: After the build is complete, run `cpack` from your build directory.

    ```bash
    # To create the default package for your OS (DEB on Ubuntu/Debian, RPM on RHEL)
    cpack -G DEB   # For Debian-based
    cpack -G RPM   # For RedHat-based
    cpack -G TGZ   # For a generic binary tarball
    ```
3. Result: You will find a file like `mariadb-11.x.x-linux-x86_64.deb` in your build directory, which can be installed via `dpkg -i` or `rpm -ivh`.
