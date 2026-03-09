---
description: >-
  Explains how to provision and configure virtual machine instances specifically
  for Buildbot testing.
---

# Installing Correct Libraries for PAM and readline

Some additional/alternative libraries needs to be installed to handle readline\
and PAM correctly.

The newer libreadline is GPLv3 and so not compatible with the MariaDB/MySQL\
GPLv2 license. The PAM libraries are needed for the PAM plugin.

On the Centos and RHEL -build VMs, install the pam-devel package:

```
sudo yum install pam-devel
```

On all the Debian/Ubuntu -build virtual machines, install libpam0g-dev:

```
sudo apt-get install libpam0g-dev
```

On debian6/maverick/natty, install libreadline5-dev (replacing any\
libreadline6-dev already there):

```
sudo apt-get install libreadline5-dev
```

On oneiric (and any newer, eg. Debian 7 or Ubuntu 12.04), the package is\
called libreadline-gplv2-dev:

```
sudo apt-get install libreadline-gplv2-dev
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
