---
description: >-
  Authenticate MariaDB Enterprise Operator to MariaDB with TLS client
  certificates instead of passwords, as required for strict FIPS 140-3 mode.
---

# TLS client certificate authentication

The operator can authenticate to `MariaDB` using a **TLS client certificate** instead of a password. When this mode is enabled, the operator (and the components it manages) present the mounted client certificate to the server, and the server authorizes the connection based on the certificate's X.509 subject and issuer (`REQUIRE SUBJECT` / `REQUIRE ISSUER`) rather than a shared secret.

This is primarily intended for **strict FIPS 140-3 compliance** (`GODEBUG=fips140=only`), where password-based authentication plugins rely on cryptographic primitives (e.g. SHA-1) that are prohibited under strict enforcement. See the [TLS guide](tls.md) for how the operator provisions and mounts certificates.

Please refer to the [MariaDB documentation](https://mariadb.com/docs/server/security/user-account-management/user-account-management-securing/securing-connections-for-client-and-server#requiring-tls) for more details about requiring TLS for user accounts.

## Overview

When `spec.tls.clientAuth.enabled` is set to `true`:

- The operator **no longer manages a root password**: `spec.rootPasswordSecretKeyRef` must not be set, and no root password `Secret` is generated.
- The `root` user is bootstrapped with a certificate requirement (`REQUIRE SUBJECT '...' ISSUER '...'`) and an empty password.
- The operator connects to MariaDB using its certificates, instead of passwords. Passwords are read on demand from secrets.
- Internal users managed by the operator (replication, metrics, MaxScale) are provisioned to require an X.509 client certificate as well.

It is **disabled by default**, so existing `MariaDB` resources are unaffected.

Additionally, once a `MariaDB` CR is created, the value of `spec.tls.clientAuth.enabled` cannot be changed. To move an existing password-based `MariaDB` to this mode, see the [migration guide](../migrations/migrate-to-tls-client-authentication.md).

## Prerequisites

- **TLS must be enabled** (`spec.tls.enabled: true`). Client certificate authentication builds on the operator's PKI, which issues both the server and client certificates. The webhook rejects `clientAuth` when TLS is disabled, and since `clientAuth` is immutable, TLS cannot be disabled afterwards.
- A **root password must not be configured**. Setting both `spec.tls.clientAuth.enabled` and `spec.rootPasswordSecretKeyRef` is rejected by the validating webhook.

## Enabling client certificate authentication

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb
spec:
  # [...]
  tls:
    enabled: true
    clientAuth:
      enabled: true
```

Because the operator authenticates with a certificate, do **not** provide `rootPasswordSecretKeyRef`:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb
spec:
  # [...]
  # rootPasswordSecretKeyRef: <-- must be omitted when clientAuth is enabled
  tls:
    enabled: true
    clientAuth:
      enabled: true
```

A complete example provisioning a replication cluster with client certificate authentication is available in `mariadb_replication_client_tls.yaml` in the [examples catalog](../examples-catalog.md).

## TLS requirements

`spec.tls.clientAuth` exposes two `TLSRequirements` overrides:

- **`rootTLSRequirements`**: the requirement the `root` user is required to present. By default, it is
  **derived from the operator-issued client PKI**: `REQUIRE SUBJECT '/CN=<mariadb-name>-client' ISSUER '/CN=<mariadb-name>-ca'`.
- **`tlsRequirements`**: the requirement every other operator-managed user (replication, metrics, MaxScale's
  internal users, ...) is required to present. It defaults to the effective `root` requirement, so overriding
  only `rootTLSRequirements` applies to every operator-managed user.

Both accept the same shape as a `User`'s `spec.require` (`subject`, `issuer`). The operator-managed users are
passwordless, so `subject` is mandatory: `ssl`-only (any TLS connection) and `x509`-only (any certificate issued by the
trusted client CAs) requirements are rejected, as they would not bind the account to a certificate identity.

For a `MariaDB` named `mariadb`, the defaults result in `REQUIRE SUBJECT '/CN=mariadb-client' ISSUER '/CN=mariadb-ca'` for `root` and for the other users.

There is no per-component override (for example, for the replication user): `tlsRequirements` is the single setting for every operator-managed user other than `root`, so the certificate presented by the replicas must match it.

## Bring your own certificates

When you provide your own client certificate (`spec.tls.clientCertSecretRef`), your own CA (`spec.tls.clientCASecretRef`) or a cert-manager issuer (`spec.tls.clientCertIssuerRef`) whose distinguished names do not follow the default convention, override the expected requirements explicitly. Subject/Issuer must be expressed in OpenSSL one-line format:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb
spec:
  # [...]
  tls:
    enabled: true
    clientAuth:
      enabled: true
      # Override the requirement the root user must present.
      # Only 'subject'/'issuer' are supported for root, and 'subject' is mandatory: root is bootstrapped
      # by the container entrypoint, which requires a Subject to be set.
      rootTLSRequirements:
        subject: "/CN=root"
        issuer: "/CN=my-ca"
      # Override the requirement the other operator-managed users must present. 'subject' is mandatory,
      # 'ssl' and 'x509' are not supported.
      tlsRequirements:
        subject: "/CN=my-user"
        issuer: "/CN=my-ca"
```

## Behavior across components

Client certificate authentication is propagated to every operator-managed component that connects to the database:

- **Replication**: the replication user is created with `spec.tls.clientAuth.tlsRequirements` (the `root` requirement by default), and replicas connect to the primary over TLS (`CHANGE MASTER ... MASTER_SSL=1`) using the client certificate instead of a replication password. `spec.replication.replica.replPasswordSecretKeyRef` is not required.
- **Backups and restores**: logical backups, physical backups (PVC, S3, Azure and `VolumeSnapshot`), point-in-time recovery and `bootstrapFrom` all authenticate with the client certificate. No password environment variable is injected into the backup/restore `Jobs`.
- **Metrics**: the metrics exporter user is created with `spec.tls.clientAuth.tlsRequirements` (the `root` requirement by default) and the exporter connects using the client certificate; no metrics password `Secret` is generated.
- **MaxScale**: the internal MaxScale users (`client`, `server`, `monitor`, and the config sync user) are created with a certificate requirement, and MaxScale presents the client certificate to the backend.

### MaxScale

When a `MaxScale` references a `MariaDB` that uses client certificate authentication, **MaxScale TLS must be enabled** (`spec.tls.enabled: true`). The operator will refuse to reconcile the `MaxScale` otherwise, since MaxScale needs to present a client certificate to connect to the backend.

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MaxScale
metadata:
  name: maxscale
spec:
  # [...]
  mariaDbRef:
    name: mariadb
  tls:
    enabled: true
    verifyPeerCertificate: true
```

`spec.tls.verifyPeerCertificate` defaults to `true` for the connection to the MariaDB servers when it is not set, so MaxScale validates the MariaDB server certificates. Set it explicitly to override. On the MaxScale listeners it only applies when set explicitly, and then requires every client connecting through MaxScale to present a certificate.

When the `MariaDB` uses replication, `spec.tls.replicationSSLEnabled` defaults to `true` and must not be set to `false`: MaxScale re-points the replicas after a failover using the client certificate, and the operator refuses to reconcile the `MaxScale` otherwise.

{% hint style="info" %}
MaxScale's configuration synchronization (`config_sync`) requires **MaxScale 25.10.4 or later** to authenticate with a client certificate, so older versions are not supported with client certificate authentication: earlier versions reject an empty `config_sync_password` ([MXS-6703](https://jira.mariadb.org/browse/MXS-6703)) and drop it on sync ([MXS-6704](https://jira.mariadb.org/browse/MXS-6704)).
{% endhint %}

### Galera

When a `MariaDB` uses [Galera](../topologies/galera.md) together with client certificate authentication:

- `spec.tls.galeraSSTEnabled` must be set to `true` explicitly, as it defaults to `false`. This makes the SST stream encrypted and present the client certificate. The validating webhook rejects the `MariaDB` otherwise.
- The SST authenticates as `root` without a password (`wsrep_sst_auth="root:"`).
- The `mysqldump` SST (`spec.galera.sst: mysqldump`) is not supported, as it authenticates with a password. Use `mariabackup`, which is the default.

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-galera
spec:
  # [...]
  galera:
    enabled: true
    sst: mariabackup
  tls:
    enabled: true
    galeraSSTEnabled: true
    clientAuth:
      enabled: true
```

A complete example is available as `mariadb_galera_client_tls.yaml` in the [examples catalog](../examples-catalog.md).

## Per-User client certificates

Independently of `spec.tls.clientAuth` (which governs how the *operator itself* connects), a `User` resource can have the operator issue it a dedicated TLS client certificate via `spec.clientCertificate.enabled`:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: User
metadata:
  name: user
spec:
  # [...]
  mariaDbRef:
    name: mariadb
  clientCertificate:
    enabled: true
  # Set 'require' to actually enforce certificate authentication for this user; the certificate is issued
  # either way, but without 'require' the user could still connect with a password.
  require:
    subject: "/CN=user-client"
```

- The certificate is signed by the **same CA** the referenced `MariaDB` uses for its own client certificate (operator-managed CA, bring-your-own CA, or cert-manager via `spec.tls.clientCertIssuerRef`), and stored in a `Secret` named `<user-name>-client-cert` in the `User`'s namespace.
- It requires the referenced `MariaDB` to have `spec.tls.enabled: true`; `spec.tls.clientAuth` does not need to be enabled.
- The `User` may live in a different namespace than the `MariaDB` it references (via `spec.mariaDbRef.namespace`). When the referenced `MariaDB` uses a cert-manager `Issuer` (not `ClusterIssuer`) for its client certificate, cross-namespace issuance is not possible — cert-manager `Issuer`s are namespace-scoped, so the `MariaDB` and `User` must share a namespace in that case, or a `ClusterIssuer` must be used.
- Issuing the certificate does not by itself enforce certificate authentication for the `User` — set `spec.require` to require it (see [TLS requirements](#tls-requirements) for the convention the operator's own certificates follow).

## FIPS 140-3

Under strict FIPS enforcement (`GODEBUG=fips140=only`), password-based authentication plugins cannot be used because the initial MariaDB protocol handshake eagerly evaluates SHA-1, which is prohibited. Client certificate authentication sidesteps password hashing entirely, making it the recommended authentication mode for strict FIPS deployments. See [FIPS 140-3 mode](fips.md) for how to enable strict mode.

## Limitations

- **Immutable**: `spec.tls.clientAuth` cannot be changed after the `MariaDB` is created. To enable client certificate authentication on an existing password-based `MariaDB`, migrate its data to a new instance following the [migration guide](../migrations/migrate-to-tls-client-authentication.md).
- **`ExternalMariaDB`**: client certificate authentication is not supported for `ExternalMariaDB` resources.
- **[Multi-cluster](../topologies/multi-cluster.md)**: client certificate authentication is not supported with multi-cluster, as cross-cluster replication authenticates against the remote `ExternalMariaDB` with a password.
- **MaxScale version**: client certificate authentication requires MaxScale 25.10.4 or later, as noted above. Older versions are not supported.
- **Galera SST**: `spec.tls.galeraSSTEnabled` must be set to `true` and the `mysqldump` SST is not supported, as described [above](#galera).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
