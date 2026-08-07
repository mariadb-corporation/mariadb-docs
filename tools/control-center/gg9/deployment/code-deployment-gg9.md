---
description: >-
  Creating, deploying, updating, and versioning code deployment units for
  GridGain 9 compute tasks from Control Center.
---

# Code Deployment with GridGain 9

You may want to deploy compute tasks to your GridGain nodes using Control Center. For example, you often need many dependencies to complete [distributed computing](https://www.gridgain.com/docs/gridgain9/latest/developers-guide/compute/compute) tasks.

## Deployment Units

The **Deployment Units** tab shows all your deployments and allows you to create, modify, clone and remove deployment units.

![Deployment units tab](../../../.gitbook/assets/cc-gg9-du_tab_overview.png)

### Creating a new Deployment Unit

To create a new deployment unit, click **Add Deployment Unit** and specify its name in the following dialog.

![Add deployment unit](../../../.gitbook/assets/cc-gg9-du_add_du_valid_name.png)

The newly created deployment unit is stored as a draft. As long as it is in the `Draft` state and has not been deployed, you can rename it. Once deployed, the unit cannot be renamed, you can only delete it or clone and assign it a version.

![Rename draft deployment unit](../../../.gitbook/assets/cc-gg9-du_rename_draft.png)

For a deployment unit to be eligible for deployment, it must contain the dependencies required to perform compute jobs. You can either upload the needed files or provide a direct URL to download them.

To add dependencies, first select your deployment unit while it is in the `Draft` state as you cannot add artifacts if the unit has already been deployed.

Then click **Add Artifact**. In the subsequent dialog, you have two options:

- **Uploaded artifact** - upload a new file from your local system. Files uploaded from your system will also appear in the **Sources** [tab](#sources), you can search and select artifacts.
- **Direct link** - provide the direct URL for the dependency.

![Add artefact](../../../.gitbook/assets/cc-gg9-du_add_artifact.png)

After adding all required dependencies click **Deploy**. You will be asked to set the deployment unit version before deployment.

{% hint style="info" %}
The version is not automatically incremented so you must define it manually using [semantic versioning](https://semver.org/).
{% endhint %}

When deploying a unit, you select either all nodes or a majority as the initial target. Choosing a majority means the unit is deployed on-demand to other nodes when they first need it to avoid unnecessary early copying.

![Deploy unit](../../../.gitbook/assets/cc-gg9-du_deploy.png)

You can view the version history in a separate [tab](#version-history) accessible from the **Deployment Units list**.

### Updating Deployment Unit

Deployment units are immutable, so you must create and deploy a new version whenever you want to change dependencies. To update a deployment unit:

1. Click **Clone**. This will create a new version of your deployment unit in **Draft** state.
2. Change the dependencies you need. To remove or edit existing dependencies, click ⋮ and select **Remove** or **Edit artefact** respectively. You can also **Add artefact** to add a new dependency.
3. Click **Deploy** and define a new unit version. Specify a version that is greater than the previous one.

![Add artefact](../../../.gitbook/assets/cc-gg9-du_update_unit.png)

To create a new deployment based on an existing version, click **Clone and Deploy** from the version’s menu and enter a new semver. This option may be useful for quickly replacing a unit deployed with an incorrect version.

You cannot **Clone** or **Clone and Deploy** units that were deployed via the [CLI](https://www.gridgain.com/docs/gridgain9/latest/developers-guide/code-deployment/code-deployment#deploy-new-unit). To manage a CLI-deployed unit through Control Center, create a draft version from this unit, add artifacts, and deploy the new version.

![Create draft from CLI-deployed unit](../../../.gitbook/assets/cc-gg9-du_cli_unit_draft.png)

### Version History

Control Center keeps a complete history of all deployment unit versions in the **Version History** table.

![Version History Tab](../../../.gitbook/assets/cc-gg9-du_version_history_tab.png)

The table provides the following information:

| Menu item | Description |
|---|---|
| **Version** | Version number. |
| **Status** | Current version status. Possible version statuses:<br>- `Draft` - A new unit that has not yet been deployed.<br>- `Uploading` - The unit is being deployed to the cluster.<br>- `Deployed` - The unit is currently deployed on the cluster and can be used.<br>- `Obsolete` - The command to remove unit has been received, but it is still used in some jobs.<br>- `Removing` - The unit is being removed. |
| **Files** | The number of files in the deployment unit. |
| **Deployed at** | Time and date of the deployment. |

### Reverting to an older version

If you want to switch to an older version (for example, one of the updated dependencies did not work as expected), you can deploy the previous version.

- Open **Version History**.
- Select the older version you need.
- Click **Clone and Deploy**.

Control Center will create a new version that copies all dependencies from the selected version.

## Sources

The **Sources** tab lets you review the dependencies used by your deployment units. You can see how many deployment units use each dependency and upload new dependencies for your code.

![Code deployment sources](../../../.gitbook/assets/cc-gg9-du_sources_tab.png)

### Uploaded Artifacts

This section lets you upload an artifact to Control Center. Uploaded artifacts will be stored on the Control Center host and sent to all deployment units as needed.

### Uploading New Artifacts

To add a new artifact, click **Add artifact** button and select the file you need. The artifact will then be stored locally and made available for use with your deployment units.

### Checking Dependent List

To see all deployment units that use a specific artifact, click ⋮ and select **View dependent list**. The dialog that opens lists all deployment units that use the selected artifact.

### Deleting Artifacts

To delete an artifact, click ⋮ and select **Remove**. If the selected artifact has dependents, they show in the **Dependent list** dialog - see [Checking Dependent List](#checking-dependent-list). You must delete the dependent deployment units before you can remove the artifact itself.
