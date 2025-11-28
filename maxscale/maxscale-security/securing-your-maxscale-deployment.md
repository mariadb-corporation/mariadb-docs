# Securing Your MaxScale Deployment

## Securing Your MaxScale Deployment

The following hardening steps are recommended before going into production:

* Encrypt plaintext passwords
* Secure GUI & Admin Interface Connections
* Change Admin User & Password
* Enable Audit Logging
* Encrypt Incoming Database Connections
* Encrypt Outgoing Database Connections

### Encrypt Plaintext Passwords

MaxScale configuration includes credentials MaxScale uses to e.g. monitor
database servers. By default, the passwords are written in plaintext in the
configuration file, which exposes them to being accidentally shared. Reduce this
risk by encrypting the passwords. Generate an encryption key with the
*maxkeys*-command and then convert plaintext passwords to encrypted form with
the *maxpasswd*-command.

Run `maxkeys` to generate a key file in `/var/lib/maxscale`. File ownership is
given to the *maxscale* user and only the owner has read-permissions to the
file.

```
$ maxkeys
```
Once generated, the key file can be relocated to a secure location. This key
file serves a dual purpose: it enables the encryption of passwords and
decrypting those encrypted passwords. Typically, the MaxScale administrator
encrypts passwords and MaxScale itself decrypts them when required.

The key file must remain secure to maintain the security of the encrypted
passwords. If an attacker can read the contents of the key file, they can also
decrypt any passwords read from the configuration file. Use *chown* and *chmod*
to restrict access.

Encrypt plaintext passwords used in MaxScale configuration with `maxpasswd`.
```
$ maxpasswd plaintextpassword
96F99AA1315BDC3604B006F427DD9484
```
Replace the plaintext passwords in your MaxScale configuration (CNF) files with
the encrypted versions. This enhances overall security by reducing the risk that
passwords are accidentally shared.
```
[MariaDB-Service]
type=service
router=readwritesplit
servers=MariaDB1,MariaDB2,MariaDB3
user=maxscale-user
password=96F99AA1315BDC3604B006F427DD9484
```

See [encrypting-passwords](../maxscale-management/deployment/maxscale-configuration-guide.md#encrypting-passwords)
for more information regarding password encryption.

### Secure GUI & Admin Interface Connections

MaxScale is managed during runtime through the REST-API admin interface. This
interface is used by the GUI and the *MaxCtrl* utility. It can even be accessed
using *curl*. By default, the admin interface only accepts local connections. If
you need to allow external access, modify the `admin_host` setting to change the
network the admin interface listens on. To mitigate the security risk of
external access, you can change the listening port to a non-default value.

```
[maxscale]
admin_host=10.0.0.3
admin_port=2222
```

If you need to allow external access, ensure that the network is adequately
secured and that only authorized users can access the MaxScale interface.
Consult with your network administrator to determine the most appropriate and
secure configuration.

#### Enable TLS Encryption

To properly secure the MaxScale REST-API, enable TLS encryption for data in
transit. Follow these steps to configure SSL:

**1. Generate SSL key and certificate:**

* See [Certificate Creation with OpenSSL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-in-transit-encryption/certificate-creation-with-openssl.md)
  for information on certificate creation.
* Move the generated files to a secure location MaxScale can access.

**2. Update MaxScale configuration:**

* Enable secure connections by setting `admin_secure_gui` to `true`.
* Specify the paths to the SSL certificate and key files in your CNF file:
```
[maxscale]
admin_secure_gui=true
admin_ssl_key=/certs/maxscale-key.pem
admin_ssl_cert=/certs/maxscale-cert.pem
admin_ssl_ca_cert=/certs/ca-cert.pem
```

**3. Verify Encryption:**

* Use `maxctrl` to verify that TLS encryption is functioning correctly:
```
$ maxctrl --user=my_user --password=my_password --secure --tls-ca-cert=/certs/ca-cert.pem --tls-verify-server-cert=false show maxscale
```

### Change Admin User & Password

The REST-API is initially configured to be accessed with username `admin` and
password `mariadb`. Any attacker would try these credentials first, so create a
new user account and delete the default one.

To create or delete REST-API users, use the `maxctrl`-command. To create a user
with administrative privileges, run:
```
$ maxctrl create user my_user my_password --type=admin
```
The password must be in cleartext.

To remove an existing user, such as the default admin user, use the following
command:
```
$ maxctrl destroy user admin
```
After these commands, MaxCtrl will no longer work unless you define credentials
either on the command line or in a config file.
See [MaxCtrl documentation](../reference/maxscale-maxctrl.md) for more
information.

REST-API user accounts have one of two roles: *admin* and *basic*. *admin*
allows full read and write access, *basic* only allows reading.

REST-API user accounts can also be managed through the GUI.

### Enable Audit Logging

Admin auditing in MaxScale provides comprehensive tracking of all administrative
activities, including logins, connections, and modifications. These activities
are recorded in an audit file for enhanced security and traceability.

To enable admin auditing, add the following configuration to your MaxScale
configuration file:

```
[maxscale]
admin_audit = true
admin_audit_file = /var/log/maxscale/audit_files/audit.csv
```

This configuration activates auditing and specifies the location of the audit
file. Ensure that the specified directory exists before restarting MaxScale.

Implement log rotation to manage the size and number of audit files. This can be
achieved using standard Linux log rotation tools. See
[Rotating Logs on Unix and Linux](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/rotating-logs-on-unix-and-linux.md)

For manual log rotation, use the following MaxCtrl command:
```
$ maxctrl rotate logs
```

### Encrypt Incoming Database Connections

Incoming database connections are the connections clients make to
MaxScale. Without encryption, an eavesdropper can listen to the client queries
and server responses. To enable encryption, MaxScale listeners need to be
configured for TLS.

#### 1. Enable TLS:

Add `ssl=true` to the listener section in your MaxScale configuration file. This
enforces encrypted connections from incoming clients.  The listener also
requires a certificate and its private key, configured with settings `ssl_cert`
and `ssl_key`.  If using a X509v3 certificate with extendedKeyUsage extension
settings, the *serverAuth* flag should be set in the certificate.

The listener section should look like:
```
[RWS-Listener]
type=listener
service=RWS-Service
ssl=true
ssl_key=/certs/my-cert-key.pem
ssl_cert=/certs/my-cert.pem
```

In MaxScale 25.10, the `ssl_cert` and `ssl_key` settings can be omitted, which
causes MaxScale to generate a self-signed certificate during startup. Recent
client versions (11.4 and later) can even verify this auto-generated
certificate.

For more information on SSL settings, see
[here](../maxscale-management/deployment/maxscale-configuration-guide.md#settings-for-tlsssl-encryption)

#### 2. Verify client certificates

If you want MaxScale to verify client certificates against a CA-certificate, set
`ssl_verify_peer_certificate=true` and define the CA-certificate with `ssl_ca`.
```
[RWS-Listener]
type=listener
service=RWS-Service
ssl=true
ssl_key=/certs/my-cert-key.pem
ssl_cert=/certs/my-cert.pem
ssl_ca=/certs/my_ca_cert.pem
```

### Encrypt Outgoing Database Connections

Outgoing database connections are the connections MaxScale makes to MariaDB
Servers on behalf of incoming clients. If MaxScale and the servers are running
in the same network, and you consider the network already secure, then
encrypting these connections may not be necessary. If this is not the case, both
MaxScale and the servers need to be configured to use TLS.  To configure MariaDB
Server for encryption, see
[Secure Connections Overview](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-in-transit-encryption/secure-connections-overview.md).

To enable MaxScale to connect securely to MariaDB Servers:

#### 1. Enable TLS:

Add `ssl=true` to each server section in your MaxScale configuration file. This
enforces encrypted connections to the server.

#### 2. Verify server certificate:

If you want MaxScale to verify the server certificate (to ensure it's signed by
a trusted CA), add `ssl_verify_peer_certificate=true`.  The CA certificate path
is defined with `ssl_ca`. This prevents MaxScale from routing queries to a
malicious server that has hijacked the address of the real server.

The server section in your MaxScale configuration file should look like:

```
[MariaDB-Server1]
type=server
address=...
port=...
ssl=true
ssl_verify_peer_certificate=true
ssl_ca=/certs/my_ca_cert.pem
```

If you are using MaxScale 25.10 and a recent MariaDB Server version, certificate
verification no longer requires a ca-certificate. In this case, the `ssl_ca`
setting can be omitted. See [here](https://mariadb.org/mission-impossible-zero-configuration-ssl/)
for more information.

#### 3. Configure a pre-generated certificate for connecting to the server

If the MariaDB Server requires clients (such as MaxScale) to connect with a
verified certificate, then such a certificate must be defined in the MaxScale
configuration, with settings `ssl_cert` and `ssl_key`. If using a X509v3
certificate with extendedKeyUsage extension settings, the *clientAuth* flag
should be set in the certificate.

```
[MariaDB-Server1]
type=server
address=...
port=...
ssl=true
ssl_verify_peer_certificate=true
ssl_key=/certs/my-cert-key.pem
ssl_cert=/certs/my-cert.pem
ssl_ca=/certs/my_ca_cert.pem
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
