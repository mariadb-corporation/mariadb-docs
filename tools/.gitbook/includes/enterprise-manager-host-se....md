---
title: 'Enterprise Manager host: Se...'
---

**Enterprise Manager host: Set the image locations**&#x20;

Export the image variables so the installer pulls the container images from your registry instead of the internet:

```bash
export IMAGE_SUPERMAX=<private-registry-fqdn>/mariadb/enterprise-manager-backend:<backend-version>
export IMAGE_NGINX=<private-registry-fqdn>/mariadb/enterprise-manager-frontend:<frontend-version>
export IMAGE_GRAFANA=<private-registry-fqdn>/mariadb/grafana:<grafana-version>
export IMAGE_PROMETHEUS=<private-registry-fqdn>/mariadb/prometheus:<prometheus-version>
export IMAGE_OTELCOL=<private-registry-fqdn>/mariadb/opentelemetry-collector-contrib:<otelcol-version>
```
