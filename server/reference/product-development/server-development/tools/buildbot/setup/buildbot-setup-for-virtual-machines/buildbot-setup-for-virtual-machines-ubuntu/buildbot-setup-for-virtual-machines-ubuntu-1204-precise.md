---
description: >-
  Explains how to provision and configure virtual machine instances specifically
  for Buildbot testing.
---

# Buildbot Setup for Virtual Machines - Ubuntu 12.04 "precise"

## Base Install

```
qemu-img create -f qcow2 /kvm/vms/vm-precise-amd64-serial.qcow2 8G
qemu-img create -f qcow2 /kvm/vms/vm-precise-i386-serial.qcow2 8G
```

Start each VM booting from the server install iso one at a time and perform\
the following install steps:

```
kvm -m 1024 -hda /kvm/vms/vm-precise-amd64-serial.qcow2 -cdrom /kvm/iso/ubuntu/ubuntu-12.04-server-amd64.iso -redir tcp:22255::22 -boot d -smp 2 -cpu qemu64 -net nic,model=virtio -net user
kvm -m 1024 -hda /kvm/vms/vm-precise-i386-serial.qcow2 -cdrom /kvm/iso/ubuntu/ubuntu-12.04-server-i386.iso -redir tcp:22256::22 -boot d -smp 2 -cpu qemu32,-nx -net nic,model=virtio -net user
```

Once running you can connect to the VNC server from your local host with:

```
vncviewer -via ${remote-host} localhost
```

Replace ${remote-host} with the host the vm is running on.

**Note:** When you activate the install, vncviewer may disconnect with a complaint about the rect being too large. This is fine. Ubuntu has just resized the vnc screen. Simply reconnect.

Install, picking default options mostly, with the following notes:

* Set the hostname to ubuntu-precise
* When partitioning disks, choose "Guided - use entire disk" (we do not want LVM)
* No automatic updates
* Choose software to install: OpenSSH server

Now that the VM is installed, it's time to configure it.\
If you have the memory you can do the following simultaneously:

```
kvm -m 1024 -hda /kvm/vms/vm-precise-amd64-serial.qcow2 -cdrom /kvm/iso/ubuntu/ubuntu-12.04-server-amd64.iso -redir tcp:22255::22 -boot c -smp 2 -cpu qemu64 -net nic,model=virtio -net user -nographic
kvm -m 1024 -hda /kvm/vms/vm-precise-i386-serial.qcow2 -cdrom /kvm/iso/ubuntu/ubuntu-12.04-server-i386.iso -redir tcp:22256::22 -boot c -smp 2 -cpu qemu64 -net nic,model=virtio -net user -nographic

ssh -p 22255 localhost
# edit /boot/grub/menu.lst and visudo, see below

ssh -p 22256 localhost
# edit /boot/grub/menu.lst and visudo, see below

ssh -t -p 22255 localhost "mkdir -v .ssh; sudo addgroup $USER sudo"
ssh -t -p 22256 localhost "mkdir -v .ssh; sudo addgroup $USER sudo"

scp -P 22255 /kvm/vms/authorized_keys localhost:.ssh/
scp -P 22256 /kvm/vms/authorized_keys localhost:.ssh/

echo $'Buildbot\n\n\n\n\ny' | ssh -p 22255 localhost 'chmod -R go-rwx .ssh; sudo adduser --disabled-password buildbot; sudo addgroup buildbot sudo; sudo mkdir ~buildbot/.ssh; sudo cp -vi .ssh/authorized_keys ~buildbot/.ssh/; sudo chown -vR buildbot:buildbot ~buildbot/.ssh; sudo chmod -vR go-rwx ~buildbot/.ssh'
echo $'Buildbot\n\n\n\n\ny' | ssh -p 22256 localhost 'chmod -R go-rwx .ssh; sudo adduser --disabled-password buildbot; sudo addgroup buildbot sudo; sudo mkdir ~buildbot/.ssh; sudo cp -vi .ssh/authorized_keys ~buildbot/.ssh/; sudo chown -vR buildbot:buildbot ~buildbot/.ssh; sudo chmod -vR go-rwx ~buildbot/.ssh'

scp -P 22255 /kvm/vms/ttyS0.conf buildbot@localhost:
scp -P 22256 /kvm/vms/ttyS0.conf buildbot@localhost:

ssh -p 22255 buildbot@localhost 'sudo cp -vi ttyS0.conf /etc/init/; rm -v ttyS0.conf; sudo shutdown -h now'
ssh -p 22256 buildbot@localhost 'sudo cp -vi ttyS0.conf /etc/init/; rm -v ttyS0.conf; sudo shutdown -h now'
```

Enabling passwordless sudo:

```
sudo VISUAL=vi visudo
# Add line at end: `%sudo ALL=NOPASSWD: ALL'
```

Editing /boot/grub/menu.lst:

```
sudo vi /etc/default/grub

# Add/edit these entries:
    GRUB_CMDLINE_LINUX_DEFAULT="console=tty0 console=ttyS0,115200n8"
    GRUB_TERMINAL="serial"
    GRUB_SERIAL_COMMAND="serial --unit=0 --speed=115200 --word=8 --parity=no --stop=1"

sudo update-grub
```

## VMs for building .debs

```
for i in '/kvm/vms/vm-precise-amd64-serial.qcow2 22255 qemu64' '/kvm/vms/vm-precise-i386-serial.qcow2 22256 qemu64' ; do \
  set $i; \
  runvm --user=buildbot --logfile=kernel_$2.log --base-image=$1 --port=$2 --cpu=$3 "$(echo $1 | sed -e 's/serial/build/')" \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get update" \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get -y build-dep mysql-server-5.5" \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get install -y devscripts hardening-wrapper fakeroot doxygen texlive-latex-base ghostscript libevent-dev libssl-dev zlib1g-dev libpam0g-dev libreadline-gplv2-dev autoconf automake automake1.9 defoma dpatch ghostscript-x libfontenc1 libjpeg62 libltdl-dev libltdl7 libmail-sendmail-perl libxfont1 lmodern psfontmgr texlive-latex-base-doc ttf-dejavu ttf-dejavu-extra libaio-dev xfonts-encodings xfonts-utils" ; \
done
```

Also:

* [Installing the Boost library needed for the OQGraph storage engine](../buildbot-setup-for-virtual-machines-additional-steps/installing-the-boost-library-needed-for-the-oqgraph-storage-engine.md)

## VMs for install testing.

See [Buildbot Setup for Virtual Machines - General Principles](../buildbot-setup-for-virtual-machines-general-principles.md) for how to obtain `my.seed` and `sources.append`.

```
for i in '/kvm/vms/vm-precise-amd64-serial.qcow2 22255 qemu64' '/kvm/vms/vm-precise-i386-serial.qcow2 22256 qemu64' ; do \
  set $i; \
  runvm --user=buildbot --logfile=kernel_$2.log --base-image=$1 --port=$2 --cpu=$3 "$(echo $1 | sed -e 's/serial/install/')" \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get update" \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get install -y patch libaio1 debconf-utils" \
    "= scp -P $2 /kvm/vms/my.seed /kvm/vms/sources.append buildbot@localhost:/tmp/" \
    "sudo debconf-set-selections /tmp/my.seed" \
    "sudo sh -c 'cat /tmp/sources.append >> /etc/apt/sources.list'"; \
done
```

## VMs for MySQL upgrade testing

```
for i in '/kvm/vms/vm-precise-amd64-install.qcow2 22255 qemu64' '/kvm/vms/vm-precise-i386-install.qcow2 22256 qemu64' ; do \
  set $i; \
  runvm --user=buildbot --logfile=kernel_$2.log --base-image=$1 --port=$2 --cpu=$3 "$(echo $1 | sed -e 's/install/upgrade/')" \
    'sudo DEBIAN_FRONTEND=noninteractive apt-get install -y libaio1 mysql-server-5.5' \
    'mysql -uroot -prootpass -e "create database mytest; use mytest; create table t(a int primary key); insert into t values (1); select * from t"' ;\
done
```

## VMs for MariaDB upgrade testing

_The steps below are based on the Natty steps on_ [_Installing VM images for testing .deb upgrade between versions_](../buildbot-setup-for-virtual-machines-additional-steps/installing-vm-images-for-testing-deb-upgrade-between-versions.md)_._

64-bit Ubuntu precise:

```
qemu-img create -b vm-precise-amd64-install.qcow2 -f qcow2 vm-precise-amd64-upgrade2.qcow2
kvm -m 512 -hda vm-precise-amd64-upgrade2.qcow2 -redir 'tcp:22200::22' -boot c -smp 1 -cpu qemu64 -net nic,model=virtio -net user -nographic
ssh -p 22200 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no buildbot@localhost

sudo sh -c 'cat > /etc/apt/sources.list.d/tmp.list'
deb http://ftp.osuosl.org/pub/mariadb/repo/5.5/ubuntu oneiric main
deb-src http://ftp.osuosl.org/pub/mariadb/repo/5.5/ubuntu oneiric main

sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 1BB943DB
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y --allow-unauthenticated mariadb-server mariadb-test libmariadbclient-dev
sudo apt-get -f install
mysql -uroot -prootpass -e "create database mytest; use mytest; create table t(a int primary key); insert into t values (1); select * from t"
sudo rm /etc/apt/sources.list.d/tmp.list
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y libaio1
sudo DEBIAN_FRONTEND=noninteractive apt-get upgrade -y
sudo shutdown -h now
```

32-bit Ubuntu precise:

```
qemu-img create -b vm-precise-i386-install.qcow2 -f qcow2 vm-precise-i386-upgrade2.qcow2
kvm -m 512 -hda vm-precise-i386-upgrade2.qcow2 -redir 'tcp:22200::22' -boot c -smp 1 -cpu qemu64 -net nic,model=virtio -net user -nographic
ssh -p 22200 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no buildbot@localhost

sudo sh -c 'cat > /etc/apt/sources.list.d/tmp.list'
deb http://ftp.osuosl.org/pub/mariadb/repo/5.5/ubuntu oneiric main
deb-src http://ftp.osuosl.org/pub/mariadb/repo/5.5/ubuntu oneiric main

sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 1BB943DB
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y --allow-unauthenticated mariadb-server mariadb-test libmariadbclient-dev
sudo apt-get -f install
mysql -uroot -prootpass -e "create database mytest; use mytest; create table t(a int primary key); insert into t values (1); select * from t"
sudo rm /etc/apt/sources.list.d/tmp.list
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y libaio1
sudo DEBIAN_FRONTEND=noninteractive apt-get upgrade -y
sudo shutdown -h now
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
