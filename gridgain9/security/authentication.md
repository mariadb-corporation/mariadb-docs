---
description: >-
  Enable and configure user authentication on a GridGain 9 cluster, using either
  basic authentication or an LDAP authentication provider.
---

# User Authentication

You can configure cluster authentication. GridGain 9 supports basic and LDAP authentication.

## Basic Authentication

To start using basic authentication on the cluster, you need to enable it and create an initial administrator user. By default, the role that grants administrator permissions is called `admin`, but you can change it in cluster configuration.

Here is an example of configuration that initializes the cluster and enables security on it:

- Prepare cluster configuration file with security configuration:

  ```javascript
  ignite {
    security {
      enabled:true
      authentication {
        providers=[
          {
            name=default
            type=basic
            users=[
              {
                displayName=administrator
                password="ignite"
                roles=[
                  system
                ]
                username=ignite
              }
            ]
          }
        ]
      }
    }
  }
  ```

- Initialize the cluster with the license and security configuration:

  ```bash
  cluster init --name=sampleCluster --license=/license.conf --config-files=/cluster-config.conf
  ```

When cluster has been initialized, it has basic authorization configured for `ignite` user name and `ignite` password with system level access. However, by default security is disabled. To enable it:

```bash
cluster config update ignite.security.enabled=true
```

{% hint style="info" %}
This command writes to the `ignite.security` subtree, so it requires both the `WRITE_CLUSTER_CONFIG` and `WRITE_SECURITY_CONFIG` privileges. The same applies to every update under `ignite.security`, including the password change below. See [User Permissions and Roles](user-permissions-and-roles.md).
{% endhint %}

{% hint style="danger" %}
If you lose access to all accounts with system role, you will lose administrator access to the cluster.
{% endhint %}

After authorization is enabled, you will be disconnected from the cluster and must reconnect to the cluster:

```bash
connect http://127.0.0.1:10300 --username ignite --password ignite
```

You can change the password for the default user by updating cluster configuration, for example:

```bash
cluster config update  ignite.security.authentication.providers.default.users.ignite.password=myPass
```

## LDAP Authentication

{% hint style="info" %}
This feature is only available as a part of GridGain 9 Enterprise and Ultimate editions.
{% endhint %}

To start using LDAP authentication on the cluster, add an authentication provider with the `ldap` type to the `ignite.security.authentication.providers` list in the cluster configuration.
Below is an example configuration in the JSON format.

{% hint style="info" %}
In GridGain 9, you can create and maintain the configuration in either JSON or HOCON format.
{% endhint %}

```json
{
    "ignite": {
        "security": {
            "enabled": true,
            "authentication": {
                "providers": [
                    {
                        "name": "default",
                        "type": "basic",
                        "users": [
                            {
                                "displayName": "administrator",
                                "password": "ignite",
                                "roles": [
                                    "system"
                                ],
                                "username": "ignite"
                            }
                        ]
                    },
                    {
                        "name": "ldap",
                        "type": "ldap",
                        "url": "ldap://ldap.example.com:1389",
                        "userSearch": {
                            "dn": "ou=People,dc=example,dc=com",
                            "scope": "SUB_TREE",
                            "filter": "",
                            "groupAttribute": "memberof"
                        },
                        "groupSearch": {
                            "dn": "ou=Groups,dc=example,dc=com",
                            "scope": "SUB_TREE",
                            "filter": "",
                            "userAttribute": "member"
                        },
                        "roleMapping": [
                            {
                                "groupName": "Database Administrators",
                                "roles": ["system"]
                            },
                            {
                                "groupName": "Software Developers",
                                "roles": ["developer"]
                            }
                        ]
                    }
                ]
            }
        }
    }
}
```

{% hint style="warning" %}
Keep a basic authentication provider with at least one `system` role user in the configuration. Otherwise, you may lose administrator access to the cluster if the LDAP server becomes unavailable.
{% endhint %}

When a user authenticates, GridGain uses a search-then-bind flow:

1. GridGain binds to the LDAP server as the service account defined by `bindDn` and `bindCredentials`. If `bindDn` is empty, GridGain binds anonymously.
2. GridGain searches for the user under `userSearch.dn` using `userSearch.filter`. The filter must match exactly one entry; if no entry or more than one entry matches, authentication fails.
3. GridGain re-binds as the located user DN with the provided password to verify the credentials.
4. GridGain resolves the user's groups over the search connection.

Because GridGain locates the user by search, users can be spread across multiple organizational units and be looked up by any attribute (for example, `uid` or `sAMAccountName`), depending on `userSearch.filter`.

GridGain identifies the authenticated user by the name the directory stores, not by the string the client sent.
When a login differs from the stored value only in letter case, the directory's spelling becomes the user's identity
throughout the product. If the search filter matched the login against no attribute, or several stored values differ
from each other only in letter case, GridGain uses the resolved user DN as the identity instead.

{% hint style="info" %}
GridGain rejects authentication attempts with an empty username or an empty password.
{% endhint %}

| Parameter | Description |
|---|---|
|`name`| The name of the authentication provider.|
|`type`| The authentication provider type. Must be `ldap` for LDAP authentication.|
|`url`| The URL of the LDAP server. Supported URL schemes: `ldap`, `ldaps`.|
|`bindDn`| The DN of the service account GridGain binds as to search for the authenticating user. If empty, GridGain performs the search over an anonymous connection. Empty by default.|
|`bindCredentials`| The password of the service account defined by `bindDn`. Required when `bindDn` is set: a simple bind with an empty password is an unauthenticated bind, which would leave the search connection anonymous instead of authenticated as the service account. Ignored when `bindDn` is empty. Empty by default.|
|`userSearch`| Configuration of the user search. GridGain searches for the authenticated user in the specified container.|
|`userSearch.dn`|The DN of the container to search for users.|
|`userSearch.scope`|The scope of the search. Possible values: `SUB_TREE`, `ONE_LEVEL`, `BASE`. Default value: `SUB_TREE`.|
|`userSearch.filter`|A filter used when searching for the user. `{0}` is replaced by the username provided when searching. Default value: `(uid={0})`.|
|`userSearch.groupAttribute`|An attribute of the user entry checked for group membership. If not empty, GridGain reads the user's groups from this attribute and ignores `groupSearch`.|
|`groupSearch`|Configuration of the group search. Used to find the user's groups when `userSearch.groupAttribute` is empty.|
|`groupSearch.dn`|The DN of the container to search for groups.|
|`groupSearch.scope`|The scope of the search. Possible values: `SUB_TREE`, `ONE_LEVEL`, `BASE`. If `ONE_LEVEL` is specified, only searches objects directly contained within the dn. If `SUB_TREE` is specified, searches all objects contained under the dn. If `BASE` is specified, the specified group is searched. Default value: `SUB_TREE`.|
|`groupSearch.filter`|A filter used when searching for the user's groups. `{0}` is replaced by the value of the user attribute defined in `groupSearch.userAttribute`. Default value: `(\|(member={0})(memberOf={0})(memberUid={0}))`.|
|`groupSearch.userAttribute`|The user attribute provided as the parameter to the filter. Empty by default; in this case, the located user DN is used as the filter parameter. If the attribute has multiple values on a user entry, GridGain performs a group lookup for each value and returns all matched groups combined.|
|`roleMapping`|A list of mappings of LDAP groups to GridGain roles. Groups without a mapping are mapped to roles with matching names.|
|`roleMapping.groupName`|The name of the LDAP group to map. When groups are resolved through `groupSearch`, the group name is the value of the `cn` attribute of the group entry.|
|`roleMapping.roles`|The list of GridGain roles assigned to users in the group.|

When security is enabled, GridGain rejects a configuration update that sets `bindDn` while leaving `bindCredentials` empty.
A node whose stored configuration already pairs a `bindDn` with empty `bindCredentials` still starts, and further updates to
that provider are not blocked, so review your existing providers after an upgrade rather than relying on the check to find them.

You can provide LDAP configuration in a similar way you provide basic authentication configuration, by passing the configuration file during cluster initialization, or by updating the configuration of a running cluster with the `cluster config update` command.
