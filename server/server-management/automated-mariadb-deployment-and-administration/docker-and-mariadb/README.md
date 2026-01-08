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
