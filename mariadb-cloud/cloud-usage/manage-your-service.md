# Manage Your Service

MariaDB Cloud's self-service management features enable authorized accounts to launch cloud databases, start and stop cloud databases, delete cloud databases, apply database configuration changes, and configure the cloud database's IP firewall.

Self-service [user management](<../Security/Managing Portal Users.md>) features enable you to define role-based access for your team to jointly manage MariaDB Cloud resources.

## Stop a Service

<figure><img src="../Portal features/stop-service.png" alt=""><figcaption></figcaption></figure>

_Stop Service_

To stop a service:

1. Log in to the [Portal](https://app.skysql.com/dashboard).
2. Click the `MANAGE` button (at right) for the desired service.
3. Choose the "Stop Service" menu item.
4. Click the "Yes, Stop this service" button to confirm this operation.

The service will be stopped. You will only be charged for storage on a stopped service.

[Notifications](notifications.md) will be generated when this operation is initiated and when the operation is performed.

## Start a Service

<figure><img src="../Portal features/start-service.png" alt=""><figcaption></figcaption></figure>

_Start Service_

To start a service:

1. Log in to the [Portal](https://app.skysql.com/dashboard).
2. Click the "MANAGE" button (at right) for the desired service.
3. Choose the "Start Service" menu item.
4. Click the "Yes, Start this service" button to confirm this operation.

The service will be started. Service start may take up to 10-15 minutes. The normal billing cycle for the service will resume.

[Notifications](notifications.md) will be generated when this operation is initiated and when the operation is performed.

## Scale Nodes In/Out

<figure><img src="../Portal features/scale-in-out.png" alt=""><figcaption></figcaption></figure>

_Service - Horizontal Scaling_

Horizontal scaling is performed by scaling nodes In (reducing node count) or Out (increasing node count).

To scale nodes horizontally:

1. Log in to the [Portal](https://app.skysql.com/dashboard).
2. Identify the service you want to scale. Services must be in a "Healthy" state to scale.
3. Click the "MANAGE" button (at right) for the desired service.
4. Choose the "Scale nodes in/out" menu item.
5. Change the node count to the desired value.
6. Optionally, you can check the "Auto-scale nodes horizontally" checkbox to enable [Autonomous](../../Autonomously%20scale%20Compute,%20Storage/) features for this service.
7. Click the "Apply Changes" button.

The service immediately goes into scaling status.

[Notifications](notifications.md) will be generated when this operation is initiated and when the operation is performed.

## Scale Nodes Up/Down

<figure><img src="../Portal features/scale-up-down.png" alt=""><figcaption></figcaption></figure>

_Service - Vertical Scaling_

Vertical scaling is performed by scaling nodes Up (increasing node size) or Down (decreasing node size).

To scale nodes vertically:

1. Log in to the [Portal](https://app.skysql.com/dashboard).
2. Identify the service you want to scale. Services must be in a "Healthy" state to scale.
3. Click the "MANAGE" button (at right) for the desired service.
4. Choose the "Scale nodes up/down" menu item.
5. Change the node count to the desired value.
6. Optionally, you can check the "Auto-scale nodes vertically" checkbox to enable [Autonomous](../../Autonomously%20scale%20Compute,%20Storage/) features for this service.
7. Click the "Apply Changes" button.

The service immediately goes into scaling status.

[Notifications](notifications.md) will be generated when this operation is initiated and when the operation is performed.

## Scale Storage

<figure><img src="../Portal features/scale-storage.png" alt=""><figcaption></figcaption></figure>

_Service - Scale Storage_

To expand block storage capacity:

1. Log in to the [Portal](ttps://app.skysql.com/dashboard).
2. Identify the service you want to scale. Services must be in a "Healthy" state to scale.
3. Click the "MANAGE" button (at right) for the desired service.
4. Choose the "Scale storage" menu item.
5. Use the slider to select the desired amount of storage.
6. Click the "Apply Changes" button.

Storage scaling is subject to a 6-hour cooldown period.

Storage upgrades are not reversible.

## Delete a Service

<figure><img src="../Portal features/delete-service.png" alt=""><figcaption></figcaption></figure>

_Service - Delete_

To delete a service:

1. Log in to the [Portal](ttps://app.skysql.com/dashboard).
2. Identify the service you want to delete.
3. Click the "MANAGE" button (at right) for that service.
4. Choose the "Delete Service" menu item.
5. Read the warning and follow the provided instructions to confirm your delete operation.
6. Click "Yes, delete".

Your service and all its data will be deleted. This operation is non-reversible.

[Notifications](notifications.md) will be generated when this operation is initiated and when the operation is performed.

## Other Self-Service Operations

* [Service Launch](launch-page.md)
* [Firewall Management](<../Security/Configuring Firewall.md>)
* [Configuration Management](../cloud-management/config/)
* Private Connections:
  * [AWS PrivateLink](../connecting-to-mariadb-cloud-dbs/using-aws-azure-gcp-private-vpc-connections/setting-up-aws-private-link.md)
  * [GCP Private Service Connect](../connecting-to-mariadb-cloud-dbs/using-aws-azure-gcp-private-vpc-connections/setting-up-gcp-private-service-connect.md)
* [User Management](<../Security/Managing Portal Users.md>)
