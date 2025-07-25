# Tools Available for Developing on the MariaDB Code

The code is hosted on [server](https://github.com/MariaDB/server). You can\
branch the latest code from there, and you can also push your own changes as a\
new branch that can be shared with others.

[Building the code from source](https://github.com/mariadb-corporation/docs-server/blob/test/server-management/install-and-upgrade-mariadb/compiling-mariadb-from-source/README.md) is done with standard Unix tools: CMake (or autotools for MariaDB versions below 5.5), Gnu Make, GCC (or other C/C++ compiler on some systems). On [Windows](https://github.com/mariadb-corporation/docs-server/blob/test/server-management/install-and-upgrade-mariadb/compiling-mariadb-from-source/building_mariadb_on_windows.md), CMake and Visual Studio are used.

The current state of the source with respect to build/test failures can be seen\
in [buildbot](../../../../development-articles/general-info/tools/buildbot/).

For project management and bug tracking, we use [JIRA](../../../../development-articles/general-info/tools/jira.md).

The [source](https://github.com/mariadb-corporation/docs-server/blob/test/server-management/install-and-upgrade-mariadb/compiling-mariadb-from-source/README.md) page has links to instructions on setting up a full development environment, if you are interested.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
