---
description: >-
  Explains how to provision and configure virtual machine instances specifically
  for Buildbot testing.
---

# Install Cassandra on Fulltest VMs

CassandraSE is no longer actively being developed and has been removed in [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/what-is-mariadb-106). See [MDEV-23024](https://jira.mariadb.org/browse/MDEV-23024).

Here are the steps I took to install Cassandra on the Fulltest VMs.

1. backed up the fulltest VMs with:

```
rsync -avP /kvm/vms/*fulltest* host:/destination/path/
```

1. boot the amd64 fulltest VM:

```
vm=vm-precise-amd64-fulltest.qcow2
kvm -m 2048 -hda /kvm/vms/${vm} -boot c -smp 2 -cpu qemu64 -net nic,model=virtio -net user,hostfwd=tcp:127.0.0.1:22666-:22 -nographic
```

1. login to the VM:

```
ssh -t -p 22666 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -i /kvm/vms/ssh-keys/id_dsa dbart@localhost
```

1. in the VM, install Cassandra:

```
sudo vi /etc/apt/sources.list.d/cassandra.list

# paste in the following two lines:
deb http://www.apache.org/dist/cassandra/debian 11x main
deb-src http://www.apache.org/dist/cassandra/debian 11x main

gpg --keyserver pgp.mit.edu --recv-keys F758CE318D77295D
gpg --export --armor F758CE318D77295D | sudo apt-key add -

gpg --keyserver pgp.mit.edu --recv-keys 2B5C1B00
gpg --export --armor 2B5C1B00 | sudo apt-key add -

sudo apt-get update
sudo apt-get install cassandra
```

1. in the VM, launch the `cassandra-cli` program and test the Cassandra installation:

```
CREATE keyspace DEMO; 
USE DEMO; 

CREATE COLUMN family Users 
WITH key_validation_class = 'UTF8Type' 
AND comparator = 'UTF8Type' 
AND default_validation_class = 'UTF8Type'; 

SET Users[1234][name] = scott; 
SET Users[1234][password] = tiger; 
GET Users[1234]; 
quit;
```

* Output of the above:

```
dbart@ubuntu-precise-amd64:~$
 cassandra-cli

Connected to: "Test Cluster" on 127.0.0.1/9160
Welcome to Cassandra CLI version 1.1.9

Type 'help;' or '?' for help.
Type 'quit;' or 'exit;' to quit.

[default@unknown]
 create keyspace DEMO;

622a672f-dd03-37bf-bf78-f3e99a8f18a6
Waiting for schema agreement...
... schemas agree across the cluster
[default@unknown]
 use DEMO;

Authenticated to keyspace: DEMO
[default@DEMO]
 create column family Users

...    
 with key_validation_class = 'UTF8Type'

...    
 and comparator = 'UTF8Type'

...    
 and default_validation_class = 'UTF8Type';

605eea14-d3e5-3d1d-ab1d-f4863c814538
Waiting for schema agreement...
... schemas agree across the cluster
[default@DEMO]
 set Users[1234][name] = scott;

Value inserted.
Elapsed time: 46 msec(s).
[default@DEMO]
 set Users[1234][password] = tiger;

Value inserted.
Elapsed time: 2.77 msec(s).
[default@DEMO]
 get Users[1234];

=> (column=name, value=scott, timestamp=1361818884084000)
=> (column=password, value=tiger, timestamp=1361818887944000)
Returned 2 results.
Elapsed time: 53 msec(s).
[default@DEMO]
 quit;
```

1. in the VM, shut it down:

```
sudo shutdown -h now
```

1. Do steps 2-6 for `vm-precise-i386-fulltest.qcow2`. The output of the testing step was:

```
dbart@ubuntu-precise-i386:~$
 cassandra-cli

Connected to: "Test Cluster" on 127.0.0.1/9160
Welcome to Cassandra CLI version 1.1.9

Type 'help;' or '?' for help.
Type 'quit;' or 'exit;' to quit.

[default@unknown]
 create keyspace DEMO;

5eafc25e-71b6-3585-9db1-891b3348790c
Waiting for schema agreement...
... schemas agree across the cluster
[default@unknown]
 use DEMO;

Authenticated to keyspace: DEMO
[default@DEMO]
 create column family Users

...    
 with key_validation_class = 'UTF8Type'

...    
 and comparator = 'UTF8Type'

...    
 and default_validation_class = 'UTF8Type';

9c2ad7bc-8dc0-35ce-8067-4dc4577319f1
Waiting for schema agreement...
... schemas agree across the cluster
[default@DEMO]
 set Users[1234][name] = scott;

Value inserted.
Elapsed time: 51 msec(s).
[default@DEMO]
 set Users[1234][password] = tiger;

Value inserted.
Elapsed time: 2.44 msec(s).
[default@DEMO]
 get Users[1234];

=> (column=name, value=scott, timestamp=1361819341068000)
=> (column=password, value=tiger, timestamp=1361819345337000)
Returned 2 results.
Elapsed time: 57 msec(s).
[default@DEMO]
 quit;
```

1. on the other build hosts, rsync the files over:

```
rsync -avP host::kvm/vms/*fulltest* /kvm/vms/
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
