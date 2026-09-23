---
description: >-
  GridGain 9 supports JWT authentication for REST users, letting them obtain,
  use, and revoke JSON Web Tokens to authenticate to the cluster.
---

# JWT Authorization

In addition to other ways of authentication, GridGain 9 provides JWT authentication for users who use REST to work with the cluster. JWT allows users to safely, securely and quickly authenticate to the cluster without requiring the overhead of verifying every request separately.

GridGain regularly updates the private keys used to create JWT tokens. The frequency can be changed by using the `ignite.security.jwt.keyTtl` property. By default, the keys are updated every 14 days.

## Getting JWT Token

To get the JWT token, send a request to `/management/v1/authentication/login` endpoint. The request body should contain the GridGain credentials for the user the token is provided for. For more information on how to create a user, see [Basic authentication](authentication.md#basic-authentication)

```bash
curl -X 'POST' \
'http://cluster_url:10300/management/v1/authentication/login' \
-H 'accept: application/jwt' \
-H 'Content-Type: application/json' \
-d '{
"username": "User",
"password": "MyPass"
}'
```

All JWT tokens have a limited TTL. You can configure the TTL by using the `ignite.security.jwt.ttl` configuration parameter. By default, all tokens are valid for 3600000ms (8 hours).

## Using JWT in Requests

After you get JWT token as described above, you can send it in the message header instead of using basic authentication:

```bash
curl -X 'GET' \
  'http://cluster_url:10300/management/v1/cluster/state' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer <token>'
```

## Revoking JWT Tokens

GridGain supports two ways to revoke tokens:

- Use the `/management/v1/authentication/jwt` endpoint to revoke all tokens issued to a specific user
- Use the `/management/v1/authentication/jwt/{token}` endpoint to revoke a specific JWT token

{% hint style="info" %}
The user who attempts to revoke tokens must have the `REVOKE_TOKEN` [permission](user-permissions-and-roles.md) on the cluster. Otherwise, the operation will fail.
{% endhint %}

Here is how you can revoke all tokens from a specific user:

```bash
curl -X 'DELETE' \
'http://localhost:10300/management/v1/authentication/jwt?username=John' \
-H 'accept: */*' \
-H 'Authorization: Bearer <token>'
```
