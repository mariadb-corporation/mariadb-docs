---
description: >-
  Instructions for building MariaDB binaries from a source RPM package using
  tools like `rpmbuild`, `yum`, or `dnf`.
---

# Building MariaDB from a Source RPM

For some distributions you can build MariaDB from a source RPM. (See also [Why Source RPMs (SRPMs) Aren't Packaged For Some Platforms](../binary-packages/rpm/why-source-rpms-srpms-arent-packaged-for-some-platforms.md)).

You can build it as follows:

### using `dnf`

On RHEL8 you might need to start with:

```bash
sudo dnf config-manager --set-enabled codeready-builder-beta-for-rhel-8-x86_64-rpms
```

Then, on all `dnf` distributions:

```bash
sudo dnf install rpm-build perl-generators
    dnf download --source MariaDB
    sudo dnf builddep MariaDB-*.src.rpm
    rpmbuild --rebuild MariaDB-*.src.rpm
```

### using `yum`

```bash
sudo yum install rpm-build yum-utils
    yumdownloader --source MariaDB
    sudo yum-builddep MariaDB-*.src.rpm
    rpmbuild --rebuild MariaDB-*.src.rpm
```

### using `zypper`

```bash
sudo zypper in rpm-build
    sudo zypper si MariaDB
    sudo rpmbuild -bb /usr/src/packages/SPECS/MariaDB.spec
```

Or (to avoid building as root):

```bash
sudo zypper in rpm-build
    sudo zypper si -d MariaDB
    zypper --pkg-cache-dir=`pwd` si --download-only MariaDB
    rpmbuild --rebuild mariadb/srpms/MariaDB-*.src.rpm
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
