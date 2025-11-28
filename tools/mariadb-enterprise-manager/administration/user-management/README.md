# User Management

MariaDB Enterprise Manager uses a Role-Based Access Control (RBAC) system to manage user permissions. This guide explains how to manage users and create custom roles to fit your organization's security needs.

### Accessing User Management

{% stepper %}
{% step %}
### Open Settings

Click the **Settings icon (⚙️)** in the left navigation bar.
{% endstep %}

{% step %}
### Open User Management

Select **User management**.

<figure><img src="../../../.gitbook/assets/image (19).png" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}

## Permissions, Roles & Users

In MariaDB Enterprise Manager, permissions, roles, and users are organized in a clear structure:

* Permissions define specific actions a user can perform (viewing data, editing settings, accessing the SQL editor).
* Roles are collections of one or more permissions grouped together. They can be pre-configured (for example `admin`, `monitoring-admin`, `viewer`) or custom-defined.
* Users are assigned one or more roles and inherit the associated permissions.

<figure><img src="../../../.gitbook/assets/image (20).png" alt=""><figcaption></figcaption></figure>

This structure allows administrators to manage access by assigning roles to users rather than setting individual permissions per user.

### The Admin Permission

Access to the User Management page is restricted based on a user's assigned permissions.

* ✅ Only users with `admin` permissions (assigned via a role) can add, modify, or remove other users and roles.
*   ❌ Non-admin users cannot access or change these settings, but they can update their own password via their Profile page.\


    <figure><img src="../../../.gitbook/assets/image (21).png" alt=""><figcaption></figcaption></figure>

## Default Roles

Enterprise Manager ships with three pre-configured roles:

* `admin`: Has all permissions. Can do everything, including managing other users.
* `monitoring-admin`: Can manage databases and monitoring, but cannot manage users or roles.
* `viewer`: Has read-only access to monitoring data and can use the Workspace.

{% hint style="info" %}
**Create custom roles instead of editing pre-configured ones**

While it's possible to edit or delete the pre-configured roles (`admin`, `viewer`, etc.), the recommended best practice is to create a new custom role to fit your specific permission requirements.

Leaving the pre-configured roles unmodified ensures you always have a known, baseline configuration to reference or fall back on.
{% endhint %}

Roles (pre-configured or custom) are built from combinations of the following base permissions:

### Base Permission in MariaDB Enterprise Manager

| Permission | Description                                                                                                                     |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `admin`    | Can view and manage all users and roles.                                                                                        |
| `edit`     | Can manage databases and monitoring settings. **Requires the `view` permission to be selected as well.**                        |
| `view`     | Can view dashboards and monitoring data.                                                                                        |
| `sql`      | Can access the Query Editor and ERD tools in the Workspace. **Enabling this allows you to set a query row limit for the role.** |

## Managing Roles

Only users with the `admin` permission can create or modify roles.

### Creating a Custom Role

{% stepper %}
{% step %}
### Roles tab

From the User Management page, select the **Roles** tab.
{% endstep %}

{% step %}
### Add role

Click the **Add** button.
{% endstep %}

{% step %}
### Name role

Enter a name for your new role (e.g., "Developer" or "Auditor").
{% endstep %}

{% step %}
### Select base permissions

Select the checkboxes for the **Base Permissions** you want to grant.
{% endstep %}

{% step %}
### Confirm

Click **Add**.

<figure><img src="../../../.gitbook/assets/image (23).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
If you select the `sql` permission, a **"Query editor row limit"** dropdown will appear. You can adjust this value as needed.

![](<../../../.gitbook/assets/image (26).png>)
{% endhint %}

{% hint style="warning" %}
When creating a role, selecting the `edit` permission requires you to also select the `view` permission. 
{% endhint %}
{% endstep %}
{% endstepper %}

### Modifying or Deleting a Role

{% stepper %}
{% step %}
### Locate role

From the **Roles** tab, locate the custom role you wish to change.
{% endstep %}

{% step %}
### Open role menu

Click the three-dot menu (⋮) on the right side of the role's row.
{% endstep %}

{% step %}
### Choose action

Select one of the following options:

<figure><img src="../../../.gitbook/assets/image (27).png" alt=""><figcaption></figcaption></figure>

* **Update**: Opens the "Edit Role" dialog where you can change the role's name or its assigned permissions.
* **Delete**: Permanently removes the custom role. A confirmation dialog will appear.

{% hint style="info" %}
Roles that are currently assigned to any user cannot be deleted.
{% endhint %}
{% endstep %}
{% endstepper %}

## Managing Users

### Adding a User

{% stepper %}
{% step %}
### Users tab

From the User Management page, ensure you are on the **Users** tab.

{% hint style="info" %}
Users tab show the list of User associated with your Enterprise Manager instance. 

![](<../../../.gitbook/assets/image (60).png>)

The User you're logged in with to Enterprise Manager is shown in **bold**.
{% endhint %}
{% endstep %}

{% step %}
### Add user

Click the **Add** button.
{% endstep %}

{% step %}
### Enter credentials

Enter a unique **Username** and a secure **Password**.
{% endstep %}

{% step %}
### Assign role

Select a **Role** for the user from the dropdown menu.
{% endstep %}

{% step %}
### Confirm

Click **Add**.
{% endstep %}
{% endstepper %}

### Modifying or Deleting a User

{% stepper %}
{% step %}
### Locate user

From the **Users** tab, locate the user you wish to change.
{% endstep %}

{% step %}
### Open user menu

Click the three-dot menu (⋮) on the right side of the user's row.
{% endstep %}

{% step %}
### Choose action

Select one of the following options:

<figure><img src="../../../.gitbook/assets/image (28).png" alt=""><figcaption></figcaption></figure>

* **Update**: Opens the "Edit User" dialog where you can change the user's assigned role or update their password.
* **Delete**: Permanently removes the user from MariaDB Enterprise Manager.

{% hint style="info" %}
You cannot delete the user account that you are currently logged in with. To delete an administrator account, you must first log in with a different administrator account.
{% endhint %}
{% endstep %}
{% endstepper %}

## The Default Admin User

Upon installation of MariaDB Enterprise Manager, a default `admin` user is created with an automatically generated password.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
