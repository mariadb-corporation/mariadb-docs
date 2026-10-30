---
description: >-
  GridGain Software Identification (SWID) tags — ISO 19770-2 XML artifacts that
  identify the product for software asset management tools, and where to find them.
---

# Software Identification (SWID Tags)

GridGain distributions include a Software Identification (SWID) tag — an ISO 19770-2 compliant XML artifact that uniquely identifies the product in software asset management (SAM) systems.

SWID tags are generated per package and included in ZIP, Docker, and other distributions. Each tag contains the product name, edition, and version, allowing SAM tools to accurately track GridGain installations across your environment.

## SWID Tag Location

### ZIP Distribution

The SWID tag is located in the `swidtag/` directory inside the unpacked archive:

```
gridgain-<edition>-<version>/
└── swidtag/
    └── com.gridgain.gridgain-<edition>_<version>.swidtag
```

### Docker Image

The SWID tag is located in the following directories inside the container, in a file named `com.gridgain.gridgain-<edition>_<version>.swidtag`:

```
/usr/share/swidtag/
/opt/gridgain/swidtag/
```

To extract it from a running container:

```shell
docker cp my-gridgain-node:/usr/share/swidtag/. .
```

Or from an image without starting a container:

```shell
docker run --rm --entrypoint sh gridgain/ultimate:8.10.0 -c "cat /usr/share/swidtag/*.swidtag"
```

## SWID Tag Fields

Each SWID tag is an XML file containing the following fields:

| Field | Location | Description |
|---|---|---|
| `name` | `SoftwareIdentity` | Product name. Value: `GridGain`. |
| `tagId` | `SoftwareIdentity` | Identifier of this tag, in the form `com.gridgain.gridgain-<edition>_<version>`. For example: `com.gridgain.gridgain-ultimate_8.10.0`. |
| `tagVersion` | `SoftwareIdentity` | Version of this SWID document. Value: `1`. |
| `version` | `SoftwareIdentity` | Full product version in `Major.Minor.Maintenance` format. For example: `8.10.0`. |
| `versionScheme` | `SoftwareIdentity` | Version format identifier. Value: `semver`. |
| `Entity name` | `Entity` | Product creator and tag creator. Value: `GridGain Systems`, with `role="tagCreator softwareCreator"` and `regid="regid.2009-11.com.gridgain"`. |
| `product` | `Meta` | Product name. Value: `GridGain`. |
| `productFamily` | `Meta` | Product family. Value: `GridGain`. |
| `edition` | `Meta` | Edition of the package. For example: `Ultimate`, `Enterprise`. |
| `summary` | `Meta` | Short product description. Value: `GridGain is an enterprise in-memory computing platform`. |

## Example SWID Tag

{% include "../.gitbook/includes/gg8-swid-example.md" %}

## Edition and Lifecycle Information

The `edition` attribute of the `Meta` element and the `tagId` encode the edition, for example:

- `Ultimate` (`com.gridgain.gridgain-ultimate_8.10.0`)
- `Enterprise` (`com.gridgain.gridgain-enterprise_8.10.0`)

The `version` attribute encodes the full version including major and minor components. These can be mapped to end-of-standard-support (EOS) dates using the [Versioning and Support Lifecycle](versioning-and-support-lifecycle.md) page.
