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

If you have deployed the operator on OpenShift via OperatorHub, you need to edit the `Subscription` for the MariaDB Enterprise Operator to inject the environment variable. After deploying the operator, edit the subscription and add the `config` section to the spec:

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

When FIPS mode is enabled, the Go runtime enforces strict rules on the cryptographic algorithms that can be used. The MariaDB Operator ensures that all its communications are FIPS-compliant.

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
- Health check probes

By enforcing these specific curves, the operator guarantees that all its external communication over TLS is FIPS-compliant.

## Limitations

### AWS S3 SSE-C Encryption

Backups configured to use Server-Side Encryption with Customer-Provided Keys (SSE-C) with an S3-compatible storage provider are not supported when FIPS mode is enabled. The S3 protocol for SSE-C requires the use of the MD5 hashing algorithm for integrity checking, which is not FIPS-compliant.

## Further Reading

- [Go FIPS 140-3 Compliance](https://go.dev/doc/security/fips140)