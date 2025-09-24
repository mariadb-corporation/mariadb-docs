# MaxScale Admin User Resource

## Overview

Admin users represent administrative users that are able to query and change
MaxScale's configuration.

## Resource Operations

### Get network user

```
GET /v1/users/:name
GET /v1/users/inet/:name
```

Get a single network user. The _:name_ in the URI must be a valid network
user name.

#### Response

`Status: 200 OK`

```javascript
{
    "data": {
        "attributes": {
            "account": "admin",
            "created": "Fri, 25 Jul 2025 15:43:46 GMT",
            "last_login": "Fri, 25 Jul 2025 15:44:03 GMT",
            "last_update": null,
            "name": "admin",
            "permissions": [
                "admin",
                "edit",
                "view",
                "sql"
            ]
        },
        "id": "admin",
        "links": {
            "self": "http://localhost:8989/v1/users/admin/"
        },
        "type": "users"
    },
    "links": {
        "self": "http://localhost:8989/v1/users/admin/"
    }
}
```

### Get all network users

```
GET /v1/users
GET /v1/users/inet
```

Get all network users.

#### Response

`Status: 200 OK`

```javascript
{
    "data": [
        {
            "attributes": {
                "account": "admin",
                "created": "Fri, 25 Jul 2025 15:43:46 GMT",
                "last_login": "Fri, 25 Jul 2025 15:44:03 GMT",
                "last_update": null,
                "name": "admin",
                "permissions": [
                    "admin",
                    "edit",
                    "view",
                    "sql"
                ]
            },
            "id": "admin",
            "links": {
                "self": "http://localhost:8989/v1/users/admin/"
            },
            "type": "users"
        }
    ],
    "links": {
        "self": "http://localhost:8989/v1/users/"
    }
}
```

### Get all users

```
GET /v1/users
```

Get all administrative users.

#### Response

`Status: 200 OK`

```javascript
{
    "data": [
        {
            "attributes": {
                "account": "admin",
                "created": "Fri, 25 Jul 2025 15:43:46 GMT",
                "last_login": "Fri, 25 Jul 2025 15:44:03 GMT",
                "last_update": null,
                "name": "admin",
                "permissions": [
                    "admin",
                    "edit",
                    "view",
                    "sql"
                ]
            },
            "id": "admin",
            "links": {
                "self": "http://localhost:8989/v1/users/admin/"
            },
            "type": "users"
        }
    ],
    "links": {
        "self": "http://localhost:8989/v1/users/"
    }
}
```

### Create a network user

```
POST /v1/users
POST /v1/users/inet
```

Create a new network user. The request body must define at least the
following fields.

* `data.id`

  * The username.

* `data.attributes.password`

  * The password for this user.

* `data.attributes.role` or `data.attributes.account`

  * The role that this user account uses. The set of available roles can be
    retrieved with `GET /v1/roles`. The old fixed set of roles that older
    versions of MaxScale used are also read from the `account` field, if
    used. If both the `role` and the `account` field are present, the value of
    the `role` field is used.

Here is an example request body defining the network user _my-user_ with the
password _my-password_ that is allowed to execute only read-only operations.

```javascript
{
    "data": {
        "id": "my-user", // The user to create
        "attributes": {
            "password": "my-password", // The password to use for the user
            "role": "admin" // The type of the account
        }
    }
}
```

#### Response

```
Status: 204 No Content
```

### Delete a network user

```
DELETE /v1/users/:name
DELETE /v1/users/inet/:name
```

The _:name_ part of the URI must be a valid user name.

#### Response

```
Status: 204 No Content
```

### Update a network user

```
PATCH /v1/users/:name
PATCH /v1/users/inet/:name
```

Update network user. The following fields can be modified:

* `data.attributes.password`

  * Changes the password for this user.

* `data.attributes.role` or `data.attributes.account`

  * Changes the role for this user. If both fields are defined, the value of
    `role` is used.

Modifying a user requires administrative privileges.

Here is an example request body that updates the password.

```javascript
{
    "data": {
        "attributes": {
            "password": "new-password"
        }
    }
}
```

#### Response

```
Status: 204 No Content
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
