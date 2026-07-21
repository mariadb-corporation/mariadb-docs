---
description: >-
  Instructions for configuring SMTP credentials and server details in the
  environment file to enable email alerts from the integrated alerting engine.
---

# SMTP Server Configuration

This page explains how to configure email alerting for MariaDB Enterprise Manager using Grafana's integrated alerting engine. SMTP is configured through Grafana's standard `GF_SMTP_*` environment variables, which are passed to the Grafana container via the Enterprise Manager `.env` file. For the complete list of available options, refer to the [Grafana SMTP configuration documentation](https://grafana.com/docs/grafana/latest/setup-grafana/configure-grafana/#smtp).

{% stepper %}
{% step %}
#### Edit the environment file

1. Navigate to your MariaDB Enterprise Manager installation directory:

```bash
cd enterprise-manager/
```

2. Open the `.env` file in a text editor (example uses nano):

```bash
nano .env
```

3. Add the following block of variables to the file, filling in values for your SMTP server:

```ini
# --- Grafana SMTP Email Settings ---
# Set to true to enable email alerting
GF_SMTP_ENABLED=true

# Your SMTP server hostname and port
# Port 25 is typical for internal mail relays; use 587 for authenticated submission
# (e.g. Gmail, Office 365) or 465 for SMTPS (implicit TLS)
GF_SMTP_HOST=smtp.example.com:25

# Credentials for your SMTP user
# Leave blank if your internal relay does not require authentication
GF_SMTP_USER=
GF_SMTP_PASSWORD=

# Set to true if your server uses a self-signed or internal-CA certificate
GF_SMTP_SKIP_VERIFY=false

# The "From" address that will appear on alert emails
GF_SMTP_FROM_ADDRESS=alerts@my-domain.com

# The display name for the sender
GF_SMTP_FROM_NAME=MariaDB Enterprise Manager
```

4. Save the file and exit the editor.
{% endstep %}

{% step %}
#### Restart the Grafana service

The new settings are applied only after Grafana restarts.

From the `enterprise-manager/` directory, restart only the Grafana container so other Enterprise Manager components are not affected:

{% code title="Restart Grafana container" %}
```bash
# Take down the existing Grafana container
docker compose down grafana

# Start a new Grafana container with the updated configuration
docker compose up -d grafana
```
{% endcode %}
{% endstep %}

{% step %}
#### Verify the configuration in Grafana

After Grafana restarts:

1. Open the Grafana UI.
2. Create a new "Contact point".
3. Use the "Test" button to send a test email and confirm that SMTP settings are correct and Enterprise Manager can send alerts.

If the test email fails on an internal relay, common causes are the relay advertising STARTTLS with a certificate Grafana does not trust (set `GF_SMTP_SKIP_VERIFY=true`) or the relay requiring a specific TLS policy (see `GF_SMTP_STARTTLS_POLICY` in the [Grafana SMTP documentation](https://grafana.com/docs/grafana/latest/setup-grafana/configure-grafana/#smtp)).
{% endstep %}
{% endstepper %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
