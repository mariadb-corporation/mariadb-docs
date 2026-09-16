---
description: >-
  Authenticate GridGain 9 REST API requests using Basic authentication or
  token-based JWT Bearer authentication, and revoke issued tokens.
---

# REST Authentication

When using GridGain 9’s REST API, you can authenticate your requests using either Basic authentication or a token-based (Bearer flow) authentication. Tokens are issued through an OAuth 2.0–style mechanism.

To use REST authentication, first [enable](../../administrators-guide/security/authentication.md) it on in cluster configuration.

## Authentication Methods

### Basic Authentication

When using Basic authentication, the client sends a Base64-encoded string in the Authorization header on each request. This string is constructed from the username and password in the following format:

```
username:password
```

Then, authorization is added to the request header:

```
Authorization: Basic <base64(username:password)>
```

Here is how a request secured by basic authorization may look like:

```bash
curl -X GET "http://localhost:10300/management/v1/cluster/topology/logical" -H "Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ=="
```

Here, `QWxhZGRpbjpvcGVuIHNlc2FtZQ==` is the Base64 encoding of `Aladdin:open sesame`.

{% hint style="info" %}
Although HTTPS encrypts the transmission, using Basic authorization requires sending the username and password in every request. This approach is supported primarily for backward compatibility or controlled environments. For production use, token-based authentication is recommended as it provides improved security.
{% endhint %}

### JWT Bearer Authentication (Token-Based)

When using the JWT Bearer authentication, the client first obtains a JSON Web Token (JWT) by sending the username and password to the authentication endpoint and then uses this token in all subsequent requests. This token adheres to an OAuth 2.0–like design and is then used for subsequent requests.

#### Obtaining a Token

To obtain the token required for the authentication, send the POST request to the `/management/v1/authentication/login` endpoint. Request body should be a JSON formatted in the following way:

```json
{
  "username": "user@example.com",
  "password": "yourPassword"
}
```

The example below shows how you can get the authorization token:

```bash
curl -X POST "http://localhost:10300/management/v1/authentication/login" -H "Content-Type: application/json" -d '{"username": "user@example.com","password": "yourPassword"}'
```

On success, the endpoint returns a JWT token in the response. The token is then used as a Bearer token in the Authorization header for all subsequent API calls.

#### Using the Bearer Token

Once you obtained the token, include it in the Authorization header for your requests:

```
Authorization: Bearer <your_jwt_token>
```

Here is how you can do it in when using curl:

```bash
curl -X GET "https://your-gridgain-host:port/your-endpoint" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

## Token Expiration and Cancellation

Issued tokens expire according to cluster [security](../../administrators-guide/config/cluster-config.md#security-configuration) configuration. If a token needs to be revoked sooner, you can cancel it by sending a dedicated endpoint. GridGain supports two ways to revoke tokens:

- Use the `/management/v1/authentication/jwt` endpoint to revoke all tokens issued to a specific user
- Use the `/management/v1/authentication/jwt/{token}` endpoint to revoke a specific JWT token

{% hint style="info" %}
The user who attempts to revoke tokens must have the `REVOKE_TOKEN` [permission](../../administrators-guide/security/permissions.md) on the cluster. Otherwise, the operation will fail.
{% endhint %}

Here is how you can revoke all tokens from a specific user:

```bash
curl -X 'DELETE' 'http://localhost:10300/management/v1/authentication/jwt?username=John' -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'
```
