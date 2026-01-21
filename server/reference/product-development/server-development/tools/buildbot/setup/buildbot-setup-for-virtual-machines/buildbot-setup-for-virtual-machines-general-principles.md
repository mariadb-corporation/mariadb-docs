---
description: >-
  Explains how to provision and configure virtual machine instances specifically
  for Buildbot testing.
---

# Buildbot Setup for Virtual Machines - General Principles

The installations are kept minimal, picking mostly default options. This helps\
ensure our stuff works on default installs, and also saves effort during the\
creation of the virtual machines.

Since most of the logic happens in the Buildbot slave on a host machine, and\
inside the Buildbot master, there is no need to install Buildbot or other\
similar complex stuff inside the VMs.

## ssh

The virtual machines are configured with ssh access. An account called\
'buildbot' is created, with passwordless login (using ssh public key\
authentication), and with passwordless sudo access (needed for automated\
scripting). The public key for user buildbot is installed in every VM, and the\
private key is added to the account running the Buildbot master on the host\
machine.

To generate the ssh keys:

```
ssh-keygen -t dsa
```

Leave the passphrase empty. Run this as the user running the Buildbot slave on\
the KVM host machine. The resulting /.ssh/id\_dsa.pub will be needed below for\
each virtual machine install.

## Serial port

The vms are configured to use the (emulated) serial port as the console. When\
running KVM on the host, the console then maps to the stdin/stdout. This is\
useful to get kernel log messages available to easier debug any problems. The\
bootloader Grub is similarly configured to use the serial port.

The vms are also set up to give a login prompt on the serial port (running\
getty). In retrospect this has proven not really needed, as if needing to\
manually log in and investigate things, it is often as easy to just run KVM in\
graphics mode. It may be useful in cases where the host machine is remote\
though (in this case graphics mode does still work but can be a bit slow).

To configure for serial console, the following two files are referenced below,\
and should be prepared in advance:

### `ttyS0`

```
# ttyS0 - getty
#
# This service maintains a getty on ttyS0 from the point the system is
# started until it is shut down again.

start on stopped rc2
start on stopped rc3
start on stopped rc4
start on stopped rc5

stop on runlevel 0
stop on runlevel 1
stop on runlevel 6

respawn
exec /sbin/getty 115200 ttyS0
```

### `ttyS0.conf`

```
# ttyS0 - getty
#
# This service maintains a getty on ttyS0 from the point the system is
# started until it is shut down again.

start on stopped rc RUNLEVEL=[2345]
stop on runlevel [!2345]

respawn
exec /sbin/getty -L 115200 ttyS0 vt102
```

## Unattended MariaDB install on Debian/Ubuntu

### my.seed

The MariaDB (and MySQL) package on Debian and Ubuntu prompts the user about the\
root password to set. We want to test this important step, but we do not want\
the prompt of course. To do this we use the following configuration file for\
defaults for debconf. This file is needed in the steps below under the name\
"my.seed" (be careful to preserve it exactly as here, including trailing space\
and tab characters!)

```
mariadb-server-5.1	mysql-server/root_password_again	password	rootpass
    mariadb-server-5.1	mysql-server/root_password	password	rootpass
    mariadb-server-5.1	mysql-server/error_setting_password	error	
    mariadb-server-5.1	mysql-server-5.1/nis_warning	note	
    mariadb-server-5.1	mysql-server-5.1/really_downgrade	boolean	false
    mariadb-server-5.1	mysql-server-5.1/start_on_boot	boolean	true
    mariadb-server-5.1	mysql-server-5.1/postrm_remove_databases	boolean	false
    mariadb-server-5.1	mysql-server/password_mismatch	error	
    mariadb-server-5.1	mysql-server/no_upgrade_when_using_ndb	error
```

For some background see [here](https://blog.hjksolutions.com/articles/2007/07/27/unattended-package-installation-with-debian-and-ubuntu).\
The file my.seed can be generated from an existing install using\
debconf-get-selections.

### sources.append

For Debian/Ubuntu, we add a local repository to the list of apt source to be\
able to test `apt-get install`. For this, the following file "sources.append"\
must be prepared:

```
deb file:///home/buildbot/buildbot/debs binary/
deb-src file:///home/buildbot/buildbot/debs source/
```

## Emulation options

The default network card emulated by KVM has poor performance. To solve this we\
instead use the "virtio" network device, using the KVM options "-net\
nic,model=virtio -net user". Except on Debian 4, which has an old kernel\
without support for virtio. Background info [here](https://episteme.arstechnica.com/eve/forums/a/tpc/f/96509133/m/303006642931).

A detail is that some 32-bit vms crashed during boot with default options. This\
was fixed by using the kvm "-cpu qemu32,-nx" option. Some background\
information [here](https://bugs.launchpad.net/ubuntu/+source/kvm/+bug/396219).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
