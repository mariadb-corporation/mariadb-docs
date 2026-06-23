---
description: How to run MariaDB Enterprise Operator in FIPS 140-3 mode.
---

# FIPS 140-3 Mode

The MariaDB Enterprise Operator for Kubernetes can be configured to operate in FIPS 140-3 mode. When enabled, the operator uses NIST-approved cryptographic modules for its operations and configures managed components to use NIST-approved algorithms.

## Activating FIPS Mode

To activate FIPS mode, you must set the `GODEBUG` environment variable for the operator. When installing via Helm, you can achieve this by setting the `extraEnv` value.

Create a `values.yaml` file with the following content:

```yaml
extraEnv:
  - name: GODEBUG
    value: "fips140=on"
```

Then, install the operator using this values file:

```sh
helm install mariadb-enterprise-operator mariadb-enterprise-operator/mariadb-enterprise-operator \
  -f values.yaml
```

This will inject the required environment variable into the operator's Pod to enable FIPS mode.

### OpenShift

If you have deployed the operator on OpenShift, you need to edit the `Subscription` for the MariaDB Enterprise Operator to inject the environment variable. After deploying the operator, edit the subscription and add the `config` section to the spec:

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: mariadb-enterprise-operator
  namespace: openshift-operators
spec:
  # [...]
  config:
    env:
      - name: GODEBUG
        value: fips140=on
  # [...]
```

## Implications of FIPS Mode

When FIPS mode is enabled, strict rules are enforced on the cryptographic algorithms that can be used across the Operator and the managed resources.

### Go Cryptography (Operator & Exporters)

The Operator and Prometheus exporters are written in Go. Enabling FIPS mode via `GODEBUG=fips140=on` directs them to use the [Go Cryptographic Module](#nist-cmvp-certificates), a NIST-approved cryptographic module.

### TLS Communication

For all TLS-based communication, the operator programmatically configures the underlying clients to use only NIST-approved cryptography. This is achieved by explicitly setting the allowed TLS `CurvePreferences` to a list of NIST-approved elliptic curves:
- `P-521`
- `P-384`
- `P-256`

This enforcement applies to communication with:
- Kubernetes API Server
- Amazon S3 compatible storage
- Azure Blob Storage
- MariaDB server
- MariaDB Agent Sidecars
- MaxScale API server

By enforcing these specific curves, the operator configures all its external TLS communication to use NIST-approved elliptic curves.

### OpenSSL Configuration (Operand Containers)

The MariaDB server, MaxScale, and various system utilities running inside the operand containers rely on a [OpenSSL FIPS provider](#nist-cmvp-certificates) for their cryptographic operations. This provider is configured when FIPS mode is enabled. 

When FIPS mode is enabled, the Operator automatically handles configuring OpenSSL for the managed databases by dynamically injecting the FIPS provider configuration. For each `MariaDB` and `MaxScale` custom resource, the Operator will:

1. **Generate a FIPS OpenSSL ConfigMap**: Create a `<resource-name>-fips` ConfigMap containing an `openssl-fips.cnf` file that instructs OpenSSL to load the `fips` provider and sets the default property query to `fips=yes` (ensuring only NIST-approved algorithms are returned).
2. **Mount the ConfigMap as a Volume**: Automatically mount this ConfigMap into the `StatefulSet` pod template at `/etc/ssl/fips`.
3. **Set the `OPENSSL_CONF` Environment Variable**: Inject the `OPENSSL_CONF="/etc/ssl/fips/openssl-fips.cnf"` environment variable into the MariaDB and MaxScale containers.

By dynamically creating and injecting this configuration, the Operator configures Enterprise Server, MaxScale, and other relevant processes in the managed containers to use OpenSSL in FIPS mode.

## Database Authentication

The MariaDB Enterprise Operator utilizes the `mysql_native_password` authentication plugin for connecting to the database. While this plugin internally uses the SHA-1 hashing algorithm, the SHA-1 payload can be wrapped with NIST-approved cryptography:

- **Encryption in Transit**: Enable TLS for all database connections. The Operator configures the underlying clients to use NIST-approved cryptography (e.g., NIST-approved elliptic curves) for TLS, so the authentication exchange is wrapped within a TLS tunnel.
- **Encryption at Rest**: By configuring encryption at rest with an approved elliptic curve, passwords will be stored using NIST-approved cryptography.

## Limitations

#### AWS S3 SSE-C Encryption

Backups configured to use [Server-Side Encryption with Customer-Provided Keys (SSE-C)](../../backup-and-restore/physical_backup.md#server-side-encryption-with-customer-provided-keys-sse-c-for-s3) with an S3-compatible storage provider are not supported when FIPS mode is enabled. The S3 protocol for SSE-C requires the use of the MD5 hashing algorithm for integrity checking, which is not approved for FIPS.

## NIST CMVP Certificates

The MariaDB Enterprise Operator and its underlying components rely on cryptographic modules validated by the NIST Cryptographic Module Validation Program (CMVP):

| Cryptographic Module | Description | CMVP Reference |
| :--- | :--- | :--- |
| **Go Cryptographic Module** | The built-in cryptographic module in Go (used by the Operator). | [Certificate #5247](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/5247) |
| **OpenSSL FIPS provider** | The cryptography provider utilized by MariaDB Enterprise Server and MaxScale. | [Certificate #4857](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4857) |

## Further Reading

- [Go FIPS 140-3](https://go.dev/doc/security/fips140)
- [MariaDB Server: TLS and Cryptography Libraries](https://mariadb.com/docs/server/security/encryption/tls-and-cryptography-libraries-used-by-mariadb#fips-certification)