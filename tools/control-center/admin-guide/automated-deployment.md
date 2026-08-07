---
description: >-
  Fully automated, Infrastructure-as-Code deployment of GridGain Control Center
  using its REST API, with JSON configuration files for users, teams, clusters,
  notifications, and alerts.
---

# Automated Deployment

Control Center provides a comprehensive REST API that enables fully automated, Infrastructure-as-Code (IaC) deployment and configuration. This allows you to manage Control Center resources declaratively, integrate with CI/CD pipelines, and maintain reproducible deployments following GitOps patterns.

## Overview

With automated deployment, you can programmatically manage:

- **Users** - Create and update user accounts with profiles and admin privileges
- **Teams** - Create teams and manage team membership
- **Clusters** - Attach GridGain 9 or Apache Ignite 3 clusters and configure sharing with teams or users
- **Notification Channels** - Set up EMAIL, SMS, and WEBHOOK notification endpoints
- **Alert Configurations** - Define metric-based alerts with thresholds and notification routing

This approach enables you to:

- Define your desired Control Center state in configuration files
- Apply changes automatically and repeatably
- Detect configuration drift (resources not defined in your configuration)
- Integrate Control Center setup into your deployment automation

{% hint style="info" %}
Resource names, such as alerts, teams, and notification channels, must be unique. You cannot create multiple resources with the same name.
{% endhint %}

## Demo Project

GridGain provides a complete working example demonstrating automated deployment:

[Control Center Automated Deployment Demo](https://github.com/GridGain-Demos/control-center-automated-deployment-demo)

The demo includes:

- Docker Compose setup with Control Center and sample Ignite clusters
- Example configuration files defining users, teams, clusters, notifications, and alerts
- Deployment scripts in both Bash and Python
- OpenAPI specification for all REST API endpoints

Use this demo as a starting point for your own automation scripts.

## Deployment Workflow

The automated deployment follows this sequence:

1. **Health Check** - Wait for Control Center to be available
2. **Authentication** - Obtain a JWT token using admin credentials
3. **User Synchronization** - Create or update user accounts
4. **Team Synchronization** - Create teams and manage memberships
5. **Cluster Synchronization** - Attach clusters and configure sharing
6. **Notification Channels** - Configure notification endpoints per cluster
7. **Alert Configurations** - Set up metric-based alerts per cluster

Each step uses a create-or-update pattern, making the deployment idempotent and safe to re-run.

## Prerequisites

Before running automated deployment, you must configure the administrator account and license. In a fully automated scenario, these are set up before Control Center starts, eliminating the need for manual UI interaction.

### Administrator Account

In automated deployments, you configure the default administrator account via Control Center configuration parameters instead of creating it through the UI. Set these parameters before starting Control Center:

| Parameter | Description |
|---|---|
| `account.admin.email` | Email address for the administrator account |
| `account.admin.password` | Password for the administrator account |

You can provide these values via:

- Configuration file (`application.properties` or `application.yml`)
- Environment variables (`ACCOUNT_ADMIN_EMAIL` and `ACCOUNT_ADMIN_PASSWORD`)
- Java system properties

The demo uses environment variables, which is the recommended approach for containerized deployments:

```yaml
control-center-backend:
  environment:
    - ACCOUNT_ADMIN_EMAIL=${CC_ADMIN_EMAIL}
    - ACCOUNT_ADMIN_PASSWORD=${CC_ADMIN_PASSWORD}
```

This administrator account is used by your deployment scripts to authenticate with the REST API and perform all configuration tasks.

### License Management

Control Center requires a valid license to operate. For automated deployments, you have several options to provide the license without manual UI interaction.

#### Mount License File (Recommended for Containers)

The simplest approach for containerized deployments is to mount the license file directly to Control Center's license directory. The demo uses this method:

```yaml
control-center-backend:
  volumes:
    - ./config/control-center-license.xml:/opt/gridgain-control-center/license/control-center-license.xml:ro
```

On startup, Control Center automatically loads the license from its `license/` folder.

#### File Watcher for Dynamic Updates

For environments where you need to update the license without restarting Control Center, enable the file watcher:

```properties
control.license.filestorage=true
control.license.path=/etc/cc/license/control-center-license.xml
```

When enabled, Control Center monitors the specified path and automatically applies license updates.

#### REST API Upload

{% hint style="danger" %}
These examples are for demonstration purposes only. In production, manage credentials using secure mechanisms such as secrets managers, environment variables, or encrypted vaults. Do not store credentials in plain text or embed them directly in commands.
{% endhint %}

You can also upload or update the license programmatically via the REST API:

```bash
curl -X POST \
  -u "admin@example.com:password" \
  "https://<control-center-url:port>/rest/v1/license" \
  -H "Content-Type: application/xml" \
  --data-binary @control-center-license.xml
```

For detailed license management options, see [Managing Licenses](license.md).

### Health Check

Before running deployment scripts, verify that Control Center is fully started and ready to accept requests. The demo script polls the health endpoint until Control Center reports a healthy status:

```bash
curl -s "https://<control-center-url:port>/actuator/health"
```

Response when Control Center is ready:

```json
{
  "status": "UP"
}
```

This health check ensures that Control Center has completed initialization and is ready to process API requests before your deployment script attempts to authenticate and configure resources.

## Configuration Files

Define your desired state using JSON configuration files. The following sections show the structure for each resource type.

### Users Configuration

{% hint style="danger" %}
These examples use plain-text credentials on the command line for simplicity. In production, manage credentials using secure mechanisms such as secrets managers, environment variables, or encrypted vaults. Do not store credentials in plain text or embed them directly in commands.
{% endhint %}

Define user accounts with their profiles:

```json
{
  "users": [
    {
      "username": "alice.johnson@example.com",
      "password": "SecurePassword123!",
      "firstName": "Alice",
      "lastName": "Johnson",
      "company": "ACME Corporation",
      "country": "USA",
      "admin": false
    },
    {
      "username": "bob.smith@example.com",
      "password": "SecurePassword456!",
      "firstName": "Bob",
      "lastName": "Smith",
      "company": "ACME Corporation",
      "country": "USA",
      "admin": true
    }
  ]
}
```

### Teams Configuration

Define teams and their members:

```json
{
  "teams": [
    {
      "name": "development-team",
      "members": [
        "alice.johnson@example.com",
        "bob.smith@example.com"
      ]
    },
    {
      "name": "operations-team",
      "members": [
        "ops-lead@example.com",
        "ops-engineer@example.com"
      ]
    }
  ]
}
```

{% hint style="info" %}
Users must exist before they can be added to teams. Process users before teams in your deployment script.
{% endhint %}

### Clusters Configuration

Define clusters to attach and configure their sharing settings:

```json
{
  "clusters": [
    {
      "tag": "production-cluster",
      "connectorName": "cloud-connector",
      "restUrl": "http://ignite-cluster:10300",
      "shareWith": ["operations-team"]
    },
    {
      "tag": "development-cluster",
      "connectorName": "cloud-connector",
      "restUrl": "http://dev-cluster:10300",
      "shareWith": ["development-team", "operations-team"]
    }
  ]
}
```

The `shareWith` field accepts team names or individual usernames.

### Notification Channels Configuration

Define notification endpoints for each cluster:

```json
{
  "notifications": [
    {
      "clusterTag": "production-cluster",
      "channels": [
        {
          "tag": "ops-email-alerts",
          "type": "EMAIL",
          "emails": ["ops-alerts@example.com", "oncall@example.com"]
        },
        {
          "tag": "pagerduty-webhook",
          "type": "WEBHOOK",
          "url": "https://events.pagerduty.com/integration/your-key/enqueue"
        },
        {
          "tag": "sms-critical",
          "type": "SMS",
          "phones": ["+1234567890"]
        }
      ]
    }
  ]
}
```

Supported notification types:

- `EMAIL` - Send alerts to email addresses
- `WEBHOOK` - POST alerts to a webhook URL
- `SMS` - Send SMS messages to phone numbers

### Alert Configurations

Define metric-based alerts with conditions and notification routing:

```json
{
  "alerts": [
    {
      "clusterTag": "production-cluster",
      "configurations": [
        {
          "tag": "low-node-count",
          "enabled": true,
          "condition": {
            "template": "topology.cluster.TotalNodes",
            "node": "*",
            "conditionType": "LESS_THAN",
            "thresholdValue": 2,
            "gracePeriod": 60000
          },
          "notificationChannelTags": ["ops-email-alerts", "pagerduty-webhook"]
        },
        {
          "tag": "high-heap-memory",
          "enabled": true,
          "condition": {
            "template": "jvm.memory.heap.Used",
            "node": "*",
            "conditionType": "GREATER_THAN",
            "thresholdValue": 500000000,
            "gracePeriod": 120000,
            "autoClosePeriod": 300000
          },
          "notificationChannelTags": ["ops-email-alerts"]
        }
      ]
    }
  ]
}
```

Condition types include:

- `LESS_THAN` - Alert when metric falls below threshold
- `GREATER_THAN` - Alert when metric exceeds threshold
- `EQUALS` - Alert when metric equals threshold

The `gracePeriod` (in milliseconds) prevents alert flapping by requiring the condition to persist before triggering. The optional `autoClosePeriod` automatically closes alerts when the condition is no longer met.

## Getting Started

To implement automated deployment for your environment:

1. **Clone the demo repository**

   ```bash
   git clone https://github.com/GridGain-Demos/control-center-automated-deployment-demo.git
   ```
2. **Review the OpenAPI specification**

   The `openapi/` directory contains the complete API specification. Use this as a reference for all available endpoints and their parameters.
3. **Create your configuration files**

   Define your users, teams, clusters, notification channels, and alerts in JSON files following the structures shown above.
4. **Implement your deployment script**

   Use the demo's Bash or Python scripts as a starting point. The key patterns are:

   - Authenticate first to obtain a JWT token
   - Use create-or-update patterns for idempotency
   - Process resources in dependency order (users before teams, clusters before notifications)
   - Handle errors gracefully and report results
5. **Integrate with your CI/CD pipeline**

   Run your deployment script as part of your infrastructure automation to ensure consistent Control Center configuration across environments.

## REST API Reference

The automated deployment uses Control Center's REST API. Key endpoint categories include:

- `/rest/v1/authentication` - Authentication and JWT management
- `/rest/v1/users` - User management
- `/rest/v1/teams` - Team management
- `/rest/v1/clusters` - Cluster attachment and sharing
- `/rest/v1/clusters/{connectionId}/notifications` - Notification channels
- `/rest/v1/clusters/{connectionId}/alert-configurations` - Alert configurations
- `/rest/v1/clusters/{connectionId}/health` - Cluster health reports

For detailed API documentation, refer to the [OpenAPI specification](https://www.gridgain.com/sdk/controlcenter/latest/openapi/openapi.html).

{% hint style="info" %}
GridGain 8 clusters will be automatically attached and shared with all members of a [global team](configuration.md#teams) if `account.globalTeam.enabled` is enabled.
{% endhint %}
