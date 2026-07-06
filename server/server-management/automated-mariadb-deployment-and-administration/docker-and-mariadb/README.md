---
description: >-
  Discusses running MariaDB in Docker containers, covering the benefits of
  isolation and ease of deployment for development and testing environments.
---

# MariaDB Containers

Containers are an OCI standard format for software images and their specified time all bundled up into a single distributable time. They can be used for production, development or testing.

Docker Inc. run a [Docker Official Images](https://docs.docker.com/docker-hub/official_images) program to provide users with an essential base implementation of MariaDB in a container and to exemplify best practices of a container.

The containers are [available on Docker Hub](https://hub.docker.com/_/mariadb) as **docker.io/library/mariadb** though many container runtime implementation will fill in the **docker.io/library** where the host/path isn't specified.

The containers are in a Open Container Initiative format that allows the containers to be interoperable with a number of container runtime implementations. Docker, or more fully Docker Engine, is just one of the many available runtimes.

Many people use MariaDB Docker Official Image containers in CI systems like GitHub Actions, though its possible to use these in production environments like kubernetes.

The MariaDB Server container images are available with a number of tags:

* A full version, like 10.11.5
* A major version like 10.11
* The most recent stable GA version - latest
* The most recent stable LTS version - lts

Versions that aren't stable will be suffixed with **-rc**, or **-alpha** to clearly show their release status, and enables [Renovatebot](https://github.com/grooverdan/mariadb-docker/commit/a9a98d720ddc5afe5c62449bbe737f4780aee0fe) and other that follow [semantic versioning](https://docs.renovatebot.com/modules/versioning/#semantic-versioning) to follow updates.

For a consistent application between testing an production environment using the SHA hash of the image is recommended like **docker.io/library/mariadb@sha256:29fe5062baf36bae8ec68f21a3dce4f0372dadc185e687624f1252fc49d91c67**. There is a list of mapping and history of tags to SHA hash on the [Docker Library repository](https://github.com/docker-library/repo-info/tree/master/repos/mariadb/remote).

{% columns %}
{% column %}
{% content-ref url="adding-plugins-to-the-mariadb-docker-official-image.md" %}
[adding-plugins-to-the-mariadb-docker-official-image.md](adding-plugins-to-the-mariadb-docker-official-image.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Instructions on how to extend the official MariaDB Docker image by installing additional plugins and dependencies using a custom Dockerfile.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="benefits-of-managing-mariadb-containers-with-orchestration-software.md" %}
[benefits-of-managing-mariadb-containers-with-orchestration-software.md](benefits-of-managing-mariadb-containers-with-orchestration-software.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explains the advantages of using orchestration tools like Kubernetes or Docker Swarm for managing MariaDB containers, including automated failover, scaling, and rolling updates.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="container-backup-and-restoration.md" %}
[container-backup-and-restoration.md](container-backup-and-restoration.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete container backup guide: docker volume create, mariadb-dump --all-databases, mariadb-backup --backup/--prepare/--copy-back operations.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="container-security-concerns.md" %}
[container-security-concerns.md](container-security-concerns.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Discusses security best practices for running MariaDB in containers, addressing topics like root user privileges, volume permissions, and network isolation.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="creating-a-custom-container-image.md" %}
[creating-a-custom-container-image.md](creating-a-custom-container-image.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Guide to building a custom MariaDB container image to include specific configuration files, scripts, or pre-loaded data.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="deploy-mariadb-enterprise-server-with-docker.md" %}
[deploy-mariadb-enterprise-server-with-docker.md](deploy-mariadb-enterprise-server-with-docker.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Instructions for deploying MariaDB Enterprise Server using the official enterprise Docker images, including handling license keys and entitlements.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-enterprise-docker-registry-for-mariadb-enterprise-server.md" %}
[mariadb-enterprise-docker-registry-for-mariadb-enterprise-server.md](mariadb-enterprise-docker-registry-for-mariadb-enterprise-server.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to authenticate with and pull images from the private MariaDB Enterprise Docker Registry.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="docker-and-aws-ec2.md" %}
[docker-and-aws-ec2.md](docker-and-aws-ec2.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Specific considerations and steps for running MariaDB Docker containers on Amazon EC2 instances.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="docker-and-google-cloud.md" %}
[docker-and-google-cloud.md](docker-and-google-cloud.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Guide for deploying MariaDB containers on Google Cloud Platform (GCP) compute resources.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="docker-and-microsoft-azure.md" %}
[docker-and-microsoft-azure.md](docker-and-microsoft-azure.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Instructions for running MariaDB containers within the Microsoft Azure ecosystem.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="docker-official-image-frequently-asked-questions.md" %}
[docker-official-image-frequently-asked-questions.md](docker-official-image-frequently-asked-questions.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Answers to common questions regarding the official MariaDB image, covering versioning, tagging, and default configurations.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="installing-and-using-mariadb-via-docker.md" %}
[installing-and-using-mariadb-via-docker.md](installing-and-using-mariadb-via-docker.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete guide to MariaDB in Docker. Complete resource for container deployment, volume management, networking, and environment setup for production use.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-container-cheat-sheet.md" %}
[mariadb-container-cheat-sheet.md](mariadb-container-cheat-sheet.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A concise reference of common Docker commands and environment variables used with MariaDB containers.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-server-docker-official-image-environment-variables.md" %}
[mariadb-server-docker-official-image-environment-variables.md](mariadb-server-docker-official-image-environment-variables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete guide to MariaDB in Docker. Complete resource for container deployment, volume management, networking, and environment setup for production use.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="setting-up-a-lamp-stack-with-docker-compose.md" %}
[setting-up-a-lamp-stack-with-docker-compose.md](setting-up-a-lamp-stack-with-docker-compose.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete LAMP stack Docker Compose: define docker-compose.yml services (web/mariadb), set volumes/env vars (${MARIADB_VERSION}), docker-compose up/down.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="using-healthcheck-sh.md" %}
[using-healthcheck-sh.md](using-healthcheck-sh.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete healthcheck.sh Docker reference: --connect, --innodb_initialized, --replication_* checks, .my-healthcheck.cnf config, and environment variables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-enterprise-container-image-configuration-reference.md" %}
[mariadb-enterprise-container-image-configuration-reference.md](mariadb-enterprise-container-image-configuration-reference.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configuration reference for the official MariaDB Enterprise container images — environment variables, command-line flags, and sidecar patterns for production deployments.
{% endcolumn %}
{% endcolumns %}
