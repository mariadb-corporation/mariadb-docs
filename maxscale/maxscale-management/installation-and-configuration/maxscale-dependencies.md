---
description: >-
  How to obtain the complete list of MariaDB MaxScale runtime and build
  dependencies on Debian, Ubuntu, RHEL, Rocky Linux, Alma Linux, SLES, and
  container images.
---

# MaxScale Dependencies

MariaDB MaxScale does not require any external software at version-pinned ranges that you must track separately from the package itself. The platform packages (RPM, DEB) and the container image declare their runtime requirements through the standard packaging metadata, and your package manager resolves and installs the right versions for your operating system release.

This page describes how to enumerate those dependencies on each supported platform, so you can answer questions such as "Which exact libraries does MaxScale link against on this host?" or "What needs to be available before I can install or upgrade?" without guessing.

{% hint style="info" %}
If you need a CycloneDX Software Bill of Materials (SBOM) for compliance purposes such as SOC 2, FedRAMP, or the EU Cyber Resilience Act, [contact MariaDB Support](https://mariadb.com/support/).
{% endhint %}

## Debian and Ubuntu

Before installation, query the package's declared dependencies from the repository or a downloaded `.deb` file.

```bash
# From the configured MariaDB repository
apt-cache depends maxscale

# Recursive (the full transitive dependency tree)
apt-rdepends maxscale

# From a downloaded .deb file
dpkg-deb --info maxscale_*.deb | grep -E '^ (Depends|Recommends|Suggests):'
```

After installation, inspect the installed package metadata:

```bash
dpkg -s maxscale
dpkg -s maxscale-common
```

The `Depends:` and `Recommends:` lines list both the package-internal dependencies (for example, `maxscale-common`) and the system libraries pulled in by `dpkg-shlibdeps` at build time.

## RHEL, Rocky Linux, and Alma Linux

Before installation:

```bash
# From the configured MariaDB repository
dnf repoquery --requires maxscale
dnf repoquery --requires --resolve maxscale       # show concrete package versions

# From a downloaded .rpm file
rpm -qpR /path/to/maxscale-*.rpm
```

After installation:

```bash
rpm -qi maxscale
rpm -qR maxscale
rpm -qR maxscale-common
```

The `Requires:` entries cover both the internal `maxscale-common` dependency and the system libraries that `rpmbuild` detected as needed at link time.

## SLES

The commands match RHEL because SLES also uses RPM. The repository query uses `zypper`:

```bash
zypper info --requires maxscale
rpm -qR maxscale
```

## Container images

For MariaDB-published MaxScale container images, the dependencies are baked into the image layers. Use either the standard Docker tooling or a scanner that understands image layers:

```bash
# Inspect image labels and history
docker image inspect mariadb/maxscale:latest
docker image history mariadb/maxscale:latest

# Generate an SBOM from the running image (no MariaDB tooling required)
syft mariadb/maxscale:latest -o cyclonedx-json
trivy image --format cyclonedx mariadb/maxscale:latest
```

`syft` and `trivy` produce CycloneDX 1.6 output covering all OS packages plus any bundled language-level dependencies (for example, the `maxctrl` and MaxGUI Node.js trees).

## Shared library dependencies

To see exactly which shared libraries the running MaxScale binary and its loaded modules link against on a given host, use `ldd`:

```bash
ldd /usr/bin/maxscale
ldd /usr/lib/*/maxscale/*.so       # adjust path for your distribution layout
```

This is the most reliable way to answer "Does my host have everything MaxScale needs?" — `ldd` reports any unresolved symbols as `not found`.

## Building from source

When you build MaxScale from source, build-time dependencies are exhaustive and distribution-specific. The canonical list is the script that the MariaDB build infrastructure itself uses:

[`BUILD/install_build_deps.sh`](https://github.com/mariadb-corporation/MaxScale/blob/develop/BUILD/install_build_deps.sh) in the MaxScale source repository contains the full `apt-get install`, `yum install`, and `zypper install` invocations for every supported build platform. Running it (as root) installs everything required to build MaxScale on that host.

For step-by-step source-build instructions, see [Building MariaDB MaxScale from Source Code](https://github.com/mariadb-corporation/MaxScale/blob/develop/Documentation/Getting-Started/Building-MaxScale-from-Source-Code.md) in the MaxScale repository.
