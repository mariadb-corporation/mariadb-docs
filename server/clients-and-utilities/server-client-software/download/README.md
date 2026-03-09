# Downloads

#### Latest Packages

Tarballs, source and binaries (Linux and Windows), and packages for some Linux distributions are available at [mariadb.org/download](https://mariadb.org/download/).

We hope that interested [community](https://mariadb.com/kb/en/community/) package maintainers will step forward, as others already have, to build packages for their distributions. We ask for strict adherence to your packaging system's best practices and invite you to create a [bug report](https://mariadb.org/jira) if our project impedes this in any way.

Instructions how to install the packages can be found [here](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/). See the [Includes MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/distributions-including-mariadb) documentation page for a list of which Linux distributions that include MariaDB.

#### Pre-Release Binaries

Binaries from our [Buildbot](/broken/spaces/WCInJQ9cmGjq1lsTG91E/pages/YDeiIobaziVWZCxk4IlA) system at [buildbot.mariadb.org](https://buildbot.mariadb.org) are available as containers on quay.io/mariadb-foundation/mariadb-devel:{major version}. Tags available are listed [here](https://quay.io/repository/mariadb-foundation/mariadb-devel?tab=tags).

These haven't passed through a full release process; however changes there have been reviewed and are considered complete by the server developers. Its recommend to use these for testing.

#### Getting the Source

The [mariadb.org/download](https://mariadb.org/download/) download page contains the source for all released binaries. You can find the latest source code at [server](https://github.com/MariaDB/server)

To retrieve the code, the [Git](/broken/spaces/WCInJQ9cmGjq1lsTG91E/pages/xRCtl21mrR3GrhPpJgOM) source control software offers\
the path of least resistance. If you are unfamiliar with git, please refer to\
the [git documentation](https://git-scm.com/doc) for an understanding\
of version control with git.

For instructions on creating a local branch of MariaDB, see the [Getting the MariaDB Source Code](getting-the-mariadb-source-code.md) page.

See the [Generic Build Instructions](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/compiling-mariadb-from-source/generic-build-instructions.md) page for\
general instructions on compiling MariaDB from the source.\
The [source](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/compiling-mariadb-from-source/) page has links to platform and distribution-specific\
information, including information on how we build the release packages.

#### Old Versions

Running the [most recent MariaDB version](https://mariadb.com/kb/en/new-and-old-releases/) is generally the best choice. Note that there are long-term releases, maintained for five years, short-term releases, maintained for one year, and rolling releases. However, some organizations still use old or very old versions of MariaDB. An\
upgrade would probably require important changes in their applications, and\
sometimes they don't even have the sources of those applications.

[mariadb.org/download/](https://mariadb.org/download?t=mariadb\&o=true) contains all historical releases.

There are source and repositories there. To use repositories see the following link:

* [RHEL and RPM distros](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/yum.md#pinning-the-mariadb-repository-to-a-specific-minor-release)
* [Debian/Ubuntu based distos](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-deb-files.md#pinning-the-mariadb-repository-to-a-specific-minor-release)

It is also possible to access Docker Official Images of MariaDB back to 5.5.40 when it became an official image ([available tags](https://soaphub.org/imagehub/?q=mariadb\&n=library\&p=1)).
