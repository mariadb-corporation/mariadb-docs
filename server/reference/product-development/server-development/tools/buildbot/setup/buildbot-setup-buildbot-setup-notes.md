---
description: >-
  A collection of miscellaneous technical notes and best practices for
  troubleshooting Buildbot installations.
---

# Buildbot Setup Notes

General setup instructions are available in the [BuildBot manual](https://docs.buildbot.net/current/manual/index.html), specifically in the section on [Setting up a build slave](https://docs.buildbot.net/current/manual/installation/worker.html).

In addition to installing BuildBot on the slave host, it is also necessary to install all the tools needed to branch MariaDB from Launchpad and compile it. It is a good idea to first manually branch the code from Launchpad and successfully build it, as otherwise a lot of time may be needed fixing things one at a time as new builds are started and fail in one way or the other.

Unfortunately, bzr is memory hungry, so at least 1 Gigabyte of memory is recommended (you may be able to squeeze through with less, but bzr is a real memory hog). A few Gigabytes of disk space are also needed to hold the build directory.

Here are some detailed instructions for various systems:

* [Buildbot Setup for Ubuntu-Debian](buildbot-setup-for-ubuntu-debian.md)
* [Buildbot Setup for MacOSX](buildbot-setup-buildbot-setup-for-macosx.md)
* [Buildbot Setup for Solaris](buildbot-setup-for-solaris-sparc.md)
* [Buildbot Setup for Windows](buildbot-setup-buildbot-setup-for-windows.md)

See the [Buildbot TODO](../buildbot-todo.md) for plans and ideas on improving Buildbot.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
