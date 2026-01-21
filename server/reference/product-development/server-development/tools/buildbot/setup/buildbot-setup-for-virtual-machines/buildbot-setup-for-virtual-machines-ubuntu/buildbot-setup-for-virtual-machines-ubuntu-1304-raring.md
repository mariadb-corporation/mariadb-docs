---
description: >-
  Explains how to provision and configure virtual machine instances specifically
  for Buildbot testing.
---

# Buildbot Setup for Virtual Machines - Ubuntu 13.04 "raring"

## Base Install

```
qemu-img create -f qcow2 /kvm/vms/vm-raring-amd64-serial.qcow2 15G
qemu-img create -f qcow2 /kvm/vms/vm-raring-i386-serial.qcow2 15G
```

Start each VM booting from the server install iso one at a time and perform\
the following install steps:

```
kvm -m 2048 -hda /kvm/vms/vm-raring-amd64-serial.qcow2 -cdrom /kvm/iso/ubuntu/ubuntu-13.04-server-amd64.iso -boot d -smp 2 -cpu qemu64 -net nic,model=virtio -net user,hostfwd=tcp:127.0.0.1:2279-:22
kvm -m 2048 -hda /kvm/vms/vm-raring-i386-serial.qcow2 -cdrom /kvm/iso/ubuntu/ubuntu-13.04-server-i386.iso -boot d -smp 2 -cpu qemu64 -net nic,model=virtio -net user,hostfwd=tcp:127.0.0.1:2280-:22
```

Once running you can connect to the VNC server from your local host with:

```
vncviewer -via ${remote-host} localhost
```

Replace ${remote-host} with the host the vm is running on.

**Note:** When you activate the install, vncviewer may disconnect with a\
complaint about the rect being too large. This is fine. Ubuntu has just resized\
the vnc screen. Simply reconnect.

Install, picking default options mostly, with the following notes:

* Set the hostname to ubuntu-raring-amd64 or ubuntu-raring-i386
* When partitioning disks, choose "Guided - use entire disk" (we do not want LVM)
* No automatic updates
* Choose software to install: OpenSSH server

Now that the VM is installed, it's time to configure it.\
If you have the memory you can do the following simultaneously:

```
kvm -m 2048 -hda /kvm/vms/vm-raring-amd64-serial.qcow2 -cdrom /kvm/iso/ubuntu/ubuntu-13.04-server-amd64.iso -boot c -smp 2 -cpu qemu64 -net nic,model=virtio -net user,hostfwd=tcp:127.0.0.1:2279-:22 -nographic
kvm -m 2048 -hda /kvm/vms/vm-raring-i386-serial.qcow2 -cdrom /kvm/iso/ubuntu/ubuntu-13.04-server-i386.iso -boot c -smp 2 -cpu qemu64 -net nic,model=virtio -net user,hostfwd=tcp:127.0.0.1:2280-:22 -nographic

ssh -p 2279 localhost
# edit /boot/grub/menu.lst and visudo, see below

ssh -p 2280 localhost
# edit /boot/grub/menu.lst and visudo, see below

ssh -t -p 2279 localhost "mkdir -v .ssh; sudo addgroup $USER sudo"
ssh -t -p 2280 localhost "mkdir -v .ssh; sudo addgroup $USER sudo"

scp -P 2279 /kvm/vms/authorized_keys localhost:.ssh/
scp -P 2280 /kvm/vms/authorized_keys localhost:.ssh/

echo $'Buildbot\n\n\n\n\ny' | ssh -p 2279 localhost 'chmod -vR go-rwx .ssh; sudo adduser --disabled-password buildbot; sudo addgroup buildbot sudo; sudo mkdir -v ~buildbot/.ssh; sudo cp -vi .ssh/authorized_keys ~buildbot/.ssh/; sudo chown -vR buildbot:buildbot ~buildbot/.ssh; sudo chmod -vR go-rwx ~buildbot/.ssh'
echo $'Buildbot\n\n\n\n\ny' | ssh -p 2280 localhost 'chmod -vR go-rwx .ssh; sudo adduser --disabled-password buildbot; sudo addgroup buildbot sudo; sudo mkdir -v ~buildbot/.ssh; sudo cp -vi .ssh/authorized_keys ~buildbot/.ssh/; sudo chown -vR buildbot:buildbot ~buildbot/.ssh; sudo chmod -vR go-rwx ~buildbot/.ssh'

scp -P 2279 /kvm/vms/ttyS0.conf buildbot@localhost:
scp -P 2280 /kvm/vms/ttyS0.conf buildbot@localhost:

ssh -p 2279 buildbot@localhost 'sudo apt-get update && sudo apt-get -y dist-upgrade;'
ssh -p 2280 buildbot@localhost 'sudo apt-get update && sudo apt-get -y dist-upgrade;'

ssh -p 2279 buildbot@localhost 'sudo cp -vi ttyS0.conf /etc/init/; rm -v ttyS0.conf; sudo shutdown -h now'
ssh -p 2280 buildbot@localhost 'sudo cp -vi ttyS0.conf /etc/init/; rm -v ttyS0.conf; sudo shutdown -h now'
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
GRUB_HIDDEN_TIMEOUT_QUIET=false
GRUB_TIMEOUT=0
GRUB_CMDLINE_LINUX_DEFAULT="console=tty0 console=ttyS0,115200n8"
GRUB_TERMINAL="serial"
GRUB_SERIAL_COMMAND="serial --unit=0 --speed=115200 --word=8 --parity=no --stop=1"

sudo update-grub
# exit back to the host server
```

## VMs for building .debs

```
for i in '/kvm/vms/vm-raring-amd64-serial.qcow2 2279 qemu64' '/kvm/vms/vm-raring-i386-serial.qcow2 2280 qemu64' ; do \
  set $i; \
  runvm --user=buildbot --logfile=kernel_$2.log --base-image=$1 --port=$2 --cpu=$3 "$(echo $1 | sed -e 's/serial/build/')" \
    "= scp -P $2 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no /kvm/boost_1_49_0.tar.gz buildbot@localhost:/dev/shm/" \
    "= scp -P $2 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no /kvm/thrift-0.9.0.tar.gz buildbot@localhost:/dev/shm/" \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get update" \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get -y build-dep mysql-server-5.5" \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get install -y devscripts hardening-wrapper fakeroot doxygen texlive-latex-base ghostscript libevent-dev libssl-dev zlib1g-dev libpam0g-dev libreadline-gplv2-dev autoconf automake automake1.9 dpatch ghostscript-x libfontenc1 libjpeg62 libltdl-dev libltdl7 libmail-sendmail-perl libxfont1 lmodern texlive-latex-base-doc ttf-dejavu ttf-dejavu-extra libaio-dev xfonts-encodings xfonts-utils libxml2-dev unixodbc-dev bzr" \
    "bzr co --lightweight lp:mariadb-native-client" \
    "cd /usr/local/src;sudo tar zxf /dev/shm/thrift-0.9.0.tar.gz;pwd;ls" \
    "cd /usr/local/src/thrift-0.9.0;echo;pwd;sudo ./configure --prefix=/usr --enable-shared=no --enable-static=yes CXXFLAGS=-fPIC CFLAGS=-fPIC && echo && echo 'now making' && echo && sleep 3 && sudo make && echo && echo 'now installing' && echo && sleep 3 && sudo make install" \
    "cd /usr/local/src;sudo tar zxf /dev/shm/boost_1_49_0.tar.gz;cd /usr/local/include/;sudo ln -vs ../src/boost_1_49_0/boost ." ; \
done
```

## VMs for install testing.

See [Buildbot Setup for Virtual Machines - General Principles](../buildbot-setup-for-virtual-machines-general-principles.md) for how to obtain `my.seed` and `sources.append`.

```
for i in '/kvm/vms/vm-raring-amd64-serial.qcow2 2279 qemu64' '/kvm/vms/vm-raring-i386-serial.qcow2 2280 qemu64' ; do \
  set $i; \
  runvm --user=buildbot --logfile=kernel_$2.log --base-image=$1 --port=$2 --cpu=$3 "$(echo $1 | sed -e 's/serial/install/')" \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get update" \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get install -y patch libaio1 debconf-utils" \
    "= scp -P $2 /kvm/vms/my55.seed /kvm/vms/sources.append buildbot@localhost:/tmp/" \
    "sudo debconf-set-selections /tmp/my55.seed" \
    "sudo sh -c 'cat /tmp/sources.append >> /etc/apt/sources.list'"; \
done
```

## VMs for MySQL upgrade testing

```
for i in '/kvm/vms/vm-raring-amd64-serial.qcow2 2279 qemu64' '/kvm/vms/vm-raring-i386-serial.qcow2 2280 qemu64' ; do \
  set $i; \
  runvm --user=buildbot --logfile=kernel_$2.log --base-image=$1 --port=$2 --cpu=$3 "$(echo $1 | sed -e 's/serial/upgrade/')" \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get update" \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get install -y patch libaio1 debconf-utils" \
    "= scp -P $2 /kvm/vms/my55.seed /kvm/vms/sources.append buildbot@localhost:/tmp/" \
    "sudo debconf-set-selections /tmp/my55.seed" \
    "sudo sh -c 'cat /tmp/sources.append >> /etc/apt/sources.list'" \
    'sudo DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server-5.5' \
    'mysql -uroot -prootpass -e "create database mytest; use mytest; create table t(a int primary key); insert into t values (1); select * from t"' ;\
done
```

## VMs for MariaDB upgrade testing

_The steps below are based on the Natty steps on_ [_Installing VM images for testing .deb upgrade between versions_](../buildbot-setup-for-virtual-machines-additional-steps/installing-vm-images-for-testing-deb-upgrade-between-versions.md)_._

```
for i in '/kvm/vms/vm-raring-amd64-serial.qcow2 2279 qemu64' '/kvm/vms/vm-raring-i386-serial.qcow2 2280 qemu64' ; do \
  set $i; \
  runvm --user=buildbot --logfile=kernel_$2.log --base-image=$1 --port=$2 --cpu=$3 "$(echo $1 | sed -e 's/serial/upgrade2/')" \
    "= scp -P $2 /kvm/vms/my55.seed /kvm/vms/sources.append buildbot@localhost:/tmp/" \
    "= scp -P $2 /kvm/vms/mariadb-raring.list buildbot@localhost:/tmp/tmp.list" \
    "sudo debconf-set-selections /tmp/my55.seed" \
    'sudo mv -vi /tmp/tmp.list /etc/apt/sources.list.d/' \
    'sudo apt-key adv --recv-keys --keyserver pgp.mit.edu 0xcbcb082a1bb943db' \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get update" \
    'sudo DEBIAN_FRONTEND=noninteractive apt-get install -y mariadb-server mariadb-server-5.5 mariadb-client mariadb-client-5.5 mariadb-test libmariadbclient-dev mysql-common=5.5.30-mariadb1~quantal libmysqlclient18=5.5.30-mariadb1~quantal' \
    'mysql -uroot -prootpass -e "create database mytest; use mytest; create table t(a int primary key); insert into t values (1); select * from t"' \
    'sudo rm -v /etc/apt/sources.list.d/tmp.list' \
    'sudo DEBIAN_FRONTEND=noninteractive apt-get update' \
    "sudo sh -c 'cat /tmp/sources.append >> /etc/apt/sources.list'" \
    'sudo DEBIAN_FRONTEND=noninteractive apt-get install -y patch libaio1 debconf-utils' \
    'sudo DEBIAN_FRONTEND=noninteractive apt-get upgrade -y'; \
done
```

## Add Key to known\_hosts

Do the following on each kvm host server (terrier, terrier2, i7, etc...) to add\
the VMs to known\_hosts.

```
# raring-amd64
cp -avi /kvm/vms/vm-raring-amd64-install.qcow2 /kvm/vms/vm-raring-amd64-test.qcow2
kvm -m 1024 -hda /kvm/vms/vm-raring-amd64-test.qcow2 -redir tcp:2279::22 -boot c -smp 2 -cpu qemu64 -net nic,model=virtio -net user -nographic
sudo su - buildbot
ssh -p 2279 buildbot@localhost sudo shutdown -h now
# answer "yes" when prompted
exit # the buildbot user
rm -v /kvm/vms/vm-raring-amd64-test.qcow2

# raring-i386
cp -avi /kvm/vms/vm-raring-i386-install.qcow2 /kvm/vms/vm-raring-i386-test.qcow2
kvm -m 1024 -hda /kvm/vms/vm-raring-i386-test.qcow2 -redir tcp:2280::22 -boot c -smp 2 -cpu qemu64 -net nic,model=virtio -net user -nographic
sudo su - buildbot
ssh -p 2280 buildbot@localhost sudo shutdown -h now
# answer "yes" when prompted
exit # the buildbot user
rm -v /kvm/vms/vm-raring-i386-test.qcow2
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
