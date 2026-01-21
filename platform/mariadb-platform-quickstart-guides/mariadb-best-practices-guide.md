---
cover: broken-reference
coverY: 0
---

# Best Practices

_This Quickstart Guide outlines MariaDB best practices for robust deployments. Key areas include regular, tested backups and structured change management. It emphasizes dedicated production servers, thorough pre-production testing, and timely updates. Also highlighted are understanding business requirements and leveraging commercial support for optimal performance and security._

### Quickstart Guide: MariaDB Best Practices

Adhering to best practices is crucial for ensuring the performance, stability, and security of your MariaDB deployments. This guide summarizes key recommendations.

#### 1. General Recommendations

* **Understand Business Requirements:** Before deploying MariaDB, thoroughly understand your business needs and how the database will integrate with existing systems.

#### 2. Backups

* **Perform Regular Backups:** Always back up existing data and configurations before any production changes or upgrades/downgrades.
* **Establish and Test Restoration Plans:** Have a clear plan for data restoration and regularly test your backups to ensure they are complete and viable.

#### 3. Change Management

* **Implement Formal Change Management:** All server configuration changes should follow a documented change management process.
* **Maintain Accurate Records:** Keep precise records of when and why changes were made to facilitate faster issue diagnosis.
* **Automate Deployments:** Utilize automation and orchestration for repeatable and consistent server deployments and testing, including system provisioning.

#### 4. Production Controls

* **Dedicated Servers:** Avoid running other workloads on database servers to prevent resource contention.
* **Understand Isolation and Control Requirements:** Before deployment, clearly define workload, data isolation, and audit control requirements.

#### 5. Testing

* **Pre-Production Validation:** Validate servers thoroughly before exposing them to production workloads and data.
* **Prevent Unconfigured Access:** Restrict access to servers until they are fully configured and validated.
* **Assess Key Details:** During validation, assess server capacity, security configuration and hardening, tuning for initial data loads versus production workloads, and alignment with business requirements.

#### 6. Updates

* **Stay Informed:** Keep aware of new MariaDB releases, including critical security fixes, by subscribing to MariaDB Product Notifications.
* **Follow Enterprise Lifecycle:** If using MariaDB Enterprise Server, adhere to its enterprise lifecycle for updates and upgrades.

#### 7. Obtaining Support

* **Utilize Commercial Support:** For comprehensive technical support and services, consider engaging with MariaDB Corporation's commercial support. Existing customers can access assistance via the MariaDB Customer Portal.

This guide provides a high-level overview. For more in-depth information, refer to the official MariaDB documentation on best practices.

{% @marketo/form formId="4316" %}
