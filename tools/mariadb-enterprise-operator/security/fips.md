---
description: How to run MariaDB Enterprise Operator in FIPS 140-3 compliant mode.
---

# FIPS 140-3 Compliance

The MariaDB Enterprise Operator for Kubernetes can be configured to operate in a FIPS 140-3 compliant mode. This ensures that all cryptographic operations performed by the operator adhere to the strict standards required by FIPS.

## Activating FIPS Mode

To activate FIPS mode, you must set the `GODEBUG` environment variable for the operator controller. When installing via Helm, you can achieve this by setting the `extraEnv` value.

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

This will inject the required environment variable into the operator's Pod to enable FIPS-compliant mode.

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

The Operator and Prometheus exporters are written in Go. Enabling FIPS mode via `GODEBUG=fips140=on` ensures that their standard library cryptographic routines are compliant. This guarantees that the core Operator logic and metrics collection adhere to FIPS standards.

### TLS Communication

For all TLS-based communication, the operator programmatically configures the underlying HTTP clients to use only FIPS-approved cryptography. This is achieved by explicitly setting the allowed TLS `CurvePreferences` to a list of NIST-approved elliptic curves:
- `P-521`
- `P-384`
- `P-256`

This enforcement applies to communication with:
- Kubernetes API Server
- Amazon S3 compatible storage
- Azure Blob Storage
- The MariaDB Agent Sidecars

By enforcing these specific curves, the operator guarantees that all its external communication over TLS is FIPS-compliant.

### OpenSSL Configuration (Operand Containers)

The MariaDB server, MaxScale, and various system utilities running inside the operand containers rely on OpenSSL for their cryptographic operations.

To ensure end-to-end FIPS compliance within the Pod, OpenSSL must also be configured to operate in FIPS mode. **The operand containers rely on the underlying host operating system to be FIPS compliant and to provide the necessary validated OpenSSL FIPS provider modules.**

When FIPS mode is enabled for the Operator, it automatically handles configuring OpenSSL for the managed databases by dynamically injecting the FIPS provider configuration. For each `MariaDB` and `MaxScale` custom resource, the Operator will:

1. **Generate a FIPS OpenSSL ConfigMap**: Create a `<resource-name>-fips` ConfigMap containing an `openssl-fips.cnf` file that instructs OpenSSL to load the `fips` provider and sets the default property query to `fips=yes` (ensuring only FIPS-approved algorithms are returned).
2. **Mount the ConfigMap as a Volume**: Automatically mount this ConfigMap into the `StatefulSet` pod template at `/etc/ssl/fips`.
3. **Set the `OPENSSL_CONF` Environment Variable**: Inject the `OPENSSL_CONF="/etc/ssl/fips/openssl-fips.cnf"` environment variable into the MariaDB and MaxScale containers.

By dynamically creating and injecting this configuration, the Operator ensures that Enterprise Server, MaxScale, and any other relevant processes running within the managed containers will utilize OpenSSL in a strictly FIPS-compliant manner.

## Database Authentication

The MariaDB Enterprise Operator utilizes the `mysql_native_password` authentication plugin for connecting to the database. While this plugin internally uses the SHA-1 hashing algorithm, it can still be used in a FIPS 140-3 compliant environment. To pass an audit and maintain compliance, the following requirements must be met to ensure that the SHA-1 payload is always wrapped with compliant cryptography:

- **Encryption in Transit**: You must enable TLS for all database connections. The Operator configures the underlying clients to strictly use FIPS-approved cryptography (e.g., NIST-approved elliptic curves) for TLS. This ensures that the authentication exchange is securely wrapped within a compliant TLS tunnel and never exposed over the network.
- **Encryption at Rest**: You must ensure that the underlying storage platform utilizes FIPS-compliant encryption at rest.

By wrapping the `mysql_native_password` exchange with FIPS-compliant encryption both at rest and in transit, the overall system maintains strict compliance standards.

## Limitations

### AWS S3 SSE-C Encryption

Backups configured to use Server-Side Encryption with Customer-Provided Keys (SSE-C) with an S3-compatible storage provider are not supported when FIPS mode is enabled. The S3 protocol for SSE-C requires the use of the MD5 hashing algorithm for integrity checking, which is not FIPS-compliant.

## NIST CMVP Certificates

The MariaDB Enterprise Operator and its underlying components rely on cryptographic modules validated by the NIST Cryptographic Module Validation Program (CMVP):

| Cryptographic Module | Description | CMVP Reference |
| :--- | :--- | :--- |
| **Go Cryptographic Module** | The built-in cryptographic module in Go (used by the Operator). | [Certificate #5247](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/5247) |
| **OpenSSL** | The cryptography provider utilized by MariaDB Enterprise Server and MaxScale. | [Certificate #4857](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4857) |

## Further Reading

- [Go FIPS 140-3 Compliance](https://go.dev/doc/security/fips140)
- [MariaDB Server: TLS and Cryptography Libraries](https://mariadb.com/docs/server/security/encryption/tls-and-cryptography-libraries-used-by-mariadb#fips-certification)