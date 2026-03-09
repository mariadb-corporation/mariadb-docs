---
hidden: true
---

# Compiling MariaDB From Source: The Master Guide

{% hint style="info" %}
This guide covers compiling MariaDB on Unix-like systems, including Linux and macOS. If you are building on Windows, please refer to the dedicated [Building MariaDB on Windows](building_mariadb_on_windows.md) guide.
{% endhint %}

This guide provides the universal workflow for building MariaDB Server from source code. While specific dependencies may vary by operating system, the core build process remains consistent across all modern platforms.

## Major Steps

{% stepper %}
{% step %}
### Prepare Your Environment

Before you begin, your system must have the necessary compilers, build tools, and library headers.

* Core Requirements: You need `git`, `cmake`, `bison`, and a C++ compiler (GCC or Clang).
* Platform Dependencies: For specific `apt`, `dnf`, or `brew` commands for your OS, see the \[System Dependencies Reference] (Placeholder).
{% endstep %}

{% step %}
### Obtain the Source Code

Decide whether you need the latest development branch or a specific stable release.

*   Option A: Git Clone (Best for Developers)

    ```bash
    git clone --branch 11.4 https://github.com/MariaDB/server.git
    cd server
    ```
*   Option B: Source Tarball (Best for Stability)

    Download the `.tar.gz` from the [official MariaDB downloads](https://mariadb.org/download/) and extract it.
{% endstep %}

{% step %}
### Configure the Build (CMake)

MariaDB uses out-of-source builds to keep the source tree clean. This is where you define installation paths and features.

1. Create a build directory: `mkdir build && cd build`
2.  Run CMake:

    ```bash
    cmake .. -DCMAKE_BUILD_TYPE=RelWithDebInfo
    ```

    * _Common flags like `-DCMAKE_INSTALL_PREFIX` or debug options go here._
{% endstep %}

{% step %}
### Compile

Once configured, use the CMake build tool to compile the binaries. Using the `-j` flag speeds this up by using multiple CPU cores.

```bash
cmake --build . --parallel $(nproc)
```
{% endstep %}

{% step %}
### Installation and Initialization

After a successful build, you must prepare the data directory and system tables before the server can start.

1. Install: `sudo cmake --install .` (or run directly from the build directory for testing).
2. Create Data Directory: Ensure the `mysql` user exists and has permissions.
3.  Initialize System Tables:

    ```bash
    ./scripts/mariadb-install-db --user=mysql --datadir=/var/lib/mysql
    ```
{% endstep %}

{% step %}
### Start and Verify

Launch the server and check that it is responsive.

```bash
./bin/mariadbd-safe --user=mysql &
./bin/mariadb -u root -p
```
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

## Pro-Tip: The "Quick Way"

If you just want to test a bug fix quickly, see the \[Lazy Way to Build] section for a streamlined script that automates these phases.

