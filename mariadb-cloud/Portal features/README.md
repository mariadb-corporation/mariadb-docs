# Portal features

From the SkySQL Portal, you can launch, monitor, and manage your SkySQL services.

## Access the Portal

You can access the Portal [here](https://app.skysql.com/dashboard)

## Dashboard

[![dashboard](dashboard.png)](dashboard.png)


From the Dashboard, you can see a list of your SkySQL services and status information for each service.

From a different view, the Dashboard can be accessed by clicking the "Dashboard" link in the main menu (left navigation in the Portal).

## Launch

To launch a new service, click the "+ Launch New Service" button on the Dashboard.

See "[Service Launch](<./Launch page.md>)" for details on the service launch process and launch-time selections.

## Service-Specific Interfaces

Service-specific interfaces are available from the Dashboard by clicking on the service name for the desired service.

Service-specific interfaces will vary by topology.

Service-specific interfaces are provided to:

- [Connect](<../Connecting to Sky DBs/>)
- [Manage](<./Manage your Service.md>)
- [Monitor](<./Service Monitoring Panels.md>)
- [Service Details](<./Service Details page.md>)
- Alerts
- Logs

## Connect

From the Dashboard, the details needed to connect to your SkySQL service can be seen by clicking on the "CONNECT" button for the desired service.

See "[Client Connections](<../Connecting to Sky DBs/>)" for details on how to connect to a service.

## Manage

From the Dashboard, the "MANAGE" button for a service provides access to:

- [Self-Service Operations](<./Manage your Service.md>) to stop/start, delete, or scale your service
- [Security access](<../Security/Configuring Firewall.md>) to manage the firewall
- [Autonomous](<../Autonomously scale Compute, Storage/>) settings for auto-scale of nodes and auto-scale of storage
- [Apply custom configuration](../config/)

## Billing

The Dashboard includes a Spending gauge to indicate current charges. More detailed billing information can be accessed by clicking on the Spending gauge.

Alternatively, you can access detailed billing and invoice information by clicking on your name in the upper-right corner of the interface, then select "Billing" from the menu.

See "[Billing](<./Billing.md>)" for additional details.

## Monitoring

The Dashboard includes monitoring gauges for Current SQL Commands, CPU Load, and QPS (Queries Per Second). More detailed monitoring can be accessed by clicking on one of these gauges.

Alternatively, you can access detailed server and service monitoring by clicking on the service name from the Dashboard, then accessing the Monitoring tab (the default view).

See "[Monitoring](<./Service Monitoring Panels.md>)" for additional details.

## Alerts

The Dashboard includes the count of active monitoring alerts for your service. More detailed alert information can be accessed by clicking on the Alerts gauge.

Alternatively, you can access monitoring alerts by clicking the "Alerts" link in the main menu (left navigation in the Portal).

## Logs

Server log files can be accessed by clicking the "Logs" link in the main menu (left navigation in the Portal).

## Settings

These settings can be accessed by clicking the "Settings" link in the main menu (left navigation in the Portal):

- [User Management](<../Security/Managing Portal Users.md>)
- [Configuration Manager](../config/)
- [Firewall](<../Security/Configuring Firewall.md>)
- [Notification Channels](<../Portal features/Notifications.md>) for delivery of monitoring alerts by email
- Policies for monitoring alerts

## Notifications

Actions performed through the Portal will generate a notification.

To view current notifications, click the bell icon in the upper-right corner of the interface.

See "[Notifications](<../Portal features/Notifications.md>)" for additional details.

## User Preferences

To customize your email notification preferences, click your name in the upper-right corner of the interface, then choose "User preferences".

See "[Notifications](<../Portal features/Notifications.md>)" for additional details.

## Logout

To log out from SkySQL, click your name in the upper-right corner of the interface, then choose "Logout" from the menu.
