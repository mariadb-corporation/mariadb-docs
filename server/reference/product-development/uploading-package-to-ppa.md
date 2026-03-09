---
description: >-
  Provides instructions for developers to upload MariaDB source packages to a
  Personal Package Archive (PPA) using tools like dput for Ubuntu-based
  distributions.
---

# Uploading Package to PPA

After creating a Launchpad account:

#### Docker build, cloning the MariaDB repository and mapping it to the docker container

1. mkdir mariadb-source
2. cd mariadb-source
3. vi Dockerfile
4. Copy the following contents to Dockerfile:

```
# MariaDB 10.3 Ubuntu 17.10 build environment
# Published as mariadb-10-3-ubuntu-17.10-build-env
FROM ubuntu:17.10
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
apt-get install -y --no-install-recommends \
systemd \
devscripts \
build-essential \
lsb-release \
equivs \
git \
curl \
git-buildpackage \
nano \
vim \
pristine-tar

RUN curl -skO https://raw.githubusercontent.com/ottok/mariadb-10.1/ubuntu-17.10/debian/control

ENV GIT_SSL_NO_VERIFY true

RUN mk-build-deps -t 'apt-get -y -o Debug::pkgProblemResolver=yes --no-install-recommends' -i control

ENV container docker
ENV DEBIAN_FRONTEND noninteractive
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
```

5. Run `docker build . -t ubuntu-17.10-packaging`
6. Do git clone of the latest repository:

`cd && mkdir debian-packaging && cd debian-packaging && git clone https://salsa.debian.org/mariadb-team/mariadb-10.1.git`

#### Generate, publish and upload PGP key

7. Generate OpenPGP key with the following command:

`$ gpg --gen-key`

* select (1) RSA and RSA
* Keysize: accept 2048
* Valid for: accept 0
* Type name, email and comment (comment is optional)
* Type 0
* Type passphrase (twice)
* Follow instructions to help generate a random key
* Keep the Key ID and fingerprint text, they are needed in the next step

Set generated key as default in `~/.bashrc`

`$ nano ~/.bashrc`

\[.. add this ..]

`export GPGKEY=<key_id>`

Restart GPG-agent and source '/.bashrc', or restart session

8. Publish the key to the key server:

`gpg --keyserver keyserver.ubuntu.com --send-keys 12345678` and substitute `12345678` with your key's id

* If this gives timeout error, keep re-trying after a while

9. Upload the key's fingerprint here:\
   Upload [ImportingYourPGPKey](https://help.launchpad.net/YourAccount/ImportingYourPGPKey) fingerprint here [+editpgpkeys](https://launchpad.net/~rsurve/+editpgpkeys)
10. `gpg --export [your-key-id] > ~/debian-packaging/pub.key`
11. `gpg --export-secret-key [your-key-id] > ~/debian-packaging/secret.key`

`gpg -k`

^Should show the key

12. How to upload:[How-to-upload-to-Launchpad-PPA-repository-(.deb-packages)](https://github.com/exelearning/iteexe/wiki/How-to-upload-to-Launchpad-PPA-repository-\(.deb-packages\))
13. Open `/etc/devscripts.conf`

And look for this line:

`DEBSIGN_MAINT`

Uncomment it and add your name there

`export DEBEMAIL=[your-email-id]`

#### From inside the container

14. `docker run -v ~/debian-packaging/:/repo -it ubuntu-17.10-packaging bash`
15. `apt-get install devscripts`
16. `gpg --import pub.key`
17. `gpg --import secret.key`
18. `gpg -k`
19. `cd /repo/mariadb-10.1 && git fetch && git checkout pristine-tar && git checkout ubuntu-17.10`
20. `git clean -dffx && git reset --hard HEAD`
21. `export DEB_BUILD_OPTIONS="parallel=10 nocheck"` or `export DEB_BUILD_OPTIONS="parallel=5 nocheck"`
22. Go to `/repo` folder (Inside docker) and delete all the files except mariadb-10.1 folder:

`rm *`

23.

`gbp buildpackage`

#### For re-running the set up container

24. To generate an ID, run:`docker commit <container-id>` This will generate an ID.

For restarting the same container again use this ID:`docker run -v ~/debian-packaging/:/repo -it <ID> bash`

25. Last command for uploading package to PPA:

`backportpackage -u <your-ppa-address> -d <ubuntu-version-to-backport-to> -S ~<a-version-suffix-name-for-this-package> <the-most-recent-dsc-file>`

Example:

`backportpackage -u ppa:cvicentiu/mariadb-10.0-dev2 -d bionic -S ~testtry mariadb-10.1_10.1.30-0ubuntu0.17.10.1.dsc`

Run this command in the `/repo` folder, where the `.dsc` file is located\
It should ask for the gpg key password again

* Docker tutorial available here:[edit#slide=id.p4](https://docs.google.com/presentation/d/1euJrK7MJ9QRvwW33iwESIEo5Dyi7JWExIKFrISktFao/edit#slide=id.p4)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
