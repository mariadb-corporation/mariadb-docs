---
description: >-
  Run a multi-tenant MariaDB MCP server in a container with Docker Compose or
  Podman, behind a TLS-terminating reverse proxy, with API keys, the built-in
  authorization server, or Keycloak.
---

# Running in a Container

The MariaDB Shell container image runs a [multi-tenant](multi-tenant-mode.md) MCP server over streamable HTTP. Every request needs an API key or an OAuth2 access token, and each user has their own connections. This page shows how to run it with Docker Compose or Podman Compose, behind a reverse proxy that terminates TLS, in two setups:

* [Without Keycloak](#setup-without-keycloak): users sign in with their MariaDB account, or use API keys.
* [With Keycloak](#setup-with-keycloak): Keycloak signs users in, in a realm that the container prepares on its first start.

The image doesn't serve a single-user server or the `stdio` transport. For an MCP client on your own machine, run MariaDB Shell directly, as described in [Starting the MCP Server](starting-the-mcp-server.md).

## The Image

The image is available for `linux/amd64` and `linux/arm64`, and is based on Debian. It contains a MariaDB Shell release and nothing else: no MariaDB server and no [migration tooling](migration-tooling.md). The server provides the `db` tools, the only group of a multi-tenant server.

| Property | Value |
| --- | --- |
| Port | `8080`, plain HTTP |
| User | `mcp`, uid `10001` |
| Volume | `/home/mcp`: the configuration, the users, and the [credential store](../connecting/credential-store.md) with the users' API keys and connection passwords |
| Default command | `start-server` |

On its first start, the container configures the server from [environment variables](#environment-variables) and then starts it. On later starts, it applies the variables again only if one of them changed, and prepares the Keycloak realm again only if the mode, the public URL or a `KEYCLOAK_*` variable changed. So a secret that is needed only for the first start, such as the Keycloak administrator password, can be removed afterwards. Removing a variable doesn't always undo its setting. A server taken out of `MCP_LOGIN_SERVERS` is removed, removing `MCP_REQUIRED_ROLE` clears the role, and the variables that `mcp start-server` reads (`MCP_TRUSTED_PROXIES`, `MCP_ALLOWED_HOSTS`, `MCP_MAX_CONNECTIONS` and `MCP_PORT`) apply on every start. What the others created stays: the user from `MCP_INITIAL_USER`, and the client, role grants and login theme in the Keycloak realm. Remove them with `mcp setup` or in the Keycloak administration console.

A program of the image, such as `sh`, runs as it is. Any other command runs `mariadb-shell` with its arguments. Use this to administer a running server:

```bash
docker compose exec mcp mariadb-shell -- mcp setup --show --allUsers
```

{% hint style="warning" %}
The volume holds every user's API key and connection passwords. The `login-path` credential store only obfuscates them. Restrict access to the volume and its backups as you would to the passwords themselves.
{% endhint %}

The files in the volume are private to the user that created them, so a volume stays with that uid. A container started under another uid, for example with `--user` or by OpenShift, can set up a new volume, but stops with *belongs to uid …* on one that another uid set up. Run it as that uid, or change the owner of the volume's files.

### Build the Image

To build the image yourself, use the `docker` folder of the [MariaDB Shell repository](https://github.com/mariadb-corporation/mariadb-shell/tree/main/docker). The build downloads the release that `VERSION` names for each platform and checks it against the release's checksums; nothing is compiled:

```bash
docker buildx build --platform linux/amd64,linux/arm64 \
  --build-arg VERSION=<version> -t mariadb/mariadb-shell-mcp-server:<version> \
  -f docker/linux-debian13-mcp-server.Dockerfile docker
```

With Podman and other clients that don't resolve short names through Docker Hub, use the fully qualified name, `docker.io/mariadb/mariadb-shell-mcp-server`.

## Environment Variables

| Variable | Mode | Description |
| --- | --- | --- |
| `MCP_OAUTH_MODE` | All | `none` (API keys only, the default), `builtin`, or `keycloak`. API keys work in every mode. See [OAuth Authentication](oauth-authentication.md). |
| `MCP_PUBLIC_URL` | `builtin`, `keycloak` | The URL that clients reach the MCP endpoint at, including `/mcp`, for example `https://mcp.example.com/mcp`. See [The Public URL](oauth-authentication.md#the-public-url). |
| `MCP_INITIAL_USER` | All | A user to create on the first start, by email address or user ID. A server without users starts only in a mode that creates users at their first sign-in. |
| `MCP_LOGIN_SERVERS` | `builtin` | The MariaDB servers that users sign in to, as connection URIs without a user. The list is complete: a server removed from it is removed from the configuration. |
| `MCP_REQUIRED_ROLE` | `builtin` | The MariaDB role that an account must hold to sign in. Without it, every account may sign in. |
| `KEYCLOAK_URL` | `keycloak` | The Keycloak base URL, for example `https://kc.example.com`. |
| `KEYCLOAK_REALM` | `keycloak` | The realm to prepare. It must exist. |
| `KEYCLOAK_ADMIN_REALM` | `keycloak` | The realm that the administrator signs in to. Default: `master`. |
| `KEYCLOAK_ADMIN_USER` | `keycloak` | The Keycloak administrator. |
| `KEYCLOAK_ADMIN_PASSWORD_FILE` | `keycloak` | A file that contains the administrator's password, for example a Compose secret. `KEYCLOAK_ADMIN_PASSWORD` takes the password itself instead, but stays visible in the container's configuration. |
| `KEYCLOAK_CLIENT_ID` | `keycloak` | The client created for MCP clients. Default: `mariadb-mcp`. |
| `KEYCLOAK_GRANT_ROLE_TO` | `keycloak` | Comma-separated Keycloak users to give the realm role `mcp-user`. |
| `KEYCLOAK_LOGIN_THEME` | `keycloak` | A login theme to select for the realm, such as `mariadb-mcp`. See [Use the MariaDB Login Theme](oauth-authentication.md#use-the-mariadb-login-theme). |
| `MCP_TRUSTED_PROXIES` | All | The addresses that the reverse proxy's requests arrive from. See [Reverse Proxy](#reverse-proxy). |
| `MCP_ALLOWED_HOSTS` | All | Additional `Host` header values to accept. In `none` mode behind a reverse proxy, the proxy's host name, for example `mcp.example.com`. See [Host and Origin Validation](security-and-session-handling.md#host-and-origin-validation). |
| `MCP_MAX_CONNECTIONS` | All | The most database connections that the server holds open, for all users together. Default: `64`. |
| `MCP_PORT` | All | The port in the container. Default: `8080`. |

In `keycloak` mode, the first start runs [`mcp setup-keycloak-realm`](oauth-authentication.md#prepare-the-realm) with these values. Arguments after `start-server` in the container's command go to [`mcp start-server`](starting-the-mcp-server.md#options).

## Reverse Proxy

The server in the container serves plain HTTP and listens on all addresses of the container, so that the published port reaches it. Publish the port on the host's loopback address only, and let a reverse proxy on the host terminate TLS. At startup, the server warns that it listens without TLS; behind a proxy, that is expected.

Pass everything to the container, not just `/mcp`: the OAuth2 metadata is under `/.well-known/`, and in `builtin` mode, the sign-in and token endpoints are at the root. Pass the original `Host` header on. In `builtin` and `keycloak` mode, the server accepts the host name of its public URL. In `none` mode, it has no public URL, so set `MCP_ALLOWED_HOSTS` to the host name, for example `mcp.example.com`. Don't buffer responses, because the streamable HTTP transport answers with server-sent events. For nginx:

```nginx
server {
    listen 443 ssl;
    server_name mcp.example.com;
    ssl_certificate     /etc/letsencrypt/live/mcp.example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/mcp.example.com/privkey.pem;

    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Connection "";
        proxy_buffering off;
        proxy_read_timeout 1h;
        proxy_send_timeout 1h;
    }
}
```

Behind the proxy, every request reaches the server from the same address, so the per-address limits apply to all clients together. To give the server the clients' own addresses, set `MCP_TRUSTED_PROXIES`, as described in [Client Addresses Behind a Reverse Proxy](security-and-session-handling.md#client-addresses-behind-a-reverse-proxy).

Inside the container, the proxy's requests don't arrive from the proxy's address on the host, but from an address of the container network, for example its gateway, or with rootless Podman, an address that can change when the container is recreated. The Compose files on this page give the network a fixed subnet and trust it:

```yaml
services:
  mcp:
    environment:
      MCP_TRUSTED_PROXIES: 172.30.0.0/24

networks:
  default:
    ipam:
      config:
        - subnet: 172.30.0.0/24
```

This trusts every container in the network, so keep only your own services in it. To check the address, look at the access log of the server, which shows the immediate peer of every request:

```text
INFO:     172.30.0.1:52262 - "POST /mcp HTTP/1.1" 401 Unauthorized
```

## Setup Without Keycloak

This setup runs the MCP server with its [built-in authorization server](oauth-authentication.md#using-the-built-in-authorization-server), next to a MariaDB server that users sign in to. Users need no setup on the MCP server: their user is created at their first sign-in, and their sessions run as the MariaDB account they signed in with.

1.  Create `compose.yaml`:

    {% code title="compose.yaml" %}
    ```yaml
    services:
      db:
        image: mariadb:11.8
        restart: unless-stopped
        environment:
          MARIADB_ROOT_PASSWORD: ${DB_ROOT_PASSWORD}
        volumes:
          - db-data:/var/lib/mysql

      mcp:
        image: mariadb/mariadb-shell-mcp-server:latest
        restart: unless-stopped
        depends_on:
          - db
        environment:
          MCP_OAUTH_MODE: builtin
          MCP_PUBLIC_URL: https://mcp.example.com/mcp
          MCP_LOGIN_SERVERS: mariadb://db:3306
          MCP_REQUIRED_ROLE: mcp_access
          MCP_TRUSTED_PROXIES: 172.30.0.0/24
        volumes:
          - mcp-data:/home/mcp
        ports:
          - "127.0.0.1:8080:8080"

    volumes:
      db-data:
      mcp-data:

    networks:
      default:
        ipam:
          config:
            - subnet: 172.30.0.0/24
    ```
    {% endcode %}

    The server signs users in over TLS, and connects to a login server that isn't on the loopback address only with TLS. MariaDB 11.4 and later enable TLS with a generated certificate when none is configured. To use an existing MariaDB server instead of the `db` service, set `MCP_LOGIN_SERVERS` to its URI, for example `mariadb://db.example.com:3306?ssl-mode=VERIFY_IDENTITY`.
2.  Store the root password of the database in a `.env` file next to `compose.yaml`, which Compose reads, and start the services:

    ```bash
    printf 'DB_ROOT_PASSWORD=%s\n' "$DB_ROOT_PASSWORD" > .env
    chmod 600 .env
    docker compose up -d
    docker compose logs mcp
    ```
3.  Create the role that the server requires, and grant it to the accounts that may use the MCP server, as described in [Configure the Login Servers](oauth-authentication.md#configure-the-login-servers):

    ```bash
    docker compose exec db mariadb -uroot -p
    ```

    ```sql
    CREATE ROLE mcp_access;
    GRANT SELECT ON shop.* TO mcp_access;
    GRANT mcp_access TO 'ada'@'%';
    SET DEFAULT ROLE mcp_access FOR 'ada'@'%';
    ```
4.  Set up the [reverse proxy](#reverse-proxy) for `mcp.example.com`, and register the server with an MCP client. Users sign in with their MariaDB user name and password when the client first connects:

    ```bash
    claude mcp add --scope user --transport http mariadb https://mcp.example.com/mcp
    ```

### API Keys Only

For clients that send an API key instead of signing in, such as scripts and server-side applications, replace the `builtin` variables of the `mcp` service with a first user:

```yaml
    environment:
      MCP_INITIAL_USER: ada@example.com
      MCP_ALLOWED_HOSTS: mcp.example.com
      MCP_TRUSTED_PROXIES: 172.30.0.0/24
```

This mode has no public URL, so `MCP_ALLOWED_HOSTS` names the host that the proxy passes on. Without it, the server answers every request through the proxy that carries a valid API key with `421 Misdirected Request`. A request without a key gets `401 Unauthorized` first, so the missing host name shows only once a client authenticates.

The API key isn't written to the log. Read it, give the user a connection, and register the server with the key, as described in [Multi-Tenant Mode](multi-tenant-mode.md#connect-a-client-with-an-api-key):

```bash
docker compose exec mcp mariadb-shell -- mcp setup --showApiKey=ada@example.com
docker compose exec mcp mariadb-shell -- mcp setup --user=ada@example.com \
  --addConnection='mariadb://ada@db:3306'
```

The setup asks for the connection's password. In a script, pipe it in with `--passwordStdin` and `docker compose exec -T` instead, as described in [Automated Setup](automated-setup.md#passwords).

API keys keep working in the other modes as well.

## Setup With Keycloak

This setup runs Keycloak with its own MariaDB database next to the MCP server. On its first start, the MCP container prepares the Keycloak realm with [`mcp setup-keycloak-realm`](oauth-authentication.md#prepare-the-realm) and selects the [MariaDB login theme](oauth-authentication.md#use-the-mariadb-login-theme) for it. Keycloak and the MCP server each get their own host name at the reverse proxy, here `kc.example.com` and `mcp.example.com`.

1.  Copy the login theme out of the image, so that Keycloak can load it:

    ```bash
    docker run --rm --entrypoint tar mariadb/mariadb-shell-mcp-server:latest \
      -C /opt/mariadb-shell/lib/mariadb-shell/plugins/mcp_plugin -cf - keycloak-theme | tar -xf -
    ```
2.  Create `compose.yaml`:

    {% code title="compose.yaml" %}
    ```yaml
    services:
      keycloak-db:
        image: mariadb:11.8
        restart: unless-stopped
        environment:
          MARIADB_DATABASE: keycloak
          MARIADB_USER: keycloak
          MARIADB_PASSWORD: ${KC_DB_PASSWORD}
          MARIADB_RANDOM_ROOT_PASSWORD: "yes"
        volumes:
          - keycloak-db-data:/var/lib/mysql

      keycloak:
        image: quay.io/keycloak/keycloak:26.8.0
        restart: unless-stopped
        command: start
        depends_on:
          - keycloak-db
        environment:
          KC_DB: mariadb
          KC_DB_URL: jdbc:mariadb://keycloak-db:3306/keycloak
          KC_DB_USERNAME: keycloak
          KC_DB_PASSWORD: ${KC_DB_PASSWORD}
          KC_HOSTNAME: https://kc.example.com
          KC_HTTP_ENABLED: "true"
          KC_PROXY_HEADERS: xforwarded
          KC_BOOTSTRAP_ADMIN_USERNAME: admin
          KC_BOOTSTRAP_ADMIN_PASSWORD: ${KC_ADMIN_PASSWORD}
        volumes:
          - ./keycloak-theme/mariadb-mcp:/opt/keycloak/themes/mariadb-mcp:ro
        ports:
          - "127.0.0.1:8180:8080"

      mcp:
        image: mariadb/mariadb-shell-mcp-server:latest
        restart: unless-stopped
        depends_on:
          - keycloak
        environment:
          MCP_OAUTH_MODE: keycloak
          MCP_PUBLIC_URL: https://mcp.example.com/mcp
          KEYCLOAK_URL: https://kc.example.com
          KEYCLOAK_REALM: mariadb
          KEYCLOAK_ADMIN_USER: admin
          KEYCLOAK_ADMIN_PASSWORD_FILE: /run/secrets/kc_admin_password
          KEYCLOAK_GRANT_ROLE_TO: ada
          KEYCLOAK_LOGIN_THEME: mariadb-mcp
          MCP_TRUSTED_PROXIES: 172.30.0.0/24
        secrets:
          - kc_admin_password
        volumes:
          - mcp-data:/home/mcp
        ports:
          - "127.0.0.1:8080:8080"

    secrets:
      kc_admin_password:
        file: ./kc-admin-password

    volumes:
      keycloak-db-data:
      mcp-data:

    networks:
      default:
        ipam:
          config:
            - subnet: 172.30.0.0/24
    ```
    {% endcode %}
3.  Store the passwords. Compose reads `KC_DB_PASSWORD` and `KC_ADMIN_PASSWORD` from a `.env` file next to `compose.yaml`, and the MCP container reads the administrator password from `kc-admin-password`:

    ```bash
    printf 'KC_DB_PASSWORD=%s\nKC_ADMIN_PASSWORD=%s\n' "$KC_DB_PASSWORD" "$KC_ADMIN_PASSWORD" > .env
    printf '%s' "$KC_ADMIN_PASSWORD" > kc-admin-password
    chmod 644 kc-admin-password
    ```

    Compose mounts the file into the container with its owner and mode from the host, and the server runs as uid `10001`, so the file must be readable by that user. Keep it in a directory that only you can open. With rootless Podman, give the file to the container's user instead: `podman unshare chown 10001:10001 kc-admin-password`.
4.  Set up the reverse proxy for both host names: `mcp.example.com` as described in [Reverse Proxy](#reverse-proxy), and `kc.example.com` to `127.0.0.1:8180`, with the headers `X-Forwarded-For`, `X-Forwarded-Proto`, `X-Forwarded-Host`, and `X-Forwarded-Port`, which Keycloak reads with `KC_PROXY_HEADERS: xforwarded`.
5.  Start Keycloak, and create the realm and its users. The realm must exist before the MCP server's first start:

    ```bash
    docker compose up -d keycloak
    docker compose exec keycloak /opt/keycloak/bin/kcadm.sh config credentials \
      --server http://localhost:8080 --realm master --user admin
    docker compose exec keycloak /opt/keycloak/bin/kcadm.sh create realms -s realm=mariadb -s enabled=true
    ```

    Create the users in the admin console at `https://kc.example.com/admin/`, or connect the realm to identity providers such as Google. The users named in `KEYCLOAK_GRANT_ROLE_TO` must exist before the next step.
6.  Start the MCP server, and check that it prepared the realm:

    ```bash
    docker compose up -d
    docker compose logs mcp
    ```

    ```text
    entrypoint-mcp-server: applying the configuration (keycloak)
    Multi-tenant mode on.
    Public URL set to https://mcp.example.com/mcp.
    Client scope mcp:db created.
    Audience https://mcp.example.com/mcp added to mcp:db.
    Realm role mcp-user created.
    Realm role mcp-user given to ada.
    Client mariadb-mcp created.
    Client mariadb-mcp may request mcp:db.
    Login theme of realm 'mariadb': mariadb-mcp.
    Realm 'mariadb' is prepared for https://mcp.example.com/mcp. Issuer: https://kc.example.com/realms/mariadb
    OAuth mode: keycloak.
    Keycloak issuer: https://kc.example.com/realms/mariadb.
    ```

    Then empty `kc-admin-password`. The container starts without it, as long as the mode, the public URL and the `KEYCLOAK_*` variables stay the same.
7.  Give the users their connections. A user who signs in through Keycloak is linked to a user of the MCP server by their **verified** email address, or created at their first sign-in if they hold the realm role `mcp-user`, but without connections. Create the user beforehand with the email address of their Keycloak account, which must be marked as verified in Keycloak, and add their connections. The setup asks for each connection's password:

    ```bash
    docker compose exec mcp mariadb-shell -- mcp setup --addUser=ada@example.com
    docker compose exec mcp mariadb-shell -- mcp setup --user=ada@example.com \
      --addConnection='mariadb://ada@db.example.com:3306'
    ```

    See [How the Server Checks a Keycloak Token](oauth-authentication.md#how-the-server-checks-a-keycloak-token) for how sign-ins are mapped to users.
8.  Register the server with an MCP client, with the client that the realm setup created, and sign in through Keycloak:

    ```bash
    claude mcp add --scope user --transport http --client-id mariadb-mcp mariadb https://mcp.example.com/mcp
    ```

The MCP server reads the realm's keys from `KEYCLOAK_URL`, so the container must reach Keycloak under the same name that the realm's issuer uses, here `https://kc.example.com`. If that name resolves to an address that isn't reachable from inside the container, for example a public address that your router doesn't forward back into your network, point it at the reverse proxy on the host:

```yaml
  mcp:
    extra_hosts:
      - "kc.example.com:host-gateway"
```

## Troubleshooting

| Message or symptom | Cause | Solution |
| --- | --- | --- |
| *entrypoint-mcp-server: … belongs to uid …, and the container runs as uid …* | The volume was set up by another uid, and its files are private to that uid. | Run the container as the uid named, or give the volume's files to the container's uid. |
| *entrypoint-mcp-server: KEYCLOAK_ADMIN_PASSWORD_FILE: cannot read … as uid 10001* | The password file isn't readable by the server's user in the container. | Make it readable by uid `10001`, as described in [Setup With Keycloak](#setup-with-keycloak). |
| *entrypoint-mcp-server: MCP_OAUTH_MODE=… needs …* | A variable that the mode needs isn't set. The container stops before it changes anything, so the previous configuration stays in place. | Set the variable the message names. |
| *entrypoint-mcp-server: preparing the Keycloak realm needs KEYCLOAK_ADMIN_PASSWORD or KEYCLOAK_ADMIN_PASSWORD_FILE* | The mode, the public URL or a `KEYCLOAK_*` variable changed since the realm was last prepared, or the realm was never prepared. The container stops before it changes anything. | Pass the administrator password for one start, then empty it again. |
| *Keycloak has no login theme 'mariadb-mcp'* | The theme isn't mounted into the Keycloak container, or Keycloak was started before it was. | Mount the theme and restart Keycloak. |
| A client receives `421 Misdirected Request`. | The client uses a host name other than the public URL's, for example the published port directly. In `none` mode, which has no public URL, the proxy's host name isn't in `MCP_ALLOWED_HOSTS`. | Use the public URL, or add the name with `MCP_ALLOWED_HOSTS`. |
| The container restarts again and again, and the log shows that the server refused to start. | The server has no user, and the mode doesn't create users at their first sign-in. | Set `MCP_INITIAL_USER`, or use `builtin` or `keycloak` mode. |
| The server's log lines show the same address for every client. | `MCP_TRUSTED_PROXIES` doesn't contain the address that the proxy's requests arrive from. | Compare it with the address in the access log. See [Reverse Proxy](#reverse-proxy). |
