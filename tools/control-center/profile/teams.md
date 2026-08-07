---
description: >-
  Creating and managing Control Center teams, adding and promoting members, and
  using the system-managed Global Team.
---

# Managing Teams

As a Control Center user, you can use teams to share Control Center features (such as the Dashboards, SQL, and Alerts screens) between the team participants.

One of the shareable features is access to clusters - for details, see [Cluster Management Screen](../cluster-management.md) and [My Cluster Screen](../gg9/dashboard/my-cluster.md).

{% hint style="info" %}
You need no special privileges to create a team.
{% endhint %}

A team participant can be:

- *Member* - a Control Center user who had been invited to the team by one of that team's administrators. Members can use the features and clusters the team has access to. They can also leave the team.
- *Administrator* - a Control Center user who had created the team, or who had been promoted to the administrator status upon joining that team. Administrators can perform a full set of team activities, including renaming the team, inviting and removing members, etc.

You manage teams and team members on the **Teams** screen. To navigate to this screen, select **Team Management** from the user profile menu.

![Teams screen](../../.gitbook/assets/cc-profile-teams_page.png)

The left-hand side of the screen lists all the existing teams.

The right-hand side of the screen, titled **\<Team name>**|**All**, lists:

- If a specific team is selected on the left-hand side - members of that team
- If **All** is selected - all members of all teams you (the current user) belong to
- If **Global Team** is selected - all Control Center users or, if integrated with AD/LDAP, all AD/LDAP users who had logged into Control Center at least once

{% hint style="info" %}
**Global Team** appears on the list only if `account.globalTeam.enabled` is enabled in your environment. By default, global team includes all active Control Center users. When `account.globalTeam.attachCluster` is also enabled, all clusters in the environment will be automatically shared with all users from the [global team](#global-team). For details, see [Global Team](#global-team).
{% endhint %}

To find a team member, you can use the incremental search field located above the **\<Team name>** list.

## Teams

### Creating a Team

To create a team, click **Add Team**. Control Center prompts you for a team name.

{% hint style="info" %}
Team names are not unique within a Control Center instance.
{% endhint %}

Enter a name for the team and click **Create Team**.

Control Center prompts you to add a member to the new team. Add a member - see [Adding Members to a Team](#adding-members-to-a-team) - or click **Cancel** to add members later.

The team you have created appears on list in the left-hand part of the screen. You automatically become an *administrator* of that team.

### Renaming a Team

{% hint style="info" %}
Only team *administrators* can rename a team.
{% endhint %}

To rename a team, click `⋮` next to the team name and select **Rename**. Edit the team name and click **Save**.

### Removing a Team

{% hint style="info" %}
Only team *administrators* can remove a team.
{% endhint %}

To remove a team, select that team on the left-hand side of the screen, then click **Remove Team** above the team member list on the right-hand side.

In the confirmation dialog, click **Remove**.

Users who had access to clusters and features as members of the removed team lose that access.

## Members

### Adding Members to a Team

{% hint style="info" %}
Only team *administrators* can add members to a team.
{% endhint %}

To add members to a team, select that team on the left-hand side of the screen, then click **Add Members** above the team member list on the right-hand side. In the **Add Members** dialog, start typing a Control Center user's email or LDAP ID. As you type, the incremental search mechanism displays suggestions in a drop-down list. Select one of the suggested users or type the email/ID to the end, then click \[Enter]. You can add multiple users in a single operation. When done, click **Add**.

The users are added to the selected team as *members*.

### Promoting and Demoting Members

By default, the Control Center users are added to a team with the *member* role.

As a team administrator, you can promote a team member to the *administrator* role. To promote a member, click `⋮` by that member's name on the list in the right-hand part of the screen and select **Make Administrator**. In the confirmation dialog, click **Make**.

As a team administrator, you can also demote another administrator to the *member* role. To demote an administrator, click `⋮` by that administrator's name on the list in the right-hand part of the screen and select **Make Member**. In the confirmation dialog, click **Make**.

### Removing a Member

As a team administrator, you can remove a member from the team. Click `⋮` next to the *member* or *administrator* you want to remove and select **Remove**. In the confirmation dialog, click **Remove**.

### Leaving a Team

As a team member or administrator, you can leave any team you belong to.

{% hint style="info" %}
If you are the only *administrator* of a team, you need to promote one of the *members* of that team to the *administrator* role before leaving. For details, see [Promoting and Demoting Members](#promoting-and-demoting-members).
{% endhint %}

Click `⋮` next to the team you want to leave and select **Leave Team**. In the confirmation dialog, click **Leave**.

## Global Team

The Global Team is a system-managed team available when `account.globalTeam.enabled` is set to `true` in your [environment configuration](../admin-guide/configuration.md#teams). Unlike regular teams, its membership is managed automatically by Control Center — you do not need to invite users or manage access manually.

### How It Works

When enabled, Control Center automatically creates a team called *Global Team*:

- All active local Control Center users are added to Global Team automatically.
- If your environment is integrated with AD/LDAP, AD/LDAP users are added to Global Team upon their first login into Control Center. Users who have never logged in are not included.

Because membership is managed by the system, you cannot manually add or remove individual users from Global Team, nor rename or delete it.

### Cluster Auto-Attach

When `account.globalTeam.attachCluster` is set to `true`, Control Center automatically shares every cluster in the environment with Global Team — including clusters registered after this setting is enabled.

{% hint style="info" %}
`account.globalTeam.attachCluster` applies to all clusters. You cannot exclude individual clusters from auto-attach while this setting is enabled. To restrict access to specific clusters, disable `account.globalTeam.attachCluster` and share clusters with individual teams manually.
{% endhint %}

This makes Global Team useful for automating cluster access management in large environments. For example, you can attach clusters without generating individual tokens. For details, see [How can I automate connection of clusters to Control Center?](../faq.md#how-can-i-automate-connection-of-clusters-to-control-center)

### Limitations

- Global Team membership is managed automatically — individual users cannot be added or removed manually.
- AD/LDAP users are added only after their first login; users who have never logged in are not included.
- `account.globalTeam.attachCluster` applies to all clusters — you cannot exclude individual clusters from auto-attach while the setting is enabled.
- Global Team cannot be renamed or deleted.
