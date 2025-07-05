# Docker Official Image Frequently Asked Questions

Frequently asked questions about the Docker Official Image

## How to Reset Passwords

If you have an existing data directory and wish to reset the root and user passwords, and to create a database which the user can fully modify, perform the following steps.

First create a `passwordreset.sql` file:

```
CREATE USER IF NOT EXISTS root@localhost IDENTIFIED BY 'thisismyrootpassword';
SET PASSWORD FOR root@localhost = PASSWORD('thisismyrootpassword');
GRANT ALL ON *.* TO root@localhost WITH GRANT OPTION;
GRANT PROXY ON ''@'%' ON root@localhost WITH GRANT OPTION;
CREATE USER IF NOT EXISTS root@'%' IDENTIFIED BY 'thisismyrootpassword';
SET PASSWORD FOR root@'%' = PASSWORD('thisismyrootpassword');
GRANT ALL ON *.* TO root@'%' WITH GRANT OPTION;
GRANT PROXY ON ''@'%' ON root@'%' WITH GRANT OPTION;
CREATE USER IF NOT EXISTS myuser@'%' IDENTIFIED BY 'thisismyuserpassword';
SET PASSWORD FOR myuser@'%' = PASSWORD('thisismyuserpassword');
CREATE DATABASE IF NOT EXISTS databasename;
GRANT ALL ON databasename.* TO myuser@'%';
```

Adjust `myuser`, `databasename` and passwords as needed.

Then:

```
$ docker run --rm -v /my/own/datadir:/var/lib/mysql -v /my/own/passwordreset.sql:/passwordreset.sql:z %%IMAGE%%:latest --init-file=/passwordreset.sql
```

On restarting the MariaDB container in this `/my/own/datadir`, the `root` and `myuser` passwords will be reset.

## Temp Server Start Timeout

Question, are you getting errors like the following where a temporary server start fails to succeed in 30 seconds?

Example of log:

```
2023-01-28 12:53:42+00:00 [Note] [Entrypoint]: Starting temporary server
2023-01-28 12:53:42+00:00 [Note] [Entrypoint]: Waiting for server startup
2023-01-28 12:53:42 0 [Note] mariadbd (server 10.10.2-MariaDB-1:10.10.2+maria~ubu2204) starting as process 72 ...
....
2023-01-28 12:53:42 0 [Note] InnoDB: Setting file './ibtmp1' size to 12.000MiB. Physically writing the file full; Please wait ...
2023-01-28 12:54:13 0 [Note] mariadbd: ready for connections.
Version: '10.10.2-MariaDB-1:10.10.2+maria~ubu2204'  socket: '/run/mysqld/mysqld.sock'  port: 0  mariadb.org binary distribution
2023-01-28 12:54:13+00:00 [ERROR] [Entrypoint]: Unable to start server.
```

The timeout on a temporary server start is a quite generous 30 seconds.

The lack of a message like the following indicates it failed to complete writing a temporary file of 12MiB in 30 seconds.

```
2023-01-28 12:53:46 0 [Note] InnoDB: File './ibtmp1' size is now 12.000MiB.
```

If the datadir where this is stored is remote storage maybe it's a bit slow. It's ideal to have an InnoDB temporary path local so this can be configured using the command or configuration setting:

```
innodb_temp_data_file_path=/dev/shm/ibtmp1:12M:autoextend
```

Note: depending on container runtime this space may be limited.

## Creating a replication pair

`MARIADB_REPLICATION_USER` / `MARIADB_REPLICATION_PASSWORD` specify the authentication for the connection. The `MARIADB_MASTER_HOST` is the indicator that it is a replica and specifies the container aka hostname, of the master.

A `docker-compose.yml` example:

```
version: "3"
services:
  master:
    image: mariadb:latest
    command: --log-bin --log-basename=mariadb
    environment:
      - MARIADB_ROOT_PASSWORD=password
      - MARIADB_USER=testuser
      - MARIADB_PASSWORD=password
      - MARIADB_DATABASE=testdb
      - MARIADB_REPLICATION_USER=repl
      - MARIADB_REPLICATION_PASSWORD=replicationpass
    healthcheck:
      test: ["CMD", "healthcheck.sh", "--connect", "--innodb_initialized"]
      interval: 10s
      timeout: 5s
      retries: 3
  replica:
    image: mariadb:latest
    command: --server-id=2 --log-basename=mariadb
    environment:
      - MARIADB_ROOT_PASSWORD=password
      - MARIADB_MASTER_HOST=master
      - MARIADB_REPLICATION_USER=repl
      - MARIADB_REPLICATION_PASSWORD=replicationpass
      - MARIADB_HEALTHCHECK_GRANTS=REPLICA MONITOR
    healthcheck:
      test: ["CMD", "healthcheck.sh", "--connect", "--replication_io", "--replication_sql", "--replication_seconds_behind_master=1", "--replication"]
      interval: 10s
      timeout: 5s
      retries: 3
    depends_on:
      master:
        condition: service_healthy
```

## Event Scheduler: An error occurred when initializing system tables. Disabling the Event Scheduler.

This will show up in the container log as:

```
2024-01-29 17:38:13 0 [ERROR] Incorrect definition of table mysql.event: expected column 'definer' at position 3 to have type varchar(, found type char(141).
2024-01-29 17:38:13 0 [ERROR] mariadbd: Event Scheduler: An error occurred when initializing system tables. Disabling the Event Scheduler.
```

The cause is the underlying table has change structure from the last MariaDB version. The easiest solution to this is to start the container with the environment variable [MARIADB\_AUTO\_UPGRADE=1](mariadb-server-docker-official-image-environment-variables.md#mariadb_auto_upgrade-mariadb_disable_upgrade_backup) and system tables will be updated. This is safe to keep on as it detects the version installed. The next start should not show this error.

## InnoDB: Upgrade after a crash is not supported. The redo log was created with MariaDB X.Y.Z

This will show up in the error log as:

```
2022-05-23 12:29:20 0 [ERROR] InnoDB: Upgrade after a crash is not supported. The redo log was created with MariaDB 10.5.4.
2022-05-23 12:29:20 0 [ERROR] InnoDB: Plugin initialization aborted with error Generic error
```

This is attempting to start on a higher MariaDB version when the shutdown of the previous version crashed.

By crashed, it means the MariaDB was force killed or had a hard power failure. MariaDB, being a durable database, can recover from these, if started with the same version. The redo log however is a less stable format, so the recovery has to be on the same Major.Minor version, in this case 10.5. This error message is saying that you when from force killed MariaDB to a later version.

So whenever you encounter this message. Start with the again with the tag set to the version in the error message, like 10.5.4, or as the redo long format is consistent in the Major.Minor version 10.5 is sufficient. After this has been started correctly, cleanly shut the service down and it will be recovered.

The logs on shutdown should have a message like:

```
2023-11-06 10:49:23 0 [Note] InnoDB: Shutdown completed; log sequence number 84360; transaction id 49
2023-11-06 10:49:23 0 [Note] mariadbd: Shutdown complete
```

After you see this, you can update your MariaDB tag to a later version.

## Every MariaDB start gives permission denied messages

```
2024-02-06 03:03:18+00:00 [Note] [Entrypoint]: Entrypoint script for MariaDB Server 1:10.11.6+maria~ubu2204 started.
/usr/local/bin/docker-entrypoint.sh: line 600: /var/lib/mysql//mysql_upgrade_info: Permission denied
2024-02-06 03:03:18+00:00 [Note] [Entrypoint]: MariaDB upgrade (mariadb-upgrade) required, but skipped due to $MARIADB_AUTO_UPGRADE setting
2024-02-06  3:03:18 0 [Warning] Can't create test file '/var/lib/mysql/80a2bb81d698.lower-test' (Errcode: 13 "Permission denied")
2024-02-06  3:03:18 0 [Note] Starting MariaDB 10.11.6-MariaDB-1:10.11.6+maria~ubu2204 source revision fecd78b83785d5ae96f2c6ff340375be803cd299 as process 1
2024-02-06  3:03:18 0 [ERROR] mariadbd: Can't create/write to file './ddl_recovery.log' (Errcode: 13 "Permission denied")
2024-02-06  3:03:18 0 [ERROR] DDL_LOG: Failed to create ddl log file: ./ddl_recovery.log
2024-02-06  3:03:18 0 [ERROR] Aborting
```

Or:

```
2024-08-16  4:54:05 0 [ERROR] InnoDB: Operating system error number 13 in a file operation.
2024-08-16  4:54:05 0 [ERROR] InnoDB: The error means mariadbd does not have the access rights to the directory.
```

In this case, the container is running as a user that, inside the container, does not have write permissions on the datadir `/varlib/mysql`.

## Bad magic header in tc log

From the [transaction coordinator log](../../../../../server-monitoring-logs/transaction-coordinator-log/transaction-coordinator-log-overview.md#bad-magic-header-in-tc-log) this is a corrupted file. This will have a log message like the following:

```
2024-05-21  8:55:58 0 [Note] Recovering after a crash using tc.log
2024-05-21  8:55:58 0 [ERROR] Bad magic header in tc log
2024-05-21  8:55:58 0 [ERROR] Crash recovery failed. Either correct the problem (if it's, for example, out of memory error) and restart, or delete tc log and start server with --tc-heuristic-recover={commit|rollback}
2024-05-21  8:55:58 0 [ERROR] Can't init tc log
2024-05-21  8:55:58 0 [ERROR] Aborting
```

The cause of this is headed by the first not, its a crash recovery. Like the [Every MariaDB start is a crash recovery](docker-official-image-frequently-asked-questions.md#every-mariadb-start-is-a-crash-recovery) answer below, this is an indication that MariaDB wasn't given enough time by the container runtime to shutdown cleanly. While MariaDB was shutdown, the new version that was started is a newer MariaDB and doesn't recognise the updated magic information in the header.

MariaDB should always perform crash recovery with the same version that actually crashed, the same major/minor number at least.

As such the solution is to restart the container with the previous MariaDB version that was running, and configure the container runtime to allow a longer stop time. See the [Every MariaDB start is a crash recovery](docker-official-image-frequently-asked-questions.md#every-mariadb-start-is-a-crash-recovery) answer below to see if the timeout is sufficiently extended.

## Every MariaDB start is a crash recovery

Do you get on every start:

```
db-1  | 2023-02-25 19:10:02 0 [Note] Starting MariaDB 10.11.2-MariaDB-1:10.11.2+maria~ubu2204-log source revision cafba8761af55ae16cc69c9b53a341340a845b36 as process 1                                                                                                         
db-1  | 2023-02-25 19:10:02 0 [Note] mariadbd: Aria engine: starting recovery                                                                                                                                                                                                   
db-1  | tables to flush: 3 2 1 0                                                                                                                                                                                                                                                
db-1  |  (0.0 seconds);                                                                                                                                                                                                                                                         
db-1  | 2023-02-25 19:10:02 0 [Note] mariadbd: Aria engine: recovery done  
...
db-1  | 2023-02-26 13:03:29 0 [Note] InnoDB: Initializing buffer pool, total size = 32.000GiB, chunk size = 512.000MiB
db-1  | 2023-02-26 13:03:29 0 [Note] InnoDB: Completed initialization of buffer pool
db-1  | 2023-02-26 13:03:29 0 [Note] InnoDB: File system buffers for log disabled (block size=512 bytes)
db-1  | 2023-02-26 13:03:29 0 [Note] InnoDB: Starting crash recovery from checkpoint LSN=193796878816
```

Container runtimes are assume to start and stop very quickly. Check the shutdown logs. They may be a log like:

```
db-1  | 2023-02-26 13:03:17 0 [Note] InnoDB: Starting shutdown...                                                                                                                                                                                                               
db-1  | 2023-02-26 13:03:17 0 [Note] InnoDB: Dumping buffer pool(s) to /var/lib/mysql/ib_buffer_pool                                                                                                                                                                            
db-1  | 2023-02-26 13:03:17 0 [Note] InnoDB: Restricted to 519200 pages due to innodb_buf_pool_dump_pct=25                                                                                                                                                                      
db-1  | 2023-02-26 13:03:17 0 [Note] InnoDB: Buffer pool(s) dump completed at 230226 13:03:17                                                                                                                                                                                   
db-1 exited with code 0
```

Note that the logs didn't include the following messages:

```
db-1  | 2023-02-26 13:03:43 0 [Note] InnoDB: Shutdown completed; log sequence number 46590; transaction id 15
db-1  | 2023-02-26 13:03:43 0 [Note] mariadbd: Shutdown complete
```

As these messages aren't here, the container was killed off before it could just down cleanly. When this happens, the startup will be a crash recovery and you won't be able to upgrade your MariaDB instance (previous FAQ) to the next Major.Minor version.

Solution is to extend the timeout in the container runtime to allow MariaDB to complete its shutdown.

## How do I create a MariaDB-backup of the data?

```
docker volume create backup
docker run --name mdb -v backup:/backup -v datavolume:/var/lib/mysql mariadb
docker exec mdb mariadb-backup --backup --target-dir=/backup/d --user root --password soverysecret
docker exec mdb mariadb-backup --prepare --target-dir=/backup/d
docker exec mdb sh -c '[ ! -f /backup/d/.my-healthcheck.cnf ] && cp /var/lib/mysql/.my-healthcheck.cnf /backup/d'
docker exec --workdir /backup/d mdb tar -Jcf ../backup.tar.xz .
docker exec mdb  rm -rf /backup/d
```

## How do I restore from a MariaDB-backup

With the backup prepared like previously:

```
docker run -v backup:/docker-entrypoint-initdb.d -v newdatavolume:/var/lib/mysql mariadb
```

## How to start MariaDB with Apptainer

Because Apptainer has all the filesystems readonly except or the volume, the /run/mysqld directory is used as a pidfile and socket directory. An easy way is to mark this as a scratch directory.

```
mkdir mydatadir
apptainer run --no-home --bind $PWD/mydatadir:/var/lib/mysql --env MARIADB_RANDOM_ROOT_PASSWORD=1 --net --network-args "portmap=3308:3306/tcp" --fakeroot --scratch=/run/mysqld  docker://mariadb:10.5
```

Alternately:

```
apptainer run --no-home --bind $PWD/mydatadir:/var/lib/mysql --env MARIADB_RANDOM_ROOT_PASSWORD=1 --net --network-args "portmap=3308:3306/tcp" --fakeroot   docker://mariadb:10.5 --socket=/var/lib/mysql/mariadb.sock --pid-file=/var/lib/mysql/mariadb.pid
```

## Why does the MariaDB container start as root?

The MariaDB entrypoint briefly starts as root, and if a explicit volume is there, the owner of this volume will be root. To allow MariaDB to use the CHOWN capability to change to the volume owner to a user that can write to this volume, it needs to be briefly root. After this one action is taken, the entrypoint uses **gosu** to drop to a non-root user and continues execution. There is no accessible exploit vector to remotely affect the container startup when it is briefly running as the root user.

## Can I run the MariaDB container as an arbitrary user?

Yes. using the _user: 2022_ in a compose file, or _--user 2022_ as a command will run the entrypoint as the user id 2022. When this occurs, it is assumed that the volume of the datadir has the right permissions for MariaDB to access the datadir. This can be useful if your local user is user id 2022 and your datadir is owned locally by this user. Note inside the container there isn't the same user names outside the container defined, so working with numbers is more portable.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
