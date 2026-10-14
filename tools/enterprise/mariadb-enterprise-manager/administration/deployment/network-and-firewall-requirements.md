---
description: >-
  Outlines the necessary network ports and firewall configurations (such as
  ports 8090 and 4318) required for UI access and agent telemetry data
  collection.
---

# Network and Firewall Requirements

{% hint style="warning" %}
It's recommended to run MariaDB Enterprise Manager on an internal, secured network. Direct public exposure is not recommended.
{% endhint %}

Before installing MariaDB Enterprise Manager, ensure that your firewall and network rules allow traffic on all required ports. Proper connectivity is essential for the system to function correctly.

The following table details the necessary ports and their purposes.

| Service/Component             | Port   | Protocol | Traffic Direction | Purpose                                                                             |
| ----------------------------- | ------ | -------- | ----------------- | ----------------------------------------------------------------------------------- |
| **Enterprise Manager Server** | `8090` | HTTP/S   | Inbound           | **User Access**: Allows users to access the Enterprise Manager UI.                  |
| **Enterprise Manager Server** | `4318` | HTTP/S   | Inbound           | **Agent Metrics**: Receives metrics data pushed from the Enterprise Manager Agents. |
| **Enterprise Manager Agent**  | `4318` | HTTP/S   | Outbound          | **Agent Metrics**: Pushes metrics data to the Enterprise Manager Server.            |
| **Enterprise Manager Server** | `4318` | HTTP/S   | Inbound           | **GridGain 8 Metrics**: Receives metrics pushed from GridGain 8 nodes.              |
| **Enterprise Manager Server** | `8090` | HTTPS    | Inbound           | **Control Center Sign-In**: Control Center reads Enterprise Manager's key set and exchanges sign-in tokens. |
| **GridGain Control Center**   | `8008` or `3000` | HTTPS | Inbound   | **Control Center Connection**: Enterprise Manager reads the cluster list from Control Center, and users open Control Center from Enterprise Manager. Port `8008` for a Docker or Kubernetes installation, `3000` for a binary installation. |

{% hint style="info" %}
All ports listed are TCP. Ensure your firewall rules explicitly allow TCP traffic for the specified ports.
{% endhint %}

### Summary of Required Firewall Rules

For the current version of MariaDB Enterprise Manager, ensure the following rules are in place:

* From user workstations, allow traffic to the Enterprise Manager Server on TCP port `8090`.
* From agent hosts, allow traffic to the Enterprise Manager Server on TCP port `4318`.
* If you monitor GridGain 8 clusters:
  * From GridGain 8 nodes, allow traffic to the Enterprise Manager Server on TCP port `4318`.
  * From the Control Center host, allow traffic to the Enterprise Manager Server on TCP port `8090`.
  * From the Enterprise Manager Server and from user workstations, allow traffic to Control Center on TCP port `8008` (Docker or Kubernetes) or `3000` (binary installation).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
