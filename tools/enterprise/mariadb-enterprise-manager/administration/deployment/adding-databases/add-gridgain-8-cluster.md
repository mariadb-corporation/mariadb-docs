---
description: >-
  Connect Enterprise Manager to GridGain Control Center to show GridGain 8
  clusters in the Databases list, open them in Control Center with single
  sign-on, and send their metrics to Enterprise Manager.
---

# Add a GridGain 8 Cluster

You don't add GridGain 8 clusters to MariaDB Enterprise Manager one at a time. Enterprise Manager reads the clusters that GridGain Control Center already monitors. Connect Enterprise Manager to Control Center once, and every GridGain 8 cluster attached to Control Center appears in the **Databases** list.

GridGain 8 clusters are view-only in Enterprise Manager. To manage a cluster, open it in Control Center from the **Databases** list.

## Prerequisites

* Enterprise Manager and Control Center are installed and reachable from each other and from users' browsers.
* Enterprise Manager 26.10 or later.
* GridGain Control Center 2026.2 or later, installed on its own host, with your GridGain 8 clusters attached to it. For installation steps, see the GridGain Control Center installation documentation.
* You can sign in to Enterprise Manager as `admin` and edit Control Center's `application.properties`.
* You have Enterprise Manager's CA certificate, `certs/ca-cert.pem` in the Enterprise Manager install directory. Skip this if Enterprise Manager uses a certificate from a public CA.

## Step 1: Configure Control Center

{% stepper %}
{% step %}
**Choose an SSO client secret**

Any string without spaces, `+`, `/`, `=` or `%`. You enter the same value in Enterprise Manager in Step 2.
{% endstep %}

{% step %}
**Add the integration settings**

Add these lines to Control Center's `application.properties`. Replace `<enterprise-manager-host>` with Enterprise Manager's address and `<control-center-url>` with the address users open Control Center at (`https://<control-center-host>:8008` for Docker or Kubernetes, `https://<control-center-host>:3000` for a binary install).

```properties
control.base-url=<control-center-url>

spring.security.oauth2.client.registration.em.provider=em
spring.security.oauth2.client.registration.em.client-id=cc_sso_service_account
spring.security.oauth2.client.registration.em.client-secret=<sso-client-secret>

spring.security.oauth2.client.provider.em.authorization-uri=https://<enterprise-manager-host>/authorize
spring.security.oauth2.client.provider.em.token-uri=https://<enterprise-manager-host>/token
spring.security.oauth2.client.provider.em.jwk-set-uri=https://<enterprise-manager-host>/jwks

account.oidc.rbac.enabled=true
account.oidc.skip-sign-up=true
account.global-team.enabled=true
account.global-team.attach-cluster=true
```

| Property                                                      | What it does                                                                                          |
| ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `control.base-url`                                            | Address users open Control Center at. Same value as the **Control Center URL** in Enterprise Manager. |
| `spring.security.oauth2.client.registration.em.provider`      | Links the `em` sign-in option to the Enterprise Manager endpoints below.                              |
| `spring.security.oauth2.client.registration.em.client-id`     | Account Control Center uses to sign in to Enterprise Manager. Fixed value.                            |
| `spring.security.oauth2.client.registration.em.client-secret` | Password for that account. Same value as the **SSO client secret** in Enterprise Manager.             |
| `spring.security.oauth2.client.provider.em.authorization-uri` | Enterprise Manager page where users sign in.                                                          |
| `spring.security.oauth2.client.provider.em.token-uri`         | Enterprise Manager endpoint that returns the signed-in user's email and role.                         |
| `spring.security.oauth2.client.provider.em.jwk-set-uri`       | Enterprise Manager's public keys, used to check requests from Enterprise Manager.                     |
| `account.oidc.rbac.enabled`                                   | Gives Enterprise Manager admins admin access in Control Center; other roles get regular access.       |
| `account.oidc.skip-sign-up`                                   | Creates the Control Center account automatically on first sign-in, without a sign-up form.            |
| `account.global-team.enabled`                                 | Lets all users see all clusters.                                                                      |
| `account.global-team.attach-cluster`                          | Adds every newly connected cluster to that shared view automatically.                                 |

Save the file with LF line endings. Do not add `issuer-uri` or `user-info-uri` for the `em` provider.
{% endstep %}

{% step %}
**Trust Enterprise Manager's certificate**

Import Enterprise Manager's CA certificate into Control Center's Java trust store. Skip this if Enterprise Manager uses a public-CA certificate.
{% endstep %}
{% endstepper %}

## Step 2: Connect Enterprise Manager to Control Center

{% stepper %}
{% step %}
**Open the Control Center settings**

1. Log in to the Enterprise Manager web interface as a user with the `admin` role.
2. Go to **Settings** and open **Control Center**.
{% endstep %}

{% step %}
**Enter the connection details**

| Field                                  | Description                                                                                                                                                     |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Control Center URL**                 | The same value as `control.base-url` in Step 1, e.g. `https://<control-center-host>:8008`. No username or password in the URL.                                  |
| **SSO client secret**                  | The same secret as in Step 1.                                                                                                                                   |
| **Control Center CA certificate path** | Path on the Enterprise Manager host to the CA certificate that signed Control Center's certificate. Leave empty if Control Center uses a public-CA certificate. |
{% endstep %}

{% step %}
**Save the settings**

Save the form. Enterprise Manager confirms with the message "Control Center settings updated".
{% endstep %}
{% endstepper %}

## Check the Connection

A status indicator next to the **Control Center** page title shows whether Enterprise Manager can reach Control Center:

| Indicator | Tooltip                                             |
| --------- | --------------------------------------------------- |
| Green     | Control Center is reachable                         |
| Red       | Control Center is not reachable                     |
| Grey      | Control Center connectivity has not been determined |

Enterprise Manager checks the connection continuously, so a corrected URL or certificate, or a Control Center restart, shows up within a few seconds.

If the indicator is red, check the **Control Center URL** and the CA certificate. The Enterprise Manager backend log contains the details of the failure.

If Control Center is reachable but no GridGain 8 clusters appear, Control Center can't verify the tokens Enterprise Manager sends, usually because it doesn't trust Enterprise Manager's certificate.&#x20;

If **Manage GridGain** doesn't sign you in to Control Center, check that the **SSO client secret** is the same in Enterprise Manager and Control Center.

When the connection works, the **Databases** list shows a **Control Center** indicator in its header that links to Control Center. Each GridGain 8 cluster appears as a row of type **GridGain Cluster**, with its nodes listed as **Server** and **Client** rows.

## Open a Cluster in Control Center

In the **Databases** list, click the three-dot menu (⋮) next to a GridGain 8 cluster and select **Manage GridGain**. Control Center opens the cluster's dashboard, and you are signed in with your Enterprise Manager account. You don't need a separate Control Center login.

Your Control Center access level follows your Enterprise Manager role. Only the built-in `admin` role gets Control Center administrator access. Every other role, including a custom role with full permissions, gets regular access.

## Use a Shared Identity Provider

Enterprise Manager and Control Center can both sign users in through the same external OpenID Connect identity provider, so users sign in with their corporate identities. **Manage GridGain** single sign-on still works in this setup:

1. Configure Enterprise Manager to use the identity provider. See [Configure OpenID Connect Identity Provider](../../user-management/configure-openid-connect-identity-provider.md). Enterprise Manager uses the provider's `email` claim as the username and its `account` claim as the role.
2. Keep Control Center configured to use Enterprise Manager as its OpenID Connect provider. When a user selects **Manage GridGain**, Control Center signs them in through Enterprise Manager, which signs them in through the identity provider without another prompt.
3. Optionally, register the same identity provider in Control Center as well, so that users can also sign in to Control Center directly. A user reaches the same Control Center account either way, matched by email.

## Send Cluster Metrics to Enterprise Manager

The GridGain 8 dashboards and alert rules in Enterprise Manager need metrics from the cluster. GridGain 8 nodes push their metrics to Enterprise Manager through the OpenTelemetry metric exporter, which you configure on every node of the cluster.

1. In the **Databases** list, click the three-dot menu (⋮) next to the GridGain 8 cluster and select **Metrics configuration**. You need the `admin` role.
2.  Copy the three values the dialog shows:

    | Property           | Value                                                                                    |
    | ------------------ | ---------------------------------------------------------------------------------------- |
    | `endpoint`         | The Enterprise Manager address on port `4318`, for example `https://em.example.com:4318` |
    | `serviceNamespace` | `gridgain`                                                                               |
    | `serviceName`      | The cluster name                                                                         |
3. Set these properties on the `OpenTelemetryMetricExporterSpi` bean in the configuration of every node. Also set `protocol` to `HTTP`: the dialog doesn't show it, the exporter uses gRPC by default, and port `4318` accepts only OTLP over HTTP. Without it, no metrics reach Enterprise Manager.
4. If Enterprise Manager's certificate comes from a private CA, which is the default, add that CA's certificate to the Java trust store of every node. By default, it is `certs/ca-cert.pem` in the Enterprise Manager installation folder. Build the trust store from a copy of the JDK's `lib/security/cacerts`, so that the nodes keep trusting public CAs. The Enterprise Manager receiver accepts only TLS connections.
5. Restart the nodes. For the full exporter procedure, select **View setup instructions** in the dialog, or see [OpenTelemetry](https://app.gitbook.com/s/ArQLGGUSG0VzKl1t2Y53/reference/monitoring/generic-metrics#opentelemetry) in the GridGain 8 documentation.

When metrics arrive, the **Uptime** and **Last metric age** columns fill in for the cluster's nodes, and the **View monitoring dashboard** action opens the [GridGain 8 dashboards](../../../usage/monitoring/dashboards/).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
