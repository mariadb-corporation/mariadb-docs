#!/bin/bash

if [ "$1" == "" ]
then
    echo "usage: $0 major.minor.patch [maturity] [release-date]"
    echo "       release-date is free-form, house style is '15 Jun 2026'."
    exit 1
fi

VERSION=$1

patch=${VERSION##*.}
major_minor=${VERSION%.*}
major=${major_minor%%.*}
minor=${major_minor##*.}

if [ "$2" == "" ]
then
    echo "No maturity specified, assuming GA."
    maturity="GA"
else
    maturity=$2
fi

if [ "$3" == "" ]
then
    echo "No release date specified, leaving a TBD placeholder."
    release_date="TBD"
    release_date_is_tbd=yes
else
    release_date=$3
fi

if [ ! -d "$major_minor" ]
then
    echo "error: $major_minor does not exist or is not a directory."
    exit 1
fi

# Script location
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

output=$major.$minor/$VERSION.md

echo Creating/overwriting $output.
echo

# For version 6, this is just the major version. For other versions, it
# is $major.$minor. Needs to be updated whenever a new major release is
# out or if the versioning scheme for MaxScale changes.
upgrade_version="$major.$minor"

# Literal license notice, per DOCS-6394 — release-notes pages carry the notice
# inline rather than via a reusable include. Every MaxScale series from 22.08
# onwards uses the copyright form (21.06 and older use CC BY-SA / GNU FDL).
# The year is intentionally hardcoded so generated pages match their siblings;
# bump it here whenever the repo-wide notice year is bumped.
license_notice='<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>'

cat <<EOF > $output
# MaxScale ${VERSION} Release Notes

Release ${VERSION} is a ${maturity} release.

**Release Date:** ${release_date}

This document describes the changes in release ${VERSION}, when compared to the previous release in the same series.

If you are upgrading from an older major version of MaxScale, please read the [upgrading document](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-management/deployment/upgrading-maxscale) for this MaxScale version.

For any problems you encounter, please consider submitting a bug report on [our Jira](https://jira.mariadb.org/projects/MXS).

`${SCRIPT_DIR}/list_fixed.sh ${VERSION}`

## Known Issues and Limitations

There are some limitations and known issues within this version of MaxScale. For more information, please refer to the [Limitations](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-management/mariadb-maxscale-limitations-guide) document.

## Packaging

RPM and Debian packages are provided for the supported Linux distributions.

Packages can be downloaded [here](https://mariadb.com/downloads).

$license_notice

{% @marketo/form formid="4316" formId="4316" %}
EOF

echo Manually update the following files:
echo - $major.$minor/$major.$minor-changelog.md
echo - ./all-releases.md
echo - ../SUMMARY.md.

if [ "$release_date_is_tbd" == "yes" ]
then
    echo
    echo "WARNING: $output has 'Release Date: TBD' - set the real date before committing."
fi
