# TLS

MariaDB Enterprise Kubernetes Operator supports issuing, configuring and rotating TLS certificates for both your `MariaDB` and `MaxScale` resources. It aims to be secure by default; for this reason, TLS certificates are issued and configured by the operator as a default behaviour.

## `MariaDB` configuration

{% hint style="info" %}
This section covers TLS configuration in new instances. If you are looking to migrate an existing instance to use TLS, please refer to [Enabling TLS in existing instances](migrations/enabling-tls-in-existing-instances.md) instead.
{% endhint %}

TLS can be configured in `MariaDB` resources by setting `tls.enabled=true`:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-galera
spec:
  ...
  tls:
    enabled: true
```

As a result, the operator will generate a Certificate Authority (CA) and use it to issue the leaf certificates mounted by the instance. It is important to note that the TLS connections are not enforced in this case i.e. both TLS and non-TLS connections will be accepted. This is the default behaviour when no `tls` field is specified.

If you want to enforce TLS connections, you can set `tls.required=true`:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-galera
spec:
  ...
  tls:
    enabled: true
    required: true
```

This approach ensures that any unencrypted connection will fail, effectively enforcing security best practices.

If you want to fully opt-out from TLS, you can set `tls.enabled=false`:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-galera
spec:
  ...
  tls:
    enabled: false
```

This will disable certificate issuance, resulting in all connections being unencrypted.

Refer to further sections for a more advanced TLS configuration.

## `MaxScale` configuration

{% hint style="info" %}
This section covers TLS configuration in new instances. If you are looking to migrate an existing instance to use TLS, please refer to [Enabling TLS in existing instances](migrations/enabling-tls-in-existing-instances.md) instead.
{% endhint %}

TLS will be automatically enabled in `MaxScale` when the referred `MariaDB` (via `mariaDbRef`) has TLS enabled and enforced. Alternatively, you can explicitly enable TLS by setting `tls.enabled=true`:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MaxScale
metadata:
  name: maxscale-galera
spec:
  ...
  mariaDbRef:
    name: mariadb-galera
  tls:
    enabled: true
```

As a result, the operator will generate a Certificate Authority (CA) and use it to issue the leaf certificates mounted by the instance. It is important to note that, unlike `MariaDB`, `MaxScale` does not support TLS and non-TLS connections simultaneously (see [limitations](tls.md#limitations)). Therefore, TLS connections will be enforced in this case i.e. unencrypted connections will fail, ensuring security best practises.

If you want to fully opt-out from TLS, you can set `tls.enabled=false`. This should only be done when `MariaDB` TLS is not enforced or disabled:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MaxScale
metadata:
  name: maxscale-galera
spec:
  ...
  mariaDbRef:
    name: mariadb-galera
  tls:
    enabled: false
```

This will disable certificate issuance, resulting in all connections being unencrypted.

Refer to further sections for a more advanced TLS configuration.

## `MariaDB` certificate specification

The `MariaDB` TLS setup consists of the following certificates:

* Certificate Authority (CA) keypair to issue the server certificate.
* Server leaf certificate used to encrypt server connections.
* Certificate Authority (CA) keypair to issue the client certificate.
* Client leaf certificate used to encrypt and authenticate client connections.

As a default behaviour, the operator generates a single CA to be used for issuing both the server and client certificates, but the user can decide to use dedicated CAs for each case. Root CAs, and [intermedicate CAs](tls.md#intermediate-cas) in some cases, are supported, see [limitations](tls.md#limitations) for further detail.

The server certificate contains the following Subject Alternative Names (SANs):

* `<mariadb-name>.<namespace>.svc.<cluster-name>`
* `<mariadb-name>.<namespace>.svc`
* `<mariadb-name>.<namespace>`
* `<mariadb-name>`
* `*.<mariadb-name>-internal.<namespace>.svc.<cluster-name>`
* `*.<mariadb-name>-internal.<namespace>.svc`
* `*.<mariadb-name>-internal.<namespace>`
* `*.<mariadb-name>-internal`
* `<mariadb-name>-primary.<namespace>.svc.<cluster-name>`
* `<mariadb-name>-primary.<namespace>.svc`
* `<mariadb-name>-primary.<namespace>`
* `<mariadb-name>-primary`
* `<mariadb-name>-secondary.<namespace>.svc.<cluster-name>`
* `<mariadb-name>-secondary.<namespace>.svc`
* `<mariadb-name>-secondary.<namespace>`
* `<mariadb-name>-secondary`
* `localhost`

Whereas the client certificate is only valid for the `<mariadb-name>-client` SAN.

## `MaxScale` certificate specification

The `MaxScale` TLS setup consists of the following certificates:

* Certificate Authority (CA) keypair to issue the admin certificate.
* Admin leaf certificate used to encrypt the administrative REST API and GUI.
* Certificate Authority (CA) keypair to issue the listener certificate.
* Listener leaf certificate used to encrypt database connections to the listener.
* Server CA bundle used to establish trust with the MariaDB server.
* Server leaf certificate used to connect to the MariaDB server.

As a default behaviour, the operator generates a single CA to be used for issuing both the admin and the listener certificates, but the user can decide to use dedicated CAs for each case. Client certificate and CA bundle configured in the referred MariaDB are used as server certificates by default, but the user is able to provide its own certificates. Root CAs, and [intermedicate CAs](tls.md#intermediate-cas) in some cases, are supported, see [limitations](tls.md#limitations) for further detail.

Both the admin and listener certificates contain the following Subject Alternative Names (SANs):

* `<maxscale-name>.<namespace>.svc.<clusername>`
* `<maxscale-name>.<namespace>.svc`
* `<maxscale-name>.<namespace>`
* `<maxscale-name>`
* `<maxscale-name>-gui.<namespace>.svc.<clusername>`
* `<maxscale-name>-gui.<namespace>.svc`
* `<maxscale-name>-gui.<namespace>`
* `<maxscale-name>-gui`
* `*.<maxscale-name>-internal.<namespace>.svc.<clusername>`
* `*.<maxscale-name>-internal.<namespace>.svc`
* `*.<maxscale-name>-internal.<namespace>`
* `*.<maxscale-name>-internal`

For details about the server certificate, see [MariaDB certificate specification](tls.md#mariadb-certificate-specification).

## CA bundle

As you could appreciate in [MariaDB certificate specification](tls.md#mariadb-certificate-specification) and [MaxScale certificate specification](tls.md#maxscale-certificate-specification), the TLS setup involves multiple CAs. In order to establish trust in a more convenient way, the operator groups the CAs together in a CA bundle that will need to be specified when [securely connecting from your applications](tls.md#connect-applications-with-tls). Every `MariaDB` and `MaxScale` resources have a dedicated bundle of its own available in a `Secret` named `<instance-name>-ca-bundle`.

These trust bundles contain non expired CAs needed to connect to the instances. New CAs are automatically added to the bundle after [renewal](tls.md#ca-renewal), whilst old CAs are removed after they expire. It is important to note that both the new and old CAs remain in the bundle for a while to ensure a smooth update when the new certificates are issued by the new CA.

## Issue certificates with the operator

By setting `tls.enabled=true`, the operator will generate a root CA for each instance, which will be used to issue the certificates described in the [MariaDB cert spec](tls.md#mariadb-certificate-specification) and [MaxScale cert spec](tls.md#maxscale-certificate-specification) sections:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb
spec:
  ...
  tls:
    enabled: true
```

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MaxScale
metadata:
  name: maxscale
spec:
  ...
  tls:
    enabled: true
```

To establish trust with the instances, the CA's public key will be added to the [CA bundle](tls.md#ca-bundle). If you need a different trust chain, please refer to the [custom trust](tls.md#custom-trust) section.

The advantage of this approach is that the operator fully manages the `Secrets` that contain the certificates without depending on any third party dependency. Also, since the operator fully controls the renewal process, it is able to pause a leaf certificate renewal if the CA is being updated at that moment, as described in the [cert renewal](tls.md#certificate-renewal) section.

## Issue certificates with cert-manager

{% hint style="warning" %}
[cert-manager](https://cert-manager.io/) must be previously installed in the cluster in order to use this feature.
{% endhint %}

cert-manager is the de-facto standard for managing certificates in Kubernetes. It is a Kubernetes native certificate management controller that allows you to automatically provision, manage and renew certificates. It supports multiple [certificate backends](https://cert-manager.io/docs/configuration/issuers/) (in-cluster, Hashicorp Vault...) which are configured as `Issuer` or `ClusterIssuer` resources.

As an example, we are going to setup an in-cluster root CA `ClusterIssuer`:

```yaml
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: selfsigned
spec:
  selfSigned: {}
---
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: root-ca
  namespace: default
spec:
  duration: 52596h # 6 years
  commonName: root-ca
  usages:
  - digital signature
  - key encipherment
  - cert sign
  issuerRef:
    name: selfsigned
    kind: ClusterIssuer
  isCA: true
  privateKey:
    encoding: PKCS1
    algorithm: ECDSA
    size: 256
  secretTemplate:
    labels:
      enterprise.mariadb.com/watch: ""
  secretName: root-ca
  revisionHistoryLimit: 10
---
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: root-ca
spec:
  ca:
    secretName: root-ca
```

Then, you can reference the `ClusterIssuer` in the `MariaDB` and `MaxScale` resources:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-galera
spec:
  ...
  tls:
    enabled: true
    serverCertIssuerRef:
      name: root-ca
      kind: ClusterIssuer
    clientCertIssuerRef:
      name: root-ca
      kind: ClusterIssuer
```

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MaxScale
metadata:
  name: maxscale-galera
spec:
  ...
  tls:
    enabled: true
    adminCertIssuerRef:
      name: root-ca
      kind: ClusterIssuer
    listenerCertIssuerRef:
      name: root-ca
      kind: ClusterIssuer
```

The operator will create cert-manager's [Certificate resources](https://cert-manager.io/docs/reference/api-docs/#cert-manager.io/v1.Certificate) for each certificate, and will mount the resulting [TLS Secrets](https://kubernetes.io/docs/concepts/configuration/secret/#tls-secrets) in the instances. These `Secrets` containing the certificates will be managed by cert-manager as well as its renewal process.

To establish trust with the instances, the [ca.crt field provided by cert-managed](https://cert-manager.io/docs/faq/#why-isnt-my-certificates-chain-in-my-issued-secrets-cacrt) in the `Secret` will be added to the [CA bundle](tls.md#ca-bundle). If you need a different trust chain, please refer to the [custom trust](tls.md#custom-trust) section.

The advantage of this approach is that you can use any of the [cert-manager's certificate backends](https://cert-manager.io/docs/configuration/issuers/), such as the in-cluster CA or HashiCorp Vault, and potentially reuse the same `Issuer`/`ClusterIssuer` with multiple instances.

## Provide your own certificates

Providing your own certificates is as simple as creating the `Secrets` with the appropriate structure and referencing them in the `MariaDB` and `MaxScale` resources. The certificates must be compliant with the [MariaDB cert spec](tls.md#mariadb-certificate-specification) and [MaxScale cert spec](tls.md#maxscale-certificate-specification).

The CA certificate must be provided as a `Secret` with the following structure:

```yaml
apiVersion: v1
kind: Secret
type: Opaque
metadata:
  name: mariadb-galera-server-ca
  labels:
    enterprise.mariadb.com/watch: ""
data:
  ca.crt:
  -----BEGIN CERTIFICATE-----
  <public-key>
  -----END CERTIFICATE-----
  ca.key:
  -----BEGIN EC PRIVATE KEY-----
  <private-key>
  -----END EC PRIVATE KEY-----
```

The `ca.key` field is only required if you want to the operator to automatically re-issue certificates with this CA, see [bring your own CA](tls.md#bring-your-own-ca) for further detail. In other words, if only `ca.crt` is provided, the operator will trust this CA by adding it to the [CA bundle](tls.md#ca-bundle), but no certificates will be issued with it, the user will responsible for upating the certificate `Secret` manually with renewed certificates.

The `enterprise.mariadb.com/watch` label is required only if you want the operator to automatically trigger an update when the CA is renewed, see [CA renewal](tls.md#ca-renewal) for more detail.

The leaf certificate must match the previous CA's public key, and it should provided as a [TLS Secret](https://kubernetes.io/docs/concepts/configuration/secret/#tls-secrets) with the following structure:

```yaml
apiVersion: v1
kind: Secret
type: kubernetes.io/tls  
metadata:
  name: mariadb-galera-server-tls 
  labels:
    enterprise.mariadb.com/watch: ""
data:
  tls.crt:
  -----BEGIN CERTIFICATE-----
  <public-key>
  -----END CERTIFICATE-----
  tls.key:
  -----BEGIN EC PRIVATE KEY-----
  <private-key>
  -----END EC PRIVATE KEY-----
```

The `enterprise.mariadb.com/watch` label is required only if you want the operator to automatically trigger an update when the certificate is renewed, see [cert renewal](tls.md#certificate-renewal) for more detail.

Once the certificate `Secrets` are available in the cluster, you can create the `MariaDB` and `MaxScale` resources referencing them:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-galera
spec:
  ...
  tls:
    enabled: true
    serverCASecretRef:
      name: mariadb-server-ca
    serverCertSecretRef:
      name: mariadb-galera-server-tls
    clientCASecretRef:
      name: mariadb-client-ca
    clientCertSecretRef:
      name: mariadb-galera-client-tls
```

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MaxScale
metadata:
  name: maxscale-galera
spec:
  ...
  tls:
    enabled: true
    adminCASecretRef:
      name: maxscale-admin-ca
    adminCertSecretRef:
      name: maxscale-galera-admin-tls
    listenerCASecretRef:
      name: maxscale-listener-ca
    listenerCertSecretRef:
      name: maxscale-galera-listener-tls
    serverCASecretRef:
      name: mariadb-galera-ca-bundle
    serverCertSecretRef:
      name: mariadb-galera-client-tls
```

## Bring your own CA

If you already have a CA setup outside of Kubernetes, you can use it with the operator by providing the CA certificate as a `Secret` with the following structure:

```yaml
apiVersion: v1
kind: Secret
type: Opaque
metadata:
  name: mariadb-ca
  labels:
    enterprise.mariadb.com/watch: ""
data:
  ca.crt:
  -----BEGIN CERTIFICATE-----
  <public-key>
  -----END CERTIFICATE-----
  ca.key:
  -----BEGIN EC PRIVATE KEY-----
  <private-key>
  -----END EC PRIVATE KEY-----
```

Just by providing a reference to this `Secret`, the operator will use it to issue leaf certificates instead of generating a new CA:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-galera
spec:
  ...
  tls:
    enabled: true
    serverCASecretRef:
      name: mariadb-server-ca
    clientCASecretRef:
      name: mariadb-client-ca
```

## Intermediate CAs

Intermediate CAs are supported by the operator with [some limitations](tls.md#limitations). Leaf certificates issued by the intermediate CAs are slightly different, and include the intermediate CA public key as part of the certificate, in the following order: `Leaf certificate -> Intermediate CA`. This is a common practise to easily establish trust in complex PKI setups, where multiple CA are involved.

Many applications support this `Leaf certificate -> Intermediate CA` structure as a valid leaf certificate, and are able to establish trust with the intermediate CA. Normally, the intermediate CA will not be directly trusted, but used as a path to the root CA, which should be trusted by the application. If not trusted already, you can add the root CA to the [CA bundle](tls.md#ca-bundle) by using a [custom trust](tls.md#custom-trust).

## Custom trust

You are able to provide a set of CA public keys to be added to the [CA bundle](tls.md#ca-bundle) by creating a `Secret` with the following structure:

```yaml
apiVersion: v1
kind: Secret
type: Opaque
metadata:
  name: custom-trust
  labels:
    enterprise.mariadb.com/watch: ""
data:
  ca.crt:
  -----BEGIN CERTIFICATE-----
  <my-org-root-ca>
  -----END CERTIFICATE-----
  -----BEGIN CERTIFICATE-----
  <root-ca>
  -----END CERTIFICATE-----
```

And referencing it in the `MariaDB` and `MaxScale` resources, for instance:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MaxScale
metadata:
  name: maxscale-galera
spec:
  ...
  tls:
    enabled: true
    adminCASecretRef:
      name: custom-trust
    adminCertIssuerRef:
      name: my-org-intermediate-ca
      kind: ClusterIssuer
    listenerCASecretRef:
      name: custom-trust
    listenerCertIssuerRef:
      name: intermediate-ca
      kind: ClusterIssuer
```

This is specially useful when issuing certificates with an intermediate CA, see [intermediate CAs](tls.md#intermediate-cas) section for further detail.

## Distributing trust

Distributing the [CA bundle](tls.md#ca-bundle) to your application namespace is out of the scope of this operator, the bundles will remain in the same namespace as the `MariaDB` and `MaxScale` instances.

If your application is in a different namespace, you can copy the CA bundle to the application namespace. Projects like [trust-manager](https://github.com/cert-manager/trust-manager) can help you to automate this process and continously reconcile bundle changes.

## TLS version configuration

You may configure the supported TLS versions in `MariaDB` by setting:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-galera
spec:
  tls:
    versions:
      - TLSv1.3
      - TLSv1.2
      - TLSv1.1
      - TLSv1.0
```

If not specified, the MariaDB's default TLS versions will be used. See [MariaDB docs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-in-transit-encryption/ssltls-system-variables).

Regarding `MaxScale`, you can also configure the supported TLS versions, both for the Admin REST API and MariaDB servers:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MaxScale
metadata:
  name: maxscale-galera
spec:
  ...
  tls:
    adminVersions:
      - TLSv13
      - TLSv12
      - TLSv11
      - TLSv10
    serverVersions:
      - TLSv13
      - TLSv12
      - TLSv11
      - TLSv10
```

If not specified, the MaxScale's default TLS versions will be used. See MaxScale docs:

* [Admin TLS version](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-management/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide#admin_ssl_version)
* [Server TLS version](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-management/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide#ssl_version)

## Certificate lifetime configuration

By default, CA certificates are valid for 3 years, while leaf certificates have a validity of 3 months. This lifetime can be customized in both `MariaDB` and `MaxScale` resources through the certificate configuration fields. For example:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-galera
spec:
  tls:
    enabled: true
    required: true
    serverCertConfig:
      caLifetime: 8766h # 1 year
      certLifetime: 720h # 1 month
    clientCertConfig:
      caLifetime: 8766h # 1 year
      certLifetime: 720h # 1 month
```

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MaxScale
metadata:
  name: maxscale-galera
spec:
  tls:
    enabled: true
    adminCertConfig:
      caLifetime: 8766h # 1 year
      certLifetime: 1h # 1 month
    listenerCertConfig:
      caLifetime: 8766h # 1 year
      certLifetime: 720h # 1 month
```

When issuing certificates with cert-manager, you can specify the certificate configuration field alongside the issuer reference:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-galera
spec:
  tls:
    enabled: true
    required: true
    serverCertIssuerRef:
      name: root-ca
      kind: ClusterIssuer
    serverCertConfig:
      caLifetime: 8766h # 1 year
      certLifetime: 720h # 1 month
    clientCertIssuerRef:
      name: root-ca
      kind: ClusterIssuer
    clientCertConfig:
      caLifetime: 8766h # 1 year
      certLifetime: 720h # 1 month
```

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MaxScale
metadata:
  name: maxscale-galera
spec:
  tls:
    enabled: true
    adminCertIssuerRef:
      name: root-ca
      kind: ClusterIssuer
    adminCertConfig:
      caLifetime: 8766h # 1 year
      certLifetime: 1h # 1 month
    listenerCertIssuerRef:
      name: root-ca
      kind: ClusterIssuer
    listenerCertConfig:
      caLifetime: 8766h # 1 year
      certLifetime: 720h # 1 month
```

## Private key configuration

By default, private keys are generated with the `ECDSA` algorithm and a size of `256`. You can customize the private key configuration in both `MariaDB` and `MaxScale` resources through the certificate configuration fields. For example:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-galera
spec:
  tls:
    enabled: true
    required: true
    serverCertConfig:
      privateKeyAlgorithm: RSA
      privateKeySize: 2048
    clientCertConfig:
      privateKeyAlgorithm: RSA
      privateKeySize: 2048
```

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MaxScale
metadata:
  name: maxscale-galera
spec:
  tls:
    enabled: true
    adminCertConfig:
      privateKeyAlgorithm: RSA
      privateKeySize: 2048
    listenerCertConfig:
      privateKeyAlgorithm: RSA
      privateKeySize: 2048
```

When issuing certificates with cert-manager, you can specify the private key configuration field alongside the issuer reference:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-galera
spec:
  tls:
    enabled: true
    required: true
    serverCertIssuerRef:
      name: root-ca
      kind: ClusterIssuer
    serverCertConfig:
      privateKeyAlgorithm: ECDSA
      privateKeySize: 256
    clientCertIssuerRef:
      name: root-ca
      kind: ClusterIssuer
    clientCertConfig:
      privateKeyAlgorithm: ECDSA
      privateKeySize: 256
```

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MaxScale
metadata:
  name: maxscale-galera
spec:
  tls:
    enabled: true
    adminCertIssuerRef:
      name: root-ca
      kind: ClusterIssuer
    adminCertConfig:
      privateKeyAlgorithm: ECDSA
      privateKeySize: 256
    listenerCertIssuerRef:
      name: root-ca
      kind: ClusterIssuer
    listenerCertConfig:
      privateKeyAlgorithm: ECDSA
      privateKeySize: 256
```

The following set of algorithms and sizes are supported:

| Algorithm | Key Sizes        |
| --------- | ---------------- |
| RSA       | 2048, 3072, 4096 |
| ECDSA     | 256, 384, 521    |

## CA renewal

Depending on the setup, CAs can be managed and renewed by either MariaDB Enterprise Kubernetes Operator or cert-manager.

When managed by the operator, CAs have a lifetime of 3 years by default, and are marked for renewal after 66% of its lifetime has passed i.e. \~2 years. After being renewed, the operator will trigger an update of the instances to include the new CA in the bundle.

When managed by cert-manager, the renewal process is fully controlled by cert-manager, but the operator will also update the CA bundle after the CA is renewed.

You may choose any of the available [update strategies](updates.md) to control the instance update process.

## Certificate renewal

Depending on the setup, certificates can be managed and renewed by the operator or cert-manager. In either case, certificates have a lifetime of 90 days by default, and marked for renewal after 66% of its lifetime has passed i.e. \~60 days.

When the [certificates are issued by the operator](tls.md#issue-certificates-with-the-operator), the operator is able to pause a leaf certificate renewal if the CA is being updated at that same moment. This approach ensures a smooth update by avoiding the simultaneous rollout of the new CA and its associated certificates. Rolling them out together could be problematic, as all Pods need to trust the new CA before its issued certificates can be utilized.

When the [certificates are issued by cert-manager](tls.md#issue-certificates-with-cert-manager), the renewal process is fully managed by cert-manager, and the operator will not interfere with it. The operator will only update the instances whenever the CA or the certificates get renewed.

You may choose any of the available [update strategies](updates.md) to control the instance update process.

## Certificate status

To have a high level picture of the certificates status, you can check the `status.tls` field of the `MariaDB` and `MaxScale` resources:

```sh
kubectl get mariadb mariadb-galera -o jsonpath="{.status.tls}" | jq
{
  "caBundle": [
    {
      "issuer": "CN=mariadb-galera-ca",
      "notAfter": "2028-01-20T14:26:50Z",
      "notBefore": "2025-01-20T13:26:50Z",
      "subject": "CN=mariadb-galera-ca"
    }
  ],
  "clientCert": {
    "issuer": "CN=mariadb-galera-ca",
    "notAfter": "2025-04-20T14:26:50Z",
    "notBefore": "2025-01-20T13:26:50Z",
    "subject": "CN=mariadb-galera-client"
  },
  "serverCert": {
    "issuer": "CN=mariadb-galera-ca",
    "notAfter": "2025-04-20T14:26:50Z",
    "notBefore": "2025-01-20T13:26:50Z",
    "subject": "CN=mariadb-galera.default.svc.cluster.local"
  }
}
```

```sh
kubectl get maxscale maxscale-galera -o jsonpath="{.status.tls}" | jq
{
  "adminCert": {
    "issuer": "CN=maxscale-galera-ca",
    "notAfter": "2025-04-20T14:33:09Z",
    "notBefore": "2025-01-20T13:33:09Z",
    "subject": "CN=maxscale-galera.default.svc.cluster.local"
  },
  "caBundle": [
    {
      "issuer": "CN=maxscale-galera-ca",
      "notAfter": "2028-01-20T14:33:09Z",
      "notBefore": "2025-01-20T13:33:09Z",
      "subject": "CN=maxscale-galera-ca"
    },
    {
      "issuer": "CN=mariadb-galera-ca",
      "notAfter": "2028-01-20T14:28:46Z",
      "notBefore": "2025-01-20T13:28:46Z",
      "subject": "CN=mariadb-galera-ca"
    }
  ],
  "listenerCert": {
    "issuer": "CN=maxscale-galera-ca",
    "notAfter": "2025-04-20T14:33:09Z",
    "notBefore": "2025-01-20T13:33:09Z",
    "subject": "CN=maxscale-galera.default.svc.cluster.local"
  },
  "serverCert": {
    "issuer": "CN=mariadb-galera-ca",
    "notAfter": "2025-04-20T14:28:46Z",
    "notBefore": "2025-01-20T13:28:46Z",
    "subject": "CN=mariadb-galera-client"
  }
}
```

## TLS requirements for `Users`

You are able to declaratively manage access to your `MariaDB` instances by creating [User SQL resources](sql-resources.md#user-cr). In particular, when TLS is enabled, you can provide additional requirements for the user when connecting over TLS.

For instance, if you want to require a valid x509 certificate for the user to be able o connect:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: User
metadata:
  name: user
spec:
  ...
  require:
    x509: true
```

In order to restrict which subject the user certificate should have and/or require a particular issuer, you may set:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: User
metadata:
  name: user
spec:
  ...
  require:
    issuer: "/CN=mariadb-galera-ca"
    subject: "/CN=mariadb-galera-client"
```

When any of these TLS requirements are not met, the user will not be able to connect to the instance.

See [MariaDB docs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-in-transit-encryption/securing-connections-for-client-and-server#requiring-tls) and the [API reference](api-reference.md) for further detail.

## Galera Enterprise SSL modes

MariaDB Enterprise Cluster (Galera) supports multiple SSL modes to secure the communication between the nodes. For configuring the SSL enforcement level on the server i.e. WSREP, you can set:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-galera
spec:
  tls:
    enabled: true
    galeraServerSSLMode: SERVER_X509
```

The following values are supported: `SERVER_X509`, `SERVER` and `PROVIDER`. Refer to the [MariaDB Enterprise Cluster documentation](https://mariadb.com/docs/galera-cluster/galera-security/mariadb-enterprise-cluster-security#wsrep-tls-modes) for further detail about these modes.

You may also configure the SSL enforcement level used during Snapshot State Transfers(SST) by setting:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-galera
spec:
  tls:
    enabled: true
    galeraSSTEnabled: true
    galeraClientSSLMode: VERIFY_IDENTITY
```

The following values are supported: `VERIFY_IDENTITY`, `VERIFY`, `REQUIRED` and `DISABLED`. Refer to the [MariaDB Enterprise Cluster documentation](https://mariadb.com/docs/galera-cluster/galera-security/mariadb-enterprise-cluster-security#sst-tls-modes) for further detail about these modes.

If you are willing to increase the enforcement level in an existing instance, make sure you follow the migration guide provided in the [Enabling TLS in existing instances](migrations/enabling-tls-in-existing-instances.md) section.

## Secure application connections with TLS

In this guide, we will configure TLS for an application running in the `app` namespace to connect with `MariaDB` and `MaxScale` instances deployed in the `default` namespace. We assume that the following resources are already present in the `default` namespace with TLS enabled:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-galera
spec:
  rootPasswordSecretKeyRef:
    name: mariadb
    key: root-password
  storage:
    size: 1Gi
  replicas: 3
  galera:
    enabled: true
  tls:
    enabled: true
    required: true
---
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MaxScale
metadata:
  name: maxscale-galera
spec:
  replicas: 2
  mariaDbRef:
    name: mariadb-galera
  tls:
    enabled: true
```

The first step is to create a `User` resource and grant the necessary permissions:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: User
metadata:
  name: app
  namespace: app
spec:
  mariaDbRef:
    name: mariadb-galera
    namespace: default
  require:
    issuer: "/CN=mariadb-galera-ca"
    subject: "/CN=mariadb-galera-client"
  host: "%"
---
apiVersion: enterprise.mariadb.com/v1alpha1
kind: Grant
metadata:
  name: grant-app
  namespace: app
spec:
  mariaDbRef:
    name: mariadb-galera
    namespace: default
  privileges:
    - "ALL PRIVILEGES"
  database: "*"
  table: "*"
  username: app
  host: "%"
```

The `app` user will be able to connect to the `MariaDB` instance from the `app` namespace by providing a certificate with subject `mariadb-galera-client` and issued by the `mariadb-galera-ca` CA.

With the permissions in place, the next step is to prepare the certificates required for the application to connect:

* CA Bundle: The trust bundle for `MariaDB` and `MaxScale` is available as a `Secret` named `<instance-name>-ca-bundle` in the `default` namespace. For more details, refer to the sections on [CA bundle](tls.md#ca-bundle) and [distributing trust](tls.md#distributing-trust).
* Client Certificate: `MariaDB` provides a default client certificate stored in a `Secret` named `<mariadb-name>-client-cert` in the `default` namespace. You can either use this `Secret` or generate a new one with the subject `mariadb-galera-client`, issued by the `mariadb-galera-ca` CA. While issuing client certificates for applications falls outside the scope of this operator, you can [test them using Connection resources](tls.md#test-tls-certificates-with-connections).

In this example, we assume that the following `Secrets` are available in the `app` namespace:

* `mariadb-bundle`: CA bundle for the `MariaDB` and `MaxScale` instances.
* `mariadb-galera-client-cert`: Client certificate required to connect to the `MariaDB` instance.

With these `Secrets` in place, we can proceed to define our application:

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: mariadb-client
  namespace: app
spec:
  schedule: "*/1 * * * *"
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: mariadb-client
            image: mariadb:11.4.4
            command:
              - bash
            args:
              - -c
              - >
                mariadb -u app -h mariadb-galera-primary.default.svc.cluster.local
                --ssl-ca=/etc/pki/ca.crt --ssl-cert=/etc/pki/tls.crt
                --ssl-key=/etc/pki/tls.key --ssl-verify-server-cert
                -e "SELECT 'MariaDB connection successful!' AS Status;" -t
            volumeMounts:
            - name: pki
              mountPath: /etc/pki
              readOnly: true
          volumes:
          - name: pki
            projected:
              sources:
              - secret:
                  name: mariadb-bundle
                  items:
                  - key: ca.crt
                    path: ca.crt
              - secret:
                  name: mariadb-galera-client-cert
                  items:
                  - key: tls.crt
                    path: tls.crt
                  - key: tls.key
                    path: tls.key
          restartPolicy: Never
```

The application will connect to the `MariaDB` instance using the `app` user, and will execute a simple query to check the connection status. The `--ssl-ca`, `--ssl-cert`, `--ssl-key` and `--ssl-verify-server-cert` flags are used to provide the CA bundle, client certificate and key, and to verify the server certificate respectively.

If the connection is successful, the output should be:

```sh
+---------------------------------+
| Status                          |
+---------------------------------+
| MariaDB connection successful!  |
+---------------------------------+
```

You can also point the application to the `MaxScale` instance by updating the host to `maxscale-galera.default.svc.cluster.local`:

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: maxscale-client
  namespace: app
spec:
  schedule: "*/1 * * * *"
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: maxscale-client
            image: mariadb:11.4.4
            command:
              - bash
            args:
              - -c
              - >
                mariadb -u app -h maxscale-galera.default.svc.cluster.local
                --ssl-ca=/etc/pki/ca.crt --ssl-cert=/etc/pki/tls.crt
                --ssl-key=/etc/pki/tls.key --ssl-verify-server-cert
                -e "SELECT 'MaxScale connection successful!' AS Status;" -t
            volumeMounts:
            - name: pki
              mountPath: /etc/pki
              readOnly: true
          volumes:
          - name: pki
            projected:
              sources:
              - secret:
                  name: mariadb-bundle
                  items:
                  - key: ca.crt
                    path: ca.crt
              - secret:
                  name: mariadb-galera-client-cert
                  items:
                  - key: tls.crt
                    path: tls.crt
                  - key: tls.key
                    path: tls.key
          restartPolicy: Never
```

If successful, the expected output is:

```sh
+---------------------------------+
| Status                          |
+---------------------------------+
| MaxScale connection successful! |
+---------------------------------+
```

## Test TLS certificates with `Connections`

In order to validate your TLS setup, and to ensure that you TLS certificates are correctly issued and configured, you can use the `Connection` resource to test the connection to both your `MariaDB` and `MaxScale` instances:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: Connection
metadata:
  name: connection
spec:
  mariaDbRef:
    name: mariadb-galera
  username: mariadb
  passwordSecretKeyRef:
    name: mariadb
    key: password
  tlsClientCertSecretRef:
    name: mariadb-galera-client-cert
  database: mariadb
  healthCheck:
    interval: 30s
```

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: Connection
metadata:
  name: connection-maxscale
spec:
  maxScaleRef:
    name: maxscale-galera
  username: mariadb
  passwordSecretKeyRef:
    name: mariadb
    key: password
  tlsClientCertSecretRef:
    name: mariadb-galera-client-cert
  database: mariadb
  healthCheck:
    interval: 30s
```

If successful, the `Connection` resource will be in a `Ready` state, which means that your TLS setup is correctly configured:

```sh
kubectl get connections
NAME                         READY   STATUS    SECRET                AGE
connection                   True    Healthy   connection            2m8s
connection-maxscale          True    Healthy   connection-maxscale   97s
```

This could be specially useful when [providing your own certificates](tls.md#provide-your-own-certificates) and issuing certificates for your applications.

## Limitations

### Galera and intermediate CAs

Leaf certificates issued by [intermediate CAs](tls.md#intermediate-cas) are not supported by Galera, see [MDEV-35812](https://jira.mariadb.org/browse/MDEV-35812). This implies that a root CA must be used to issue the `MariaDB` certificates.

This doesn't affect `MaxScale`, as it is able to establish trust with intermediate CAs, and therefore you can still issue your application facing certificates (MaxScale listeners) with an intermediate CA, giving you more flexibility in your PKI setup.

### MaxScale

* Unlike `MariaDB`, TLS and non-TLS connections on the same port are not supported simultaneously.
* TLS encryption must be enabled for listeners when they are created. For servers, the TLS can be enabled after creation but it cannot be disabled or altered.

Refer to the [MaxScale documentation](tls.md#maxscale-configuration) for further details.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
