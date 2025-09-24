# MaxScale Admin Role Resource

Admin roles represent a set of permissions that define which operations are
allowed on the REST-API.

## Resource Operations

### Get role

```
GET /v1/role/:name
```

Get a single role. The _:name_ in the URI must be a valid role name.

#### Response

`Status: 200 OK`

```javascript
{
    "data": {
        "attributes": {
            "permissions": [
                "admin",
                "edit",
                "view",
                "sql"
            ]
        },
        "id": "admin",
        "links": {
            "self": "http://localhost:8989/v1/roles/admin/"
        },
        "type": "roles"
    },
    "links": {
        "self": "http://localhost:8989/v1/roles/admin/"
    }
}
```

### Get all roles

```
GET /v1/roles
```

Get all roles.

#### Response

`Status: 200 OK`

```javascript
{
    "data": [
        {
            "attributes": {
                "permissions": [
                    "edit",
                    "view",
                    "sql"
                ]
            },
            "id": "editor",
            "links": {
                "self": "http://localhost:8989/v1/roles/editor/"
            },
            "type": "roles"
        },
        {
            "attributes": {
                "permissions": [
                    "admin",
                    "edit",
                    "view",
                    "sql"
                ]
            },
            "id": "admin",
            "links": {
                "self": "http://localhost:8989/v1/roles/admin/"
            },
            "type": "roles"
        },
        {
            "attributes": {
                "permissions": [
                    "sql"
                ]
            },
            "id": "sql",
            "links": {
                "self": "http://localhost:8989/v1/roles/sql/"
            },
            "type": "roles"
        },
        {
            "attributes": {
                "permissions": [
                    "view",
                    "sql"
                ]
            },
            "id": "basic",
            "links": {
                "self": "http://localhost:8989/v1/roles/basic/"
            },
            "type": "roles"
        }
    ],
    "links": {
        "self": "http://localhost:8989/v1/roles/"
    }
}
```

### Create a role

```
POST /v1/roles
```

Create a new role. The request body must define the following fields.

* `data.id`

  * The role name

* `data.attributes.permissions`

  * A JSON array of strings that define the permissions. Any permissions that
    are unknown are stored as extra user-defined permissions that are available
    in the `/roles` endpoint. These extra permissions can then be used by
    external systems or as a way to label account types.

The supported permissions are:

* `admin`: Access to the administrative endpoints `/users` and `/roles` which
  are used to create new user accounts and roles.

* `edit`: Write access to all endpoints that create objects except the
  administrative endpoints `/users` and `/roles`. This permission is required
  for creating, modifying or destroying objects via the REST-API.

* `sql`: Read-only access to the `/maxscale`, `/servers`, `/services` and
  `/listeners` endpoints as well as full permissions on the `/sql`
  endpoint. This permission is needed by the Query Editor feature.

* `view`: Read-only access to all endpoints except the administrative endpoints
  `/users` and `/roles`. This permission is required for most read-only
  operations in the GUI.

Here is an example request that defines a new role `my-role` that can view and
edit objects but cannot use the Query Editor.

```javascript
{
    "data": {
        "id": "my-role",
        "attributes": {
            "permissions": ["view", "edit"]
        }
    }
}
```

#### Response

```
Status: 204 No Content
```

### Update a role

```
PATCH /v1/roles/:name
```

Update a role. Only the `data.attributes.permissions` field can be
modified. Modifying a role requires administrative privileges.

Here is an example request body that updates the permissions of a role.

```javascript
{
    "data": {
        "attributes": {
            "permissions": ["view, "edit"]
        }
    }
}
```

#### Response

```
Status: 204 No Content
```

### Delete a role

```
DELETE /v1/roles/:name
```

The _:name_ part of the URI must be a valid role name.

#### Response

```
Status: 204 No Content
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
