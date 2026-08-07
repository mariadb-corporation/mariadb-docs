---
description: >-
  Setting up OpenID Connect authentication for GridGain Control Center,
  including RBAC, scopes, redirect URI, and provider configuration.
---

# OpenID Connect Authentication

Set up OpenID authentication so users can log in to Control Center using their OpenID accounts, allowing them to bypass traditional email and password sign-in to simplify access management. Authentication can be restricted exclusively to OpenID, preventing the creation of login-password accounts. Additionally, role management could be handled via OpenID, meaning that both authentication and role assignments are controlled externally.

## Enable RBAC via OpenId Connect

To enable Control Center role assignment using OpenID Connect accounts, update your [configuration file](configuration.md) with the following properties:

- `account.oidc.rbac.enabled`: Set to `true` to activate OpenID-based role management and enable OpenID login. You also need to [configure](#add-openid-to-configuration) `spring.security.oauth2.client.provider.{name}.user-info-uri` property for this setting to take effect.
- `account.oidc.rbac.attributeName`: OpenID Connect attribute name that is used in your OpenID configuration to define the Control Center role. The default attribute name is `cc-role`, but you can use any custom name. This attribute can define the following Control Center roles:

- `admin` - Users with this role will have administrator permissions in Control Center.
- `regular` - Users with this role will have user permissions in Control Center.
- `no-access` - Users with this role will have no access to Control Center.

{% hint style="info" %}
When user roles are managed via OpenID Connect, manual admin assignments or user locks will cause errors. To allow some users to be managed via OpenID Connect while others remain as regular users, set `account.internal.enabled` to `true`.
{% endhint %}

Below is an example of a configuration file section related to configuring OpenID:

{% tabs %}
{% tab title="YAML" %}
```yaml
# Sign up configuration.
# Deprecated: account.signup.enabled is replaced by account.self-registration.enabled.
account:
    self-registration:
        enabled: true
    internal:
        enabled: false
    oidc:
        skipSignUp: false
        rbac:
            enabled: true
            attributeName: cc-role
```
{% endtab %}

{% tab title="XML" %}
```xml
<properties>
    <entry key="account.self-registration.enabled">true</entry>
    <entry key="account.internal.enabled">false</entry>
    <entry key="account.oidc.skipSignUp">false</entry>
    <entry key="account.oidc.rbac.enabled">true</entry>
    <entry key="account.oidc.rbac.attributeName">cc-role</entry>
</properties>
```
{% endtab %}
{% endtabs %}

To restrict Control Center authentication to OpenID exclusively, configure the following options:

- `account.internal.enabled`: Set to `false` to disable Control Center’s built-in email and password authentication. Role management via OpenID Connect will be available in any case, if internal accounts are enabled or not.
- `account.oidc.skipSignUp`: Set to `true` to skip password creation during OpenID authentication for quicker access. If `account.internal.enabled` is disabled, this property doesn't need to be configured.

{% hint style="info" %}
Keep in mind that setting `account.self-registration.enabled` to `false` will disable any kind of self sign up for OpenID users, meaning that new user accounts must be created by an administrator in Control Center.
{% endhint %}

## Authenticate Cluster Actions via OpenId Connect

When OpenID provider-based login is enabled in Control Center, any GridGain 8 cluster action such as starting SQL or renaming the cluster will trigger an authentication prompt, asking users to log in with either Control Center credentials or an OpenID account.

To control access to cluster actions, both the OpenID provider configuration and the cluster must specify an attribute that contains the user's role name, which determines their permissions on the cluster.

To do so, you need to configure the `permissionsJson` scope, which defines the role name and its corresponding [permissions](../gg8/auth/authorization-permissions.md) for the user, and the `claimName` attribute in the GridGain 8 cluster [configuration](https://www.gridgain.com/docs/latest/administrators-guide/security/authentication#control-center-openid-authentication) file.

You can configure the `claimName` attribute in two ways:

- Define a field named `gg-role` in your OpenID provider, as by default the cluster will look for an attribute named `gg-role`. Then assign this claim a value that matches one of the roles defined in the `permissionsJson` map.
- Specify a custom attribute name by setting the `claimName` field in the configuration file. For example, if you set `claimName` to `my-cluster-role`, ensure that in your OpenID provider it is assigned a value that matches one of the roles defined in the `permissionsJson` map (e.g., `mycache` to allow read and destroy operations on `MYCACHE`).

The example below shows how to create a custom `claimName` attribute with the `my-cluster-role` role, assuming that on the OpenID provider side, `my-cluster-role` is assigned either `mycache` or `default` permissions.

```xml
<property name="authenticator">
                        <bean class="org.gridgain.grid.security.composite.CompositeAuthenticator">
                            <property name="authenticators">
                                <list>
                                    <bean class="org.gridgain.grid.security.passcode.PasscodeAuthenticator">
                                        <!-- Set acl provider. -->
                                        <property name="aclProvider">
                                            <bean class="org.gridgain.grid.security.passcode.AuthenticationAclBasicProvider">
                                                <constructor-arg>
                                                    <map>
                                                        <entry key-ref="node.cred" value="{defaultAllow:true}"/>
                                                        <entry key-ref="cc_login.user.cred" value="{defaultAllow:true, {cache:'allow_cache', permissions:[CACHE_READ, CACHE_PUT, CACHE_REMOVE]},{cache:'deny_cache', permissions:[]}}"/>
                                                    </map>
                                                </constructor-arg>
                                            </bean>
                                        </property>
                                    </bean>
                                    <bean class="org.gridgain.grid.security.oidc.OpenIdAuthenticator">
                                        <property name="userInfoUrl" value="{user_info_url}"/>
                                        <property name="claimName" value="my-cluster-role"/>
                                        <property name="permissionsJson">
                                            <map>
                                                <entry key="default" value="{defaultAllow:true}"/>
                                                <entry key="mycache" value="{defaultAllow:false, {cache:'MYCACHE*',permissions:['CACHE_READ','CACHE_DESTROY']}}"/>
                                            </map>
                                        </property>
                                    </bean>
                                </list>
                            </property>
                        </bean>
                    </property>
```

## Get OpenID Credentials

First, set up OpenID credentials for your chosen OpenID provider. Specify the following parameters in your configuration:

### Scopes

Control Center requests the scopes defined in the `spring.security.oauth2.client.scope` property, which by default includes `openid`, `profile`, and `email`.

For features such as RBAC and role management via OpenID connect, a refresh token is required. Adding the `offline_access` scope lets Control Center to obtain a refresh token, which automatically renews access tokens requiring the user to log in again. This also helps maintain long-lived sessions and enables background tasks to run uninterrupted on behalf of the user.

### Redirect URI

Redirect URI is required for your OpenID provider to know where to send responses to user authentication requests. The URI for Control Center uses the `http://{host}:{port}/api/v1/oauth2/login/{providerName}`, where `providerName` is the name you specify in the configuration file on the following step.

For example, if you use Google as a provider and run Control Center on `localhost:3100`, your redirect URI is:

```
http://localhost:3100/api/v1/oauth2/login/google
```

If frontend and backend have different hosts or ports, set a `control.base-url` value equal to frontend URI, for example `https://example.com:1234`.

### Client ID and Secret

OpenID provider generates ID and secret, which should then be specified in the configuration file.

## Add OpenID to Configuration

To connect Control Center to your OpenID provider, add OpenID configuration to the [Configuration file](configuration.md).

The following configuration sets up a connection to Google's OAuth 2.0 API:

```yaml
spring.security.oauth2.client:
    # Define client credentials.
    registration:
        # You can specify any name as long as it is consistent
        # with the name in the provider section and redirect URI.
        google:
            client-id: {your-ID}
            client-secret: {your-secret}
    # Define your OpenID provider endpoints.
    # Most services provide this  information on a .well-known page.
    # For this example we use Google endpoints,
    # taken from the https://accounts.google.com/.well-known/openid-configuration page.
    provider:
        google:
            authorization-uri: https://accounts.google.com/o/oauth2/v2/auth # authorization_endpoint
            token-uri: https://oauth2.googleapis.com/token # token_endpoint
            jwk-set-uri: https://www.googleapis.com/oauth2/v3/certs # jwks_uri
            user-info-uri: https://openidconnect.googleapis.com/v1/userinfo # userinfo_endpoint
```

After the configuration is set up, restart Control Center. Users can now log in by using their OpenID credentials.

## Communications Between Control Center and OIDC Provider

According to the OIDC specification, during the Authorization Code Flow, Control Center must exchange authorization code for a token pair via an [HTTP POST request](https://openid.net/specs/openid-connect-basic-1_0.html#ObtainingTokens) (from the Control Center backend to the OIDC provider's token endpoint). Make sure that the Control Center backend is allowed to perform such requests.

{% hint style="warning" %}
If you get an error during the login flow, after finishing the login phase at the OIDC provider site, this is most likely due to the HTTP POST request failure.
{% endhint %}

Possible reasons for the above failure are:

- Firewall blocks the outgoing requests - verify firewall settings and adjust them as required.
- Connectivity issues between Control Center and the remote OIDC provider - verify network settings and adjust them as required. You can use the cURL utility to test connectivity between Control Center and the external OIDC provider:

  ```bash
  curl -X POST -u $CLIENT_ID:$CLIENT_SECRET --data-urlencode "grant_type=authorization_code" --data-urlencode "code=ignored" $OIDC_PROIVDER_TOKEN_URL
  ```

  You should get and error response HTTP 4xx with content similar to:

  ```json
  {"error":"invalid_grant","error_description":"Code not valid"}
  ```
- The remote OIDC provider uses self-signed SSL certificate - import this certificate to Control Center truststore.
