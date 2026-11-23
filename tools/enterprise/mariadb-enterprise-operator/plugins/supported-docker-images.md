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

In the **Supported Tags** column, `x` stands for any patch version. For more information on how to find the exact tags available in the registry, see [Listing tags manually](../docker-images.md#listing-tags-manually).

| Component | Image | Supported Tags | CPU Architecture |
|-----------|-------|----------------|------------------|
| MariaDB Enterprise Server | docker.mariadb.com/enterprise-server |  11.8.x <br>  11.4.x <br>  10.6.x <br>  |  amd64 <br>  arm64 <br>  ppc64le <br>  |
| MariaDB Enterprise Server (tiered) | docker.mariadb.com/enterprise-server |  12.3.x (also 12.3.x-minimal, 12.3.x-standard) <br>  11.8.x (also 11.8.x-minimal, 11.8.x-standard) <br>  11.4.x (also 11.4.x-minimal, 11.4.x-standard) <br>  10.6.x (also 10.6.x-minimal, 10.6.x-standard) <br>  |  amd64 <br>  arm64 <br>  ppc64le <br>  |


<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}