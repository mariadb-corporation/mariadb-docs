# Change Hostname or IP Address

To set the hostname or IP address for an existing MariaDB Enterprise Management instance, follow these instructions. Changing the hostname or IP address is useful if your server's IP changed or if you need to switch from an IP address to a public DNS name.

{% stepper %}
{% step %}
#### Connect to your server

SSH into the server where your Enterprise Manager is running:

```bash
ssh user@your-server-ip
```
{% endstep %}

{% step %}
#### Navigate to the directory

Change into the `enterprise-manager` directory, where your Docker Compose files are located:

```bash
cd enterprise-manager
```
{% endstep %}

{% step %}
#### Edit the `.env` file

Open the environment file with a text editor (for example `nano`):

```bash
nano .env
```

Find the line that begins with `MEMA_HOSTNAME=` and update it with the new hostname or IP address. Example:

```env
MEMA_HOSTNAME=your.new.hostname.or.ip
```
{% endstep %}

{% step %}
#### Save the file

Save the file and exit the editor.
{% endstep %}

{% step %}
#### Restart the services

Restart the MEM services so the new environment variable takes effect. The `--force-recreate` flag ensures the containers are rebuilt using the updated environment variables:

```bash
docker compose up -d --force-recreate
```

After the restart, your Enterprise Manager will be accessible at the new hostname or IP address.
{% endstep %}
{% endstepper %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
