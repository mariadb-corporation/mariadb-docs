---
description: >-
  Set up a private certificate authority for one MariaDB Raft Cluster: node
  certificates, revocation lists, certificate replacement, and CA rotation
---

# A CA for One Raft Cluster

This page sets up a private certificate authority (CA) for one Raft cluster. It covers node certificates, revocation, and rotation. The commands use OpenSSL 3.

{% hint style="warning" %}
This is an example setup only. The plain `openssl ca` commands show what the cluster needs. They are not a production procedure. In production, use a private PKI that your organization approves and operates. Such a PKI keeps CA keys in an HSM or offline, controls and audits issuance, and publishes revocation lists. The requirements on this page apply to it too: a trust anchor for each cluster, the extended key usages, and current revocation lists.
{% endhint %}

## A Trust Anchor for Each Cluster

Under `raft_tls_mode=VERIFY_CA`, a node accepts a peer when the peer certificate chains to a CA certificate in `raft_ssl_ca`. The node does not check a host name or a subject. Thus each certificate that chains to the trust anchor, and has the necessary extended key usage, is accepted as a node of the cluster.

The trust anchor must be a self-signed root CA. A node does not accept a chain that ends at an intermediate CA in `raft_ssl_ca`.

Use a root CA that signs only the node certificates of this cluster:

* **A new key pair.** The key identifies the CA, not the name. Do not use the key of a CA again, for another cluster or for a new CA of the same cluster.
* **A unique subject.** A node finds the issuer of a certificate, and the revocation list of the issuer, by the subject name. Two CAs with the same subject break these lookups. Put the cluster name and a CA generation in the subject, for example `/O=Example/OU=MariaDB Raft/CN=cluster1 CA 1`. If cluster names can be the same in different environments, add the environment name.
* **No other use.** Do not use the CA for other clusters, for SQL clients, for the server certificate of SQL connections, or for state transfer data.
* **The key off the nodes.** Keep the CA key on a host that is not a node, or in an HSM. Keep it offline when you do not issue certificates or revocation lists.

### Organization Root CAs

Do not use the root CA of your organization as the trust anchor of a cluster. Also do not use a root CA that more than one cluster shares.

An issuing CA for each cluster under a shared root does not isolate the clusters. `raft_ssl_ca` must contain the shared root. Then a node accepts each certificate under that root that has `serverAuth` or `clientAuth`: the nodes of other clusters, and often other hosts of the organization.

If your organization operates the PKI, ask for a separate root CA for each cluster.

## Create the CA

On the CA host, make a directory for the CA:

```bash
mkdir -p /etc/mysql/raft-ca && cd /etc/mysql/raft-ca
mkdir -p private newcerts && chmod 700 private
touch index.txt && echo 1000 > serial && echo 1000 > crlnumber
```

Write `ca.cnf`:

```ini
[ ca ]
default_ca       = raft_ca

[ raft_ca ]
dir              = .
database         = $dir/index.txt
new_certs_dir    = $dir/newcerts
serial           = $dir/serial
crlnumber        = $dir/crlnumber
certificate      = $dir/ca.crt
private_key      = $dir/private/ca.key
default_md       = sha256
default_days     = 1095
default_crl_days = 180
policy           = policy_node
unique_subject   = no

[ policy_node ]
organizationName = optional
commonName       = supplied

[ req ]
distinguished_name = req_dn

[ req_dn ]

[ v3_ca ]
basicConstraints       = critical, CA:true
keyUsage               = critical, keyCertSign, cRLSign
subjectKeyIdentifier   = hash

[ v3_node ]
basicConstraints       = critical, CA:false
keyUsage               = critical, digitalSignature, keyEncipherment
extendedKeyUsage       = serverAuth, clientAuth
subjectKeyIdentifier   = hash
authorityKeyIdentifier = keyid

[ v3_server ]
basicConstraints       = critical, CA:false
keyUsage               = critical, digitalSignature, keyEncipherment
extendedKeyUsage       = serverAuth
subjectKeyIdentifier   = hash
authorityKeyIdentifier = keyid

[ v3_client ]
basicConstraints       = critical, CA:false
keyUsage               = critical, digitalSignature, keyEncipherment
extendedKeyUsage       = clientAuth
subjectKeyIdentifier   = hash
authorityKeyIdentifier = keyid
```

The policy keeps only `O` and `CN` in a node certificate subject. Add other fields to `policy_node` if you use them.

Create the CA certificate and key. Give each CA a subject of its own. A new CA for a rotation needs a different subject, see [Rotate the CA](#rotate-the-ca).

```bash
openssl req -x509 -new -config ca.cnf -extensions v3_ca \
  -newkey rsa:3072 -noenc -keyout private/ca.key -out ca.crt \
  -days 7300 -subj "/O=Example/OU=MariaDB Raft/CN=cluster1 CA 1"
```

### Lifetimes

The example values are:

| Item             | Lifetime | Set by                   |
| ---------------- | -------- | ------------------------ |
| CA certificate   | 20 years | `-days 7300`             |
| Node certificate | 3 years  | `default_days = 1095`    |
| Revocation list  | 180 days | `default_crl_days = 180` |

Use the values of your organization policy. Keep these rules:

* **The CA outlives the node certificates.** When the CA expires, each node certificate that it signed fails validation, and the cluster stops. `openssl ca` issues a certificate that expires after the CA. Rotate the CA at least one node certificate lifetime before it expires.
* **A longer node certificate lifetime needs revocation.** A stolen key is valid until you revoke the certificate or it expires. Without revocation lists, use a shorter lifetime.
* **An expired revocation list stops the cluster.** New connections fail, a node does not start, and `FLUSH SSL` fails. A revocation takes effect when you put a new list in force, not when the old list expires. Thus a long list lifetime does not delay a revocation. Renew the list at half of its lifetime, see [Renew the Revocation List](#renew-the-revocation-list).

Create the first revocation list. It is empty:

```bash
openssl ca -config ca.cnf -gencrl -out ca.crl
```

Configure a revocation list from the start. `raft_ssl_crl` is read-only, so adding it later needs a restart of each node.

## Issue a Node Certificate

Do these steps for each node. The example is for `node1`:

```bash
openssl req -new -config ca.cnf -newkey rsa:3072 -noenc \
  -keyout node1.key -out node1.csr -subj "/O=Example/CN=node1"
openssl ca -batch -config ca.cnf -extensions v3_node -notext \
  -in node1.csr -out node1.crt
```

The `v3_node` certificate has `serverAuth` and `clientAuth`. The node uses it for the connections it accepts and for the connections it initiates.

If your policy gives one TLS role to each certificate, issue the node certificate with `-extensions v3_server` instead. Then issue a `clientAuth` certificate for the connections that the node initiates:

```bash
openssl req -new -config ca.cnf -newkey rsa:3072 -noenc \
  -keyout node1-client.key -out node1-client.csr \
  -subj "/O=Example/CN=node1 client"
openssl ca -batch -config ca.cnf -extensions v3_client -notext \
  -in node1-client.csr -out node1-client.crt
```

Check the certificates:

```bash
openssl verify -CAfile ca.crt -CRLfile ca.crl -crl_check_all \
  -purpose sslserver node1.crt
openssl verify -CAfile ca.crt -CRLfile ca.crl -crl_check_all \
  -purpose sslclient node1.crt node1-client.crt
```

## Install the Files on a Node

Copy `ca.crt`, `ca.crl`, and the certificate and key of the node to the node. Only the account that runs the server must have access to a key file. The node does not start if all accounts can write a key file. It logs a warning if the group or other accounts have any access.

```bash
install -d -m 750 -o mysql -g mysql /etc/mysql/raft
install -m 644 -o mysql -g mysql ca.crt ca.crl node1.crt /etc/mysql/raft/
install -m 600 -o mysql -g mysql node1.key /etc/mysql/raft/
```

Add to the server configuration of the node:

```ini
[mariadb]
raft_tls_mode = VERIFY_CA
raft_ssl_ca   = /etc/mysql/raft/ca.crt
raft_ssl_crl  = /etc/mysql/raft/ca.crl
raft_ssl_cert = /etc/mysql/raft/node1.crt
raft_ssl_key  = /etc/mysql/raft/node1.key
```

For a separate client certificate, add:

```ini
raft_ssl_client_cert = /etc/mysql/raft/node1-client.crt
raft_ssl_client_key  = /etc/mysql/raft/node1-client.key
```

At startup, the node validates its own certificates against the CA and the revocation list. If a check fails, the node does not start, and the error log gives the reason. See [TLS Configuration Checks](mariadb-advanced-cluster-quickstart-guide.md#tls-configuration-checks).

To see the TLS in force, and when each peer certificate expires:

```sql
SELECT remote_address, tls_mode, certificate_verification,
       certificate_subject, certificate_not_after
FROM INFORMATION_SCHEMA.WSREP_CONNECTIONS
WHERE connection_scheme = 'ssl';
```

This query shows only the connections that the local plugin opens. See [Monitoring Cluster Connections](mariadb-advanced-cluster-quickstart-guide.md#monitoring-cluster-connections).

## Put Files in Force: FLUSH SSL

A node reads its TLS files when it builds a TLS context. After you replace a file, run `FLUSH SSL` on each node that has the new file:

```sql
FLUSH SSL;
```

Keep the same paths. The paths are read-only.

`FLUSH SSL` applies to the connections that start after it. Established connections continue with the old material.

If the new files fail the checks, `FLUSH SSL` fails and the node keeps the old material. Correct the files and run it again.

On a node that is not ready, for example a node without quorum, set `wsrep_dirty_reads=ON` in the session before `FLUSH SSL`.

See [Reloading TLS Material](mariadb-advanced-cluster-quickstart-guide.md#reloading-tls-material).

## Renew the Revocation List

A revocation list has a `Next Update` time. With `default_crl_days = 180`, this time is 180 days after you create the list. After this time, the list is expired. Then each new connection fails validation, a node does not start, and `FLUSH SSL` fails.

Create a new list at half of its lifetime, and put it in force on each node:

```bash
openssl ca -config ca.cnf -gencrl -out ca.crl
openssl crl -in ca.crl -noout -nextupdate
```

Copy `ca.crl` to each node, then run `FLUSH SSL` on each node.

`INFORMATION_SCHEMA.WSREP_CONNECTIONS` does not show the revocation list. Monitor the `Next Update` time of the list on each node, and the expiry of the CA certificate:

```bash
openssl crl -in /etc/mysql/raft/ca.crl -noout -nextupdate
openssl x509 -in /etc/mysql/raft/ca.crt -noout -enddate
```

## Revoke a Node Certificate

On the CA host, revoke the certificate and create a new list:

```bash
openssl ca -config ca.cnf -revoke node2.crt
openssl ca -config ca.cnf -gencrl -out ca.crl
```

If the node has a separate client certificate, revoke it too.

Copy `ca.crl` to each node, then run `FLUSH SSL` on each node.

Established connections of the revoked node are not closed. The other nodes refuse the revoked node when it connects again, for example after a restart or a network failure. To remove the node at once, stop it.

## Replace a Node Certificate

Replace a certificate before it expires, or when its key is compromised:

1. Issue a new certificate and key, as in [Issue a Node Certificate](#issue-a-node-certificate).
2. On the node, write the new files over the old files. Keep the paths and the permissions.
3. Run `FLUSH SSL` on the node.

If the key is compromised, also revoke the old certificate.

## Rotate the CA

To replace the CA, trust both CAs for a period:

1. Create a new CA in a new directory, as in [Create the CA](#create-the-ca). Give it a new key and a different subject, for example `"/O=Example/OU=MariaDB Raft/CN=cluster1 CA 2"`. Create its empty revocation list.
2. Put both CA certificates in one file for `raft_ssl_ca`, and both revocation lists in one file for `raft_ssl_crl`. On the CA host, in `/etc/mysql`:

   ```bash
   cat raft-ca/ca.crt raft-ca-2/ca.crt > ca.crt
   cat raft-ca/ca.crl raft-ca-2/ca.crl > ca.crl
   ```

   Copy the two files to each node, then run `FLUSH SSL` on each node. Each CA needs a current list, because revocation is checked for each certificate in the chain.
3. Issue a new certificate for each node from the new CA. Include the separate client certificate, if the node has one. On each node, replace the files and run `FLUSH SSL`.
4. When each node has a certificate from the new CA, put only the new CA in the `raft_ssl_ca` file and only its list in the `raft_ssl_crl` file. Then run `FLUSH SSL` on each node.

In step 4, `FLUSH SSL` fails on a node that still has a certificate from the old CA. The node keeps the old material. Replace the certificate, then run `FLUSH SSL` again.

Renew the list of each CA during the period, as in [Renew the Revocation List](#renew-the-revocation-list).

If you use `raft_ssl_capath` and `raft_ssl_crlpath` instead of files, put the certificates and lists of both CAs in the directories, and run `openssl rehash` on each directory.

## State Transfer and SQL Connections

The cluster CA applies to the cluster connections and to the state transfer request. It does not apply to the state transfer data or to SQL connections. See [State Transfer and SQL Connections](mariadb-advanced-cluster-quickstart-guide.md#state-transfer-and-sql-connections).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
