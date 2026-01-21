---
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
  metadata:
    visible: true
---

# MariaDB Cloud UI Portal

The MariaDB Cloud Portal provides a unified management interface to launch, manage, and monitor your MariaDB Cloud services.

## Access the Portal

The Portal offers an intuitive dashboard, real-time performance metrics, and seamless access to various administrative tools. You can access the Portal [here](https://app.skysql.com/dashboard). After signing in, you will be taken directly to the main dashboard, where you can view various features such as health indicators, performance charts, alerts, logs, configuration options, etc.&#x20;

## Dashboard

<figure><img src="../.gitbook/assets/dashboard.png" alt=""><figcaption></figcaption></figure>

From the Dashboard, you can see a list of your MariaDB Cloud services and status information for each service.

## Launch

To launch a new service, click the "+ Launch New Service" button on the Dashboard.

See "[Service Launch](launch-page.md)" for details on the service launch process and launch-time selections.

## Service-Specific Interfaces

Service-specific interfaces are available from the Dashboard by clicking on the service name for the desired service. Service-specific interfaces will vary by topology.

Service-specific interfaces are provided to:

* [Connect](../connecting-to-mariadb-cloud-dbs/)
* [Manage](manage-your-service.md)
* [Monitor](service-monitoring-panels.md)
* [Service Details](service-details-page.md)
* Alerts
* Logs

## Connect

From the Dashboard, the details needed to connect to your MariaDB Cloud service can be seen by clicking on the "CONNECT" button for the desired service.

See "[Client Connections](../connecting-to-mariadb-cloud-dbs/)" for details on how to connect to a service.

## Manage

From the Dashboard, the "MANAGE" button for a service provides access to:

* [Self-Service Operations](manage-your-service.md) to stop/start, delete, or scale your service
* [Security access](../security/configuring-firewall.md) to manage the firewall
* [Autonomous](../cloud-management/autonomously-scale-compute-storage.md) settings for auto-scale of nodes and auto-scale of storage
* [Apply custom configuration](../cloud-management/config/)

## Billing

The Dashboard includes a Spending gauge to indicate current charges. More detailed billing information can be accessed by clicking on the Spending gauge.

Alternatively, you can access detailed billing and invoice information by clicking on your name in the upper-right corner of the interface, then selecting "Billing" from the menu.

See "[Billing](billing.md)" for additional details.

## Monitoring

The Dashboard includes monitoring gauges for Current SQL Commands, CPU Load, and QPS (Queries Per Second). More detailed monitoring can be accessed by clicking on one of these gauges.

Alternatively, you can access detailed server and service monitoring by clicking on the service name from the Dashboard, then accessing the Monitoring tab (the default view).

See "[Monitoring](service-monitoring-panels.md)" for additional details.

## Alerts

The Dashboard includes the count of active monitoring alerts for your service. More detailed alert information can be accessed by clicking on the Alerts gauge.

Alternatively, you can access monitoring alerts by clicking the "Alerts" link in the main menu (left navigation in the Portal).

## Logs

Server log files can be accessed by clicking the "Logs" link in the main menu (left navigation in the Portal).

## Settings

The Settings page allows you to access administrative and organizational configuration options for your MariaDB Cloud account. You can access the page by clicking the "Settings" link in the main menu (left navigation in the Portal). \
Once you click the Settings link, the following options appear:

* Organization
* [User Management](../security/managing-portal-users.md)
* [Secure Access (Firewall)](../security/configuring-firewall.md)
* [Configuration Manager](../cloud-management/config/)
* Policies for monitoring alerts
* [Notification Channels](notifications.md) for the delivery of monitoring alerts by email

## Notifications

The Portal generates notifications whenever specific actions are performed. To view current notifications, click the bell icon in the upper-right corner of the interface.

See "[Notifications](notifications.md)" for additional details.

## User Preferences

To customize your email notification preferences, click your name in the upper-right corner of the interface, then choose "Account Settings".

See "[Notifications](notifications.md)" for additional details.

## Logout

To log out from MariaDB Cloud, click your name in the upper-right corner of the interface, then choose "Logout" from the menu.
