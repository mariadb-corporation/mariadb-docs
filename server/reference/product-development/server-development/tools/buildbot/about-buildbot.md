---
description: >-
  Provides a high-level overview of the Buildbot continuous integration system
  and its role in testing MariaDB.
---

# About Buildbot

## Overview

The goal of MariaDB Foundation Buildbot is to ensure that the MariaDB Server is being thoroughly tested on all supported platforms and environments. We are currently running 100 different configurations for the following platforms:

* x64 and x86
* aarch64
* ppc64le
* s390x

and operating systems:

* Debian 9, 10, 11 and Sid
* Ubuntu 16.04, 18.04, 20.04 and 21.04
* Fedora 33 and 34
* CentOS 7 and 8
* RHEL 7 and 8
* SLES 12 and 15
* OpenSUSE 15 and 42
* Windows
* AIX-7.2

Moreover, we run other ecosystem tests for:

* PHP
* DBdeployer
* MySqlJS
* PyMySQL

Packages built by buildbot can be downloaded from [here](https://ci.mariadb.org/).

## What is Buildbot?

The MariaDB Foundation uses Buildbot, a continuous integration and testing framework to test and create MariaDB Server packages. It is hosted onand ensures that each push to the MariaDB Server GitHub repository is properly tested.

## Who uses Buildbot?

Buildbot should be used by each MariaDB developer to ensure that the new changes that are made are properly tested on all supported platforms and environments. In order to enforce this, Buildbot is used for [branch protection](branch-protection-using-buildbot.md). However, even though branch protection is enabled, **only a selected few** builders are part of it. So, it is the developer's responsibility to monitor all the builders and make sure that everything is fine before making the final push to the main MariaDB branch.

## Buildbot keywords

* Changes/Repository - Any change that occurs in the source code (commit)
* Build Master - The main process that runs on a dedicated machine. It checks for changes in the source code and is in charge of scheduling builds
* Build - The actual configuration that is tested. It consists of a sequence of steps that define the actual test (e.g. get source code, compile, run tests, etc)
* Buildbot Worker - The process which waits for commands from the Build Master in order to run a build

## How does the Buildbot work?

As it comes to the Buildbot Master, we use a multi-master configuration. This means that we have multiple running master processes. So, we have a dedicated master for the user interface and several other that deal with looking for changes and scheduling builds.

Each time a push is made to the MariaDB Server Repository, it is detected by the buildbot master which schedules all the builds. Each build defines a different test configuration. We mainly use Docker Latent Workers which means that for each build, the master starts a Docker container on a remote machine. The container is configured to run the buildbot-worker process on startup. This process can now receive instructions from the master. In this way, by using latent workers there isn’t a buildbot-worker process continuously running on the worker machine. Instead, for each build a separate container is started.

Below, you can find a detailed step by step overview of what happens after a push is made to the MariaDB Server repository:

* Step 1: Detect a new change in the MariaDB Server repository
  * Trigger source tarball creation
* Step 2: Tarball creation
  * Clone the repository and create a source tarball corresponding to the latest changes
  * Trigger bintar builds
* Step 3: Bintar builds
  * Fetch the source tarball previously created
  * Compile
  * Test (mysql-test-run)
  * Save bintar
  * Trigger package creation builds
  * Trigger ecosystem builds
* Step 4.1: Package creation
  * Fetch source
  * Create packages
  * Save packages
  * Trigger installation builds
* Step 4.2: Ecosystem tests
* Step 5: Installation builds
  * Fetch packages
  * Test if they install successfully
  * Trigger upgrade builds
* Step 6: Upgrade builds
  * Test if the previously MariaDB Server version can be successfully upgraded to the current one

The information below refers to the old Buildbot (), and not the new Buildbot (). The information is old, outdated, or otherwise currently incorrect.

## Overview

The current state of the MariaDB trees with respect to build or test failures\
is always available from the [Buildbot setup](https://buildbot.askmonty.org/buildbot/) page.

* [MariaDB-5.5 waterfall status page.](https://buildbot.askmonty.org/buildbot/waterfall?branch=5.5)
* [MariaDB-10.0 waterfall status page.](https://buildbot.askmonty.org/buildbot/waterfall?branch=10.0)
* [MariaDB-10.1 waterfall status page.](https://buildbot.askmonty.org/buildbot/waterfall?branch=10.1)

The BuildBot setup polls the Launchpad trees every 5 minutes for\
changes. Whenever a new push is found in one of our trees, the new\
code is compiled and run through the test suite.

If all platforms are green after this, everything is good. If not, it\
means there is a problem with the push, and someone needs to look into\
it ASAP. If it was your push, then the someone who needs to look at it\
is you!

BuildBot is a generic, GPL'ed program providing a continuous\
integration test framework. For more information on BuildBot, see the [the BuildBot project homepage](https://buildbot.net/trac).

## Volunteering to Run a Build Slave

Many of our build hosts are run by [community](https://github.com/mariadb-corporation/docs-server/blob/test/en/community/README.md) members, and we are always\
looking for additional volunteers to help us cover additional platforms or\
build options in BuildBot.

If you are able to provide a spare machine for this purpose, your help is\
greatly appreciated! This is a good way to get involved without having to spend\
a lot of time on it. Get started by writing an email to 'developers (at)\
lists.mariadb.org' with an offer to run a BuildBot slave.

## Setting up the Slave BuildBot

See [buildbot-setup](setup/).

### Pausing mysql-test-run.pl

Sometimes you need to work when your computer is busy running tests\
for buildbot. We've added a new feature to the mysql-test-run.pl\
script which allows you to stop it temporarily so you can use your\
computer and then restart the tests when you're ready.

To do this, define the environment variable "MTR\_STOP\_FILE". Whenever\
the file specified by this environment variable exists, the\
mysql-test-run.pl script will stop as soon as it is able to do so\
(i.e. it won't stop immediately). When the file is removed, the\
mysql-test-run.pl script will continue from where it left off.

If you plan on using this feature you should also set the\
"MTR\_STOP\_KEEP\_ALIVE" environment variable with a value of 120. This\
will make the script print messages to buildbot every 2 minutes which\
will prevent a timeout.

## Database with Test Results

Buildbot saves the results of test runs in a database, to be used for\
enhanced reporting on web pages without need to change the Buildbot\
code, and for data mining when investigating test failures.

The database schema is documented under [Buildbot Database Schema](buildbot-buildbot-database-schema.md).\
The schema is likely to evolve as we gradually add more kinds of\
information.

For now, the data is not externally available. But the plan is to set\
up a slave database to replicate the data, and provide access (eg.\
remote database accounts) to members of the community with interesting\
ideas about how to present or mine this data, or who are just curious\
to play with it. If anyone has an interest in this, or wants to\
volunteer a slave host for this purpose, please send a [developers@lists.mariadb.org](mailto:developers@lists.mariadb.org).\
The more people show interest in this, the faster it is likely to happen!

## Reports

We are developing new reports fed off the test results in the\
database. These reports will be located [here](https://buildbot.askmonty.org/buildbot/reports/). The first\
report is the [Cross Reference](https://buildbot.askmonty.org/buildbot/reports/cross_reference)\
report. This report allows all test failures to be searched.

## Buildbot Maintenance

Here is some information on how our Buildbot installation is set up\
and maintained:

* The configuration file is included in the [Tools for MariaDB](https://github.com/MariaDB/mariadb.org-tools) repository.
* The building and testing of binary packages is documented on the [package-testing-with-buildbot-and-kvm](package-testing-with-buildbot-and-kvm.md) page.
* We developed a small tool, [runvm](runvm.md), which is used to do some\
  of the builds inside a virtual machine, mostly to test builds of binary\
  packages.
* The [BuildBot Development](buildbot-buildbot-development.md) page describes how we developed some of the\
  enhancements to BuildBot that we use and have contributed upstream.

## See Also

* The [Buildbot ToDo](buildbot-todo.md) page

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
