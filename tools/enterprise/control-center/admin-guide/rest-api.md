---
description: >-
  The GridGain Control Center REST API for user management, cluster attachment,
  alerting configuration, and health monitoring.
---

# REST API

Control Center provides a REST API for programmatic access to its functionality. The API enables automation of common tasks including user management, cluster attachment, alerting configuration, and health monitoring.

## API Overview

The REST API includes endpoints for:

- **Authentication** - Login and JWT token management
- **Users** - Create, update, and manage user accounts
- **Teams** - Create teams and manage team membership
- **Clusters** - Attach clusters and configure sharing
- **Notifications** - Configure email, SMS, webhook, and in-app notification channels
- **Alerts** - Set up metric-based alert configurations
- **Health** - Retrieve cluster health reports
- **License** - Upload and manage licenses
- **Connector** - Get the list of connectors for the current user

For the complete API specification, see the OpenAPI documentation.

To learn how to use the REST API for fully automated Control Center deployment, see [Automated Deployment](automated-deployment.md).

## Authentication

{% hint style="danger" %}
These examples use plain-text credentials on the command line for simplicity. In production, manage credentials using secure mechanisms such as secrets managers, environment variables, or encrypted vaults. Do not store credentials in plain text or embed them directly in commands.
{% endhint %}

- Authenticate requests using HTTP Basic Authentication with your Control Center credentials (email and password):

  ```bash
  curl -u "username@example.com:password" \
    "https://<control-center-url:port>/rest/v1/..." \
    -H "Accept: application/json"
  ```
- Alternatively, obtain a JWT token by calling the login endpoint:

  ```bash
  curl -X POST \
    "https://<control-center-url:port>/rest/v1/authentication/login" \
    -H "Content-Type: application/json" \
    -d '{"username": "username@example.com", "password": "password"}'
  ```

  Then use the token in subsequent requests:

  ```bash
  curl -H "Authorization: Bearer <jwt-token>" \
    "https://<control-center-url:port>/rest/v1/..." \
    -H "Accept: application/json"
  ```

## Get Cluster Health Reports

Authenticate with your Control Center credentials (email and password) and specify the `connectionId` in the request.

```
GET /rest/v1/clusters/{connectionId}/health
```

![Connection id GridGain 9 and GridGain 8](../../../.gitbook/assets/cc-gg9-connection-id.png)

The endpoint returns the cluster health report in JSON format.

Example request:

```bash
curl -v \
  -u "username@example.com:password" \
  "https://<control-center-url:port>/rest/v1/clusters/<connectionId>/health" \
  -H "Accept: application/json"
```

Example response:

```json
{
  "status": "GOOD",
  "reports": [
    {
      "reportName": "OfflineCmgNodes",
      "description": null,
      "status": "GOOD"
    },
    {
      "reportName": "OfflineMgNodes",
      "description": null,
      "status": "GOOD"
    },
    {
      "reportName": "Alerts",
      "description": null,
      "status": "GOOD"
    },
    {
      "reportName": "PartitionLoss",
      "description": null,
      "status": "GOOD"
    }
  ]
}
```

You can also view a specific report by passing `reportName` property to the endpoint:

```
/rest/v1/clusters/{connectionId}/health/{reportName}
```

Example response:

```json
{
   "reportName": "PartitionLoss",
   "description": null,
   "status": "GOOD"
}
```

## Send In-App Notifications

You can send a notification to the **Notifications** panel of Control Center users without configuring an alert. Only administrators can use this endpoint. If another user sends the request, it fails with the `403` status.

```bash
POST /rest/v1/notifications
```

| Parameter | Description |
|---|---|
| title | Required. The title of the notification. |
| message | Required. The text of the notification. |
| targetUrl | Required. A valid URL. When a user clicks the notification, the URL opens in a new browser tab, and the notification is marked as read. |
| username | The email address of the user who receives the notification. |
| connectionId | The ID of a cluster connection. The notification is associated with the cluster, and the cluster tag is displayed in the notification. |
| broadcast | Set to `true` to send the notification to all users. The default value is `false`. When it is `true`, do not set `username` or `connectionId`. |

The recipients depend on the parameters that you set:

- `username` - only the specified user.
- `connectionId` without `username` - all users who have access to the cluster.
- `broadcast` set to `true` - all users.

You must set at least one of `username`, `connectionId`, or `broadcast`. Otherwise, the request fails with the `400` status. If the specified `username` does not exist, the request fails with the `404` status.

Example request:

```bash
curl -X POST \
  -u "admin@example.com:password" \
  "https://<control-center-url:port>/rest/v1/notifications" \
  -H "Content-Type: application/json" \
  -d '{"connectionId": "<connectionId>", "username": "operator@example.com", "title": "Maintenance window", "message": "The cluster restarts at 22:00.", "targetUrl": "https://example.com/maintenance"}'
```

Example response:

```json
{
  "notificationId": "ed5e4954-fd49-404f-9f55-f70a1b47b177",
  "createdNotificationCount": 1
}
```

`createdNotificationCount` is the number of users who received the notification. A successful request returns the `201` status.

To delete a notification, send a `DELETE` request to `/rest/v1/notifications/<notificationId>`. A successful request returns the `204` status.
