---
description: >-
  Understand the Software Identification (SWID) tags that GridGain 9
  distributions ship, where they are located, and the fields they carry.
---

# Software Identification (SWID Tags)

GridGain distributions include a Software Identification (SWID) tag — an XML artifact, defined by ISO/IEC 19770-2:2015, that identifies the installed product to software asset management (SAM) systems such as HCL BigFix Inventory and ServiceNow.

Each deliverable carries its own tag, placed at the location that SAM tooling scans for that package format. The tag records the product name, edition, and version, so SAM tools can discover GridGain installations across your environment without a custom detection rule.

{% hint style="info" %}
SWID tags are available in GridGain 9.1.23 and later.
{% endhint %}

## Tagged Deliverables

Tag files are named `<tagId>.swidtag`, where `tagId` combines the package identifier with the product version:

| Deliverable | Product Name | Tag File Name |
| --- | --- | --- |
| Database (ZIP, TAR, RPM, DEB, MSI) | `GridGain 9` | `com.gridgain.gridgain9-db_<version>.swidtag` |
| Docker image | `GridGain 9` | `com.gridgain.gridgain9-docker_<version>.swidtag` |
| CLI tool (ZIP, RPM, DEB) | `GridGain 9 CLI` | `com.gridgain.gridgain9-cli_<version>.swidtag` |
| ODBC driver (ZIP, TAR, RPM, DEB, MSI) | `GridGain 9 ODBC Driver` | `com.gridgain.gridgain9-odbc_<version>.swidtag` |

{% hint style="info" %}
The tag identifies the product and its version. It does not carry a checksum of the package — there is no `<Payload>`, `<File>`, or `<Hash>` element.
Package checksums are distributed separately, as SHA512 files.
{% endhint %}

## SWID Tag Location

### ZIP and TAR Archives

In the database and CLI archives, the tag is located in the `swidtag/` directory at the root of the unpacked archive:

```
gridgain9-db-9.1/
└── swidtag/
    └── com.gridgain.gridgain9-db_9.1.swidtag
```

The ODBC driver archives use a flat tree, so the tag is located in `lib/swidtag/` instead:

```
lib/
└── swidtag/
    └── com.gridgain.gridgain9-odbc_9.1.swidtag
```

### RPM and DEB Packages

The tag is installed to `/usr/lib/swidtag/`, the standard SWID discovery path on Linux. To list it:

{% tabs %}
{% tab title="RPM" %}
```bash
rpm -ql gridgain9-db | grep swidtag
```
{% endtab %}

{% tab title="DEB" %}
```bash
dpkg -L gridgain9-db | grep swidtag
```
{% endtab %}
{% endtabs %}

### Windows MSI Packages

The tag is located in the `swidtag` subdirectory of the installation directory.

### Docker Image

The tag is located in `/usr/lib/swidtag/` inside the container. To extract it from a running container:

```bash
docker cp my-gridgain-node:/usr/lib/swidtag/com.gridgain.gridgain9-docker_9.1.swidtag .
```

Or from an image without starting a container:

```bash
docker run --rm --entrypoint cat gridgain/gridgain9:9.1 /usr/lib/swidtag/com.gridgain.gridgain9-docker_9.1.swidtag
```

## SWID Tag Fields

The tag is a single `<SoftwareIdentity>` element with an `<Entity>` child and a `<Meta>` child. The following attributes are set:

| Attribute | Element | Description |
| --- | --- | --- |
| `name` | `SoftwareIdentity` | Product name. For example: `GridGain 9`, `GridGain 9 CLI`. |
| `tagId` | `SoftwareIdentity` | Identifier for this tag, in the form `<package-identifier>_<version>`. For example: `com.gridgain.gridgain9-db_9.1.23`. |
| `tagVersion` | `SoftwareIdentity` | Revision of this tag document. Value: `1`. |
| `version` | `SoftwareIdentity` | Product version, including any pre-release qualifier. For example: `9.1.23`, `9.1.23-p1`. |
| `versionScheme` | `SoftwareIdentity` | Format of the `version` attribute. Value: `semver`. |
| `xml:lang` | `SoftwareIdentity` | Language of the human-readable attribute values. Value: `en-US`. |
| `name` | `Entity` | Product and tag creator. Value: `GridGain Systems`. |
| `regid` | `Entity` | Registration identifier of the creator. Value: `regid.2009-11.com.gridgain`. |
| `role` | `Entity` | Roles held by the entity. Value: `tagCreator softwareCreator`. |
| `product` | `Meta` | Product name. Matches the `name` attribute of `SoftwareIdentity`. |
| `productFamily` | `Meta` | Product family. Value: `GridGain 9`. |
| `edition` | `Meta` | Product edition. Value: `Enterprise`. |
| `summary` | `Meta` | Short product description. |

For example, the tag shipped with the database ZIP archive:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<SoftwareIdentity
    xmlns="http://standards.iso.org/iso/19770/-2/2014-DIS/schema.xsd"
    xmlns:gg="https://www.gridgain.com/swid-ext/1.0"
    name="GridGain 9"
    tagId="com.gridgain.gridgain9-db_9.1.23"
    tagVersion="1"
    version="9.1.23"
    versionScheme="semver"
    xml:lang="en-US">

    <Entity
        name="GridGain Systems"
        regid="regid.2009-11.com.gridgain"
        role="tagCreator softwareCreator"/>

    <Meta
        product="GridGain 9"
        productFamily="GridGain 9"
        edition="Enterprise"
        summary="GridGain 9 is a distributed database for high-performance computing with in-memory speed"/>

</SoftwareIdentity>
```

The default namespace URI is `http://standards.iso.org/iso/19770/-2/2014-DIS/schema.xsd`.
This is the target namespace declared by the ISO/IEC 19770-2:2015 schema, and every generated tag is validated against that schema at build time.

## GridGain Extension Attributes

Where a deliverable targets a single platform and package format, the `<Meta>` element also carries attributes from the GridGain extension namespace `https://www.gridgain.com/swid-ext/1.0`:

| Attribute | Description |
| --- | --- |
| `gg:os` | Target operating system. Value: `linux`. |
| `gg:format` | Package format. Value: `docker`. |

The Docker image is currently the only deliverable that sets them:

```xml
<Meta
    product="GridGain 9"
    productFamily="GridGain 9"
    edition="Enterprise"
    summary="GridGain 9 distributed database Docker image"
    gg:os="linux"
    gg:format="docker"/>
```

These attributes are omitted from the ZIP, TAR, RPM, DEB, and MSI tags, because those deliverables are not restricted to a single platform.

ISO/IEC 19770-2:2015 permits attributes from other namespaces on the `<Meta>` element, so the tag remains valid against the standard schema.
SAM tools that do not recognize the extension namespace ignore these attributes.
