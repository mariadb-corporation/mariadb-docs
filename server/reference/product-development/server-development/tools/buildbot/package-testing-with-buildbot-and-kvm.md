---
description: >-
  Explains how Buildbot utilizes Kernel-based Virtual Machines (KVM) to automate
  the testing of installation packages.
---

# Package Testing with Buildbot and KVM

## Buildbot Testing of Binary MariaDB Packages

This part of the Buildbot setup uses KVM virtual machines to build packages on a wide range of Linux distributions and test the different packages in various ways.

The builds run on a single host, which has an Intel Core i7 860 @ 2.80GHz CPU, 8 GByte of RAM, and a 500GByte disk. The build host is installed with Ubuntu 9.04 Server 64-bit.\
The current box is capable of running up to 3 builds in parallel. The entire set of 19 builds take around 3.5 hours to complete.

The build host has no virtual machines that are kept running when idle. Instead each build boots up and shuts down virtual machines on the fly as needed, using the [runvm](runvm.md) tool.

The details of the setup (installation) of the virtual machines are [here](setup/).

### Builds

(Please check the Buildbot configuration for details, in case this information becomes out of date).

At the time of writing, the builds done are these:

* Source tarball build (on a 32-bit Ubuntu 9.04 VM)
* Binary tarballs, i386 and amd64, on Ubuntu 8.04 VMs.
* Ubuntu, i386 and amd64: 8.04, 8.10, 9.04, 9.10, 10.04 (alpha).
* Debian, i386 and amd64, Debian 4 and Debian 5.
* Centos 5, i386 and amd64.

The builds use the packaging scripts from [OurDelta](https://launchpad.net/ourdelta).

In all builds (except for source tarball), the binary package is built, and subsequently attempted installed. The build is done on a virtual machine with compilers and other necessary build tools installed.\
The virtual machines are cloned from a reference image before each build (using the --base-image option to runvm). This way, the original images are not modified in any way, so there is no risk of "pollution" from previous builds, and no need to carefully clean up after a build or test.

The source tarball build is done in a virtual machine that is not reset after every build. This is to preserve the bzr shared repository setup inside the virtual machine. This way it is only necessary in each build to download new changes from Launchpad, which saves significant amounts of time (and Launchpad bandwidth). Since this particular build only works inside the source checkout directory, the risk of cross-build pollution is minimal.

The source tarball build is the only one that is triggered by bzr commits. After it has successfully built a source tarball, the tarball is uploaded to the Buildbot master, and all of the other builders are triggered to start building. Each will download the source tarball from the master and build from that rather than from a bzr checkout (this is the correct way, as we want to ensure that users building from the source tarball themselves get the same results as the packages built by us).

Since we use the OurDelta scripts, which use a "bakery" for the build scripts similar to a source tarball, there is a bakery tarball similarly generated from bzr and uploaded to the master.

Because of this triggering, it is not possible to manually force a Buildbot run on "latest bzr version" on the non-tarball builders. Instead to force a build, it is necessary to set the build properties for source tarball and bakery manually to the files one wants to tests. But it is often easier just to pick an existing build (with correct tarball) and use the "resubmit build" feature instead. Another option is to force build on the tarball build only; it will then in turn trigger all of the other builds.

### Basic Install Test

On all builds (except source tarball), after the build a test is performed where the resulting package is installed in a virtual machine and basic testing is done.

The install test is done in a separate virtual machine from the one in which it was built, with no build tools and a very minimal install (to check that we have no hidden dependencies). The install test is currently _very_ basic, basically just create a table and insert a row (it would be a nice ToDo to extend this testing to a more complete "smoke test").

Note that for .deb (Debian and Ubuntu), we set up a small fake local apt repository, so that we can properly test that ''apt-get install'' is able to pull in any extra dependencies without anything special needed on the part of the user.

### Upgrade Tests for .deb Packages

On .deb builders (Debian and Ubuntu), we do three additional upgrade tests.

Two of them install the newly built MariaDB packages on top of an already installed MySQL package (the default MySQL package on that particular distro version), as well as on top of an earlier version of the MariaDB packages. For this, separate virtual machine images are used, based on the one used in the install test, but in addition with MySQL/MariaDB pre-installed.

The third test is performed on a clean image without any pre-installed MySQL or MariaDB packages. The test installs the latest available release of the same major version from MariaDB public repo, and then runs dist-upgrade using the local repo as a source of the new packages. The main goal of this test is to check that regular system upgrades performed via dist-upgrade work as expected in regard to MariaDB server.

In all tests, some very basic test data is also created in the installation, so we can test that replacing the old server installation with our new MariaDB package does not nuke the user's existing data! The test is also useful to check that the upgrade runs correctly with respect to dependencies etc, something that is quite complex to get right with the .deb packaging.

### Upgrade Tests for .rpm Packages

On .rpm builders (CentOS, Fedora, RHEL, SLES, openSUSE) we have numerous upgrade tests, although only a small portion of them is run for every branch.

All tests upgrade an already existing installation to the new MariaDB packages. The variables are:

* what kind of existing installation is being upgraded: MariaDB server, MariaDB Galera, MySQL, Percona server, or mysql/mariadb installations provided by distributions;
* which command is used for upgrade: it can either be performed via upgrade/update (depending on the package manager), or install, or dist-upgrade;
* which packages are installed and upgraded: it can be a minimal set, server + client (plus whatever dependencies they bring), or a full set of packages.

In some cases, the tests can also set additional command-line options or environment variables for the package manager. It is normally done when the default installation does not work, and the package manager suggests using a different set of parameters.

Each test uses a clean VM image, installs an initial set of packages, and then uses one of the commands to upgrade the installation. It further checks that the server is upgraded, restarted and is reachable.

### mysql-test-run.pl Test

On the .deb builders (Debian and Ubuntu), we additionally do a full mysql-test-run.pl test run. This is done using the package _mariadb-test_.

Note that currently, due to [Bug #491349](https://bugs.launchpad.net/bugs/491349), on newer Ubuntus the default apparmor profile prevents running mysql-test-run.pl. Until this is fixed, the tests need to uninstall apparmor before running the test suite.

## See Also

* [Buildbot Setup for Virtual Machines](setup/buildbot-setup-for-virtual-machines/)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
