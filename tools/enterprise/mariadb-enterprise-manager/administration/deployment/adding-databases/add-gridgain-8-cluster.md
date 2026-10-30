---
description: >-
  Connect Enterprise Manager to GridGain Control Center to show GridGain 8
  clusters in the Databases list, open them in Control Center with single
  sign-on, and send their metrics to Enterprise Manager.
hidden: true
---

# Add a GridGain 8 Cluster

You don't add GridGain 8 clusters to MariaDB Enterprise Manager one at a time. Enterprise Manager reads the clusters that GridGain Control Center already monitors. Connect Enterprise Manager to Control Center once, and every GridGain 8 cluster attached to Control Center appears in the **Databases** list.

GridGain 8 clusters are view-only in Enterprise Manager. To manage a cluster, open it in Control Center from the **Databases** list.

## Requirements

<!-- DOCS-6280 TODO: link the Control Center installation page once the Control Center docs are published in this space. -->

* Enterprise Manager 26.10 or later.
* GridGain Control Center 2026.2 or later, installed on its own host, with your GridGain 8 clusters attached to it. For installation steps, see the GridGain Control Center installation documentation.
* Control Center configured to use Enterprise Manager as its OpenID Connect provider, with the client secret you enter as the **SSO client secret** below. For the Control Center settings, see [Enterprise Manager Integration](../../../../control-center/admin-guide/enterprise-manager-integration.md).

## Connect Enterprise Manager to Control Center

{% stepper %}
{% step %}
**Open the Control Center settings**

1. Log in to the Enterprise Manager web interface as a user with the `admin` role.
2. Go to **Settings** and open **Control Center**.
{% endstep %}

{% step %}
**Enter the connection details**

| Field                                  | Description                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Control Center URL**                 | Required. The URL at which you open the Control Center UI in a browser. For a Docker or Kubernetes installation, that is `https://<cc-host>:8443` when the Control Center frontend has a TLS certificate, or `http://<cc-host>:8008` without one. For a binary installation, it is port `3000`, for example `https://<cc-host>:3000`. The URL must start with `http://` or `https://` and must not contain a user name or password. Enterprise Manager shows this URL to every user in Control Center links, so a URL such as `https://user:password@cc-host:8008` is rejected. |
| **SSO client secret**                  | The secret Control Center uses to authenticate to Enterprise Manager for single sign-on. Enter the same value that is set in Control Center as `spring.security.oauth2.client.registration.em.client-secret`. It can't contain whitespace, `+`, `/`, `=`, or `%`. The field is always empty when the page loads. To keep the stored secret, leave it empty. See [The SSO Client Secret](#the-sso-client-secret). |
| **Control Center CA certificate path** | The path, as Enterprise Manager sees it, to the CA certificate (PEM) that signed Control Center's TLS certificate. Place the file in the `certs` folder of the Enterprise Manager installation and enter its path under `/certs`, for example `/certs/cc-ca.pem`. Required when Control Center's certificate comes from a private CA, including a self-signed certificate. If you leave it empty, Enterprise Manager trusts only certificates from public CAs. |
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

If Control Center is reachable but no GridGain 8 clusters appear, Control Center can't verify the tokens Enterprise Manager sends, usually because it doesn't trust Enterprise Manager's certificate. See [Enterprise Manager Integration](../../../../control-center/admin-guide/enterprise-manager-integration.md).

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

For the Control Center settings, including the setup where Control Center signs in through the identity provider directly, see [Enterprise Manager Integration](../../../../control-center/admin-guide/enterprise-manager-integration.md).

## Send Cluster Metrics to Enterprise Manager

The GridGain 8 dashboards and alert rules in Enterprise Manager need metrics from the cluster. GridGain 8 nodes push their metrics to Enterprise Manager through the OpenTelemetry metric exporter, which you configure on every node of the cluster.

<!-- DOCS-6280 TODO: link the GridGain 8 metric exporter setup page once its location is confirmed. -->

1. In the **Databases** list, click the three-dot menu (⋮) next to the GridGain 8 cluster and select **Metrics configuration**. You need the `admin` role.
2. Copy the three values the dialog shows:

   | Property           | Value                                                          |
   | ------------------ | -------------------------------------------------------------- |
   | `endpoint`         | The Enterprise Manager address on port `4318`, for example `https://em.example.com:4318` |
   | `serviceNamespace` | `gridgain`                                                     |
   | `serviceName`      | The cluster name                                               |
3. Set these properties on the `OpenTelemetryMetricExporterSpi` bean in the configuration of every node. Also set `protocol` to `HTTP`: the dialog doesn't show it, the exporter uses gRPC by default, and port `4318` accepts only OTLP over HTTP. Without it, no metrics reach Enterprise Manager.
4. If Enterprise Manager's certificate comes from a private CA, which is the default, add that CA's certificate to the Java trust store of every node. By default, it is `certs/ca-cert.pem` in the Enterprise Manager installation folder. Build the trust store from a copy of the JDK's `lib/security/cacerts`, so that the nodes keep trusting public CAs. The Enterprise Manager receiver accepts only TLS connections.
5. Restart the nodes. For the full procedure, select **View setup instructions** in the dialog.

When metrics arrive, the **Uptime** and **Last metric age** columns fill in for the cluster's nodes, and the **View monitoring dashboard** action opens the [GridGain 8 dashboards](../../../usage/monitoring/dashboards/).

## How the Connections Are Secured

Enterprise Manager, Control Center, the GridGain 8 nodes, and users' browsers connect in five ways. On each connection, the caller checks the server's TLS certificate against its trust store, and the server identifies the caller by a signed token, a client secret, or a user session. Certificates play no part in identifying the caller.

| Connection                             | What travels                                                                                   | How the caller trusts the server                                                                                                                                           | How the server identifies the caller                                                                                                                                                                                                                                          |
| -------------------------------------- | ---------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Enterprise Manager → Control Center    | The GridGain 8 clusters and their nodes                                                        | Enterprise Manager checks Control Center's certificate against the CA in **Control Center CA certificate path**, or against public CAs when the field is empty.            | Enterprise Manager sends a JSON Web Token (JWT) that it signs with its private key and that is valid for 5 minutes. Control Center checks it with Enterprise Manager's public keys. No password is involved. Control Center serves the clusters to the account `em-service-user@controlcenter.local`, which it creates at startup. |
| Control Center → Enterprise Manager    | Enterprise Manager's public keys and, at sign-in, the user's email and role in an ID token signed by Enterprise Manager | Control Center checks Enterprise Manager's certificate against its Java trust store. See [Enterprise Manager Integration](../../../../control-center/admin-guide/enterprise-manager-integration.md). | To get the ID token, Control Center signs in to Enterprise Manager as `cc_sso_service_account` with the **SSO client secret**. Reading the public keys needs no sign-in.                                                                                                     |
| Browser → Enterprise Manager and Control Center | The two web interfaces and the **Manage GridGain** sign-in redirects                    | The browser checks each certificate against its own trust store or the operating system's.                                                                                | The user's Enterprise Manager session. Control Center starts its own session after the sign-in.                                                                                                                                                                              |
| GridGain 8 nodes → Enterprise Manager, port `4318` | Metrics                                                                            | Each node checks Enterprise Manager's certificate against its Java trust store.                                                                                            | The receiver accepts metrics from any client that connects over TLS.                                                                                                                                                                                                          |
| Control Center agent → Control Center  | Cluster topology                                                                               | Not changed by the integration.                                                                                                                                            | Not changed by the integration.                                                                                                                                                                                                                                               |

### Certificates

Enterprise Manager and Control Center each have a TLS certificate signed by a certificate authority (CA). A caller trusts a certificate when it trusts the CA that signed it:

* **Public CA:** every caller already trusts it. There is nothing to set up.
* **Private CA:** each caller must add the CA's certificate to its trust store.

The Enterprise Manager installer creates a private CA, `certs/ca-cert.pem` in the installation folder, and signs Enterprise Manager's certificate with it. With that default, add `certs/ca-cert.pem` to the trust store of Control Center and of every GridGain 8 node. If Control Center's certificate also comes from a private CA, set **Control Center CA certificate path** to that CA's certificate.

### The SSO Client Secret

The SSO client secret is the password of an Enterprise Manager service user. When an admin saves it under **Settings** › **Control Center**, Enterprise Manager creates the user `cc_sso_service_account` with the `basic` role, or changes the password of the existing user, and stores only a hash of the secret. Control Center signs in as this user when it completes a **Manage GridGain** sign-in.

If the secret in Enterprise Manager and in Control Center differ, **Manage GridGain** can't sign users in to Control Center. The secret can't contain whitespace, `+`, `/`, `=`, or `%`: Enterprise Manager rejects them when you save.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
