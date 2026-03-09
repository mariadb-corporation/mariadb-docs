---
description: >-
  Explains how to provision and configure virtual machine instances specifically
  for Buildbot testing.
---

# Buildbot Setup for Virtual Machines - Ubuntu 14.04 "trusty"

## Base Install

```
qemu-img create -f qcow2 /kvm/vms/vm-trusty-amd64-serial.qcow2 20G
qemu-img create -f qcow2 /kvm/vms/vm-trusty-i386-serial.qcow2 20G
```

Start each VM booting from the server install iso one at a time and perform\
the following install steps:

```
kvm -m 2048 -hda /kvm/vms/vm-trusty-amd64-serial.qcow2 \
  -cdrom /kvm/iso/ubuntu/trusty-server-amd64.iso \
  -boot d -smp 2 -cpu qemu64 \
  -net nic,model=virtio \
  -net user,hostfwd=tcp:127.0.0.1:2293-:22

kvm -m 2048 -hda /kvm/vms/vm-trusty-i386-serial.qcow2 \
  -cdrom /kvm/iso/ubuntu/trusty-server-i386.iso \
  -boot d -smp 2 -cpu qemu64 \
  -net nic,model=virtio \
  -net user,hostfwd=tcp:127.0.0.1:2294-:22
```

Once running you can connect to the VNC server from your local host with:

```
vncviewer -via ${remote_host} localhost
```

Replace ${remote-host} with the host the vm is running on.

**Note:** When you activate the install, vncviewer may disconnect with a\
complaint about the rect being too large. This is fine. Ubuntu has just resized\
the vnc screen. Simply reconnect.

During the install, pick default options for the most part, with the following\
notes:

* Set the hostname to `ubuntu-trusty-amd64` or `ubuntu-trusty-i386`\
  (depending on which architecture we're installing)
* do not encrypt the home directory
* When prompted if the timezone is correct, answer "No" and when the list comes\
  up, scroll to the bottom and choose "UTC"
* When partitioning disks, choose "Guided - use entire disk" (we do not want\
  LVM)
* No automatic updates
* Choose software to install: OpenSSH server

Reboot when prompted. It will fail, so just kill the kvm process with`^Ctrl+C`.

Now that the VM is installed, it's time to configure it.\
If you have the memory you can do the following simultaneously:

```
qemu-system-x86_64 -m 2048 -hda /kvm/vms/vm-trusty-amd64-serial.qcow2 \
  -boot c -smp 2 -cpu qemu64 \
  -net nic,model=virtio \
  -net user,hostfwd=tcp:127.0.0.1:2293-:22 \
  -nographic

qemu-system-x86_64 -m 2048 -hda /kvm/vms/vm-trusty-i386-serial.qcow2 \
  -boot c -smp 2 -cpu qemu64 \
  -net nic,model=virtio \
  -net user,hostfwd=tcp:127.0.0.1:2294-:22 \
  -nographic
```

* set `vim` as the preferred editor

```
ssh -t -p 2293 localhost sudo update-alternatives --config editor
ssh -t -p 2294 localhost sudo update-alternatives --config editor
```

* Enabling passwordless sudo:

```
sudo VISUAL=vi visudo
# Add line at end: `%sudo ALL=NOPASSWD: ALL'
```

* edit /boot/grub/menu.lst:

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

* create the `.ssh` directory and the `sudo` group

```
ssh -t -p 2293 localhost "mkdir -v .ssh; sudo addgroup $USER sudo"
ssh -t -p 2294 localhost "mkdir -v .ssh; sudo addgroup $USER sudo"
```

* copy the `authorized_keys` file up to the VMs

```
scp -P 2293 /kvm/vms/authorized_keys localhost:.ssh/
scp -P 2294 /kvm/vms/authorized_keys localhost:.ssh/
```

* create the buildbot user on the amd64 VM

```
echo $'Buildbot\n\n\n\n\ny' | ssh -p 2293 localhost 'chmod -vR go-rwx .ssh; sudo adduser --disabled-password buildbot; sudo addgroup buildbot sudo; sudo mkdir -v ~buildbot/.ssh; sudo cp -vi .ssh/authorized_keys ~buildbot/.ssh/; sudo chown -vR buildbot:buildbot ~buildbot/.ssh; sudo chmod -vR go-rwx ~buildbot/.ssh'
```

* create the buildbot user on the x86 VM

```
echo $'Buildbot\n\n\n\n\ny' | ssh -p 2294 localhost 'chmod -vR go-rwx .ssh; sudo adduser --disabled-password buildbot; sudo addgroup buildbot sudo; sudo mkdir -v ~buildbot/.ssh; sudo cp -vi .ssh/authorized_keys ~buildbot/.ssh/; sudo chown -vR buildbot:buildbot ~buildbot/.ssh; sudo chmod -vR go-rwx ~buildbot/.ssh'
```

* copy the ttyS0 file to the VMs

```
scp -i -P 2293 /kvm/vms/ttyS0.conf buildbot@localhost:
scp -i -P 2294 /kvm/vms/ttyS0.conf buildbot@localhost:
```

* Apply all OS updates

```
ssh -t -i -p 2293 buildbot@localhost \
  'sudo apt-get update && sudo apt-get -y dist-upgrade;'

ssh -t -i -p 2294 buildbot@localhost \
  'sudo apt-get update && sudo apt-get -y dist-upgrade;'
```

* copy the ttyS0 file to its proper location and shut down the VM

```
ssh -t -i -p 2293 buildbot@localhost \
  'sudo cp -vi ttyS0.conf /etc/init/; rm -v ttyS0.conf; sudo shutdown -h now'

ssh -t -i -p 2294 buildbot@localhost \
  'sudo cp -vi ttyS0.conf /etc/init/; rm -v ttyS0.conf; sudo shutdown -h now'
```

## VMs for building .debs

```
for i in '/kvm/vms/vm-trusty-amd64-serial.qcow2 2293 qemu64' '/kvm/vms/vm-trusty-i386-serial.qcow2 2294 qemu64' ; do \
  set $i; \
  runvm --user=buildbot --logfile=kernel_$2.log --base-image=$1 --port=$2 --cpu=$3 "$(echo $1 | sed -e 's/serial/build/')" \
    "= scp -P $2 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no /kvm/thrift-0.9.0.tar.gz buildbot@localhost:/dev/shm/" \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get update" \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get -y build-dep mysql-server-5.5" \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get install -y devscripts hardening-wrapper fakeroot doxygen texlive-latex-base ghostscript libevent-dev libssl-dev zlib1g-dev libpam0g-dev libreadline-gplv2-dev autoconf automake automake1.9 dpatch ghostscript-x libfontenc1 libjpeg62 libltdl-dev libltdl7 libmail-sendmail-perl libxfont1 lmodern texlive-latex-base-doc ttf-dejavu ttf-dejavu-extra libaio-dev xfonts-encodings xfonts-utils libxml2-dev unixodbc-dev bzr scons check libboost-all-dev openssl epm libjudy-dev libjemalloc-dev" \
    "bzr co --lightweight lp:mariadb-native-client" \
    "cd /usr/local/src;sudo tar zxf /dev/shm/thrift-0.9.0.tar.gz;pwd;ls" \
    "cd /usr/local/src/thrift-0.9.0;echo;pwd;sudo ./configure --prefix=/usr --enable-shared=no --enable-static=yes CXXFLAGS=-fPIC CFLAGS=-fPIC && echo && echo 'now making' && echo && sleep 3 && sudo make && echo && echo 'now installing' && echo && sleep 3 && sudo make install" ; \
done
```

## VMs for install testing.

See [Buildbot Setup for Virtual Machines - General Principles](../buildbot-setup-for-virtual-machines-general-principles.md) for how to obtain `my.seed` and `sources.append`.

```
for i in '/kvm/vms/vm-trusty-amd64-serial.qcow2 2293 qemu64' '/kvm/vms/vm-trusty-i386-serial.qcow2 2294 qemu64' ; do \
  set $i; \
  runvm --user=buildbot --logfile=kernel_$2.log --base-image=$1 --port=$2 --cpu=$3 "$(echo $1 | sed -e 's/serial/install/')" \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get update" \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get install -y patch libaio1 debconf-utils unixodbc libxml2 libjudydebian1 libjemalloc1" \
    "= scp -P $2 /kvm/vms/my55.seed /kvm/vms/sources.append buildbot@localhost:/tmp/" \
    "sudo debconf-set-selections /tmp/my55.seed" \
    "sudo sh -c 'cat /tmp/sources.append >> /etc/apt/sources.list'"; \
done
```

## VMs for MySQL upgrade testing

```
for i in '/kvm/vms/vm-trusty-amd64-serial.qcow2 2293 qemu64' '/kvm/vms/vm-trusty-i386-serial.qcow2 2294 qemu64' ; do \
  set $i; \
  runvm --user=buildbot --logfile=kernel_$2.log --base-image=$1 --port=$2 --cpu=$3 "$(echo $1 | sed -e 's/serial/upgrade/')" \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get update" \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get install -y patch libaio1 debconf-utils" \
    "= scp -P $2 /kvm/vms/my55.seed /kvm/vms/sources.append buildbot@localhost:/tmp/" \
    "sudo debconf-set-selections /tmp/my55.seed" \
    "sudo sh -c 'cat /tmp/sources.append >> /etc/apt/sources.list'" \
    'sudo DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server-5.5 libjemalloc1' \
    'mysql -uroot -prootpass -e "create database mytest; use mytest; create table t(a int primary key); insert into t values (1); select * from t"' ;\
done
```

## VMs for MariaDB upgrade testing

```
for i in '/kvm/vms/vm-trusty-amd64-serial.qcow2 2293 qemu64' '/kvm/vms/vm-trusty-i386-serial.qcow2 2294 qemu64' ; do \
  set $i; \
  runvm --user=buildbot --logfile=kernel_$2.log --base-image=$1 --port=$2 --cpu=$3 "$(echo $1 | sed -e 's/serial/upgrade2/')" \
    "= scp -P $2 /kvm/vms/my55.seed /kvm/vms/sources.append buildbot@localhost:/tmp/" \
    "= scp -P $2 /kvm/vms/mariadb-trusty.list buildbot@localhost:/tmp/tmp.list" \
    "sudo debconf-set-selections /tmp/my55.seed" \
    'sudo mv -vi /tmp/tmp.list /etc/apt/sources.list.d/' \
    'sudo apt-key adv --recv-keys --keyserver pgp.mit.edu 0xcbcb082a1bb943db' \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get update" \
    'sudo DEBIAN_FRONTEND=noninteractive apt-get install -y mariadb-server libjemalloc1' \
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
# trusty-amd64
cp -avi /kvm/vms/vm-trusty-amd64-install.qcow2 /kvm/vms/vm-trusty-amd64-test.qcow2
kvm -m 1024 -hda /kvm/vms/vm-trusty-amd64-test.qcow2 -redir tcp:2293::22 -boot c -smp 2 -cpu qemu64 -net nic,model=virtio -net user -nographic
sudo su - buildbot
ssh -p 2293 buildbot@localhost sudo shutdown -h now
# answer "yes" when prompted
exit # the buildbot user
rm -v /kvm/vms/vm-trusty-amd64-test.qcow2

# trusty-i386
cp -avi /kvm/vms/vm-trusty-i386-install.qcow2 /kvm/vms/vm-trusty-i386-test.qcow2
kvm -m 1024 -hda /kvm/vms/vm-trusty-i386-test.qcow2 -redir tcp:2294::22 -boot c -smp 2 -cpu qemu64 -net nic,model=virtio -net user -nographic
sudo su - buildbot
ssh -p 2294 buildbot@localhost sudo shutdown -h now
# answer "yes" when prompted
exit # the buildbot user
rm -v /kvm/vms/vm-trusty-i386-test.qcow2
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
