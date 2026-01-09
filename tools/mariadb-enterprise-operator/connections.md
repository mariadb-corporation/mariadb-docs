# Connections

MariaDB Enterprise Kubernetes Operator provides the `Connection` resource to configure connection strings for applications connecting to MariaDB. This resource creates and maintains a Kubernetes `Secret` containing the credentials and connection details needed by your applications.

## `Connection` CR

A `Connection` resource declares an intent to create a connection string for applications to connect to a MariaDB instance. When reconciled, it creates a `Secret` containing the DSN and optionally, individual connection parameters:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: Connection
metadata:
  name: connection
spec:
  mariaDbRef:
    name: mariadb
  username: mariadb
  passwordSecretKeyRef:
    name: mariadb
    key: password
  database: mariadb
  secretName: connection
  healthCheck:
    interval: 30s
    retryInterval: 3s
```

The operator creates a `Secret` named `connection` containing a DSN and individual fields like `username`, `password`, `host`, `port`, and `database`. Applications can mount this `Secret` to obtain the connection details.

## Service selection

By default, the `host` in the generated `Secret` points to the `Service` named after the referenced `MariaDB` or `MaxScale` resource (the same as `metadata.name`). For HA `MariaDB`, this `Service` load balances across all pods, so use `serviceName` to target a specific `Service` such as `<mariadb-name>-primary`.

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: Connection
metadata:
  name: connection
spec:
  mariaDbRef:
    name: mariadb
  serviceName: mariadb-primary
  username: mariadb
  passwordSecretKeyRef:
    name: mariadb
    key: password
  secretName: connection
```

Please refer to the [Kubernetes `Service` documentation](./topologies/high-availability.md#kubernetes-services) to identify which `Services` are available.

## Credential generation

The operator can automatically generate credentials for users via the `GeneratedSecretKeyRef` type with the `generate: true` field. This feature is available in the `MariaDB`, `MaxScale`, and `User` resources.

For example, when creating a `MariaDB` resource with an initial user:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb
spec:
  username: app
  passwordSecretKeyRef:
    name: app-password
    key: password
    generate: true
  database: app
```

The operator will automatically generate a random password and store it in a `Secret` named `app-password`. You can then reference this `Secret` in your `Connection` resource:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: Connection
metadata:
  name: app-connection
spec:
  mariaDbRef:
    name: mariadb
  username: app
  passwordSecretKeyRef:
    name: app-password
    key: password
  database: app
  secretName: app-connection
```

If you prefer to provide your own password, you can opt-out from random password generation by either not providing the `generate` field or setting it to `false`. This enables the use of GitOps tools like [sealed-secrets](https://github.com/bitnami-labs/sealed-secrets) or [external-secrets](https://github.com/external-secrets/external-secrets) to seed the password.

## Secret template

The `secretTemplate` field allows you to customize the output `Secret`, allowing you to include individual connection parameters:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: Connection
metadata:
  name: connection
spec:
  mariaDbRef:
    name: mariadb
  username: mariadb
  passwordSecretKeyRef:
    name: mariadb
    key: password
  database: mariadb
  secretName: connection
  secretTemplate:
    metadata:
      labels:
        app.kubernetes.io/name: myapp
      annotations:
        app.kubernetes.io/managed-by: mariadb-enterprise-operator
    key: dsn
    usernameKey: username
    passwordKey: password
    hostKey: host
    portKey: port
    databaseKey: database
```

The resulting `Secret` will contain:
- `dsn`: The full connection string
- `username`: The database username
- `password`: The database password
- `host`: The database host
- `port`: The database port
- `database`: The database name

## Custom DSN format

You can customize the DSN format using Go templates via the `format` field:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: Connection
metadata:
  name: connection
spec:
  mariaDbRef:
    name: mariadb
  username: mariadb
  passwordSecretKeyRef:
    name: mariadb
    key: password
  database: mariadb
  params:
    parseTime: "true"
    timeout: "5s"
  secretName: connection
  secretTemplate:
    key: dsn
    format: mysql://{{ .Username }}:{{ .Password }}@{{ .Host }}:{{ .Port }}/{{ .Database }}{{ .Params }}
```

Available template variables:
- `{{ .Username }}`: The database username
- `{{ .Password }}`: The database password
- `{{ .Host }}`: The database host
- `{{ .Port }}`: The database port
- `{{ .Database }}`: The database name
- `{{ .Params }}`: Query parameters (e.g., `?parseTime=true&timeout=5s`)

Refer to the [Go documentation](https://pkg.go.dev/text/template) for additional details about the template syntax.

## TLS authentication

`Connection` supports TLS client certificate authentication as an alternative to password authentication:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: User
metadata:
  name: app
spec:
  mariaDbRef:
    name: mariadb-galera
  require:
    issuer: "/CN=mariadb-galera-ca"
    subject: "/CN=mariadb-galera-client"
  host: "%"
---
apiVersion: enterprise.mariadb.com/v1alpha1
kind: Grant
metadata:
  name: grant-app
spec:
  mariaDbRef:
    name: mariadb-galera
  privileges:
    - "ALL PRIVILEGES"
  database: "*"
  table: "*"
  username: app
  host: "%"
---
apiVersion: enterprise.mariadb.com/v1alpha1
kind: Connection
metadata:
  name: connection
spec:
  mariaDbRef:
    name: mariadb-galera
  username: app
  tlsClientCertSecretRef:
    name: mariadb-galera-client-cert
  healthCheck:
    interval: 30s
```

When using TLS authentication, provide `tlsClientCertSecretRef` instead of `passwordSecretKeyRef`. The referenced `Secret` must be a Kubernetes TLS `Secret` containing the client certificate and key.

## Cross-namespace connections

`Connection` resources can reference `MariaDB` instances in different namespaces:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: Connection
metadata:
  name: connection
  namespace: app
spec:
  mariaDbRef:
    name: mariadb
    namespace: mariadb
  username: app
  passwordSecretKeyRef:
    name: app
    key: password
  database: app
  secretName: connection
```

This creates a `Connection` in the `app` namespace that references a `MariaDB` in the `mariadb` namespace.

## MaxScale connections

`Connection` resources can reference `MaxScale` instances using `maxScaleRef`:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: Connection
metadata:
  name: connection-maxscale
spec:
  maxScaleRef:
    name: maxscale-galera
  username: maxscale-galera-client
  passwordSecretKeyRef:
    name: maxscale-galera-client
    key: password
  secretName: conn-mxs
  port: 3306
  healthCheck:
    interval: 30s
```

When referencing a `MaxScale`, the operator uses the MaxScale `Service` and its listener port. The health check will consume connections from the MaxScale connection pool.

## External MariaDB connections

`Connection` resources can reference `ExternalMariaDB` instances by specifying `kind: ExternalMariaDB` in the `mariaDbRef`:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: Connection
metadata:
  name: connection-external
spec:
  mariaDbRef:
    name: external-mariadb
    kind: ExternalMariaDB
  username: user
  passwordSecretKeyRef:
    name: mariadb
    key: password
  database: mariadb
  secretName: connection-external
  healthCheck:
    interval: 5s
```

This is useful for generating connection strings to external MariaDB instances running outside of Kubernetes.

## Health checking

The `healthCheck` field configures periodic health checks to verify database connectivity:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: Connection
metadata:
  name: connection
spec:
  mariaDbRef:
    name: mariadb
  username: mariadb
  passwordSecretKeyRef:
    name: mariadb
    key: password
  database: mariadb
  secretName: connection
  healthCheck:
    interval: 30s
    retryInterval: 3s
```

- `interval`: How often to perform health checks (default: 30s)
- `retryInterval`: How often to retry after a failed health check (default: 3s)

The `Connection` status reflects the health check results, allowing you to monitor connectivity issues through Kubernetes.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
