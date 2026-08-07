---
description: >-
  How to update GridGain Control Center to a more recent version, including
  work folder backup and automatic update application.
---

# Control Center Version Update

To update to Control Center to a more recent version:

1. On the **Release Notes** page for the target version, verify the following:
   - Your current version is compatible with the target version.
   - All requirements are met; e.g., the Java version supported by the target release is installed.
2. If you use an [external](../admin-guide/external-cluster.md) GridGain 8 cluster for data storage, skip this step.

   Otherwise, create a storage backup of the `work` folder for the Control Center version you are updating from.

   {% hint style="info" %}
   Make sure you use the [correct `work` folder](install-binary.md).
   {% endhint %}
3. Enable automatic update application by setting the `control.repositories.auto-migrate-enabled` parameter to `true` in the `application.properties`.
4. Start the new version of Control Center.

   The success or failure of the update is reflected in the log file.
5. In case of an update failure:
   - Restore from the backup created in Step 1 and run the Control Center version you attempted to update from.
   - Contact us for [support](http://support.gridgain.com/).
