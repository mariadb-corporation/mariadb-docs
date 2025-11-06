# Infrastructure Upgrades

MariaDB Cloud runs on modern Kubernetes infrastructure across AWS, GCP, and Azure cloud providers. To maintain security, performance, and compliance with cloud provider requirements, periodic infrastructure upgrades are essential for all running services.\
Infrastructure upgrades are a critical component of maintaining a secure, performant, and compliant database service. By staying current with these upgrades, you ensure continued access to the latest features, security updates, and cloud provider support.

## Understanding Infrastructure vs Database Upgrades

**Infrastructure upgrades** are different from database software upgrades:

* **Infrastructure Upgrades**: Update the underlying Kubernetes nodes, container runtime, and cloud provider components that host your database
* **Database Upgrades**: Update the MariaDB database software version itself

## Service Impact During Upgrades

**MariaDB Server with Replicas** experiences a brief service interruption while connections are cycled on the Load Balancer.

**MariaDB Server Single Node** will experience a brief downtime during the database restart, typically lasting 2-5 minutes.

Infrastructure upgrades ensure your service continues to receive:

* Security patches and vulnerability fixes
* Performance improvements and optimizations
* Continued support from cloud providers (AWS, GCP, Azure)
* Access to the latest cloud platform features

## Why Infrastructure Upgrades Are Required

### Cloud Provider Requirements

Our cloud providers (AWS, GCP, Azure) enforce strict upgrade schedules for Kubernetes infrastructure:

* **Security Compliance**: Outdated infrastructure versions may not receive critical security updates
* **Support Limitations**: Cloud providers eventually discontinue support for older infrastructure versions

## How Infrastructure Upgrades Work

### Notification Timeline

1. **3 Months Prior to Automated Upgrade**: MariaDB Cloud sends initial notification about upcoming infrastructure upgrade requirements
2. **Regular Reminders**: Follow-up notifications are sent as the deadline approaches
3. **Grace Period**: Customers have time to perform upgrades before the automatic deadline
4. **Automated Upgrade Deadline**: If not upgraded by the deadline, MariaDB Cloud will automatically perform the upgrade to maintain compliance

## Managing Infrastructure Upgrades in the Portal

### Viewing Available Upgrades

1. Log in to the [Portal](https://app.skysql.com/dashboard).
2. Any affected service will display an **Upgrade Available** or **Upgrade Required** notification.
3. An upgrade deadline will be shown, indicating the last date to perform the upgrade before automatic enforcement.

### Performing an Upgrade

1. Click **Upgrade** next to the available infrastructure update
2. Review the upgrade details and impact
3. Confirm to begin the immediate upgrade process
4. Monitor the upgrade progress through the Portal

{% hint style="info" %}
"Immediate Processing" Infrastructure upgrades begin immediately when initiated and cannot be scheduled for a future time.
{% endhint %}

### Upgrade Status Tracking

Monitor your upgrade progress through:

* Real-time status updates in the Portal
* Email notifications at key milestones
* Service monitoring panels showing restart progress

## Frequently Asked Questions

**Q: Best time to upgrade** A: Plan according to your maintenance windows.

**Q: Can I schedule an upgrade for later?** A: No, infrastructure upgrades begin immediately when initiated. Plan to perform them during appropriate maintenance windows.

**Q: What happens if I don't upgrade by the deadline?** A: MariaDB Cloud will automatically perform the upgrade to maintain cloud provider compliance and platform stability.

**Q: Will my data be affected during the upgrade?** A: No, infrastructure upgrades only restart the database service. Your data remains intact and unchanged.

**Q: Can I opt out of infrastructure upgrades?** A: No, infrastructure upgrades are mandatory to maintain security, compliance, and cloud provider support.
