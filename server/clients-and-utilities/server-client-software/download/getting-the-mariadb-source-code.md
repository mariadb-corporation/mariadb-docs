# MariaDB Source Code

## Checking out the Source with Git

The MariaDB source is hosted on GitHub: [server](https://github.com/MariaDB/server). You can get a copy with:

```
git clone https://github.com/MariaDB/server mariadb-server
```

If you want a source tarball for a specific released MariaDB version, you can find it at [downloads.mariadb.org](https://downloads.mariadb.org).

At any given time, developers is working on their own branches locally or on GitHub, with the main MariaDB branches receiving pushes less often.

The main MariaDB branches are:

* [main](https://github.com/MariaDB/server/tree/main)
* [12.3](https://github.com/MariaDB/server/tree/12.3)
* [12.2](https://github.com/MariaDB/server/tree/12.2)
* [12.1](https://github.com/MariaDB/server/tree/12.1)
* [12.0](https://github.com/MariaDB/server/tree/12.0)
* [11.8](https://github.com/MariaDB/server/tree/11.8)
* [11.7](https://github.com/MariaDB/server/tree/11.7)
* [11.4](https://github.com/MariaDB/server/tree/11.4)
* [10.11](https://github.com/MariaDB/server/tree/10.11)
* [10.6](https://github.com/MariaDB/server/tree/10.6)

Source repositories for the MariaDB Connectors are:

* [MariaDB Connector/C](https://github.com/mariadb-corporation/mariadb-connector-c)
* [MariaDB Connector/C++](https://github.com/mariadb-corporation/mariadb-connector-cpp)
* [MariaDB Connector/J](https://github.com/mariadb-corporation/mariadb-connector-j)
* [MariaDB Connector/Node.js](https://github.com/mariadb-corporation/mariadb-connector-nodejs)
* [MariaDB Connector/ODBC](https://github.com/mariadb-corporation/mariadb-connector-odbc)
* [MariaDB Connector/Python](https://github.com/mariadb-corporation/mariadb-connector-python)

See also:

* [Using git](/broken/spaces/WCInJQ9cmGjq1lsTG91E/pages/xRCtl21mrR3GrhPpJgOM) page for instructions on how to use git to check out the source code and switch between the various branches.
* [Compiling MariaDB from source](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/compiling-mariadb-from-source/)

{% hint style="danger" %}
The rest of this page contains information on checking out the MariaDB source from Launchpad. As the current source is now on GitHub, the information is mainly of historical interest and not useful for current development.
{% endhint %}

The instructions on this page will help you download your own local branch of the MariaDB source code repository with the full revision history. If you want a tarball of the source without the revision history, see the [MariaDB download page](https://mariadb.com/downloads/).

## Checking out the Source with Bazaar

If you simply want to browse the source code, you can do so from [maria](https://code.launchpad.net/maria).

### Prerequisites

You need [Bazaar](https://bazaar-vcs.org) for revision control.

### Instructions

1. Prepare a directory to keep your MariaDB code in:

```
mkdir $repo 

# where $repo is some directory (ex: ~/repos)

cd $repo
bzr init-repo maria 

# this creates ~/repos/maria

```

1. Get a clean local copy of the Maria repo with:

```
cd $repo/maria 

# (ex: ~/repos/maria)

bzr branch lp:maria trunk
```

The above will give you the latest stable MariaDB version.\
If you want to get another release use lp:maria/5.2, lp:maria/5.3...\
For a complete list, go to [Launchpad](https://launchpad.net/~maria-captains/) and choose ['Code'](https://code.launchpad.net/~maria-captains) from the top menu on the page.

* Note: The initial branch operation can take a long time depending on the speed of your Internet connection and the load on launchpad. For this initial branch you need to download over a gigabyte of data.
* Note: Bzr is written in Python and very slow for initial checkout. Even on a fast connection, expect to need 1-2 GByte of RAM and possibly several CPU hours for the checkout.

1. If you get an error like:

```
bzr: ERROR: Unknown repository format: 'Bazaar RepositoryFormatKnitPack6 (bzr 1.9)'
```

then the version of bzr you are using is too old. Using [version 1.12](https://bazaar-vcs.org/Download) or higher will fix this error.

1. If you have upgraded your bzr and are unable to successfully branch from launchpad, try using the source tree tarball (below) instead.
2. You can see the current history with:

```
cd $repo/maria/trunk
bzr log | less
```

1. If you are going to be hacking on the MariaDB source code. See the [Contributing Code](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/community/contributing-participating/contributing-code) page for help.
2. If you just want to compile MariaDB at this point, see the [Compiling MariaDB](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/compiling-mariadb-from-source/generic-build-instructions.md) page.

## Source Tree Tarball

For those that have trouble branching MariaDB from Launchpad we have created a\
tarball of a complete repository of the MariaDB tree.

### Prerequisites

You need [Bazaar](https://bazaar-vcs.org) to work with the repository.

### Using the Source Tree Tarball

1. Download the mariadb-shared-repo.tgz file from [one of the MariaDB mirrors](https://downloads.mariadb.org/mariadb-misc/1.0.0/).

* The file is 267MB, so the download may take a long time to complete depending on your Internet connection.

1. The .tgz file contains a .bzr directory. The parent directory of\
   this .bzr directory is (or becomes) a shared repository containing the\
   MariaDB source code. It is recommended to create a new directory for\
   this, so the next step is to create a directory to house the\
   repository. Call this directory anything you like ("maria", "mariadb",\
   "my", "src", etc...). Once created, cd into the directory and untar\
   the file. Here is an example using the name "mariadb" for the new\
   directory, with the directory located in a directory called "src" in\
   the home directory of the current user, and the\
   mariadb-shared-repo.tgz file located in a directory named Downloads\
   (also in the current user's home directory):

```
mariadbdir="mariadb"
downloadsdir="${HOME}/Downloads"
sourcecodedir="${HOME}/src"
cd ${sourcecodedir}
mkdir ${mariadbdir}
cd ${mariadbdir}
tar -zxvf ${downloadsdir}/mariadb-shared-repo.tgz
```

1. After the untar step you will have a bzr shared repository, but not\
   a working tree. While in the shared repository directory, use the`bzr branch` command to branch the MariaDB trees you are\
   interested in. For example:

* `bzr branch lp:maria/5.2`
* `bzr branch lp:maria`

1. Thanks to the repository, either of the above commands will complete very fast.
2. Before working with the code, make sure you pull down the latest version of the source code:

```
cd mariadb-5.2 #or to wherever your MariaDB tree is
bzr pull
```

1. You can now use this source tree as if you had branched it from launchpad directly.

## Alternate Bazaar Instructions

The following alternative instructions are what we have used for setting up\
repositories on our build machines in [buildbot](/broken/spaces/WCInJQ9cmGjq1lsTG91E/pages/YDeiIobaziVWZCxk4IlA).

### Shell Variables

To streamline later steps, we start by setting several shell variables. Set the\
values of the BZR and WORK\_DIR variables to the appropriate values for your\
Linux distribution. The rest of the variables in this section should not need\
to be changed.

#### Binaries:

```
BZR="/usr/bin/bzr"
```

#### Directories

```
WORK_DIR="${HOME}/work/monty_program"

MARIA_DIR=${WORK_DIR}/mariadb
MARIA_REPO="lp:maria"
MARIA_MASTER="${MARIA_DIR}/maria-local-master"
MARIA_WORK="${MARIA_DIR}/maria"

PACKAGING_DIR=${WORK_DIR}/packaging
PACKAGING_REPO="lp:~maria-captains/ourdelta/ourdelta-montyprogram-fixes"
PACKAGING_MASTER="${PACKAGING_DIR}/ourdelta-montyprogram-fixes-local-master"
PACKAGING_WORK="${PACKAGING_DIR}/ourdelta-montyprogram-fixes"
```

### Source Checkout

Initialize your bzr working directories, if not done already:

```
$BZR init-repo $MARIA_DIR
$BZR init-repo $PACKAGING_DIR
```

Check out MariaDB sources:

```
$BZR branch $MARIA_REPO $MARIA_MASTER
$BZR branch $MARIA_MASTER $MARIA_WORK
```

Check out packaging sources (only for [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.3/changes-improvements-in-mariadb-5-3) and below):

```
$BZR branch $PACKAGING_REPO $PACKAGING_MASTER
$BZR branch $PACKAGING_MASTER $PACKAGING_WORK
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
