---
name: mariadb-connector-cpp-install
description: "Installing and configuring MariaDB Connector/C++ — that MariaDB Connector/C is a hard prerequisite on Linux and must be installed first (3.1.1 or later for Connector/C++ 1.0, 3.3.3 or later for 1.1), while the Windows MSI brings it along; that Connector/C++ is downloaded per platform rather than pulled from the server package repository; that the binary tarball install is manual and easy to leave half-done, with the authentication plugin directory the piece most often missed; that the library is `-lmariadbcpp` and the public header is `mariadb/conncpp.hpp`; and that the build requires C++11. Use when installing, building, packaging, linking, or troubleshooting the setup of MariaDB Connector/C++."
---

# MariaDB Connector/C++: Installation and Configuration

*Last updated: 2026-10-15*

MariaDB Connector/C++ is the C++ client library for MariaDB, layered on top of MariaDB Connector/C. This skill covers installing it, satisfying its dependency, and getting an application to compile, link, and find its plugins at runtime. For the API itself, see **`mariadb-connector-cpp-usage`**.

> **Default context:** Assume the **1.0** stable line unless the user states otherwise. Where the 1.1 line differs, it is called out. Connector versions are independent of the MariaDB server version.

## What LLMs Often Miss

| If the agent writes / assumes… | …prefer the MariaDB form |
|---|---|
| Installs Connector/C++ on Linux and expects it to work | **MariaDB Connector/C is a hard prerequisite** and must be installed first. Connector/C++ **1.0** needs Connector/C **3.1.1 or later**; **1.1** needs **3.3.3 or later**. On Windows the MSI installs Connector/C for you |
| Reaches for `apt install mariadb-connector-cpp` or `dnf install` from the MariaDB repository | Connector/C++ is **not** part of the server package repository. Download the `.deb`, `.rpm`, tarball, or MSI for the platform from the MariaDB Connector/C++ download page, then install the downloaded file — note the leading `./` on Debian: `apt install ./mariadb-connector-cpp-*.deb`, run as root by the user |
| Runs the package manager or copies into `/usr` itself, as root | The agent does **not** run root steps. It hands them to the user — a single command to run, or a script to review and run — and waits; see **Privileged steps**. Unpacking the tarball into `$HOME/.local` needs no root |
| Installs from the binary tarball by copying `libmariadbcpp.so` and stopping | The tarball install is manual and has more parts than the library: the **headers** (`include/mariadb/`, including the `conncpp/` and `conncpp/compat/` subdirectories) and, most easily forgotten, the **plugin directory** (`lib/mariadb/plugin/`, or `lib64/mariadb/plugin/` in the RPM tarballs). Skip the plugins and the library builds and links fine, then fails at run time on authentication |
| Uses `/usr/lib` on an RPM distribution | Path layout differs: **`/usr/lib64`** and `/usr/lib64/mariadb/plugin` on CentOS, RHEL, and Rocky Linux; **`/usr/lib`** and `/usr/lib/mariadb/plugin` on Debian and Ubuntu |
| Links `-lmariadbcpp` but includes a Connector/C header | The public C++ header is **`mariadb/conncpp.hpp`**; the library is **`mariadbcpp`**. Including `mysql.h` pulls in the C API instead, and mixing the two in one translation unit is not the intended usage |
| Compiles with a pre-C++11 standard, or with `-std=c++98` inherited from an old project | The connector is built as **C++11** and its headers require it. Compile the application with `-std=c++11` or later |
| Installs on Windows and expects the loader to find the DLL | Add the directory containing the `mariadbcpp` library (for example `C:\Program Files\MariaDB\MariaDB C++ Connector 64-bit`) to the **`PATH`** environment variable |
| Assumes the connector reads `my.cnf` on its own | Configuration reaches the connector through **connection properties** and through Connector/C underneath it — nothing is read from an option file unless that is arranged at the Connector/C level |
| Treats the plugin directory as optional when packaging a container image | It is part of the deployable. Ship `mariadb/plugin/` alongside the library, or point the connector at it, or authentication plugins the server asks for will not load |
| Pins Connector/C++ to the MariaDB server version | There is no such correspondence. Pin Connector/C++ and Connector/C to each other using the compatibility rule above, independently of the server |

## Installing

### Privileged steps

Package installs and writes under `/usr` need root. The agent never runs these itself: privilege escalation hangs on a password prompt the agent cannot answer, and the decision to act as root belongs to the user.

- **One command** — show it exactly, ask the user to run it as root in their own terminal, and wait for confirmation.
- **Several commands** (Connector/C plus the package, or a system-wide tarball install) — write them into a script such as `install-mariadb-connector-deps.sh`, with no privilege escalation inside it, ask the user to review it and run it as root, and wait.
- **Afterwards** — verify without root: `mariadb_config --cc_version` for the Connector/C prerequisite, `ldconfig -p | grep mariadbcpp` (`/sbin/ldconfig` if it is not on `PATH`) for the library, and `ls /usr/include/mariadb/conncpp.hpp` for the headers.

### Linux, from RPM or DEB packages

Install Connector/C first, then the downloaded Connector/C++ package — a natural fit for one script:

```bash
# install-mariadb-connector-deps.sh — as root (the user runs this); keep the lines for the distribution
apt install libmariadb3 libmariadb-dev           # Debian, Ubuntu: Connector/C
apt install ./mariadb-connector-cpp-*.deb        # Debian, Ubuntu: Connector/C++, the downloaded file
dnf install MariaDB-shared MariaDB-devel         # RHEL, Rocky Linux: Connector/C
dnf install mariadb-connector-cpp-*.rpm          # RHEL, Rocky Linux: Connector/C++, the downloaded file
```

### Linux, from the binary tarball

All four groups of files matter — headers, the compatibility headers, the library, and the plugins. The library directory depends on the distribution family the tarball was built for: **`lib/mariadb`** in the Debian and Ubuntu tarballs, **`lib64/mariadb`** in the RHEL, Rocky Linux, and Fedora tarballs. Unpacked into a user prefix, none of it needs root (Connector/C must still be present — from packages or a `$HOME/.local` build, see **`mariadb-connector-c-install`**):

```bash
tar -xvzf mariadb-connector-cpp-*.tar.gz
cd mariadb-connector-cpp-*/
mkdir -p "$HOME/.local"
cp -R include lib* "$HOME/.local/"   # include/mariadb/{conncpp,conncpp/compat}; lib*/mariadb/{libmariadbcpp.so,libmariadb.so.3,plugin/*.so incl. parsec.so}
CPP_LIBDIR="$HOME/.local/lib/mariadb"     # Debian, Ubuntu
CPP_LIBDIR="$HOME/.local/lib64/mariadb"   # RHEL, Rocky Linux, Fedora — keep the line for the tarball
```

The application then compiles with `-I"$HOME/.local/include" -L"$CPP_LIBDIR" -Wl,-rpath,"$CPP_LIBDIR"`, and the plugins are found through `MARIADB_PLUGIN_DIR="$CPP_LIBDIR/plugin"` in the application's environment.

A system-wide install is a script for the user to review and run as root:

```bash
# install-mariadb-connector-cpp.sh — as root (the user runs this), from the unpacked tarball directory
install -d /usr/include/mariadb/conncpp /usr/include/mariadb/conncpp/compat
install include/mariadb/*                /usr/include/mariadb/
install include/mariadb/conncpp/*        /usr/include/mariadb/conncpp
install include/mariadb/conncpp/compat/* /usr/include/mariadb/conncpp/compat

# RHEL, Rocky Linux, Fedora: the tarball and the system both use lib64
install -d /usr/lib64/mariadb/plugin
install lib64/mariadb/libmariadbcpp.so /usr/lib64
install lib64/mariadb/plugin/*         /usr/lib64/mariadb/plugin

# Debian, Ubuntu: the tarball and the system both use lib — keep one of the two blocks
install -d /usr/lib/mariadb/plugin
install lib/mariadb/libmariadbcpp.so /usr/lib
install lib/mariadb/plugin/*         /usr/lib/mariadb/plugin
```

### Windows, from the MSI

The MSI installs Connector/C as part of the same run. Afterwards, add the installation directory to `PATH` so the loader can resolve `mariadbcpp` at run time.

### Building from source

```bash
cmake -B build -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_INSTALL_PREFIX="$HOME/.local" .
cmake --build build
cmake --install build      # user prefix, no root; a system prefix makes this a privileged step for the user
```

The library lands in `$HOME/.local/lib/mariadb` on Debian and Ubuntu and in `$HOME/.local/lib64/mariadb` on RHEL, Rocky Linux, and Fedora — the libdir follows the build host's GNU convention — so set `-L`, the rpath, and `MARIADB_PLUGIN_DIR` to match.

CMake 3.10 or newer is required, and the build targets C++11. If a `libmariadb` subdirectory is present the build uses it and installs that Connector/C alongside; otherwise it links against the Connector/C already installed on the system.

## Compiling an application against it

```bash
g++ -std=c++11 app.cpp -lmariadbcpp -o app
```

```cpp
#include <mariadb/conncpp.hpp>
```

If the headers landed somewhere other than `/usr/include`, add the corresponding `-I`; if the library did, add `-L` and make sure the runtime linker can find it (`ldconfig`, `LD_LIBRARY_PATH`, or an rpath).

## Configuration

Connection settings are supplied as properties when the driver creates a connection, rather than through a configuration file the library discovers on its own:

```cpp
sql::Driver* driver = sql::mariadb::get_driver_instance();

// Properties is taken by non-const reference, so it needs to be a named object
sql::Properties properties({
    {"user", "app"},
    {"password", "secret"},
    {"useTls", "true"},
    {"tlsCA", "/etc/ssl/certs/ca.pem"},
});

std::unique_ptr<sql::Connection> conn(
    driver->connect("jdbc:mariadb://localhost:3306/appdb", properties));
```

Because the transport underneath is Connector/C, the TLS behavior — and which TLS options are honored — follows whatever TLS library that Connector/C was built against. See **`mariadb-connector-c-install`** for that side of the configuration, including option files and certificate handling.

## Verifying the install

```cpp
std::unique_ptr<sql::Statement> stmt(conn->createStatement());
std::unique_ptr<sql::ResultSet> res(stmt->executeQuery("SELECT VERSION()"));
res->next();
std::cout << res->getString(1) << std::endl;   // columns are 1-based
```

A link error points at `-lmariadbcpp` or the library path; a load error at run time points at `PATH` (Windows) or the runtime linker path (Linux); an authentication failure right after connecting usually points at the missing plugin directory.

## See Also

- **`mariadb-connector-cpp-usage`** — using the API once it is installed: statements, result sets, transactions, batches
- **`mariadb-connector-c-install`** — installing and configuring the required underlying C client library
- Canonical reference on `mariadb.com/docs`, consult for edge cases not covered here: <https://mariadb.com/docs/connectors/mariadb-connector-cpp>

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
