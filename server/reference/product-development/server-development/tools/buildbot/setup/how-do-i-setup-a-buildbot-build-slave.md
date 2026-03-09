---
description: >-
  A foundational tutorial on the general process of creating and connecting a
  new build worker (slave).
---

# Setup of a Buildbot Build Slave

These build instructions should in general be platform agnostic. It is based on a post by Adam M. Dutko on maria-discuss. See the [list archive](https://lists.launchpad.net/maria-discuss/msg00372.html).

To setup a build slave, the basic outline is:

1. Install Python (2.4 or later)
2. Install Twisted (twistedmatrix.com 8.0.x or later) - need Core, Mail, Web and Words (possibly Conch too)
3. Install ZopeInterface ([ZopeInterface](https://www.zope.org/Products/ZopeInterface))
4. Install all the necessary compiler/build components.
5. Install Buildbot
6. Install [Git](../../using-git-with-mariadb/using-git.md) and make sure you can clone from the main project
7. Get a username/login and password from the buildmaster (dbart on [Libera.Chat](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/irc/README.md))
8. Verify your buildbot can talk to the buildbot master instance and can run builds.

The following links will also help:

1.
2. [buildbot-setup-buildbot-setup-notes](buildbot-setup-buildbot-setup-notes.md)
3. [about-buildbot](../about-buildbot.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
