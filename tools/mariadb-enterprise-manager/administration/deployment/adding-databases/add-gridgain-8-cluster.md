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

<!-- DOCS-6280 TODO: link the Control Center installation and OpenID Connect pages once the Control Center docs are published in this space. -->

* Enterprise Manager 26.10 or later.
* GridGain Control Center 2026.2 or later, installed on its own host, with your GridGain 8 clusters attached to it. For installation steps, see the GridGain Control Center installation documentation.
* Control Center configured to use Enterprise Manager as its OpenID Connect provider, with the client secret you enter as the **SSO client secret** below.

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
| **Control Center URL**                 | Required. The URL at which you open the Control Center UI in a browser: `https://<cc-host>:8008` for a Docker or Kubernetes installation, or `https://<cc-host>:3000` for a binary installation. The URL must start with `http://` or `https://` and must not contain a user name or password. Enterprise Manager shows this URL to every user in Control Center links, so a URL such as `https://user:password@cc-host:8008` is rejected. |
| **SSO client secret**                  | The secret Control Center uses to authenticate to Enterprise Manager for single sign-on. Enter the same value that is set in Control Center as `spring.security.oauth2.client.registration.em.client-secret`. The field is always empty when the page loads. To keep the stored secret, leave it empty.                                                                                        |
| **Control Center CA certificate path** | The path on the Enterprise Manager host to the CA certificate (PEM) that signed Control Center's TLS certificate, for example `/certs/cc-ca.pem`. Required when Control Center uses a self-signed certificate or a certificate from a private CA. If you leave it empty, Enterprise Manager uses the host's default trust store.                                                               |
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

If the indicator is red, check the **Control Center URL**, the CA certificate, and the **SSO client secret**. The Enterprise Manager backend log contains the details of the failure.

When the connection works, the **Databases** list shows a **Control Center** indicator in its header that links to Control Center. Each GridGain 8 cluster appears as a row of type **GridGain Cluster**, with its nodes listed as **Server** and **Client** rows.

## Open a Cluster in Control Center

In the **Databases** list, click the three-dot menu (⋮) next to a GridGain 8 cluster and select **Manage GridGain**. Control Center opens the cluster's dashboard, and you are signed in with your Enterprise Manager account. You don't need a separate Control Center login.

Your Control Center access level follows your Enterprise Manager role. Only the built-in `admin` role gets Control Center administrator access. Every other role, including a custom role with full permissions, gets regular access.

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
4. If Enterprise Manager uses a self-signed certificate or a certificate from a private CA, add that certificate to the trust store of every node. The Enterprise Manager receiver accepts only TLS connections.
5. Restart the nodes. For the full procedure, select **View setup instructions** in the dialog.

When metrics arrive, the **Uptime** and **Last metric age** columns fill in for the cluster's nodes, and the **View monitoring dashboard** action opens the [GridGain 8 dashboards](../../../usage/monitoring/dashboards/).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
