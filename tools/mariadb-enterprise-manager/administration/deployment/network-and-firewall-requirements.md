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

{% hint style="info" %}
All ports listed are TCP. Ensure your firewall rules explicitly allow TCP traffic for the specified ports.
{% endhint %}

### Summary of Required Firewall Rules

For the current version of MariaDB Enterprise Manager, ensure the following rules are in place:

* From user workstations, allow traffic to the Enterprise Manager Server on TCP port `8090`.
* From agent hosts, allow traffic to the Enterprise Manager Server on TCP port `4318`.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
