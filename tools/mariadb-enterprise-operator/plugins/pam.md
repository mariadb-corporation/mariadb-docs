# PAM Plugin

The MariaDB `pam` plugin facilitates user authentication by interfacing with the Pluggable Authentication Modules (PAM) framework, enabling diverse and centralized authentication schemes.

Currently the enterprise operator utilizes this plugin to provide support for:

- **LDAP based authentication**

## LDAP

This guide outlines the process of configuring MariaDB to authenticate users against an LDAP or Active Directory service. The integration is achieved by using MariaDB's Pluggable Authentication Module (PAM) plugin, which delegates authentication requests to the underlying Linux PAM framework.

### How Does It Work?

To enable LDAP authentication for MariaDB through PAM, several components work in tandem:

- **PAM (Pluggable Authentication Modules)**: A framework used by Linux and other UNIX-like systems to consolidate authentication tasks. Applications like MariaDB can use PAM to authenticate users without needing to understand the underlying authentication mechanism. Operations such as system login, screen unlocking, and sudo access commonly use PAM.

- **nss-pam-ldapd**: This is the software package that provides the necessary bridge between PAM and an LDAP server. It includes the core components required for authentication.

- **pam_ldap.so**: A specific PAM module, provided by the nss-pam-ldapd package. This module is the "plug-in" that the PAM framework loads to handle authentication requests destined for an LDAP server.

- **nslcd (Name Service Lookup Daemon)**: This daemon acts as an intermediary service. The pam_ldap.so module does not communicate directly with the LDAP server. Instead, it forwards authentication requests to the nslcd daemon, which manages the connection and communication with the LDAP directory. This design allows for connection caching and a more robust separation of concerns. 

{% hint style="info" %}
The `nslcd` daemon is ran as a sidecar container and communication happens through the shared socket, following container best practices of keeping a single process per container.
{% endhint %}

### What is needed for LDAP Auth?

`nslcd` is configured with 2 files. `nslcd.conf` which tells the daemon about the ldap server and `nsswitch.conf`, determine the sources from which to obtain name-service information.

`nslcd` can be configured to run as a specific user based on the `uid` and `gid` props specified in the config file, however that user should have sufficient permissions to read/write to `/var/run/nslcd`, should own both `nslcd.conf` and `nsswitch.conf` and they should not be too open (0600).

Both of these configuration files will be attached later on in the example given.

#### nslcd.conf

The `/etc/nslcd.conf` is the configuration file for LDAP nameservice daemon.

```ini
# /etc/nslcd.conf: Configuration file for nslcd(8)
# The user/group nslcd will run as. Note that these should not be LDAP users.
uid mysql # required to be `mysql`
gid mysql # required to be `mysql`

# The location of the LDAP server.
uri ldap://openldap-service.default.svc.cluster.local:389

# The search base that will be used for all queries.
base dc=openldap-service,dc=default,dc=svc,dc=cluster,dc=local

# The distinguished name with which to bind to the directory server for lookups.
# This is a service account used by the daemon.
binddn cn=admin,dc=openldap-service,dc=default,dc=svc,dc=cluster,dc=local
bindpw PASSWORD_REPLACE-ME
```

In a production environment it is recommended to use LDAPS (LDAP secure), which uses traditional TLS encryption to secure data in transit.
To do so, you need to add the following to your `nslcd.conf` file:


```diff
# Change the protocol to `ldaps`
+uri ldaps://openldap-service.default.svc.cluster.local:636
-uri ldap://openldap-service.default.svc.cluster.local:389

# ...

+tls_reqcert demand # Look at: https://linux.die.net/man/5/ldap.conf then search for TLS_REQCERT
+tls_cacertfile /etc/openldap/certs/tls.crt # You will need to mount this certificate (from a secret) later
```

#### nsswitch.conf

The Name Service Switch (NSS) configuration file, located at `/etc/nsswitch.conf`. It is used by the GNU C Library and certain other applications to determine the sources from which to obtain name-service information in a range of categories, and in what order. Each category of information is identified by a database name.

```ini
passwd:     files ldap
group:      files ldap
shadow:     files ldap
```

### Installing The PAM Plugin

The `pam` plugin is not enabled by default (even though it is installed). To enable it, you should add the following lines to your `MariaDB` Custom Resource:

```yaml
  # ....
  myCnf: |
    [mariadb]
    plugin_load_add = auth_pam # Load auth plugin
  # ....
```

See below for a complete example.

### Combining It All Together

Fistly, we need to create our ConfigMaps and Secrets, that will store the `nsswitch.conf`, `nslcd.conf` and the `mariadb` pam module.

{% hint style="warn" %}
**Make sure to adapt the `nslcd-conf` as per your ldap server configuration.**
{% endhint %}

**mariadb-nss-config.yaml:**
```yaml
---
apiVersion: v1
kind: Secret
type: Opaque
metadata:
  name: mariadb-nslcd-secret
  labels:
    enterprise.mariadb.com/watch: ""
stringData:
  nslcd.conf: |
    # Our Config Here
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: mariadb-nsswitch-configmap
  labels:
    enterprise.mariadb.com/watch: ""
data:
  nsswitch.conf: |
    passwd:     files ldap
    group:      files ldap
    shadow:     files ldap
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: mariadb-pam-configmap
  labels:
    enterprise.mariadb.com/watch: ""
data:
  mariadb: |
    # This is needed to tell PAM to use pam_ldap.so
    auth required pam_ldap.so
    account required pam_ldap.so
```
`kubectl apply -f mariadb-nss-config.yaml`

Now that our configuration is done, we need to create the MariaDB custom resource along with needed configurations.

**mariadb.yaml:**
```yaml
---
apiVersion: v1
kind: Secret
metadata:
  name: mariadb # Used to hold the mariadb and root user passwords
  labels:
    enterprise.mariadb.com/watch: ""
stringData:
  password: MariaDB11!
  root-password: MariaDB11!
---
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb
spec:
  rootPasswordSecretKeyRef:
    name: mariadb
    key: password

  username: mariadb
  passwordSecretKeyRef:
    name: mariadb-password
    key: password
    generate: true
  database: mariadb

  port: 3306

  storage:
    size: 1Gi

  service:
    type: LoadBalancer
    metadata:
      annotations:
        metallb.universe.tf/loadBalancerIPs: 172.18.0.20

  myCnf: |
    [mariadb]
    bind-address=*
    default_storage_engine=InnoDB
    binlog_format=row
    innodb_autoinc_lock_mode=2
    innodb_buffer_pool_size=800M
    max_allowed_packet=256M

    plugin_load_add = auth_pam # Load auth plugin

  resources:
    requests:
      cpu: 1
      memory: 128Mi
    limits:
      memory: 1Gi

  metrics:
    enabled: true

  volumes: # Attach `nslcd.conf`, `nsswitch.conf` and `mariadb` (pam). Also add an emptyDir volume for `nslcd` socket
    - name: nslcd
      secret:
        secretName: mariadb-nslcd-secret
        defaultMode: 0600
    - name: nsswitch
      configMap:
        name: mariadb-nsswitch-configmap
        defaultMode: 0600
    - name: mariadb-pam
      configMap:
        name: mariadb-pam-configmap
        defaultMode: 0600
    - name: nslcd-run
      emptyDir: {}

  sidecarContainers:
    # The `nslcd` daemon is ran as a sidecar container
    - name: nslcd
      image: docker.mariadb.com/nslcd:0.9.10-13
      volumeMounts:
        - name: nslcd
          mountPath: /etc/nslcd.conf
          subPath: nslcd.conf
        - name: nsswitch
          mountPath: /etc/nsswitch.conf
          subPath: nsswitch.conf
      # nslcd-run is missing because volumeMounts from main container are shared with sidecar

  volumeMounts:
    - name: mariadb-pam
      mountPath: /etc/pam.d/mariadb
      subPath: mariadb
    - name: nslcd-run
      mountPath: /var/run/nslcd
```
`kubectl apply -f mariadb.yaml`

And in the end we need to create our user in the database, which must have the same name as a user in ldap server. In the example below that's `ldap-user`.
We also create `mariadb-ldap` secret, which holds the name of the plugin we are using as well as the module we need to load.

**mariadb-user.yaml:**
```yaml
---
apiVersion: v1
kind: Secret
metadata:
  name: mariadb-ldap
stringData:
  plugin: pam # name of the plugin, must be `pam`
  pamModule: mariadb # This is the name of the pam config file placed in `/etc/pam.d/`
---
apiVersion: enterprise.mariadb.com/v1alpha1
kind: User
metadata:
  name: ldap-user # This user must exist already in your ldap server.
spec:
  mariaDbRef:
    name: mariadb
  host: "%" # Don't specify the ldap host here. Keep this as is
  passwordPlugin:
    pluginNameSecretKeyRef:
      name: mariadb-ldap
      key: plugin
    pluginArgSecretKeyRef:
      name: mariadb-ldap
      key: pamModule

  cleanupPolicy: Delete
  requeueInterval: 10h
  retryInterval: 30s
```
`kubectl apply -f mariadb-user.yaml`

After a few seconds, the user should have been created by the operator. To verify that all is working as expected, modify the `<password>` field below and run:

```sh
kubectl run mariadb-connect --rm -it --image=mariadb:11.4 -- bash -c "mariadb -u ldap-user -p'<secret>' --ssl=false -h mariadb"
```

You should see something along the lines of:

```
If you don't see a command prompt, try pressing enter.
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 95
Server version: 11.4.7-4-MariaDB-enterprise MariaDB Enterprise Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>
```

#### LDAPS

If you followed the instructions for setting up a basic MariaDB instance with ldap, you need to fetch the public certificate that your LDAP server
is set up with and add it to a [secret](https://kubernetes.io/docs/concepts/configuration/secret/#use-case-dotfiles-in-a-secret-volume) called `mariadb-ldap-tls`. 

If you have the certificate locally in a file called `cert.pem` you can run:

```sh
kubectl create secret generic mariadb-ldap-tls --from-file=./cert.pem
```

```diff
  volumes: # Attach `nslcd.conf`, `nsswitch.conf` and `mariadb` (pam). Also add an emptyDir volume for `nslcd` socket
    - name: nslcd
      secret:
        secretName: mariadb-nslcd-secret
        defaultMode: 0600
    - name: nsswitch
      configMap:
        name: mariadb-nsswitch-configmap
        defaultMode: 0600
    - name: mariadb-pam
      configMap:
        name: mariadb-pam-configmap
        defaultMode: 0600
    - name: nslcd-run
      emptyDir: {}
+    - name: ldap-tls
+      secret:
+        secretName: mariadb-ldap-tls
+        defaultMode: 0600

  sidecarContainers:
    # The `nslcd` daemon is ran as a sidecar container
    - name: nslcd
      image: docker.mariadb.com/nslcd:0.9.10-13
      volumeMounts:
        - name: nslcd
          mountPath: /etc/nslcd.conf
          subPath: nslcd.conf
        - name: nsswitch
          mountPath: /etc/nsswitch.conf
          subPath: nsswitch.conf
+        - name: ldap-tls
+          mountPath: /etc/openldap/certs/
      # nslcd-run is missing because volumeMounts from main container are shared with sidecar

  volumeMounts:
    - name: mariadb-pam
      mountPath: /etc/pam.d/mariadb
      subPath: mariadb
    - name: nslcd-run
      mountPath: /var/run/nslcd
```

### Known Issues

**Slow Start On KIND**

This may be a problem with the maximum number of file-handles a process can allocate. Some systems have this value set to really high, which causes an issue.
To remedy this, you need to delete your kind cluster and run:

```sh
sudo sysctl -w fs.nr_open=1048576
kind create cluster
```

At this point, the problem should be fixed.

For more information, check [this comment](https://github.com/kubernetes-sigs/kind/issues/4001#issuecomment-3279083954).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
