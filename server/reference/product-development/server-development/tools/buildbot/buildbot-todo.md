---
description: >-
  A roadmap and list of pending tasks, improvements, and known issues currently
  tracked for the Buildbot environment.
---

# Buildbot ToDo

## High-priority, High-ROI items

* Ability on the web pages to mark certain builds of high priority, so they\
  will be processed before others as build slaves become available. It must be\
  possible to mark pending builds so not only individually, but also by branch,\
  as well as by (branch,revision). The feature should probably interact in a\
  meaningful way with the existing "nextBuild" ability to prioritise builds\
  ([full.html#Prioritizing-Builds](https://buildbot.net/buildbot/docs/0.8.4/full.html#Prioritizing-Builds)). Eg.\
  it could set appropriate properties somewhere that would be available to the\
  nextBuild function.
* We need a way to kill all running builds, and remove all pending builds, for\
  a given combination of branch and revision. It is possible to manually cancel\
  a pending or running build, but this becomes extremely inconvenient when\
  there are many builders.
  * Comments from buildbot mailing list: "There is already a button (hidden on\
    the change page) for stopping all builds associated to a change.\
    Unfortunately, the only way to get to this page seems to be through the\
    waterfall." "Note that currently, the button on the change page only\
    cancels still-pending builds, it does not stop builds in progress."
* Fix problem when pushing multiple bzr revisions at one time:
  * Buildbot should wait a few moments before starting a build, and then start\
    building the latest (currently it seems to build the first revision\
    immedeately, and even often seems to not build the latest revision at all,\
    getting confused about the order)
  * When pushing a change that changes revision numbers, the grid display can\
    get really confused, would be nice to fix this somehow.
* Any failure other than compile/test failure should mean a re-run. Failures\
  like buildslave reboot or loss of connection or timeout of bazaar operation\
  should be interpreted as if the build has never happened, and the system\
  should re-try building.
* In the bzr source step, retry the checkout a couple of times if it fails (to\
  be more robust against temporary Launchpad problems, which we see a number\
  of). Could maybe be done as a general Buildbot optional feature for all\
  revision control systems supported, or maybe specific for the bzr depending\
  on what can work.
* Get PBXT test suite fixed in `--valgrind`; once that is done\
  include it in the list of main suites so that it is tested on all platforms\
  (and remove the special extra pbxt test steps in some Buildbot builds, as\
  they will no longer be needed).
* Load statistics. We need it to be able to see if adding another tree will\
  starve the buildbot:
  * Percentage of busy time for available slaves
  * Median/Max response time (How much time do I have to wait after I've pushed\
    for test run to complete)
* Fix that mysql-test-run uses `--skip-ssl` by default.
* Fix that `mysql-test-run.pl --mem` doesn't properly clean\
  up `/dev/shm/var*` (so that we can use `--mem`\
  and `--parallel` option to speed up the more powerful\
  machines).
* For triggered builds (ie. one builder makes a source tarball which another\
  builder consumes), make it so that the pushed changesets are also transfered,\
  so the blamelist on the build page works (currently the blame list is empty).
* Upgrade to Buildbot 0.8 on the master. Then use the facility to use a MariaDB\
  server as backend for both speedup (hopefully) and more flexible querying of\
  buildbot history.

## Lower priority items

* It should be easier to setup for a new user. Ideally, there should be one\
  tarball that one can download, unpack and run. Within the tarball there\
  should be a script and/or config files which allow to add the buildslave into\
  automatic startup. The following should not be there:
  * Dependence of buildslave on a load of python libraries. Ship them.
  * Same for bzr
  * Same for mysqld itself. Dl/make/make-install everything we need in the\
    buildbot directory.

If the above is not done, we'll never get much participation from old or\
unusual machines. The owners of such machines do not have the latest libraries,\
installing them requires some manual effort, which simply sets the bar too\
high.

* Check archivist observation/bug that build slave `uname` info disappears when\
  slave is disconnected.
* Self refresh at a time interval (ajax maybe to reduce transfer) so users can\
  know when to fire up a slave.
* In the waterfall page, second line from top is "current activity". When\
  displaying a particular branch ("?branch=5.1"), the "current activity" for\
  hosts that are currently building another branch could also display the name\
  of the branch (as a link to waterfall page for that branch) to avoid\
  confusion that it is active on the current branch.
* Run with `--valgrind-mysqld` instead\
  of `--valgrind`. Little point in Valgrinding mysqltest when we\
  in any case ignore any errors in that program.
* Show pending builds for a slave on the 'builders' page,\
  eg. [hardy-x86-rtai](https://askmonty.org/buildbot/builders/hardy-x86-rtai)
* Show dates in local time of the client. One way is with\
  Javascript: [5100-10878\_11-6016329.html](https://articles.techrepublic.com.com/5100-10878_11-6016329.html)\
  (would be nice if some dates were still shown when javascript is not\
  available).
* Check if InnoDB is fixed sufficiently to have no Valgrind leaks\
  with `innodb_use_sys_malloc`; if so remove hack\
  in `mysql-test-run.pl` to disable this in valgrind case.
* Fix problem that illegal regexp causes build exception (example:[err.text](https://buildbot.askmonty.org/buildbot/builders/sol-sparc-32/builds/157/steps/compile/logs/err.text)).\
  The problem is that Buildbot grabs regexps from the suppression file in the\
  MariaDB tree and tries to compile them; if this throws exception, then the\
  exception should be caught (and possibly warned about), not crash the whole\
  build.

## Improve binary package build and test

* Add `apt-get source mariadb-server` checking in buildbot (for package\
  testing).
* Add testing of bintar package with real start of server [mysqld\_safe](../../../../../clients-and-utilities/legacy-clients-and-utilities/mariadbd_safe.md) and\
  also test on different distro/version than what was built (eg\
  hardy<->jaunty).
* In package build, sign .debs with dummy key, to more accurately test the real\
  build process.
* Switch to build the bintar packages on centos 5, to work with older glibc\
  versions? Or maybe even Debian 4 which is older I think? But do the install\
  test in Buildbot also on other/newer distros (should probably test on several\
  in each build).
* Add a test step for .deb that tests upgrading from an earlier version of\
  MariaDB (currently we only check upgrade from MySQL).
* Add a 'follow log' feature to runvm (which does `ssh guest tail -f log > log`). Use this in the Buildbot packaging step that runs mysql-test-run.pl,\
  so that we can get mysqld.X.err.Y server logs available like for the non-kvm\
  builds.
* For runvm: add the options "-o UserKnownHostsFile=/dev/null -o\
  StrictHostKeyChecking=no" to the ssh command used to login to the guest vm,\
  so we do not get a login failure due to different host keys in different\
  guests.

## Staging trees

Idea is to set it up so that each developer/group has a stating tree. Any push\
to this tree will first get a full round of testing in Buildbot. If all results\
are green after this, it will automatically be pushed to the main tree. If\
another push gets in first, it will automatically merge the new stuff and\
re-try a full Buildbot test. If there is a problem (test failure or merge\
conflict), it will send mail with details.

* Get something working, simple initially.
* Staging tree per-captain
* `mysqltest --require` not-staging to speed up Valgrind

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
