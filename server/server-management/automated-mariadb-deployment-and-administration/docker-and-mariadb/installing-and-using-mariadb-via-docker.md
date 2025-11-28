# Installing and Using MariaDB via Docker

Sometimes we want to install a specific version of MariaDB, [MariaDB ColumnStore](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/rBEU9juWLfTDcdwF3Q14/), or [MaxScale](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/0pSbu5DcMSW4KwAkUcmX/) on a certain system, but no packages are available. Or maybe, we simply want to isolate MariaDB from the rest of the system, to be sure that we won't cause any damage.

A virtual machine would certainly serve the scope. However, this means installing a system on the top of another system. It requires a lot of resources.

In many cases, the best solution is using containers. Docker is a framework that runs containers. A container is meant to run a specific daemon, and the software that is needed for that daemon to properly work. Docker does not virtualize a whole system; a container only includes the packages that are not included in the underlying system.

Docker requires a very small amount of resources. It can run on a virtualized system. It is used both in development and in production environments. Docker is an open source project, released under the Apache License, version 2.

Note that, while your package repositories could have a package called `docker`, it is probably not the Docker we are talking about. The Docker package could be called `docker.io` or `docker-engine`.

For information about installing Docker, see [Get Docker](https://docs.docker.com/get-docker/) in Docker documentation.

## Installing Docker on Your System with the Universal Installation Script

The script below will install the Docker repositories, required kernel modules and packages on the most common Linux distributions:

```bash
curl -sSL https://get.docker.com/ | sh
```

### Starting dockerd

On some systems you may have to start the `dockerd daemon` yourself:

```bash
sudo systemctl start docker
sudo gpasswd -a "${USER}" docker
```

If `dockerd` is not running, you will encounter the following error when using most `docker` commands:

```
Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
```

## Using MariaDB Images

The easiest way to use MariaDB on Docker is choosing a MariaDB image and creating a container.

### Downloading an Image

You can download a MariaDB image for Docker from the [Offical Docker MariaDB](https://hub.docker.com/_/mariadb/), or choose another image that better suits your needs. You can search Docker Hub (the official set of repositories) for an image with this command:

```bash
docker search mariadb
```

Once you have found an image that you want to use, you can download it via Docker. Some layers including necessary dependencies will be downloaded too. Note that, once a layer is downloaded for a certain image, Docker will not need to download it again for another image.

For example, if you want to install the default MariaDB image, you can type:

```bash
docker pull mariadb:10.6
```

This will install the 10.6 version. 

You will see a list of necessary layers. For each layer, Docker will say if it is already present, or its download progress.

To get a list of installed images:

```bash
docker images
```

### Creating a Container

An image is not a running process; it is just the software needed to be launched. To run it, we must create a container first. The command needed to create a container can usually be found in the image documentation. For example, to create a container for the official MariaDB image:

```bash
docker run --name mariadbtest -e MYSQL_ROOT_PASSWORD=mypass -p 3306:3306 -d docker.io/library/mariadb:10.3
```

`mariadbtest` is the name we want to assign the container. If we don't specify a name, an id will be automatically generated.

10.2 and 10.5 are also valid target versions:

```bash
docker run --name mariadbtest -e MYSQL_ROOT_PASSWORD=mypass -p 3306:3306 -d docker.io/library/mariadb:10.2
```

```bash
docker run --name mariadbtest -e MYSQL_ROOT_PASSWORD=mypass -p 3306:3306  -d docker.io/library/mariadb:10.5
```

Optionally, after the image name, we can specify some [options for mariadbd](../../starting-and-stopping-mariadb/mariadbd-options.md). For example:

```bash
docker run --name mariadbtest -e MYSQL_ROOT_PASSWORD=mypass -p 3306:3306 -d mariadb:10.3 --log-bin --binlog-format=MIXED
```

Docker will respond with the container's id. But, just to be sure that the container has been created and is running, we can get a list of running containers in this way:

```bash
docker ps
```

We should get an output similar to this one:

```
CONTAINER ID        IMAGE                      COMMAND                CREATED             STATUS              PORTS               NAMES
819b786a8b48        mariadb                    "/docker-entrypoint.   4 minutes ago       Up 4 minutes        3306/tcp            mariadbtest
```

### Running and Stopping the Container

Docker allows us to restart a container with a single command:

```bash
docker restart mariadbtest
```

The container can also be stopped like this:

```bash
docker stop mariadbtest
```

The container will not be destroyed by this command. The data will still live inside the container, even if MariaDB is not running. To restart the container and see our data, we can issue:

```bash
docker start mariadbtest
```

With `docker stop`, the container will be gracefully terminated: a `SIGTERM` signal will be sent to the `mariadbd` process, and Docker will wait for the process to shutdown before returning the control to the shell. However, it is also possible to set a timeout, after which the process will be immediately killed with a `SIGKILL`. Or it is possible to immediately kill the process, with no timeout.

```bash
docker stop --time=30 mariadbtest
docker kill mariadbtest
```

In case we want to destroy a container, perhaps because the image does not suit our needs, we can stop it and then run:

```bash
docker rm mariadbtest
```

Note that the command above does not destroy the data volume that Docker has created for /var/lib/mysql. If you want to destroy the volume as well, use:

```bash
docker rm -v mariadbtest
```

#### Automatic Restart

When we start a container, we can use the `--restart` option to set an automatic restart policy. This is useful in production.

Allowed values are:

* `no`: No automatic restart.
* `on-failure`: The container restarts if it exits with a non-zero exit code.
* `unless-stopped`: Always restart the container, unless it was explicitly stopped as shown above.
* `always`: Similar to `unless-stopped`, but when Docker itself restarts, even containers that were explicitly stopped will restart.

It is possible to change the restart policy of existing, possibly running containers:

```bash
docker update --restart always mariadb
# or, to change the restart policy of all containers:
docker update --restart always $(docker ps -q)
```

A use case for changing the restart policy of existing containers is performing maintenance in production. For example, before upgrading the Docker version, we may want to change all containers restart policy to `always`, so they will restart as soon as the new version is up and running. However, if some containers are stopped and not needed at the moment, we can change their restart policy to `unless-stopped`.

#### Pausing Containers

A container can also be frozen with the `pause` command. Docker will freeze the process using croups. MariaDB will not know that it is being frozen and, when we `unpause` it, MariaDB will resume its work as expected.

Both `pause` and `unpause` accept one or more container names. So, if we are running a cluster, we can freeze and resume all nodes simultaneously:

```bash
docker pause node1 node2 node3
docker unpause node1 node2 node3
```

Pausing a container is very useful when we need to temporarily free our system's resources. If the container is not crucial at this moment (for example, it is performing some batch work), we can free it to allow other programs to run faster.

### Troubleshooting a Container

If the container doesn't start, or is not working properly, we can investigate with the following command:

```bash
docker logs mariadbtest
```

This command shows what the daemon sent to the stdout since the last attempt of starting - the text that we typically see when we invoke `mariadbd` from the command line.

On some systems, commands such as `docker stop mariadbtest` and `docker restart mariadbtest` may fail with a permissions error. This can be caused by AppArmor, and even `sudo` won't allow you to execute the command. In this case, you will need to find out which profile is causing the problem and correct it, or disable it. **Disabling AppArmor altogether is not recommended, especially in production.**

To check which operations were prevented by AppArmor, see [AppArmor Failures](https://gitlab.com/apparmor/apparmor/-/wikis/AppArmor_Failures) in AppArmor documentation.

To disable a profile, create a symlink with the profile name (in this example, `mariadbd`) to `etc/apparmor.d/disable`, and then reload profiles:

```bash
ln -s /etc/apparmor.d/usr.sbin.mariadbd /etc/apparmor.d/disable/
sudo apparmor_parser -R /etc/apparmor.d/usr.sbin.mariadbd
```

For more information, see [Policy Layout](https://gitlab.com/apparmor/apparmor/-/wikis/Policy_Layout) in AppArmor documentation.

After disabling the profile, you may need to run:

```bash
sudo service docker restart
docker system prune --all --volumes
```

Restarting the system will then allow Docker to operate normally.

### Accessing the Container

To access the container via Bash, we can run this command:

```bash
docker exec -it mariadbtest bash
```

Now we can use normal Linux commands like _cd_, _ls_, etc. We will have root privileges. We can even install our favorite file editor, for example:

```bash
apt-get update
apt-get install vim
```

In some images, no repository is configured by default, so we may need to add them.

Note that if we run [mariadb-admin shutdown](https://github.com/mariadb-corporation/docs-server/blob/test/server/clients-and-utilities/mariadb-admin.md#mariadb-admin-commands) or the [SHUTDOWN](../../../reference/sql-statements/administrative-sql-statements/shutdown.md) command to stop the container, the container will be deactivated, and we will automatically exit to our system.

### Connecting to MariaDB from Outside the Container

If we try to connect to the MariaDB server on `localhost`, the client will bypass networking and attempt to connect to the server using a socket file in the local filesystem. However, this doesn't work when MariaDB is running inside a container because the server's filesystem is isolated from the host. The client can't access the socket file which is inside the container, so it fails to connect.

Therefore connections to the MariaDB server must be made using TCP, even when the client is running on the same machine as the server container.

Find the IP address that has been assigned to the container:

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mariadbtest
```

You can now connect to the MariaDB server using a TCP connection to that IP address.

#### Forcing a TCP Connection

After enabling network connections in MariaDB as described above, we will be able to connect to the server from outside the container.

On the host, run the client and set the server address ("-h") to the container's IP address that you found in the previous step:

```bash
mysql -h 172.17.0.2 -u root -p
```

This simple form of the connection should work in most situations. Depending on your configuration, it may also be necessary to specify the port for the server or to force TCP mode:

```bash
mysql -h 172.17.0.2 -P 3306 --protocol=TCP -u root -p
```

#### Port Configuration for Clustered Containers and Replication

Multiple MariaDB servers running in separate Docker containers can connect to each other using TCP. This is useful for forming a Galera cluster or for replication.

When running a cluster or a replication setup via Docker, we will want the containers to use different ports. The fastest way to achieve this is mapping the containers ports to different port on our system. We can do this when creating the containers (`docker run` command), by using the `-p` option, several times if necessary. For example, for Galera nodes we will use a mapping similar to this one:

```bash
-p 4306:3306 -p 5567:5567 -p 5444:5444 -p 5568:5568
```

## Installing MariaDB on Another Image

It is possible to download a Linux distribution image, and to install MariaDB on it. This is not much harder than installing MariaDB on a regular operating system (which is easy), but it is still the hardest option. Normally we will try existing images first. However, it is possible that no image is available for the exact version we want, or we want a custom installation, or perhaps we want to use a distribution for which no images are available. In these cases, we will install MariaDB in an operating system image.

### Daemonizing the Operating System

First, we need the system image to run as a daemon. If we skip this step, MariaDB and all databases will be lost when the container stops.

To demonize an image, we need to give it a command that never ends. In the following example, we will create a Debian Jessie daemon that constantly pings the 8.8.8.8 special address:

```bash
docker run --name debian -p 3306:3306 -d debian /bin/sh -c "while true; do ping 8.8.8.8; done"
```

### Installing MariaDB

At this point, we can enter the shell and issue commands. First we will need to update the repositories, or no packages will be available. We can also update the packages, in case some of them are newer than the image. Then, we will need to install a text editor; we will need it to edit configuration files. For example:

```bash
# start an interactive Bash session in the container
docker exec -ti debian bash
apt-get -y update
apt-get -y upgrade
apt-get -y install vim
```

Now we are ready to [install MariaDB](../../install-and-upgrade-mariadb/) in the way we prefer.

## See Also

* [Official MariaDB Docker Images Webinar](https://go.mariadb.com/GLBL-WBN_2018-10-09-MariaDB_Containers.html).
* [Docker official site](https://www.docker.com/).
* [Docker Hub](https://hub.docker.com/).
* [Docker documentation](https://docs.docker.com/).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
