---
description: >-
  Explains how to provision and configure virtual machine instances specifically
  for Buildbot testing.
---

# Buildbot Setup for Virtual Machines - FreeBSD 9.2

## Base Install

```
qemu-img create -f qcow2 /kvm/vms/vm-freebsd92-amd64-serial.qcow2 15G
qemu-img create -f qcow2 /kvm/vms/vm-freebsd92-i386-serial.qcow2 15G
```

Start each VM booting from the server install iso one at a time and perform\
the following install steps:

```
kvm -m 2048 -hda /kvm/vms/vm-freebsd92-amd64-serial.qcow2 -cdrom /kvm/iso/freebsd/9.2/FreeBSD-9.2-RELEASE-amd64-dvd1.iso -boot d -smp 2 -cpu qemu64 -net nic,model=virtio -net user,hostfwd=tcp:127.0.0.1:2283-:22
kvm -m 2048 -hda /kvm/vms/vm-freebsd92-i386-serial.qcow2 -cdrom /kvm/iso/freebsd/9.2/FreeBSD-9.2-RELEASE-i386-dvd1.iso -boot d -smp 2 -cpu qemu64 -net nic,model=virtio -net user,hostfwd=tcp:127.0.0.1:2284-:22
```

Once running you can connect to the VNC server from your local host with:

```
vncviewer -via ${remote_host} localhost
```

Replace `${remote_host}` with the host the vm is running on.

{% hint style="info" %}
When you activate the install, vncviewer will disconnect after a bit with a complaint about the rect being too large. This is fine. The installer has just resized the vnc screen. Simply reconnect.
{% endhint %}

Install, picking default options mostly, with the following notes:

* Keymap Selection: Do not set non-default key mapping
* Hostname: to freebsd-92-amd64 or freebsd-92-i386
* Distribution Select: deselect "games", leave "ports" selected
* Partitioning: Guided and use the entire disk
  * Accept the default partitioning (Finish then Commit)
* Archive Extraction: ...wait while installer installs the OS...
* Network Configuration: choose `vtnet0`
  * configure ipv4 w/ DHCP
  * do not configure ipv6
* System Configuration: leave sshd selected, don't select the others
* Dumpdev Configuration: do not enable crash dumps
* add a buildbot user
  * add user to 'wheel' group
* Final Configuration: Apply configuration and exit
* Manual Configuration: yes to opening a shell
  * `echo 'console="comconsole"' >> /boot/loader.conf`
  * Edit /etc/ttys and change off to on and dialup to vt100 for the ttyu0 entry.
  * `shutdown -p now`

Now that the VM is installed, it's time to configure it.\
If you have the memory you can do the following simultaneously:

```
kvm -m 2048 -hda /kvm/vms/vm-freebsd92-amd64-serial.qcow2 -boot c -smp 2 -cpu qemu64 -net nic,model=virtio -net user,hostfwd=tcp:127.0.0.1:2283-:22 -nographic
kvm -m 2048 -hda /kvm/vms/vm-freebsd92-i386-serial.qcow2 -boot c -smp 2 -cpu qemu64 -net nic,model=virtio -net user,hostfwd=tcp:127.0.0.1:2284-:22 -nographic

ssh -p 2283 localhost
ssh -p 2284 localhost

su -

cd /usr/ports/security/sudo; make install clean # accept defaults
visudo # uncomment the '# %wheel ALL=(ALL) NOPASSWD: ALL' line
exit

cd /usr/ports/ports-mgmt/portmaster; sudo make install clean # select both autocomplete options

ssh hasky.askmonty.org
exit
sudo su buildbot -
ssh hasky.askmonty.org
exit
exit
exit

scp -P 2283 /kvm/vms/authorized_keys localhost:.ssh/
scp -P 2283 /kvm/vms/authorized_keys buildbot@localhost:.ssh/

scp -P 2284 /kvm/vms/authorized_keys localhost:.ssh/
scp -P 2284 /kvm/vms/authorized_keys buildbot@localhost:.ssh/

ssh -p 2283 localhost
ssh -p 2284 localhost

sudo portsnap fetch extract
sudo portsnap fetch update
sudo portmaster -Da

sudo shutdown -p now
```

## VMs for building BSD bintars

```
for i in '/kvm/vms/vm-freebsd92-amd64-serial.qcow2 2283 qemu64' '/kvm/vms/vm-freebsd92-i386-serial.qcow2 2284 qemu64' ; do \
  set $i; \
  runvm --user=buildbot --logfile=kernel_$2.log --base-image=$1 --port=$2 --cpu=$3 "$(echo $1 | sed -e 's/serial/build/')" \
    "cd /usr/ports/devel/libevent;     sudo make install clean BATCH=yes" \
    "cd /usr/ports/devel/boost-all;    sudo make install clean BATCH=yes" \
    "cd /usr/ports/devel/cmake;        sudo make install clean BATCH=yes" \
    "cd /usr/ports/devel/thrift/;      sudo make install clean BATCH=yes" \
    "cd /usr/ports/devel/bzr/;         sudo make install clean BATCH=yes" \
    "cd /usr/ports/devel/bison/;       sudo make install clean BATCH=yes" \
    "cd /usr/ports/databases/unixODBC; sudo make install clean BATCH=yes" \
    "cd /usr/ports/devel/doxygen;      sudo make install clean BATCH=yes"; \
done
```

## VMs for install testing.

```
qemu-img create -b /kvm/vms/vm-freebsd92-amd64-serial.qcow2 -f qcow2 /kvm/vms/vm-freebsd92-amd64-install.qcow2
qemu-img create -b /kvm/vms/vm-freebsd92-i386-serial.qcow2 -f qcow2 /kvm/vms/vm-freebsd92-i386-install.qcow2

for i in '/kvm/vms/vm-freebsd92-amd64-serial.qcow2 2283 qemu64' '/kvm/vms/vm-freebsd92-i386-serial.qcow2 2284 qemu64' ; do \
  set $i; \
  runvm --user=buildbot --logfile=kernel_$2.log --base-image=$1 --port=$2 --cpu=$3 "$(echo $1 | sed -e 's/serial/install/')" \
    "sudo portsnap cron update"; \
done
```

## VMs for MySQL upgrade testing

```
for i in '/kvm/vms/vm-freebsd92-amd64-serial.qcow2 2283 qemu64' '/kvm/vms/vm-freebsd92-i386-serial.qcow2 2284 qemu64' ; do \
  set $i; \
  runvm --user=buildbot --logfile=kernel_$2.log --base-image=$1 --port=$2 --cpu=$3 "$(echo $1 | sed -e 's/serial/upgrade/')" \
    "cd /usr/ports/databases/mysql55-server;    sudo make install clean BATCH=yes" \
    "sudo /usr/local/etc/rc.d/mysql-server onestart" \
    'mysql -uroot -e "create database mytest; use mytest; create table t(a int primary key); insert into t values (1); select * from t"' ;\
done
```

## VMs for MariaDB upgrade testing

```
for i in '/kvm/vms/vm-freebsd92-amd64-serial.qcow2 2283 qemu64' '/kvm/vms/vm-freebsd92-i386-serial.qcow2 2284 qemu64' ; do \
  set $i; \
  runvm --user=buildbot --logfile=kernel_$2.log --base-image=$1 --port=$2 --cpu=$3 "$(echo $1 | sed -e 's/serial/upgrade2/')" \
    "cd /usr/ports/databases/mariadb55-server;    sudo make install clean BATCH=yes" \
    "sudo /usr/local/etc/rc.d/mysql-server onestart" \
    'mysql -uroot -e "create database mytest; use mytest; create table t(a int primary key); insert into t values (1); select * from t"'; \
done
```

## Add Key to known\_hosts

Do the following on each kvm host server (terrier, terrier2, i7, etc...) to add\
the VMs to known\_hosts.

```
# freebsd92-amd64
cp -avi /kvm/vms/vm-freebsd92-amd64-install.qcow2 /kvm/vms/vm-freebsd92-amd64-test.qcow2
kvm -m 1024 -hda /kvm/vms/vm-freebsd92-amd64-test.qcow2 -redir tcp:2283::22 -boot c -smp 2 -cpu qemu64 -net nic,model=virtio -net user -nographic
sudo su - buildbot
ssh -p 2283 buildbot@localhost sudo shutdown -p now
# answer "yes" when prompted
exit # the buildbot user
rm -v /kvm/vms/vm-freebsd92-amd64-test.qcow2

# freebsd92-i386
cp -avi /kvm/vms/vm-freebsd92-i386-install.qcow2 /kvm/vms/vm-freebsd92-i386-test.qcow2
kvm -m 1024 -hda /kvm/vms/vm-freebsd92-i386-test.qcow2 -redir tcp:2284::22 -boot c -smp 2 -cpu qemu64 -net nic,model=virtio -net user -nographic
sudo su - buildbot
ssh -p 2284 buildbot@localhost sudo shutdown -p now
# answer "yes" when prompted
exit # the buildbot user
rm -v /kvm/vms/vm-freebsd92-i386-test.qcow2
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
