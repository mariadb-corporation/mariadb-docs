# Alerts and Notifications

MariaDB Enterprise Manager provides a powerful and flexible alerting system, built on the capabilities of the integrated **Grafana Alerting** engine. It allows you to proactively monitor your entire database fleet, define custom rules for potential issues, and receive notifications through various channels to ensure you can respond quickly.

### How It Works: The Alerting Flow

The alerting process in MariaDB Enterprise Manager follows a clear, four-step flow from detection to notification.

{% stepper %}
{% step %}
#### Alert Rule is Defined

An alert rule contains a query (what to measure, e.g., disk usage), a condition (the threshold, e.g., `> 90%`), and labels for routing (e.g., `type = server disk`).
{% endstep %}

{% step %}
#### Instances are Evaluated

Grafana periodically runs the query against your monitored targets. It creates an **Alert Instance** for each distinct entity (e.g., one for Server 01, one for Server 02, etc.).
{% endstep %}

{% step %}
#### An Instance "Fires"

If the condition is met for a specific instance (e.g., Server 01's disk usage is over 90%), that instance enters a "firing" state.
{% endstep %}

{% step %}
#### Notifications are Sent

The firing alert is routed through a **Notification Policy**. The policy matches the alert's labels (e.g., `type = server disk`) and sends a notification to the configured **Contact Point** (such as Email, Slack, or PagerDuty).
{% endstep %}
{% endstepper %}

### Key Alerting Concepts

To configure alerting effectively, it's helpful to understand these core concepts from Grafana:

| Term                          | Description                                                                                                                                                                             |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Alert Rules**               | The combination of a data query and a threshold condition defining what to measure and when it's a problem.                                                                             |
| **Alert Instances**           | Generated from an alert rule for each monitored entity, showing individual statuses.                                                                                                    |
| **Contact Points**            | Destinations for notifications, such as email, Slack, PagerDuty, or webhooks.                                                                                                           |
| **Notification Policies**     | Uses labels to route alerts to contact points, facilitating team-specific alerting.                                                                                                     |
| **Silences and Mute Timings** | Allow temporary notification pauses without halting alerts. Silences cover single events, like maintenance, while Mute Timings are for recurring periods, such as at night or weekends. |

{% hint style="info" %}
For a deep dive into advanced topics like custom message templating, alert grouping, and more complex routing, see the [official Grafana documentation](https://grafana.com/docs/grafana/latest/alerting/fundamentals/).
{% endhint %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
