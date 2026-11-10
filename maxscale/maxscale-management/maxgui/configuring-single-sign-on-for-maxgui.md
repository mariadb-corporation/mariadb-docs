---
description: >-
  Set up single sign-on (SSO) for MaxGUI with an OpenID Connect identity
  provider such as Okta or Auth0, without MariaDB Enterprise Manager.
---

# Configuring Single Sign-On for MaxGUI

{% hint style="info" %}
OpenID Connect single sign-on for MaxGUI is available from MaxScale 25.10.
{% endhint %}

MaxScale can delegate MaxGUI sign-in to an external identity provider (IdP) that supports [OpenID Connect](https://openid.net/developers/how-connect-works/) (OIDC), such as Okta, Auth0, Microsoft Entra ID, or Keycloak. Users then sign in with their corporate credentials instead of a MaxScale user name and password. MariaDB Enterprise Manager is not required.

This page shows how to register MaxScale with an IdP, configure MaxScale, and map IdP users to MaxScale permissions. For the protocol details, see [OpenID Connect](../../reference/maxscale-rest-api/maxscale-rest-api.md#openid-connect) in the REST API reference.

## How It Works

1. On the MaxGUI sign-in page, the user selects **Sign In with SSO**. The button is shown only when SSO is configured.
2. MaxScale redirects the browser to the IdP's authorization endpoint, requesting the `openid` and `profile` scopes.
3. After the user authenticates, the IdP redirects the browser back to MaxScale's `/landing` page.
4. With the code flow, MaxScale exchanges the authorization code for an ID token at the IdP's token endpoint, authenticating with the client ID and client secret. It then reads the user's details from the IdP's userinfo endpoint.
5. MaxScale issues its own token for the MaxGUI session. The user's permissions come from claims in the ID token and the userinfo response. See [Step 3: Map Users to Permissions](#step-3-map-users-to-permissions).

Signing out of MaxGUI redirects the browser to the IdP's end-session endpoint, which signs the user out of the IdP, and then back to MaxGUI.

Whether a user can reach MaxScale at all is decided in the IdP, for example by assigning the application to selected users or groups. What the user can do in MaxScale is decided by MaxScale, from the claims the IdP sends.

## Prerequisites

* MaxScale 25.10 or later, with [MaxGUI enabled](configuring-maxscale-for-maxgui.md).
* An administrator account for your IdP.
* The URL that users type to open MaxGUI, such as `https://maxscale.example.com:8989`. MaxScale builds the redirect URIs it sends to the IdP from this URL, so it must be the same URL that you register with the IdP.
* TLS for the MaxScale REST API (recommended). Without it, MaxGUI is only served over plain HTTP if [admin\_secure\_gui](../deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_secure_gui) is disabled, and some IdPs accept plain `http://` redirect URIs only for `localhost`.

## Step 1: Register MaxScale with the Identity Provider

In the IdP, create an application (Okta calls it an app integration) of the following type:

* **Sign-in method:** OpenID Connect (OIDC).
* **Application type:** web application, also called a regular web application or confidential client, which has a client secret.
* **Grant type:** authorization code.
* **Client authentication:** client secret sent with HTTP Basic authentication (`client_secret_basic`). This is the default in most IdPs.

Register these URIs, replacing `https://maxscale.example.com:8989` with your MaxGUI URL:

| IdP setting | Value |
| --- | --- |
| Sign-in redirect URI (also called callback URL) | `https://maxscale.example.com:8989/landing` |
| Sign-out redirect URI (also called post-logout redirect URI) | `https://maxscale.example.com:8989/` |
| Allowed web origin, if the IdP asks for one | `https://maxscale.example.com:8989` |

The scheme is `https` when TLS is enabled for the REST API, and `http` otherwise. The host and port are the ones the browser used to reach MaxScale. If users reach MaxScale through a reverse proxy, or by more than one host name, set [admin\_root\_url](../deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_root_url) to the public URL. MaxScale then builds both redirect URIs from that value instead.

Then assign the application to the users or groups who should have access to MaxGUI, and note down:

* the **client ID**,
* the **client secret**,
* the **issuer URL** of the authorization server. MaxScale appends `/.well-known/openid-configuration` to this URL to discover the IdP's endpoints and signing keys.

To check the issuer URL, open `<issuer URL>/.well-known/openid-configuration` in a browser. It must return a JSON document whose `issuer` field is the same URL.

## Step 2: Configure MaxScale

Set the OIDC parameters at runtime with MaxCtrl:

```bash
maxctrl alter maxscale admin_oidc_url https://idp.example.com/
maxctrl alter maxscale admin_oidc_client_id '<client ID>'
maxctrl alter maxscale admin_oidc_client_secret '<client secret>'
```

Or set them in the `[maxscale]` section of the configuration file and restart MaxScale:

```ini
[maxscale]
admin_oidc_url=https://idp.example.com/
admin_oidc_client_id=<client ID>
admin_oidc_client_secret=<client secret>
```

| Parameter | Purpose |
| --- | --- |
| [admin\_oidc\_url](../deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_oidc_url) | Issuer URL of the IdP. Setting it turns SSO on. |
| [admin\_oidc\_client\_id](../deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_oidc_client_id) | Client ID of the application registered in Step 1. |
| [admin\_oidc\_client\_secret](../deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_oidc_client_secret) | Client secret of that application. |
| [admin\_oidc\_flow](../deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_oidc_flow) | `auto` (default) uses the code flow if the IdP supports it, and the implicit flow otherwise. |
| [admin\_oidc\_extra\_options](../deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_oidc_extra_options) | Extra parameters for the authorization request, such as an Auth0 `audience`. Requires a restart. |
| [admin\_oidc\_ssl\_insecure](../deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_oidc_ssl_insecure) | Skips TLS certificate checks against the IdP. Use it only for testing with a self-signed IdP. |

{% hint style="warning" %}
Treat the client secret like a password. Don't paste it into tickets, chat messages, or slides. If it has been exposed, rotate it in the IdP.
{% endhint %}

The MaxGUI session lasts as long as [admin\_jwt\_max\_age](../deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_jwt_max_age), but never more than eight hours.

## Step 3: Map Users to Permissions

MaxScale reads the following claims from the ID token and the userinfo response, in this order of precedence:

1. **`permissions`:** an array of [REST API permissions](../../reference/maxscale-rest-api/maxscale-role-resource.md#create-a-role) (`admin`, `edit`, `sql`, `view`). If it holds at least one valid permission, MaxScale uses those permissions directly. The `account` claim, if present, is then used only as the display name.
2. **`account`:** the name of a MaxScale role, or an array of role names, in which case the first one that exists is used. The user gets that role's permissions, and later changes to the role in MaxScale apply at once. The built-in roles are `admin` (full access) and `basic` (read-only access). You can create other roles with `maxctrl create role`.
3. **`sub`:** if neither claim is present, MaxScale looks for a MaxScale user whose name matches the IdP's subject identifier, and uses that user's role. Create such users with [maxctrl create user](../administrative-tools-for-mariadb-maxscale-maxctrl/creating-a-rest-api-user-for-maxscale-with-maxctrl.md).

If none of these matches, sign-in fails, and MaxScale logs an authorization failure for the user.

Most IdPs can add a custom claim to the ID token, either a fixed value or one derived from the user's group membership. For example, to give members of an IdP group named `maxscale-admins` full access and everyone else read-only access, configure the IdP to send:

```json
{ "account": "admin" }
```

for members of `maxscale-admins`, and:

```json
{ "account": "basic" }
```

for everyone else.

## Step 4: Test the Sign-In

1. Open MaxGUI in a private browser window.
2. Select **Sign In with SSO**, and sign in at the IdP.
3. Check that MaxGUI opens with the expected permissions. Because the profile is managed by the IdP, MaxGUI's user-management pages are not available to SSO users.

Users who have a MaxScale user name and password can still sign in with them on the same page.

## Provider Notes

The steps above apply to any OIDC provider. The notes below cover settings that commonly need attention in two popular IdPs. Menu names change between IdP releases, so check your IdP's documentation for the current location.

### Okta

* Create an app integration of type **OIDC - OpenID Connect** and **Web Application**, with the redirect URIs from [Step 1](#step-1-register-maxscale-with-the-identity-provider).
* Under **Assignments**, choose whether everyone or only selected groups can use the application.
* Custom claims, such as `account`, are defined on an authorization server, under **Security > API > Authorization Servers > Claims**. Add the claim to the ID token. The authorization server also needs an access policy and a rule that allow your application to sign in.
* Set `admin_oidc_url` to the authorization server's issuer URL, as shown on its **Settings** tab, for example `https://example.okta.com/oauth2/default`. Don't use the `-admin.okta.com` console address.
* To debug sign-in problems, use **Reports > System Log** for authentication events, and the authorization server's **Token Preview** tab to see which claims a user's tokens contain.

### Auth0

* Create an application of type **Regular Web Application**.
* Under **Application URIs**, add the sign-in redirect URI to **Allowed Callback URLs**, the sign-out redirect URI to **Allowed Logout URLs**, and the MaxGUI URL to **Allowed Web Origins**.
* Under **Credentials**, set the authentication method to **Client Secret (Basic)**.
* Set `admin_oidc_url` to your tenant URL, for example `https://example.us.auth0.com/`.
* Add the `account` claim with a post-login Action. For example, this Action gives every user full access. In production, derive the value from the user's roles or metadata instead:

```javascript
exports.onExecutePostLogin = async (event, api) => {
  api.idToken.setCustomClaim("account", "admin");
};
```

* If you use an Auth0 API, pass its identifier with `admin_oidc_extra_options`, for example `admin_oidc_extra_options=audience=my-api`.

## Troubleshooting

* **The Sign In with SSO button is missing.** MaxScale could not read the IdP's discovery document. Check the MaxScale log, check that `admin_oidc_url` is the issuer URL, and check that MaxScale can reach the IdP over HTTPS. Use [admin\_oidc\_ssl\_insecure](../deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_oidc_ssl_insecure) only when testing against a self-signed IdP.
* **The IdP reports a redirect URI mismatch.** The redirect URI that MaxScale sent doesn't exactly match a registered one. Compare scheme, host, and port with the URL in the browser's address bar, or set [admin\_root\_url](../deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_root_url).
* **Sign-in at the IdP succeeds, but MaxGUI rejects the user.** The tokens carry neither a usable `permissions` nor `account` claim, and no MaxScale user matches the `sub` claim. Check which claims the IdP sends, and see [Step 3: Map Users to Permissions](#step-3-map-users-to-permissions).
* **MaxGUI returns to the sign-in page with an error such as `bad_oidc_server_response` or `userinfo_request_failed`.** The token or userinfo request to the IdP failed. Check that the client secret is correct, and that the application uses `client_secret_basic` authentication. The MaxScale log contains the IdP's response.
* To see which MaxGUI settings are in effect, run:

```bash
maxctrl show maxscale | grep -iE "admin_(gui|port|oidc|root_url|secure_gui)"
```

## See Also

* [Configuring MaxScale for MaxGUI](configuring-maxscale-for-maxgui.md)
* [OpenID Connect](../../reference/maxscale-rest-api/maxscale-rest-api.md#openid-connect) in the REST API reference
* [MaxScale Role Resource](../../reference/maxscale-rest-api/maxscale-role-resource.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
