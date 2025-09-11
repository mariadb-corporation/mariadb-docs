# Supported Docker Images

The following is a list of images that have plugins installed and available to use. 

{% hint style="warn" %}
Even though these images have plugins installed, that doesn't necessarily mean that they are enabled by default. You may need to install them.
The recommended operator native way to do so is to use:
```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb
spec:
  # ....
  myCnf: |
    [mariadb]
    plugin_load_add = auth_pam # Load auth plugin
  # ....
```

Each supported plugin will have a section on how to install it.
{% endhint %}

| Component | Image | Supported Tags | CPU Architecture |
|-----------|-------|----------------|------------------|
| MariaDB Enterprise Server (ppc64le support) | docker.mariadb.com/enterprise-server |  11.4.7-4.2 <br>  11.4 <br> |  amd64 <br>  arm64 <br>  ppc64le <br>  |

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
