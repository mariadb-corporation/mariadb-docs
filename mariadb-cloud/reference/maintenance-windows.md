---
description: >-
  Maintenance windows and scheduling policies for MariaDB Cloud — every service
  has an assigned weekly 1-hour window defined in UTC, auto-assigned per region
  and configurable per service.
---

# Maintenance Windows and Scheduling Policies

Every MariaDB Cloud database operates with an assigned weekly maintenance window. You can configure a different preferred maintenance period for each of your services.

## Window Configuration Details

* Each maintenance window is a block of **1 hour**.
* Windows are defined in **UTC** to provide consistency across global time zones and daylight saving time (DST) changes.
* If you don't select a window during or after launch, a default window is automatically assigned for your service, scheduled during off-peak hours for the deployed region's local time.

You can view and change your assigned window at any time from the **Maintenance** pane on the Service detail page. See [Maintenance Management](../cloud-usage/maintenance-management.md) for the full workflow.

## Auditability and Compliance

MariaDB Cloud maintains a comprehensive, auditable history of all maintenance activities for each service. This history records when maintenance was scheduled, executed, and completed. Customer actions — including manual application, window changes, and deferrals — are permanently recorded to provide a complete audit trail for compliance and troubleshooting.
