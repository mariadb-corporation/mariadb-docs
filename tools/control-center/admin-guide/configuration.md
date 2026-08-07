---
description: >-
  Reference for GridGain Control Center configuration parameters: common
  properties, rate and size limits, sessions, SSL/TLS, mail, LDAP, and OpenID.
---

# Configuration Parameters

When Control Center is started, it looks for the configuration parameters in the following order:

1. Java System properties, for example:

   ```bash
   export JVM_OPTS="-Dserver.port=3004"
   ```
2. The `application.properties` file in the Control Center root folder. For example:

   ```properties
   # Server Configuration
   server.port=3000
   ```
3. The `application.yml` file in the Control Center root folder. For example:

   ```yaml
   server:
     port: 3000
   ```

If the parameter is not found in the above sources, the default value is used.

Use one of the above methods to set the configuration parameters.

## Common Properties

| Parameter | Description | Default |
|---|---|---|
| account.activation.enabled | Enables account activation via email. After signing up, users will have to activate their account via email. Requires [Mail Server](#mail-server) properties. | false |
| account.activation.timeout | Activation link's timeout in milliseconds. | 1800000 |
| account.activation.send-timeout | The timeout for sending activation email, in milliseconds. | 180000 |
| account.admin.email | Email address in the administrator's account. | |
| account.admin.password | Administrator account's password. | |
| account.authentication.interval | The interval, in milliseconds, between login attempts. Increases exponentially based on the number of failed attempts. | 100 |
| account.authentication.max-attempts | The maximum number of failed attempts allowed before preventing login. An empty value means "infinity," which is the default. | |
| account.authentication.max-interval | The maximum time an account can be locked for, in milliseconds. | 300000 |
| account.signup.enabled | **Deprecated**: Use `account.self-registration.enabled` instead. When both properties are set, the new property takes precedence. | true |
| account.self-registration.enabled | Enables self-registration for new accounts. When disabled, only an admin can create users in Control Center, and self sign up is turned off. Even OpenID Connect users without account won't be able to sign up. | true |
| account.internal.enabled | Enables authentication via username and password in Control Center. If disabled, only OpenID Connect authentication is available. | true |
| account.oidc.rbac.enabled | Enable Control Center role management via OpenID Connect. If set to `true`, requires for `spring.security.oauth2.client.provider.{name}.user-info-uri` to be configured. When disabled, automatically sets `account.oidc.skipSignUp` to `true`. | false |
| account.oidc.rbac.attributeName | OpenID Connect attribute name that is used in your OpenID configuration to define the Control Center role. The default attribute name is `cc-role`, but you can use any custom name. This attribute can define the following Control Center roles: `admin`, `regular`, or `no-access`. | cc-role |
| account.oidc.skipSignUp | Skips creating a password during OpenID Connect authentication, allowing quick access. Automatically is set to `true` when `account.internal.enabled` is disabled. | false |
| compute.grid.task-execution-timeout | Task execution timeout in milliseconds. | 60000 |
| compute.grid.task-pull-timeout | Task pull timeout in milliseconds. | 60000 |
| control.agent.secret-validation.enabled | Enables cluster secret validation on handshake. | true |
| control.base-url | Control Center URL for links in notifications. If the frontend and the backend have different hosts/ports, set the frontend URI as a value (for example, https://example.com:1234). | |
| control.browsers.allowed-origins | Comma-separated allowed origins for WebSocket browsers endpoint. | |
| control.cache.backups | The number of backups for all partitioned caches, configured via control.repositories.configurations.* properties. | |
| control.license.filestorage | Enables file watcher for license updates. | false |
| control.license.path | License monitoring path for file watcher. | license/control-center-license.xml |
| control.metric-collector.limit-enabled | Enables the metrics. If false, all the metrics are collected from a cluster. Otherwise, metrics are collected on demand. | true |
| control.metric-collector.limit-file-path | The path to the YAML file with templates of the metrics that must always be collected. Has no effect if limit-enabled is false. | classpath:metrics.yml |
| control.metric-collector.pull-interval | The interval of collecting the metric values from the cluster, in milliseconds. | 5000 |
| control.repositories.auto-migrate-enabled | Enables automatic migration of internal storage (required for version updates). | false |
| `control.repositories.configurations.{cacheName}.dataRegionName` | Custom data region for the cache. The property can be used for storing browser sessions (GccSessionCache) in the in-memory data region. | |
| control.repositories.configurations.GccSessionCache.touchExpirationTimeout | The number of milliseconds that the user session should be kept alive. Default value is 7 days. | 604800000 |
| control.repositories.configurations.QuerySessionCache.create-expiration-timeout | The period (in milliseconds) after which cache entities (key-value pairs) are removed from `QuerySessionCache` to preclude uncontrolled growth of the persistent cache size. | 604800000 |
| control.repositories.limit.strict-mode.enabled | Determines whether to use strict table-size limiting mode. When strict mode is enabled, write operations are restricted once the table-size limit is reached. | true |
| control.web-socket.send-buffer-size-limit | Maximum amount of data to buffer when sending messages to a WebSocket session (in bytes). | |
| server.address | Network address to which Control Center binds. | 0.0.0.0 |
| server.port | Control Center port. This port is used to access Control Center via a web browser. Clusters connect to this port as well. | 3000 |

## Rate Limits

| Parameter | Description | Default |
|---|---|---|
| control.rate-limit.ban-duration-seconds | Duration of the ban in seconds. | |
| control.rate-limit.block-connection-on-detection | If "true," the cluster is disconnected instead of entering the "limited" state. | false |
| control.rate-limit.candidates | The number of candidates with top statistics to be banned. | |
| control.rate-limit.computeHardLimit | Compute hard limit. | |
| control.rate-limit.computeSoftLimit | Compute soft limit. | |
| control.rate-limit.disconnected-lifetime-seconds | Lifetime of the rate limit session without connection. | |
| control.rate-limit.hard-limit | Once this number of messages in the queue is reached, the agents the highest messaging rate are disconnected. | |
| control.rate-limit.lower-threshold | Count of requests between the previous and the current checks. | 1000 |
| control.rate-limit.reconnectBanDuration | Reconnect ban duration. | |
| control.rate-limit.reconnectRateLimitCount | Reconnect rate limit. | |
| control.rate-limit.reconnectRateLimitPeriod | Reconnect rate limit period duration. | |
| control.rate-limit.remove-session-interval-millis | Scheduled interval for the session removal check, in milliseconds. | |
| control.rate-limit.soft-limit | Once this number of messages in the queue is reached, all the connected agents are required to reduce the message submission rate. | |
| control.rate-limit.trace-hard-limit | Once this limit is reached, the cluster will be marked as limited and no traces will be received for the ban duration. | |
| control.rate-limit.trace-soft-limit | Once this limit is reached, all agents are required to reduce the trace rate. | |
| control.rate-limit.update-interval-millis | Scheduled interval for the alert check, in milliseconds. | |

## Time-to-Live Limits

You can [optimize the disk space utilization](disk-space-optimization.md) by modifying the time-to-live (TTL) values for the relevant entities.

{% hint style="info" %}
The TTL properties can be used in conjunction with [Table Size Limits](#table-size-limits).
{% endhint %}

| Parameter | Description | Default |
|---|---|---|
| control.metric.ttl | Metrics' TTL, after which they are removed (in days). Set to 0 for infinite TTL. | 1 |
| control.repositories.configurations.TaskSessionAttributeCache.create-expiration-timeout | Task session attribute TTL (compute) in milliseconds. | 86400000 (1 day) |
| control.repositories.configurations.TaskSessionCache.create-expiration-timeout | Task session TTL (compute) in milliseconds. | 86400000 (1 day) |
| control.repositories.configurations.QuerySessionCache.create-expiration-timeout | Query session TTL (compute) in milliseconds. | 86400000 (1 day) |
| control.repositories.configurations.SpanCache.create-expiration-timeout | Span cache TTL (compute) in milliseconds. | 86400000 (1 day) |
| control.repositories.configurations.TraceCache.create-expiration-timeout | Trace cache TTL (compute) in milliseconds. | 86400000 (1 day) |

## Table Size Limits

You can [optimize the disk space utilization](disk-space-optimization.md) by limiting the table size (number of records) for the following entities: Running Queries (QuerySession), Traces (Trace, Span), and Compute (TaskSession).

{% hint style="warning" %}
In many scenarios, [Time-to-Live Limits](#time-to-live-limits) would be more CPU/disk-efficient than Table Size Limits, especially in high-load environments.
{% endhint %}

{% hint style="info" %}
Table Size Limits can be used in conjunction with [Time-to-Live Limits](#time-to-live-limits).
{% endhint %}

| Parameter | Description | Default |
|---|---|---|
| control.metric.bufRatio | Limit coefficient. Allows to temporarily exceed the metric limit, for example set to 1.10 and the limit is 100, once the number of metrics reaches 110, 10 oldest metrics will be deleted. | 1.10 |
| control.metric.limit | The number of metrics allowed per cluster. | -1 (unlimited) |
| control.repositories.configurations.QuerySessionCache.limit.count | If >0, limits the QuerySession (running queries) table size. | No limit |
| control.repositories.configurations.TaskSessionCache.limit.count | If >0, limits the TaskSession (compute) table size. | No limit |
| control.repositories.configurations.TraceCache.limit.count | If >0, limits the Trace table size. | No limit |
| control.repositories.configurations.SpanCache.limit.count | If >0, limits the Span table size. | No limit |
| control.repositories.delete-exceeded-records.interval-millis | Interval between cleanup iterations in milliseconds. | 10000 |
| control.repositories.limit.iteration-timeout | Maximum duration of a cleanup iteration in seconds. | 30000 |
| control.repositories.limit.batch-size | The maximum batch size of delete operation in records. | 5000 |

When the table size limit is set, Control Center automatically cleans tables in a background process, starting from the oldest records.

## Sessions

| Parameter | Description | Default |
|---|---|---|
| spring.session.cache-name | The name of the cache for storing web sessions. | IgniteSessionCache |
| spring.session.timeout | The maximum inactive interval between requests before newly created sessions start getting invalidated (in milliseconds). | 604800000 |

## Teams

| Parameter | Description | Default |
|---|---|---|
| account.globalTeam.enabled | If true, automatically creates a team called *Global Team*, which includes all active users (local or AD/LDAP-managed). | false |
| account.globalTeam.attachCluster | If true, and if Global Team is enabled, automatically shares all clusters in the environment with that team. | false |

## SSL/TLS

You can enable SSL/TLS to encrypt communication between your cluster and Control Center.

| Parameter | Description | Default |
|---|---|---|
| server.ssl.ciphers | A list of SSL ciphers to use. | |
| server.ssl.client-auth | Client authentication mode. Requires a trust store. Possible values:<br>- `NEED` - Client authentication is needed and mandatory.<br>- `NONE` - Client authentication is not wanted.<br>- `WANT` - Client authentication is wanted but not mandatory. | |
| server.ssl.enabled | Enables SSL support. Takes effect only when a key store is provided. | true |
| server.ssl.enabled-protocols | Enabled SSL protocols. | |
| server.ssl.key-alias | The alias of the SSL certificate in the key store. | |
| server.ssl.key-password | Password for the SSL certificate. | |
| server.ssl.key-store | Path to the key store that holds the SSL certificate (typically a jks file). | |
| server.ssl.key-store-password | Password for the key store. | |
| server.ssl.key-store-provider | Provider for the key store. | |
| server.ssl.key-store-type | The type of the key store. | |
| server.ssl.protocol | The SSL protocol to use. | TLS |
| server.ssl.trust-store | The trust store that holds SSL certificates. | |
| server.ssl.trust-store-password | The password for the trust store. | |
| server.ssl.trust-store-provider | Provider for the trust store. | |
| server.ssl.trust-store-type | The type of the trust store. | |

## Mail Server

Control Center requires mail server parameters to send email notification and account confirmation emails.

| Parameter | Description | Default |
|---|---|---|
| spring.mail.default-encoding | Default MimeMessage encoding. | UTF-8 |
| spring.mail.host | SMTP server host. For instance, `smtp.example.com`. | |
| spring.mail.jndi-name | Session JNDI name. When set, takes precedence over other Session settings. | |
| spring.mail.password | Login password of the SMTP server. | |
| spring.mail.port | SMTP server port. | |
| spring.mail.properties.* | Additional JavaMail Session properties. | |
| spring.mail.protocol | Protocol used by the SMTP server. | smtp |
| spring.mail.test-connection | Test that the mail server is available on startup. | false |
| spring.mail.username | Login user of the SMTP server. | |

## SMS Provider

Control Center supports SMS alerts via Vonage communication provider.

1. Sign up at https://www.vonage.com/.
2. Get your api key and api secret. See [https://developer.nexmo.com/concepts/guides/authentication#api-key-and-secret](https://developer.nexmo.com/concepts/guides/authentication#api-key-and-secret).
3. Specify the api key and secret in the following properties:

| Parameter | Description |
|---|---|
| nexmo.creds.api-key | The API key. |
| nexmo.creds.api-secret | The API secret. |
| nexmo.creds.from | The name or number the message is sent from. |

## Active Directory and LDAP

You can configure the Control Center to integrate with Active Directory or LDAP to store user data externally. As every authentication request leads to Active Directory or LDAP server and no caching is performed, it is possible to log in as a new user once it is created.

{% hint style="info" %}
Both Active Directory and LDAP integration cannot be used together with native or OpenID-Connect-based authentication.
{% endhint %}

Active Directory and LDAP integrations have some limitations that you should be aware of before configuring the Control Center to use them. See the list of limitations below:

- Users can only be created by adding them to the Active Directory or LDAP server when Active Directory or LDAP integration is enabled. Signing up and creating an admin user with a link from the backend log is not applicable.
- To become admins, users need to be a part of a special group in Active Directory or LDAP. The group name can be specified using the corresponding configuration properties.
- The list of users is not displayed on the admin screen when Active Directory or LDAP integration is enabled.
- Profile information can be modified only on the Active Directory or LDAP server, not through the Control Center interface.

{% hint style="info" %}
If you are looking for more information on Active Directory or LDAP configuration, please consult the blog posts below:

- [Role-based Authorization with Active Directory for GridGain](https://medium.com/@valentin.kulichenko/role-based-authorization-with-active-directory-for-gridgain-eaad394ba173)
- [GridGain with Active Directory: Multiple Groups for a Single User](https://medium.com/@valentin.kulichenko/gridgain-with-active-directory-multiple-groups-for-a-single-user-5aa84c086261)
{% endhint %}

### Active Directory

To configure Active Directory authentication, use the following parameters:

| Parameter | Required | Description | Example |
|---|---|---|---|
| spring.activedirectory.urls | Required | Active Directory URLs of the server, including schema (ldap:// or ldaps://) and port, separated by comma. | ldap://localhost:389,ldaps://localhost:636 |
| spring.activedirectory.root-dn | Required | The Distinguished Name under which users and user groups are stored. | dc=gridgain,dc=org |
| spring.activedirectory.domain | Optional | The default domain name to be added to the user login (if no domain is specified). | gridgain.org |
| spring.activedirectory.admin-role | Optional | The name of the user group with admin permissions. | Domain Admins |

{% hint style="info" %}
If you have complex structure where users and groups should be requested by non-standard path, please use LDAP authentication instead.

The following defaults are incompatible with Active Directory and should be adjusted accordingly:

- Set the `spring.ldap.bind-authenticator.enabled` property to `true`
- Set the `spring.ldap.user-details.user-search-filter` to `(&(samaccountname={0}))`
{% endhint %}

### LDAP

To enable LDAP authentication, use the following parameters:

| Parameter | Required | Description | Example |
|---|---|---|---|
| spring.ldap.urls | Required | LDAP URLs of the server, including schema (ldap:// or ldaps://) and port, separated by comma. | ldap://localhost:389,ldap://localhost:8389 |
| spring.ldap.base | Required | Base Distinguished Name appended to group and user search requests. | dc=gridgain,dc=org |
| spring.ldap.password-comparison-authenticator.password-attribute-name | Optional | Name of the field where the password is stored. | By default, “userPassword” |
| spring.ldap.password-comparison-authenticator.user-dn-patterns | Optional | Sets the pattern that is used to supply a Distinguished Name for the user. The pattern argument {0} contains the username. | spring.ldap.password-comparison-authenticator.userDnPatterns[0]="uid={0},ou=people" |
| spring.ldap.bind-authenticator.enabled | Optional | Enables authenticator, which uses BIND operation to authenticate user. | By default, “false” |
| spring.ldap.username | Optional | The Distinguished Name for the user if you need to use special credentials to locate users/groups information | By default, not specified |
| spring.ldap.password | Optional | The user's password from `spring.ldap.username` | By default, not specified |
| spring.ldap.user-details.group-search-base | Optional | The Distinguished Name under which groups are stored. | ou=groups |
| spring.ldap.user-details.group-role-attribute | Optional | The ID of the attribute that contains the role name for a group. | By default, “cn” |
| spring.ldap.user-details.user-search-base | Optional | The Distinguished Name under which users are stored. | ou=people |
| spring.ldap.user-details.user-search-filter | Optional | The filter expression used in the user search. This is an LDAP search filter (as defined in 'RFC 2254') with optional arguments. | uid={0} |
| spring.ldap.admin-role | Optional | The name of the user group with admin permissions. | By default, “admin” |
| spring.ldap.user-details.group-member-attribute-name | Optional | Name of the multi-valued attribute that holds the DNs of users who are members of a group. | By default, “uniquemember” |

{% hint style="info" %}
By default, Control Center uses password comparison authenticator. To use BIND operation instead, set the `spring.ldap.bind-authenticator.enabled` property to `true`.

If `spring.ldap.admin-role` or spring.ldap.user-details.group-member-attribute-name are misconfigured, all users will be treated as regular user in Control Center.
{% endhint %}

### Logging of LDAP or Active Directory requests

To enable logging of request update following lines in `log4j2-loggers.xml`

```xml
<Logger name="org.springframework.ldap" level="TRACE"/>
<Logger name="org.springframework.security.ldap" level="TRACE"/>

<Root level="TRACE">
    <AppenderRef ref="CONSOLE"/>
    <AppenderRef ref="CONSOLE_ERR"/>
    <AppenderRef ref="FILE"/>
</Root>
```

## OpenID Configuration

You can set up the OpenID authentication as described in the [Connecting to OpenID provider](open-id.md) section. To enable OpenID authentication, use the following parameters (replace `{name}` with your provider name):

| Parameter | Required | Description |
|---|---|---|
| `spring.security.oauth2.client.provider.{name}` | Required | OpenID provider name. Can be anything, but must be consistent with `spring.security.oauth2.client.registration.{name}` and the name specified in redirect URI. |
| `spring.security.oauth2.client.provider.{name}.authorization-uri` | Required | The endpoint that accepts authorization request. Usually provided in the `authorization_endpoint` field of the OpenID Discovery document. |
| `spring.security.oauth2.client.provider.{name}.jwk-set-uri` | Required | The endpoint that holds public keys used to authorize users. Usually provided in the `jwks_uri` field of the OpenID Discovery document. |
| `spring.security.oauth2.client.provider.{name}.token-uri` | Required | The endpoint that receives authorization information and returns authorization token. Usually provided in the `token_endpoint` field of the OpenID Discovery document. |
| `spring.security.oauth2.client.provider.{name}.user-info-uri` | Required | User info URI for the provider. Usually provided in the `userinfo_endpoint` field of the OpenID Discovery document. This setting is required if `account.oidc.rbac.enabled` is `true`. |
| `spring.security.oauth2.client.registration.{name}` | Required | OpenID provider name. Can be anything, but must be consistent with `spring.security.oauth2.client.provider.{name}` and the name specified in redirect URI. |
| `spring.security.oauth2.client.registration.{name}.client-id` | Required | Client ID for Control Center. Provided when you set up OpenID credentials. |
| `spring.security.oauth2.client.registration.{name}.client-secret` | Required | Client secret for Control Center. Provided when you set up OpenID credentials. |

## GridGain 9 Connector Configuration

To enable and configure the GridGain 9 connector, which is required to for GridGain 9 clusters, use the following parameters:

| Parameter | Default | Description |
|---|---|---|
| connector.enabled | true | Enables GridGain 9 connector, which is required to support GridGain 9 monitoring capabilities. |
| connector.embedded.port | Control Center searches for an available port starting from 3100 | The port used for internal communications between Control Center and the GridGain 9 connector. |
| connector.cluster.monitoring.heartbeat-max-retry-attempt | 0 | Maximum failed heartbeat attempts before cluster is considered disconnected. The default of 0 means that any heartbeat failure leads to cluster disconnect. |
| connector.cluster.monitoring.heartbeat-interval | 1000 | The interval between the GridGain 9 cluster's heartbeats, in milliseconds. |
| connector.cluster.monitoring.timeout | 2000 | The monitoring cycle timeout in milliseconds. |
| connector.cluster.monitoring.interval | 2000 | The interval between monitoring cycles in milliseconds. |
| connector.sql.execute-timeout | 1 | The timeout of SQL script execution in hours. |
| connector.sql.query-timeout | 1 | The timeout of SQL query execution in 1 hours. |
| connector.sql.fetch-timeout | 10 | The timeout of cursor fetch execution in minutes. |
| connector.sql.cursor-timeout | 1 | The cursor lifetime duration in hours. If cursor in not fetched within this period, it is closed. |
