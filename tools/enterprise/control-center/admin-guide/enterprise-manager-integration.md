---
description: >-
  Configure Control Center for MariaDB Enterprise Manager: use it as the
  OpenID Connect provider, map its roles to Control Center access, and trust
  its certificate.
hidden: true
---

# Enterprise Manager Integration

<!-- DOCS-6280 extended scope (E6). Verified against gmc master @ 4989bb129; review by the Control Center team. -->

MariaDB Enterprise Manager can show the GridGain 8 clusters that Control Center monitors and open them in Control Center with single sign-on. For this, Control Center uses Enterprise Manager as an OpenID Connect provider named `em`. Configuring that provider is what enables the integration; there is no separate setting.

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
| `control.base-url`                                             | The Control Center frontend URL, the same value entered as the **Control Center URL** in Enterprise Manager, for example `https://<cc-host>:8008`. Control Center builds the sign-in redirect URL from it. Required when the Control Center frontend and backend differ in host or port, which includes every Docker and Kubernetes installation. A binary installation needs it only behind a proxy. |

{% hint style="warning" %}
Do not set these two properties for the `em` provider:

* `spring.security.oauth2.client.provider.em.issuer-uri`: Control Center would read Enterprise Manager's discovery document at startup and check the issuer. The check fails, and Control Center does not start.
* `spring.security.oauth2.client.provider.em.user-info-uri`: Control Center reads the user's role from the ID token that Enterprise Manager issues at sign-in. Enterprise Manager's user info endpoint carries no role. When the access token expires after 8 hours, the calls to it fail and log an error every 10 seconds.
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

If Control Center uses another identity provider instead of Enterprise Manager, either set `account.oidc.rbac.enabled=false` so that every authenticated user gets regular access, or have that provider issue a `cc-role` claim with the value `admin` or `regular`.

## Trust the Enterprise Manager Certificate

Control Center calls Enterprise Manager over HTTPS to read its key set and exchange tokens. Enterprise Manager uses a self-signed certificate by default, so Control Center must trust it. Otherwise Control Center cannot verify Enterprise Manager's tokens, and no clusters appear in Enterprise Manager. A certificate signed by a public CA is already trusted.

<!-- DOCS-6280 TODO (Control Center team review): gmc assembly/README.txt says to use server.ssl.trust-store, but the JWK set is fetched by Spring's default NimbusJwtDecoder (EmJwtDecoderConfig), which uses the JVM trust store. Confirm the procedure below. -->

1. Import the Enterprise Manager certificate into a trust store:

   ```bash
   keytool -importcert -noprompt \
     -alias enterprise-manager \
     -file em-cert.pem \
     -keystore em-trust.jks \
     -storepass <trust-store-password> \
     -storetype JKS
   ```

2. Point the Control Center JVM at the trust store by adding these options to `JVM_OPTS`:

   ```text
   -Djavax.net.ssl.trustStore=/path/to/em-trust.jks
   -Djavax.net.ssl.trustStorePassword=<trust-store-password>
   ```

   Setting `JVM_OPTS` replaces the default memory settings of `control-center.sh`, so include your heap settings as well, for example `-Xms1g -Xmx2g`. In Docker and Kubernetes, set `JVM_OPTS` as an environment variable of the Control Center backend container and mount the trust store file.

3. Restart Control Center.
