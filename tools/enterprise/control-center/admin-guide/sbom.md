---
description: >-
  The CycloneDX Software Bill of Materials (SBOM) published for Control Center
  and Cloud Connector downloads and Docker images, and where to find it.
hidden: true
---

# Software Bill of Materials (SBOM)

A Software Bill of Materials (SBOM) lists the components that make up a software package. An SBOM is published for each Control Center and Cloud Connector download and Docker image. You can use it to track third-party components, scan them for known vulnerabilities, or meet your own supply-chain requirements.

## SBOM Format

The SBOMs are [CycloneDX](https://cyclonedx.org/specification/overview/) 1.6 documents in JSON format. They meet the NTIA and CISA 2026 minimum elements for SBOMs.

Each SBOM contains:

- The name and version of the package it describes.
- The author and supplier of the package, `MariaDB Plc`.
- Every bundled component, with its name, version, and package URL (`purl`).
- The SPDX license identifier of each component that declares a license.
- The tools used to generate the SBOM.

If a component's metadata does not state its supplier or license, the SBOM records the value as `NOASSERTION`.

Each SBOM describes only the package it is named after:

- The SBOM for the on-premise archive covers both the backend and the web application (frontend).
- The SBOM for a Docker image also covers the operating system packages and the Java runtime in the image.

## Downloading SBOMs

An SBOM has the same name as the file it describes, with the extension replaced by `.cdx.json`. SBOMs are published next to the Control Center downloads, at `https://www.gridgain.com/media/control-center/`.

| Package                                                   | SBOM                                                    |
| --------------------------------------------------------- | ------------------------------------------------------- |
| `gridgain-control-center-on-premise-<version>.zip`        | `gridgain-control-center-on-premise-<version>.cdx.json` |
| `gridgain/control-center-backend:<version>` Docker image  | `control-center-backend-<version>.cdx.json`             |
| `gridgain/control-center-frontend:<version>` Docker image | `control-center-frontend-<version>.cdx.json`            |
| `gridgain-cloud-connector-<version>.zip`                  | `gridgain-cloud-connector-<version>.cdx.json`           |
| `gridgain-cloud-connector-<version>_all.deb`              | `gridgain-cloud-connector-<version>_all.cdx.json`       |
| `gridgain-cloud-connector-<version>.noarch.rpm`           | `gridgain-cloud-connector-<version>.noarch.cdx.json`    |
| `gridgain/cloud-connector:<tag>` Docker image             | `cloud-connector-<tag>.cdx.json`                        |

The SBOMs for Docker images are published at the same location, even though the images themselves are hosted in a Docker registry.

## Using an SBOM

Any tool that reads CycloneDX 1.6 can import these files, for example [Dependency-Track](https://dependencytrack.org/). To list the components in an SBOM from the command line, use `jq`:

```shell
jq -r '.components[] | "\(.name) \(.version)"' gridgain-control-center-on-premise-<version>.cdx.json
```
