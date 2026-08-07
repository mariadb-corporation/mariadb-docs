---
description: >-
  Answers to common GridGain Control Center questions — preserving cluster IDs,
  automating cluster connection, SSL proxying, limited clusters, and mail setup.
---

# Frequently Asked Questions

This section contains answers to common questions and recommendations for common issues.

## Control Center lost connection to my cluster after restart

The most common case for this is the cluster ID change. It can happen during the restart of an in-memory cluster, or if persistent data storage was lost for a persistent cluster.

If this happened, you can reattach the cluster and continue monitoring it. However, previously collected data and configuration settings will be lost. To avoid losing cluster information, configure a persistent cluster ID on your GridGain cluster.

### Preserving Cluster ID

#### Without a global team:

For this example, we will assume that Control Center is running on `http://mydomain.com:3000`.

When starting the cluster, you need to prepare secret, cluster id and cluster tag:

- Start your cluster and activate.
- Run the following commands in this order:

  ```bash
  control.bat --property set --name control-center-agent-cluster-secret --val 88f5ea3c-9e50-11ec-b909-0242ac120002 --yes
  control.bat --change-id 11111111-1111-1111-1111-111111111111 --yes
  control.bat --change-tag prod_cluster --yes
  management.bat --uri http://somedomain.com:3000
  ```
- Use the token command once and attach your cluster:

  ```bash
  management.bat --token
  ```

If you lose persistence, next time just run all commands except `--token` again.

#### With the global team

First, you need to configure the [global team](profile/teams.md#global-team) in Control Center with the `account.globalTeam.enabled` and `account.globalTeam.attachCluster` properties. With it configured, you no longer need to create a token.

- Start your cluster and activate it.
- Run the following commands in the order you see:

  ```bash
  control.sh --property set --name control-center-agent-cluster-secret --val 88f5ea3c-9e50-11ec-b909-0242ac120002 --yes
  control.sh --change-id 11111111-1111-1111-1111-111111111111 --yes
  control.sh --change-tag prod_cluster --yes
  ```

## How can I automate connection of clusters to Control Center?

For persistent clusters, you only need to enable the Control Center Global Team by enabling the `account.globalTeam.enabled` and `account.globalTeam.attachCluster` properties.

For in-memory clusters, consider adding a small persistent data region. It can be used to store system information, while your caches are still in-memory. If this is not possible, set cluster secret, ID, and other properties after each cluster restart by using the control script. To do this, run the following commands when starting the cluster:

```bash
control.sh --property --set --name secret --val UUID
control.sh --change-id UUID
```

{% hint style="info" %}
Always set the cluster secret first, before setting the ID.
{% endhint %}

## Global Team FAQs

### Can Global Team coexist with regular teams?

Yes. Users can belong to both Global Team and one or more regular teams simultaneously. Access granted through either is additive — a user retains all access granted by any team they belong to.

### Can I exclude specific clusters from Global Team when `account.globalTeam.attachCluster` is enabled?

No. When `account.globalTeam.attachCluster` is enabled, all clusters in the environment are automatically shared with Global Team. To restrict access to specific clusters, disable `account.globalTeam.attachCluster` and share clusters with individual teams manually.

### Are newly registered clusters automatically shared with Global Team?

Yes, if `account.globalTeam.attachCluster` is enabled at the time of registration, newly registered clusters are shared with Global Team automatically.

## I run Control Center behind SSL proxy. What is the recommended nginx configuration?

Unless you configure your proxy to allow requests through, you will get 403 error when Control Center agents will try to access Control Center server. Here is an example of nginx configuration file that allows for SSL:

```nginx
upstream <upstream_name> {
     server <control_center_host>:<control_center_port>;
}
server {
  server_name <proxy_server_hostname>;
  listen 9443 ssl;
  ssl_certificate     /etc/nginx/certs/ssl_test_certs/ggcc.crt;
  ssl_certificate_key /etc/nginx/certs/ssl_test_certs/ggcc.nopass.key;
  ssl_protocols       TLSv1.2;
  ssl_ciphers         HIGH:!aNULL:!MD5;
  access_log /var/log/nginx/access.log;
  error_log /var/log/nginx/error.log;
  location / {
    proxy_pass https://<upstream_name>;
    proxy_set_header Host $host;
  }
  location /api/v1 {
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_pass https://<upstream_name>;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
  }
  location /socket.io {
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_http_version 1.1;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header Host $host;
    proxy_pass https://<upstream_name>;
  }
  location /browsers {
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_pass_header X-XSRF-TOKEN;
    proxy_pass https://<upstream_name>;
    proxy_set_header Origin https://<upstream_name>;
  }
  location /agents {
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_http_version 1.1;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header Host $host;
    proxy_pass https://<upstream_name>;
  }
}
```

## Why does my cluster show the Limited Cluster banner?

Control Center monitors Tracing and Compute activity of your cluster; it imposes activity limitations:

- Soft limit: When the number or Tracing or Compute messages in the corresponding queue exceeds the "soft" threshold (by default, 200), Control Center attempts to automatically reduce message submission rate for your cluster.

  {% hint style="info" %}
  This option is available in GridGain version 8.8.21 and later, in Apache Ignite version 2.14.0.0 and later.
  {% endhint %}
- Hard limit: When the number or Tracing or Compute messages in the corresponding queue exceeds the "hard" threshold (by default, 1000), your cluster enters the "limited" state wherein no new Tracing or Compute messages are added to the queues. In all other respects, your cluster remains active and functional. By default, the limited state (a.k.a., "ban") lasts 3 minutes. After that, Control Center checks the status of the Tracing and Compute queues. If it finds that the number of messages diminished below the threshold, the cluster resumes its normal operation. If the number of messages is still above the threshold, the cluster remains in the limited state for another 3 minutes.

To preclude your cluster from entering the limited state, [reduce the Tracing percentage](gg8/tracing/tracing.md) for one or more scopes. If this does not help, contact our support.

You can override the default cluster activity thresholds:

1. Paste the following definitions in the application.yml file:

   ```yaml
   control.rate-limit.trace-hard-limit = 1000
   control.rate-limit.trace-soft-limit = 200
   control.rate-limit.compute-hard-limit = 1000
   control.rate-limit.compute-soft-limit = 200
   ```
2. Increase threshold values, e.g., from 200 to 500 and/or from 1000 to 2000.

You can also modify the activity limitation parameters:

1. Add any of the following parameters to the application.yml file:

   | Parameter | Description | Default Value |
   |---|---|---|
   | control.rate-limit.lower-threshold | Count of requests between the previous and the current checks. | 1000 |
   | control.rate-limit.update-interval-millis | Frequency of checks in milliseconds. | 500 |
   | control.rate-limit.ban-duration-seconds | Duration of the ban (the "limited" state) in seconds. | 3*60 |
   | control.rate-limit.block-connection-on-detection | If "true," the cluster is disconnected instead of entering the "limited" state. | false |
2. Change the parameter values as required.

## My Cache Gets Too Big Too Fast. How Can I Prevent This?

[Optimize the disc space](admin-guide/disk-space-optimization.md) utilization.

## Why do I not receive mail notifications?

GridGain Control Center requires manual configuration of a mailing server to be able to send mail notifications, such as information about teams and shared clusters, or information about alert triggers.

Configuration depends on the specific mailing server you use. The example below will be using [MailHog](https://hub.docker.com/r/mailhog/mailhog) server run in Docker:

1. Pull MailHog to your local server

   ```bash
   docker pull mailhog/mailhog
   ```
2. Start a container and expose ports to your local ones:

   ```bash
   docker run -d -p 1025:1025 -p 8025:8025 mailhog/mailhog
   ```
3. Create an `application.properties` file in the Control Center root folder and specify mailing server host and port:

   ```properties
   spring.mail.host=127.0.0.1
   spring.mail.port=1024
   ```

{% hint style="info" %}
Depending on your mailing server, additional configuration properties may be required. Full list of properties is available in the [Configuration Parameters](admin-guide/configuration.md#mail-server) document.
{% endhint %}

## How do I contact support?

Contact us at the [http://support.gridgain.com/](http://support.gridgain.com).
