---
description: >-
  Explains how to provision and configure virtual machine instances specifically
  for Buildbot testing.
---

# Installing VM Images for Testing .deb Upgrade Between Versions

This step creates virtual machine images used to do an important additional\
upgrade test for .debs. Each virtual machine is pre-installed with an older\
version of MariaDB, and the test tries upgrading this version to the newly\
build one (to check that dependencies etc. work out correctly).

This step may not be easily possible to replicate exactly for new or updated\
images. For example, when we add a new platform/distro, we will not have the\
same old version of MariaDB available for installation on the new planform. Or\
if needing to re-create an image in the future, the original old .debs used\
before may no longer be available. However, this is not a big problem, as we\
can just use whatever version of MariaDB is available. In fact, while we\
cannot reasonably test every possible upgrade combination between MariaDB\
versions, it is still useful to test upgrades from different versions on\
different platforms, to increase coverage a bit.

The bulk of the images were installed with the following two loops, using\
packages from the OurDelta repository for [MariaDB 5.1.42](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.1/5.1.42), which was the one\
available from there at the time of installation.

```
for i in "vm-hardy-amd64-install qemu64 hardy" "vm-hardy-i386-install qemu32,-nx hardy" \
          "vm-intrepid-amd64-install qemu64 intrepid" "vm-intrepid-i386-install qemu32,-nx intrepid" \
          "vm-karmic-amd64-install qemu64 karmic" "vm-karmic-i386-install qemu32,-nx karmic" \
          "vm-jaunty-amd64-install qemu64 jaunty" "vm-jaunty-i386-deb-install qemu32,-nx jaunty" \
          "vm-debian5-amd64-install qemu64 lenny" "vm-debian5-i386-install qemu32,-nx lenny" ; do \
  set $i; \
  runvm -b  $1.qcow2 -m 512 --smp=1 --port=2200 --user=buildbot --cpu=$2 $(echo $1 | sed -e 's/-install/-upgrade2/').qcow2 \
    "wget -O- http://ourdelta.org/deb/ourdelta.gpg | sudo apt-key add -" \
    "sudo sh -c \"echo 'deb http://mirror.ourdelta.org/deb $3 mariadb-ourdelta' > /etc/apt/sources.list.d/ourdelta.list\"" \
    "sudo apt-get update || true" \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get install -y mariadb-server mariadb-test libmariadbclient-dev || true" \
    'mysql -uroot -prootpass -e "create database mytest; use mytest; create table t(a int primary key); insert into t values (1); select * from t"' \
    "sudo rm /etc/apt/sources.list.d/ourdelta.list" \
    "sudo apt-get update || true" \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get upgrade -y || true" ; \
done
```

```
for i in "vm-debian4-amd64-install qemu64 etch /kvm/debian-40r8-amd64-netinst.iso" "vm-debian4-i386-install qemu32,-nx etch /kvm/debian-40r8-i386-netinst.iso" ; do \
  set $i; \
  runvm -b  $1.qcow2 -m 512 --smp=1 --port=2200 --user=buildbot --cpu=$2 --netdev=e1000 --kvm=-cdrom --kvm=$4 $(echo $1 | sed -e 's/-install/-upgrade2/').qcow2 \
    "wget -O- http://ourdelta.org/deb/ourdelta.gpg | sudo apt-key add -" \
    "sudo sh -c \"echo 'deb http://mirror.ourdelta.org/deb $3 mariadb-ourdelta' > /etc/apt/sources.list.d/ourdelta.list\"" \
    "sudo apt-get update || true" \
    "sudo sh -c 'DEBIAN_FRONTEND=noninteractive apt-get install -y mariadb-server mariadb-test libmariadbclient-dev' || true" \
    'mysql -uroot -prootpass -e "create database mytest; use mytest; create table t(a int primary key); insert into t values (1); select * from t"' \
    "sudo rm /etc/apt/sources.list.d/ourdelta.list" \
    "sudo apt-get update || true" \
    "sudo sh -c 'DEBIAN_FRONTEND=noninteractive apt-get upgrade -y' || true" ; \
done
```

The Ubuntu 10.04 "lucid" images were installed manually (as no packages for\
lucid were available from OurDelta at the time of installation):

Create and boot 64-bit lucid upgrade image:

```
qemu-img create -b vm-lucid-amd64-install.qcow2 -f qcow2 vm-lucid-amd64-upgrade2.qcow2 
kvm -m 512 -hda vm-lucid-amd64-upgrade2.qcow2 -redir 'tcp:2200::22' -boot c -smp 1 -cpu qemu64 -net nic,model=virtio -net user -nographic
```

Create directory inside the image:

```
mkdir buildbot
```

Copy in packages to be installed from outside:

```
scp -P 2200 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -r /archive/pack/mariadb-5.1-knielsen/build-277/kvm-deb-lucid-amd64/debs buildbot@localhost:buildbot/
```

Install the MariaDB packages, remove package dir, and upgrade to latest\
security fixes:

```
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y --allow-unauthenticated mariadb-server mariadb-test libmariadbclient-dev
mysql -uroot -prootpass -e "create database mytest; use mytest; create table t(a int primary key); insert into t values (1); select * from t"
rm -Rf buildbot
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get upgrade -y
```

Now the same, but for 32-bit lucid:

```
qemu-img create -b vm-lucid-i386-install.qcow2 -f qcow2 vm-lucid-i386-upgrade2.qcow2 
kvm -m 512 -hda vm-lucid-i386-upgrade2.qcow2 -redir 'tcp:2200::22' -boot c -smp 1 -cpu qemu32,-nx -net nic,model=virtio -net user -nographic
```

Create directory inside the image:

```
mkdir buildbot
```

Copy in packages to be installed from outside:

```
scp -P 2200 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -r /archive/pack/mariadb-5.1-knielsen/build-277/kvm-deb-lucid-x86/debs buildbot@localhost:buildbot/
```

Install the MariaDB packages, remove package dir, and upgrade to latest\
security fixes:

```
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y --allow-unauthenticated mariadb-server mariadb-test libmariadbclient-dev
mysql -uroot -prootpass -e "create database mytest; use mytest; create table t(a int primary key); insert into t values (1); select * from t"
rm -Rf buildbot
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get upgrade -y
```

The Ubuntu 10.10 "maverick" images were likewise installed manually:

Create and boot 64-bit maverick upgrade image:

```
qemu-img create -b vm-maverick-amd64-install.qcow2 -f qcow2 vm-maverick-amd64-upgrade2.qcow2
kvm -m 512 -hda vm-maverick-amd64-upgrade2.qcow2 -redir 'tcp:2200::22' -boot c -smp 1 -cpu qemu64 -net nic,model=virtio -net user -nographic

ssh -p 2200 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no buildbot@localhost mkdir buildbot
scp -P 2200 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -r /archive/pack/mariadb-5.1-knielsen/build-619/kvm-deb-maverick-amd64/debs buildbot@localhost:buildbot/
ssh -p 2200 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no buildbot@localhost

sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y --allow-unauthenticated mariadb-server mariadb-test libmariadbclient-dev
mysql -uroot -prootpass -e "create database mytest; use mytest; create table t(a int primary key); insert into t values (1); select * from t"
rm -Rf buildbot
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get upgrade -y
```

Same for 32-bit maverick:

```
qemu-img create -b vm-maverick-i386-install.qcow2 -f qcow2 vm-maverick-i386-upgrade2.qcow2
kvm -m 512 -hda vm-maverick-i386-upgrade2.qcow2 -redir 'tcp:2200::22' -boot c -smp 1 -cpu qemu32,-nx -net nic,model=virtio -net user -nographic

ssh -p 2200 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no buildbot@localhost mkdir buildbot
scp -P 2200 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -r /archive/pack/mariadb-5.1-knielsen/build-619/kvm-deb-maverick-x86/debs buildbot@localhost:buildbot/
ssh -p 2200 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no buildbot@localhost

sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y --allow-unauthenticated mariadb-server mariadb-test libmariadbclient-dev
mysql -uroot -prootpass -e "create database mytest; use mytest; create table t(a int primary key); insert into t values (1); select * from t"
rm -Rf buildbot
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get upgrade -y
```

For Ubuntu 11.04 "natty", mariadb packages were installed from the repository\
for the previous version.

64-bit Ubuntu natty:

```
qemu-img create -b vm-natty-amd64-install.qcow2 -f qcow2 vm-natty-amd64-upgrade2.qcow2
kvm -m 512 -hda vm-natty-amd64-upgrade2.qcow2 -redir 'tcp:2200::22' -boot c -smp 1 -cpu qemu64 -net nic,model=virtio -net user -nographic
ssh -p 2200 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no buildbot@localhost

sudo sh -c 'cat > /etc/apt/sources.list.d/tmp.list'
deb http://ftp.osuosl.org/pub/mariadb/repo/5.1/ubuntu maverick main
deb-src http://ftp.osuosl.org/pub/mariadb/repo/5.1/ubuntu maverick main

sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y --allow-unauthenticated mariadb-server mariadb-test libmariadbclient-dev
mysql -uroot -prootpass -e "create database mytest; use mytest; create table t(a int primary key); insert into t values (1); select * from t"
sudo rm /etc/apt/sources.list.d/tmp.list
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get upgrade -y
```

32-bit Ubuntu natty:

```
qemu-img create -b vm-natty-i386-install.qcow2 -f qcow2 vm-natty-i386-upgrade2.qcow2
kvm -m 512 -hda vm-natty-i386-upgrade2.qcow2 -redir 'tcp:2200::22' -boot c -smp 1 -cpu qemu64 -net nic,model=virtio -net user -nographic
ssh -p 2200 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no buildbot@localhost

sudo sh -c 'cat > /etc/apt/sources.list.d/tmp.list'
deb http://ftp.osuosl.org/pub/mariadb/repo/5.1/ubuntu maverick main
deb-src http://ftp.osuosl.org/pub/mariadb/repo/5.1/ubuntu maverick main

sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y --allow-unauthenticated mariadb-server mariadb-test libmariadbclient-dev
mysql -uroot -prootpass -e "create database mytest; use mytest; create table t(a int primary key); insert into t values (1); select * from t"
sudo rm /etc/apt/sources.list.d/tmp.list
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get upgrade -y
```

For Ubuntu 11.10 "oneiric". The steps performed are listed at: [Buildbot Setup for Virtual Machines - Ubuntu 11.10 "oneiric"](../buildbot-setup-for-virtual-machines-ubuntu/buildbot-setup-for-virtual-machines-ubuntu-1110-oneiric.md) (in the VMs for Upgrade Testing section)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
