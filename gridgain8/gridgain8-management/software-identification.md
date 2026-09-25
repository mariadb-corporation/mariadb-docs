---
description: >-
  GridGain Software Identification (SWID) tags — ISO 19770-2 XML artifacts that
  identify the product for software asset management tools, and where to find them.
---

# Software Identification (SWID Tags)

GridGain distributions include a Software Identification (SWID) tag — an ISO 19770-2 compliant XML artifact that uniquely identifies the product in software asset management (SAM) systems.

SWID tags are generated per package and included in ZIP, Docker, and other distributions. Each tag contains the product name, edition, version, target platform, and a SHA256 digest of the deliverable, allowing SAM tools to accurately track GridGain installations across your environment.

## SWID Tag Location

### ZIP Distribution

The SWID tag is located in the `swid/` directory inside the unpacked archive:

```
gridgain-<edition>-<version>/
└── swid/
    └── gridgain.swidtag
```

### Docker Image

The SWID tag is located at the following path inside the container:

```
/opt/gridgain/swid/gridgain.swidtag
```

To extract it from a running container:

```shell
docker cp my-gridgain-node:/opt/gridgain/swid/gridgain.swidtag .
```

Or from an image without starting a container:

```shell
docker run --rm --entrypoint cat gridgain/ultimate:8.9.33 /opt/gridgain/swid/gridgain.swidtag
```

## SWID Tag Fields

Each SWID tag is an XML file containing the following fields:

| Field | Type | Description |
|---|---|---|
| `tagId` | string (UUID) | Globally unique identifier for this SWID tag. |
| `tagVersion` | integer | Version of this SWID document. Starts at `1`. |
| `name` | string | Product name, including edition. For example: `GridGain 8 Ultimate Edition`, `GridGain 8 Enterprise Edition`. |
| `version` | string | Full product version in `Major.Minor.Maintenance` format. For example: `8.9.33`. |
| `versionScheme` | string | Version format identifier. Depends on the package format. For example: `semver` for ZIP and Docker, `rpm` for RPM packages. |
| `softwareCreator` | string | Product creator. Value: `GridGain Systems`. |
| `tagCreator` | string | Entity that generated this SWID tag. Value: `GridGain CI`. |
| `summary` | string | Short product description. For example: `GridGain in-memory computing platform`. |
| `os` | string | Target operating system. For example: `linux`, `windows`. |
| `arch` | string | Target architecture. For example: `amd64`, `arm64`. |
| `digest` | string | SHA256 digest of the deliverable package. |
| `format` | string | Package type. One of: `zip`, `docker`, `rpm`, `deb`, `tar`, `python`, `dotnet`. |

## Example SWID Tag

{% include "../.gitbook/includes/gg8-swid-example.md" %}

## Edition and Lifecycle Information

The `name` field encodes the product and edition, for example:

- `GridGain 8 Ultimate Edition`
- `GridGain 8 Enterprise Edition`

The `version` field encodes the full version including major and minor components. These can be mapped to end-of-standard-support (EOS) dates using the [Versioning and Support Lifecycle](versioning-and-support-lifecycle.md) page.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
