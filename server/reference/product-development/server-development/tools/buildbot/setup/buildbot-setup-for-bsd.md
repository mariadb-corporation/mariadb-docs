---
description: >-
  Outlines the necessary steps to install and configure Buildbot on various BSD
  distributions.
---

# Buildbot Setup for BSD

Here are the steps I did when installing and configuring a buildbot slave on a PC-BSD 9 box.

Add buildbot user:

```bash
sudo adduser
  buildbot
  /bin/sh
```

Python was already installed.

Bazaar was already installed.

NTP was already installed.

Install Zope3:

```bash
cd /usr/ports/www/zope3
sudo make install clean
  # accepted default options
cd /usr/ports/devel/py-zope.interface
sudo make install clean
```

Install Twisted:

```bash
cd /usr/ports/devel/py-twisted
sudo make install clean
  # accepted default options
```

Install `ccache`:

```bash
cd /usr/ports/devel/ccache
sudo make install clean
  # accepted default options
```

Run a test compile of MariaDB:

```bash
cd
cd src/maria/build
BUILD/compile-pentium64-max
  # test compile appeared to work
```

Install buildbot:

```bash
cd /usr/ports/devel/buildbot
sudo make install clean
  # accepted default options
```

Create the buildbot slave. On the build master, add new entry to `/etc/buildbot/maria-master-private.cfg` :

```ini
slave-name=bsd9
```

Remember the `${slave-name}` and `${password}` configured above, they're used in\
the next step.

Back on `bsd9`, do this:

```bash
sudo su - buildbot
buildslave create-slave --usepty=0 /home/buildbot/maria-slave \
hasky.askmonty.org:9989 ${slave-name} ${password}

echo '${contact-email-address}' > /home/buildbot/maria-slave/info/admin
echo 'A host running PC-BSD 9.' > /home/buildbot/maria-slave/info/host

bzr init-repo maria-slave/bsd9

exit
```

Start the build slave:

```bash
sudo su - buildbot
buildslave start maria-slave
```

Create the archive directory:

```bash
sudo su - buildbot
mkdir archive
exit
sudo ln -s /home/buildbot/archive /archive
```

Install Apache:

```bash
cd /usr/ports/www/apache22
sudo make install clean
  # accepted default options
```

Configure Apache:

```bash
sudo su -s
echo 'apache22_enable="YES"' >> /etc/rc.conf
echo 'alias /archive "/archive"\
<Directory "/archive">\
  Options All Multiviews\
  AllowOverride All\
  Order allow,deny\
  Allow from all\
</Directory>' >> /usr/local/etc/apache22/httpd.conf

sudo /usr/local/etc/rc.d/apache22 start
```

Install `md5sum`:

```bash
md5sum already installed at /compat/linux/usr/bin/md5sum
edited /home/buildbot/.profile and added that dir to the path
  # That didn't work, so did the following:
cd /usr/local/bin/
sudo ln -s /compat/linux/usr/bin/md5sum md5sum
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
