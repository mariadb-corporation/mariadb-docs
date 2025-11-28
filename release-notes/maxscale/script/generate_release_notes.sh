#!/bin/bash

if [ "$1" == "" ]
then
    echo "usage: $0 major.minor.patch [maturity]"
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

cat <<EOF > $output
# MariaDB MaxScale ${VERSION} Release Notes

Release ${VERSION} is a ${maturity} release.

This document describes the changes in release ${VERSION}, when compared to the
previous release in the same series.

If you are upgrading from an older major version of MaxScale, please read the
[upgrading document](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-management/deployment/upgrading-maxscale)
for this MaxScale version.

For any problems you encounter, please consider submitting a bug
report on [our Jira](https://jira.mariadb.org/projects/MXS).

`${SCRIPT_DIR}/list_fixed.sh ${VERSION}`

## Known Issues and Limitations

There are some limitations and known issues within this version of MaxScale.
For more information, please refer to the
[Limitations](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-management/mariadb-maxscale-limitations-guide)
document.

## Packaging

RPM and Debian packages are provided for the supported Linux distributions.

Packages can be downloaded [here](https://mariadb.com/downloads).

## Source Code

The source code of MaxScale is tagged at GitHub with a tag, which is identical
with the version of MaxScale. For instance, the tag of version X.Y.Z of MaxScale
is \`maxscale-X.Y.Z\`. Further, the default branch is always the latest GA version
of MaxScale.

The source code is available [here](https://github.com/mariadb-corporation/MaxScale).
EOF

echo Manually update the following files:
echo - $major.$minor/$major.$minor-changelog.md
echo - ./all-releases.md
echo - ../SUMMARY.md.
