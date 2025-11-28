# Security in Enterprise Manager

MariaDB Enterprise Manager provides security at multiple levels, including transport-layer encryption for all components, secure authentication, and a detailed audit log. 

{% hint style="info" %}
This guide covers the primary security configurations. For Users, Roles and Permissions, see [User Management](user-management/).
{% endhint %}

### SSL/TLS Certificate Management

The Enterprise Manager installation generates a self-signed TLS certificate and key for immediate use. For production environments, you should use your own custom certificates.

{% stepper %}
{% step %}
### Place custom certificates

Copy your custom certificate and private key files into the `enterprise-manager/certs/` directory on the host machine.
{% endstep %}

{% step %}
### Update the configuration

Open the `enterprise-manager/.env` file and modify the `MEMA_TLS_CERTPATH` and `MEMA_TLS_KEYPATH` variables to point to your new files.

Example: if your files are `my-host.crt` and `my-host.key`, your configuration should be:

{% code title=".env (example)" %}
```
MEMA_TLS_CERTPATH=/certs/my-host.crt
MEMA_TLS_KEYPATH=/certs/my-host.key
```
{% endcode %}

{% hint style="info" %}
The path you provide must begin with `/certs/`. This is because the host's `certs/` directory is mounted inside the Docker containers at the `/certs` path.
{% endhint %}
{% endstep %}

{% step %}
### Restart Enterprise Manager

To apply the changes, restart the services:

```
docker compose up -d
```
{% endstep %}
{% endstepper %}

### Enabling the Audit Log

The audit log records all REST API requests made to MariaDB Enterprise Manager, providing a clear trail of administrative actions for security and compliance.

{% stepper %}
{% step %}
### Step: Navigate to the directory

Open a terminal and change into your MariaDB Enterprise Manager installation directory.

```
cd enterprise-manager/
```
{% endstep %}

{% step %}
### Step: Edit the .env file

Open the environment file using a text editor.

```
nano .env
```
{% endstep %}

{% step %}
### Step: Update the audit log variable

Inside the editor, locate the line for the audit API setting.

* Find this line:

```
MEMA_AUDIT_API=false
```

* Change it to:

```
MEMA_AUDIT_API=true
```
{% endstep %}

{% step %}
### Step: Save and exit

Save the changes and exit the editor.
{% endstep %}

{% step %}
### Step: Restart Enterprise Manager

The change requires a restart to take effect.

```
docker compose up -d
```
{% endstep %}
{% endstepper %}

### Configuring Secure Connections

#### Agent to Enterprise Manager Connections

The connection from the `mema-agent` to the Enterprise Manager server is secured using HTTPS.

* To enable encryption: ensure the URL provided in the agent setup command uses `https://`.

```
mema-agent setup --endpoint=https://<MEM_Address> ...
```

* To bypass certificate checks: if you are using a self-signed or non-trusted TLS certificate on the Enterprise Manager server, you can add the `--otlp-insecure` flag to the agent setup command. This is recommended only for testing environments.

#### Enterprise Manager to Monitored Databases

You can configure secure TLS connections from Enterprise Manager to your monitored MariaDB Servers and MaxScale instances when you first add them.

In the "Add Database" page:

<figure><img src="../../.gitbook/assets/image (33).png" alt=""><figcaption></figcaption></figure>

1. Toggle the SSL/TLS option to ON.
2. To validate the server's certificate against your Certificate Authority (CA), provide the path to your CA file in the Certificate Authority field. The file must be located in the `enterprise-manager/certs/` directory and the path must begin with `/certs/`.
3. Check Verify peer certificate to enable validation.
4. (Optional) Check Verify peer host to ensure the server's hostname matches the certificate.
5. If the database requires client-side certificates for authentication, provide the paths to your client certificate and key in the Certificate and Key fields, respectively. These files must also be in the `enterprise-manager/certs/` directory.

{% hint style="warning" %}
All certificate and key files referenced for server validation or client authentication must be placed in the `enterprise-manager/certs/` directory on the host and referenced with a path beginning with `/certs/`.
{% endhint %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
