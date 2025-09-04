# Docker Images

{% include "https://app.gitbook.com/s/GxVnu02ec8KJuFSxmB93/~/reusable/b36uzH0IlkzSr1zA7hGa/" %}

## Certified images

All the Docker images used by this operator are based on [Red Hat UBI](https://catalog.redhat.com/software/base-images) and have been [certified by Red Hat](https://connect.redhat.com/en/partner-with-us/red-hat-openshift-certification). The advantages of using UBI based images are:

* Immutability: UBI images are built to be secure and stable, reducing the risk of unintended changes or vulnerabilities due to mutable base layers.
* Small size: The UBI [minimal](https://catalog.redhat.com/software/containers/ubi8/ubi-minimal/5c359a62bed8bd75a2c3fba8) and [micro](https://catalog.redhat.com/software/containers/ubi8-micro/601a84aadd19c7786c47c8ea) variants used by this operator are designed to be lightweight, containing only the essential packages. This can lead to smaller container image sizes, resulting in faster build times, reduced storage requirements, and quicker image pulls.
* Security and compliance: Regular CVE scanning and vulnerability patching help maintain compliance with industry standards and security best practices.
* Enterprise-grade support: UBI images are maintained and supported by Red Hat, ensuring timely security updates and long-term stability.&#x20;

&#x20;

## List of compatible images

MariaDB Enterprise Operator is compatible with the following Docker images:

| Component | Image | Supported Tags | CPU Architecture |
|-----------|-------|----------------|------------------|
| MariaDB Enterprise Operator (ppc64le support) | docker.mariadb.com/mariadb-enterprise-operator |  25.8.0 <br>  |  amd64 <br>  arm64 <br>  ppc64le <br>  |
| MariaDB Enterprise Operator | docker.mariadb.com/mariadb-enterprise-operator |  1.0.0 <br>  |  amd64 <br>  arm64 <br>  |
| MariaDB Enterprise Server (ppc64le support) | docker.mariadb.com/enterprise-server |  11.4.7-4.1 <br>  11.4 <br>  10.6.22-18.1 <br>  10.6 <br>  |  amd64 <br>  arm64 <br>  ppc64le <br>  |
| MariaDB Enterprise Server | docker.mariadb.com/enterprise-server |  11.4.5-3 <br>  11.4.4-2 <br>  10.6.21-17 <br>  10.6.20-16.1 <br>  10.6.19-15.1 <br>  10.6.18-14.2 <br>  10.6.17-13.2 <br>  |  amd64 <br>  arm64 <br>  |
| MaxScale Enterprise (ppc64le support) | docker.mariadb.com/maxscale |  25.01.3-1 <br>  25.01 <br>  |  amd64 <br>  arm64 <br>  ppc64le <br>  |
| MaxScale Enterprise | docker.mariadb.com/maxscale-enterprise |  25.01.2 <br>  25.01.1 <br>  |  amd64 <br>  arm64 <br>  |
| MaxScale | mariadb/maxscale |  24.02.5-ubi <br>  24.02-ubi <br>  23.08.9-ubi <br>  23.08-ubi <br>  |  amd64 <br>  arm64 <br>  |
| MariaDB Prometheus Exporter (ppc64le support) | mariadb/mariadb-prometheus-exporter-ubi |  1.1.0 <br>  |  amd64 <br>  arm64 <br>  ppc64le <br>  |
| MariaDB Prometheus Exporter | mariadb/mariadb-prometheus-exporter-ubi |  1.0.0 <br>  |  amd64 <br>  arm64 <br>  |
| MaxScale Prometheus Exporter (ppc64le support) | mariadb/maxscale-prometheus-exporter-ubi |  1.1.0 <br>  |  amd64 <br>  arm64 <br>  ppc64le <br>  |
| MaxScale Prometheus Exporter | mariadb/maxscale-prometheus-exporter-ubi |  1.0.0 <br>  |  amd64 <br>  arm64 <br>  |
| MariaDB Enterprise nslcd sidecar | docker.mariadb.com/nslcd-sidecar |  0.9.10-13 <br>  |  amd64 <br>  arm64 <br>  ppc64le <br>  |

Refer to the registry documentation to [access docker.mariadb.com with your customer credentials](customer-access-to-docker-mariadb-com.md).

## Working With Air-Gapped Environments

This section outlines several methods for pulling official MariaDB container images from `docker.mariadb.com` and making them available in your private container registry. This is often necessary for air-gapped, offline, or secure environments.

### Option 1: Direct Pull, Tag, and Push

This method is ideal for a "bastion" or "jump" host that has network access to **both** the public internet (specifically `docker.mariadb.com`) and your internal private registry.

1.  **Log in to both registries.**
    You will need a MariaDB token for the public registry and your credentials for the private one. Refer to the [official documentation](https://mariadb.com/docs/tools/mariadb-enterprise-operator/customer-access-to-docker-mariadb-com#customer-credentials).

    ```bash
    # Log in to the official MariaDB registry
    docker login docker.mariadb.com

    # Log in to your private registry
    docker login <private-registry-url>
    ```

2.  **Pull the required image.**
    Pull the official MariaDB Enterprise Operator image from its public registry.

    ```bash
    docker pull docker.mariadb.com/mariadb-enterprise-operator:25.8.0
    ```

3.  **Tag the image for your private registry.**
    Create a new tag for the image that points to your private registry's URL and desired repository path.

    ```bash
    docker tag docker.mariadb.com/mariadb-enterprise-operator:25.8.0 <private-registry-url>/mariadb/mariadb-enterprise-operator:25.8.0
    ```

4.  **Push the re-tagged image.**
    Push the newly tagged image to your private registry.

    ```bash
    docker push <private-registry-url>/mariadb/mariadb-enterprise-operator:25.8.0
    ```


### Option 2: Using a Proxy or Caching Registry

Many modern container registries can be configured to function as a pull-through cache or proxy for public registries. When an internal client requests an image, your registry pulls it from the public source, stores a local copy, and then serves it. This automates the process after initial setup.

You can use [Harbor](https://goharbor.io/docs/2.10.0/administration/configuring-replication/create-replication-rules/) as a pull-through cache (Harbor calls this Replication Rules).

### Option 3: Offline Transfer using `docker save` and `docker push`

This method is designed for fully air-gapped environments where no single machine has simultaneous access to the internet and the private registry.

#### On the Internet-Connected Machine

1.  **Log in and pull the image.**

    ```bash
    docker login docker.mariadb.com
    docker pull docker.mariadb.com/mariadb-enterprise-operator:25.8.0
    ```

2.  **Save the image to a tar archive.**
    This command packages the image into a single, portable file.

    ```bash
    docker save [docker.mariadb.com/mariadb-enterprise-operator:25.8.0 -o mariadb-enterprise-operator_25.8.0.tar
    ```

    Use a tool like `scp` or `sftp` or a USB drive to copy the generated `.tar` archives from the internet-connected machine to your isolated systems.

#### On the Machine with Private Registry Access

1.  **Load the image from the archive.**

    ```bash
    docker load -i mariadb-enterprise-operator_25.8.0.tar
    ```

2.  **Log in to your private registry.**

    ```bash
    docker login <private-registry-url>
    ```

3.  **Tag the loaded image.**
    The image loaded from the tar file will retain its original tag. You must re-tag it for your private registry.

    ```bash
    docker tag docker.mariadb.com/mariadb-enterprise-operator:25.8.0 <private-registry-url>/mariadb/mariadb-enterprise-operator:25.8.0
    ```

4.  **Push the image to your private registry.**

    ```bash
    docker push <private-registry-url>/mariadb/mariadb-enterprise-operator:25.8.0
    ```

### Option 4: For OpenShift, you can use OpenShift Disconnected Installation Mirroring

Refer to the [official Red Hat documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.15/html/disconnected_installation_mirroring/installing-mirroring-disconnected)

### Option 5: Offline Transfer for `containerd` Environments

This method is for air-gapped environments that use **`containerd`** as the container runtime (common in Kubernetes) and do not have the Docker daemon. It uses the `ctr` command-line tool to import, tag, and push images. ⚙️


#### 1. On the Bastion Host (with Internet)

First, on a machine with internet access, you'll pull the images and export them to portable archive files.

1.  **Pull the Container Image**
    Use the `ctr image pull` command to download the required image from its public registry.

    ```bash
    ctr image pull docker.mariadb.com/mariadb-enterprise-operator:25.8.0
    ```
    > **Note**: If your bastion host uses Docker, you can use `docker pull` instead as we did in Option 3.

2.   **Export the Image to an Archive**
     Next, export the pulled image to a `.tar` file using `ctr image export`. The format is `ctr image export <output-filename> <image-name>`.

     ```bash
     ctr image export mariadb-enterprise-operator-25.8.0.tar docker.mariadb.com/mariadb-enterprise-operator:25.8.0
     ```
     > **Note**: To find the exact image name as `containerd` sees it, run `ctr image ls`. The Docker equivalent for this step is `docker save <image-name> -o <output-filename>`.

Repeat this process for all the container images you need to transfer.

#### 2. Transfer the Archives

Use a tool like `scp` or `sftp` or a USB drive to copy the generated `.tar` archives from the bastion host to your isolated systems.

#### 3. On the Isolated Host

Finally, on the isolated system, you will import the archives into `containerd`. [Official Docs](https://github.com/containerd/containerd/blob/main/docs/cri/crictl.md?plain=1)

1.  **Importing for Kubernetes (Important!)** ⚙️
    If the images need to be available to **Kubernetes**, you **must** import them into the `k8s.io` namespace by adding the `-n=k8s.io` flag.

    ```bash
    ctr -n=k8s.io image import mariadb-enterprise-operator-25.8.0.tar
    ```

2.  **Verify the Image**
    Check that `containerd` recognizes the newly imported image.

    ```bash
    ctr image ls
    ```

    You can also verify that the Container Runtime Interface (CRI) sees it by running:
    ```bash
    crictl images
    ```


#### **Important Note**

The examples above use the `mariadb-enterprise-operator:25.8.0` image. You must **repeat the chosen process** for all required container images. A complete list is available [here](#list-of-compatible-images)

## Additional Resources

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
