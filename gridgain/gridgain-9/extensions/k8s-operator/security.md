---
description: >-
  Configure authentication, SSL/TLS encryption, and pod and container security
  contexts for GridGain 9 clusters managed by the Kubernetes Operator.
---

# Security

{% hint style="warning" %}
Kubernetes operator is an experimental feature. The configuration may change in a subsequent release.
{% endhint %}

The operator supports configuring authentication, SSL/TLS encryption, and Kubernetes security contexts for GridGain clusters.

## Authentication

Authentication is configured through the `clusterConfig` field. The operator supports basic and LDAP authentication types, with `basic` as the default.

Provide the authentication configuration as a JSON document in `clusterConfig.content`:

```yaml
spec:
  clusterConfig:
    content: |
      {
        "security": {
          "enabled": true,
          "authentication": {
            "providers": [
              {
                "name": "basic",
                "type": "basic",
                "users": [
                  {"username": "admin", "password": "changeme", "roles": ["system"]}
                ]
              }
            ]
          }
        }
      }
```

For further details on GridGain authentication providers and role definitions, see [Authentication](../../administrators-guide/security/authentication.md).

## SSL/TLS

SSL/TLS encryption secures communication between GridGain nodes, between clients and the cluster, and on the REST API. Configuration requires a keystore and truststore, typically stored in a Kubernetes Secret.

First, create the Secret containing your certificate files:

```bash
kubectl create secret generic gridgain-ssl-certs \
  --from-file=keystore.p12=/path/to/keystore.p12 \
  --from-file=truststore.p12=/path/to/truststore.p12
```

Then mount the Secret into pods and reference the certificates in both the cluster configuration and the node configuration.

Mount the certificates using `extraVolumes` and `extraVolumeMounts`:

```yaml
spec:
  extraVolumes:
    - name: ssl-certs
      secret:
        secretName: gridgain-ssl-certs
  extraVolumeMounts:
    - name: ssl-certs
      mountPath: /opt/gridgain/ssl
      readOnly: true
```

Enable SSL in the cluster configuration:

```yaml
spec:
  clusterConfig:
    content: |
      {
        "ssl": {
          "enabled": true,
          "keyStore": {
            "type": "PKCS12",
            "path": "/opt/gridgain/ssl/keystore.p12",
            "password": "keystorepass"
          },
          "trustStore": {
            "type": "PKCS12",
            "path": "/opt/gridgain/ssl/truststore.p12",
            "password": "truststorepass"
          },
          "clientAuth": "require"
        }
      }
```

Enable SSL on the node-level connectors in the node configuration:

```yaml
spec:
  gridgainConfig:
    content: |
      ignite {
        clientConnector {
          port=10800
          ssl {
            enabled=true
            clientAuth=require
            keyStore {
              path="/opt/gridgain/ssl/keystore.p12"
              password="keystorepass"
              type=PKCS12
            }
            trustStore {
              path="/opt/gridgain/ssl/truststore.p12"
              password="truststorepass"
              type=PKCS12
            }
          }
        }
        network {
          ssl {
            enabled=true
            keyStore {
              path="/opt/gridgain/ssl/keystore.p12"
              password="keystorepass"
              type=PKCS12
            }
            trustStore {
              path="/opt/gridgain/ssl/truststore.p12"
              password="truststorepass"
              type=PKCS12
            }
          }
        }
        rest {
          ssl {
            enabled=true
            port=10400
            keyStore {
              path="/opt/gridgain/ssl/keystore.p12"
              password="keystorepass"
              type=PKCS12
            }
            trustStore {
              path="/opt/gridgain/ssl/truststore.p12"
              password="truststorepass"
              type=PKCS12
            }
          }
        }
      }
```

For more details on GridGain SSL/TLS configuration, see [SSL/TLS documentation](../../administrators-guide/security/ssl-tls.md).

## Pod Security Context

The `securityContext` field sets the security context for the entire pod. Use it to enforce non-root execution and enable seccomp profiles:

```yaml
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1001
    fsGroup: 1001
    seccompProfile:
      type: RuntimeDefault
```

Setting `fsGroup` ensures that volumes mounted into the pod are writable by the GridGain process.

## Container Security Context

The `containerSecurityContext` field applies to the GridGain container specifically. Use it to drop capabilities and prevent privilege escalation:

```yaml
spec:
  containerSecurityContext:
    allowPrivilegeEscalation: false
    readOnlyRootFilesystem: false
    runAsNonRoot: true
    runAsUser: 1001
    capabilities:
      drop:
        - ALL
```

{% hint style="info" %}
Setting `readOnlyRootFilesystem` to `true` may prevent GridGain from writing temporary files. Leave it as `false` unless you have verified that all writable paths are covered by volume mounts.
{% endhint %}
