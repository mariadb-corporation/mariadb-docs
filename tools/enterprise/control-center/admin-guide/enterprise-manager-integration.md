---
description: >-
  Configure Control Center for Enterprise Manager: OpenID Connect provider,
  role mapping, certificate trust, HTTPS, and shared identity provider setups.
hidden: true
---

# Enterprise Manager Integration

<!-- DOCS-6280 extended scope (E6). Verified against gmc master @ e46d08169 and gmc-design-docs @ daae73f; review by the Control Center team. -->

MariaDB Enterprise Manager can show the GridGain 8 clusters that Control Center monitors and open them in Control Center with single sign-on. For this, Control Center uses Enterprise Manager as an OpenID Connect provider registered as `em`. Configuring that provider is what enables the integration; there is no separate setting. The registration name must be exactly `em`, because Enterprise Manager uses it in every link it builds into Control Center; any other name breaks the drill-through.

Control Center otherwise runs as usual: agents connect to Control Center, and users browse clusters in Control Center. You apply the settings on this page, and connect Enterprise Manager to Control Center on the Enterprise Manager side. For the Enterprise Manager steps, see [Add a GridGain 8 Cluster](../../mariadb-enterprise-manager/administration/deployment/adding-databases/add-gridgain-8-cluster.md).

## Configure Enterprise Manager as the OpenID Connect Provider

Add the following properties to the Control Center configuration. Replace `<em-host>` with the HTTPS origin of Enterprise Manager as the browser reaches it, and `<cc-url>` with the URL at which users open the Control Center UI.

```properties
spring.security.oauth2.client.registration.em.client-id=cc_sso_service_account
spring.security.oauth2.client.registration.em.client-secret=<sso-client-secret>
spring.security.oauth2.client.provider.em.authorization-uri=https://<em-host>/authorize
spring.security.oauth2.client.provider.em.token-uri=https://<em-host>/token
spring.security.oauth2.client.provider.em.jwk-set-uri=https://<em-host>/jwks
control.base-url=<cc-url>
```

| Property                                                       | Description                                                                                                                                                     |
| -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `spring.security.oauth2.client.registration.em.client-id`      | Always `cc_sso_service_account`, the Enterprise Manager account that Control Center authenticates as.                                                          |
| `spring.security.oauth2.client.registration.em.client-secret`  | The SSO client secret. Use the same value as the **SSO client secret** set in Enterprise Manager under **Settings**, **Control Center**.                         |
| `spring.security.oauth2.client.provider.em.authorization-uri`  | Enterprise Manager's authorization endpoint, `https://<em-host>/authorize`.                                                                                     |
| `spring.security.oauth2.client.provider.em.token-uri`          | Enterprise Manager's token endpoint, `https://<em-host>/token`.                                                                                                 |
| `spring.security.oauth2.client.provider.em.jwk-set-uri`        | Enterprise Manager's key set, `https://<em-host>/jwks`. Control Center uses it to verify the tokens Enterprise Manager signs.                                    |
| `control.base-url`                                             | The Control Center frontend URL, the same value entered as the **Control Center URL** in Enterprise Manager, for example `https://<cc-host>:8443`. Control Center builds the sign-in redirect URL from it. Required when the Control Center frontend and backend differ in host or port, which includes every Docker and Kubernetes installation. A binary installation needs it only behind a proxy. For the frontend ports, see [Serve Control Center over HTTPS](#serve-control-center-over-https). |

{% hint style="warning" %}
Do not set these two properties for the `em` provider:

* `spring.security.oauth2.client.provider.em.issuer-uri`: Control Center would read Enterprise Manager's discovery document at startup and check the issuer. The check fails, and Control Center does not start.
* `spring.security.oauth2.client.provider.em.user-info-uri`: Control Center reads the user's role from the ID token that Enterprise Manager issues at sign-in (see [Role Attribute Sources](open-id.md#role-attribute-sources)). Enterprise Manager's user info endpoint carries no role. When the access token expires after 8 hours, the calls to it fail and log an error every 10 seconds.
{% endhint %}

When the `em` provider is configured, Control Center creates the account `em-service-user@controlcenter.local` on its next start. Enterprise Manager uses this regular account to read the cluster list. The account joins the Global Team.

## Set the Account Properties

Set these account properties, skipping any already at the value shown:

```properties
account.oidc.rbac.enabled=true
account.oidc.skipSignUp=true
account.globalTeam.enabled=true
account.globalTeam.attachCluster=true
```

| Property                           | Why it is needed                                                                                                                                                         |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `account.oidc.rbac.enabled`        | Maps each user's Enterprise Manager role to a Control Center access level through the `cc-role` claim. See [Access Levels](#access-levels).                              |
| `account.oidc.skipSignUp`          | Creates the user's Control Center account on their first **Manage GridGain** and opens the cluster directly. Without it, the first sign-in stops at the Control Center sign-up form. |
| `account.globalTeam.enabled`       | Creates the Global Team, which includes every user. This is the default.                                                                                                 |
| `account.globalTeam.attachCluster` | Shares every cluster with the Global Team, so every user sees every cluster. This is the default.                                                                       |

For details of these properties, see [Configuration Parameters](configuration.md).

### Access Levels

| Enterprise Manager role                                 | Control Center access                                          |
| ------------------------------------------------------- | -------------------------------------------------------------- |
| `admin`                                                 | Administrator, including the **Administration** area           |
| `viewer`, `basic`, `monitoring-admin`, and any other role | Regular user, without the **Administration** area            |

Only the built-in `admin` role, matched by exact name, maps to Control Center administrator access. A custom Enterprise Manager role maps to regular access even when it has full permissions, and so does a role whose name differs only in case, such as `Admin`. Neither case reports an error; the user signs in and sees no **Administration** area.

A role change in Enterprise Manager takes effect the next time the user signs in to Control Center.

Users who sign in to Control Center directly through another identity provider get their role from that provider's `cc-role` claim, not from Enterprise Manager. A user without a `cc-role` claim gets no access. See [Use a Shared Identity Provider](#use-a-shared-identity-provider).

## Trust the Enterprise Manager Certificate

Control Center calls Enterprise Manager over HTTPS to read its key set and exchange tokens. Enterprise Manager uses a certificate from a private CA by default, so Control Center must trust that CA. Otherwise Control Center cannot verify Enterprise Manager's tokens, and no clusters appear in Enterprise Manager; the Control Center log shows `PKIX path building failed`. If Enterprise Manager's certificate comes from a public CA, Control Center already trusts it, and you can skip this section.

The Enterprise Manager installer creates the private CA and saves its certificate as `certs/ca-cert.pem` in the installation folder. Control Center reads trusted certificates from the standard Java trust store, as described in [Configuring SSL Without Management Script](../installation/install-binary.md#configuring-ssl-without-management-script).

{% hint style="warning" %}
Setting `javax.net.ssl.trustStore` replaces the default Java trust store. Build the trust store from a copy of the Java `cacerts` file, not from an empty one. Otherwise Control Center stops trusting public CAs.
{% endhint %}

1. Copy the Java `cacerts` file and import the Enterprise Manager CA into the copy. `changeit` is the default password of `cacerts`:

   ```bash
   cp $JAVA_HOME/lib/security/cacerts cc-truststore.jks
   keytool -importcert -noprompt -trustcacerts \
     -alias em-ca \
     -file ca-cert.pem \
     -keystore cc-truststore.jks \
     -storepass changeit
   ```

   If Java isn't installed on the host, run the same commands from the Control Center backend image. Replace `<tag>` with the image tag you run:

   ```bash
   docker run --rm -v "$PWD:/certs" gridgain/control-center-backend:<tag> sh -c \
     'cp /opt/java/openjdk/lib/security/cacerts /certs/cc-truststore.jks && \
      /opt/java/openjdk/bin/keytool -importcert -noprompt -trustcacerts -alias em-ca \
        -file /certs/ca-cert.pem -keystore /certs/cc-truststore.jks -storepass changeit'
   ```

2. Point the Control Center JVM at the trust store by adding these options to `JVM_OPTS`:

   ```text
   -Djavax.net.ssl.trustStore=/path/to/cc-truststore.jks
   -Djavax.net.ssl.trustStorePassword=changeit
   ```

   Setting `JVM_OPTS` replaces the default memory settings of `control-center.sh`, so include your heap settings as well, for example `-Xms1g -Xmx2g -server -XX:MaxMetaspaceSize=256m -XX:MaxDirectMemorySize=1g`.

   In Docker and Kubernetes, set `JVM_OPTS` as an environment variable of the Control Center backend container and mount the trust store file:

   ```yaml
   control-center-backend:
     environment:
       JVM_OPTS: "-Djavax.net.ssl.trustStore=/certs/cc-truststore.jks -Djavax.net.ssl.trustStorePassword=changeit"
     volumes:
       - ./cc-truststore.jks:/certs/cc-truststore.jks:ro
   ```

3. Restart Control Center.

## Serve Control Center over HTTPS

Enterprise Manager and users' browsers reach Control Center through its frontend. The frontend of a Docker or Kubernetes installation serves plain HTTP on port `8008`. When you mount a certificate and its private key, it also serves HTTPS on port `8443` and keeps `8008`. A CA certificate alone is not enough: Control Center needs its own certificate and the matching private key.

| Environment variable | Default                          | Description                                |
| -------------------- | -------------------------------- | ------------------------------------------ |
| `CC_TLS_CERT`        | `/etc/nginx/server.crt`          | Path to the certificate inside the frontend container. |
| `CC_TLS_KEY`         | `/etc/nginx/server.nopass.key`   | Path to the private key inside the frontend container. |
| `CC_TLS_PORT`        | `8443`                           | The HTTPS port.                            |

Mount the files at the default paths, or set the variables to the paths you mount:

```yaml
control-center-frontend:
  environment:
    CC_TLS_CERT: /etc/nginx/cert.pem
    CC_TLS_KEY: /etc/nginx/key.pem
  volumes:
    - ./cert.pem:/etc/nginx/cert.pem:ro
    - ./key.pem:/etc/nginx/key.pem:ro
  ports:
    - "8443:8443"
```

Without a certificate and key at those paths, the frontend serves only HTTP on `8008`.

Then use the HTTPS address as the **Control Center URL** in Enterprise Manager and as `control.base-url`, for example `https://<cc-host>:8443`. If the certificate comes from a private CA, Enterprise Manager must trust that CA: set **Control Center CA certificate path** as described in [Add a GridGain 8 Cluster](../../mariadb-enterprise-manager/administration/deployment/adding-databases/add-gridgain-8-cluster.md#connect-enterprise-manager-to-control-center).

For a binary installation, which serves the frontend and backend on one port, see [SSL Configuration](../installation/install-binary.md#ssl-configuration). For Kubernetes, see [Running Control Center and GridGain with Encryption](kubernetes-tls.md).

## How Control Center Is Secured in This Integration

On each connection, the caller checks the server's TLS certificate against its trust store, and the server identifies the caller by a signed token, a client secret, or a user session. Certificates play no part in identifying the caller. For all five connections, including the ones that don't involve Control Center, see [How the Connections Are Secured](../../mariadb-enterprise-manager/administration/deployment/adding-databases/add-gridgain-8-cluster.md#how-the-connections-are-secured). These are the connections that Control Center is part of:

* **Enterprise Manager → Control Center.** Enterprise Manager reads the GridGain 8 clusters and their nodes. Enterprise Manager sends a JSON Web Token (JWT) with each call. It signs the JWT with its private key, and the JWT is valid for 5 minutes. Control Center checks the signature with Enterprise Manager's public keys from `jwk-set-uri`, caches the keys for 5 minutes, and fetches them again when a JWT carries an unknown key ID. No password is involved. Control Center serves the clusters to the account `em-service-user@controlcenter.local`, which it creates at startup. Enterprise Manager checks Control Center's certificate against the CA you set in **Control Center CA certificate path**, or against public CAs when the field is empty.
* **Control Center → Enterprise Manager.** Control Center reads Enterprise Manager's public keys from `/jwks`, which needs no sign-in because it serves only public keys. At sign-in, it also exchanges an authorization code at `/token` for an ID token that carries the user's email and `cc-role`. The code is valid for 30 seconds. To call `/token`, Control Center signs in to Enterprise Manager as `cc_sso_service_account` with the SSO client secret. Control Center checks Enterprise Manager's certificate against its Java trust store. See [Trust the Enterprise Manager Certificate](#trust-the-enterprise-manager-certificate).
* **Browser → Control Center.** The browser checks Control Center's certificate against its own trust store or the operating system's. Control Center starts its own session after the **Manage GridGain** sign-in.
* **Control Center agent → Control Center.** The integration doesn't change this connection. See [SSL Configuration](../installation/install-binary.md#ssl-configuration).

The SSO client secret is the password of the Enterprise Manager user `cc_sso_service_account`. The value in `spring.security.oauth2.client.registration.em.client-secret` must match the one saved in Enterprise Manager. If they differ, the code exchange at `/token` fails, and **Manage GridGain** doesn't sign users in. See [The SSO Client Secret](../../mariadb-enterprise-manager/administration/deployment/adding-databases/add-gridgain-8-cluster.md#the-sso-client-secret).

## Use a Shared Identity Provider

Enterprise Manager and Control Center can sign users in through the same external OpenID Connect identity provider. The steps use Keycloak. In the steps, `<kc-url>` is the realm URL, `https://<kc-host>/realms/<realm>`, `<em-url>` is the browser-facing origin of Enterprise Manager, and `<cc-url>` is the value of `control.base-url`.

### Setup A: Control Center Signs In Through Enterprise Manager (Recommended)

Keep the `em` registration from [Configure Enterprise Manager as the OpenID Connect Provider](#configure-enterprise-manager-as-the-openid-connect-provider). **Manage GridGain** signs users in through Enterprise Manager, which signs them in through Keycloak without another prompt.

1. In Keycloak, create an OpenID Connect client for Enterprise Manager and configure Enterprise Manager to use it. See [Configure OpenID Connect Identity Provider](../../mariadb-enterprise-manager/administration/user-management/configure-openid-connect-identity-provider.md).
2. Optional, for users who sign in to Control Center directly: in Keycloak, create a second client, for example `control-center`, with **Client authentication** and **Standard flow** on, and **Valid redirect URIs** set to `<cc-url>/api/v1/oauth2/login/keycloak`. Add a mapper that puts a `cc-role` claim with the value `admin` or `regular` on the ID token and the userinfo response.
3. Add that client to Control Center as a second registration, next to `em`:

   ```properties
   spring.security.oauth2.client.registration.keycloak.provider=keycloak
   spring.security.oauth2.client.registration.keycloak.client-id=control-center
   spring.security.oauth2.client.registration.keycloak.client-secret=<client-secret>
   spring.security.oauth2.client.registration.keycloak.scope=openid,profile,email
   spring.security.oauth2.client.provider.keycloak.issuer-uri=<kc-url>
   ```

A user who signs in to Control Center directly through Keycloak gets the role from the `cc-role` claim. Without the claim, the user gets no access. If you set `account.oidc.rbac.enabled=false` instead, every account that Control Center creates at single sign-on gets regular access, including Enterprise Manager administrators.

### Setup B: Control Center Signs In Through Keycloak Directly

**Manage GridGain** goes from Control Center to Keycloak and back, without Enterprise Manager signing the user in.

1. Create Enterprise Manager's Keycloak client and configure Enterprise Manager, as in step 1 of Setup A.
2. In Keycloak, create Control Center's client as in step 2 of Setup A, with **Valid redirect URIs** set to `<cc-url>/api/v1/oauth2/login/em`. In the client's **Advanced** tab, set **ID token signature algorithm** to `PS256`. In **Realm settings**, **Keys**, add an `rsa-generated` key provider with **Algorithm** set to `PS256`. Control Center expects ID tokens for the `em` registration to be signed with `PS256`.
3. Keep the three `spring.security.oauth2.client.provider.em.*` endpoints from [Configure Enterprise Manager as the OpenID Connect Provider](#configure-enterprise-manager-as-the-openid-connect-provider). Control Center still verifies Enterprise Manager's service token with `jwk-set-uri`. Point the `em` registration at Keycloak:

   ```properties
   spring.security.oauth2.client.registration.em.provider=keycloak
   spring.security.oauth2.client.registration.em.client-id=control-center
   spring.security.oauth2.client.registration.em.client-secret=<client-secret>
   spring.security.oauth2.client.registration.em.scope=openid,profile,email
   spring.security.oauth2.client.provider.keycloak.issuer-uri=<kc-url>
   ```

In Setup B, Control Center calls Keycloak when a user selects **Manage GridGain**: Keycloak sends the browser back to Control Center with an authorization code, and Control Center exchanges the code for the user's ID token. Control Center checks Keycloak's certificate against its Java trust store. If Keycloak's certificate comes from a private CA, import that CA into the same trust store as Enterprise Manager's CA. See [Trust the Enterprise Manager Certificate](#trust-the-enterprise-manager-certificate).
