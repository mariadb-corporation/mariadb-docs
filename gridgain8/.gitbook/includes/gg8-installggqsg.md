GridGain is distributed as binary, docker, and cloud images, and via RPM/DEB. This chapter explains how to install the binary distribution.

To get started with the GridGain binary distribution:

1. Download the [GridGain binary](https://www.gridgain.com/resources/download) as a zip archive.
2. Unzip the zip archive into the installation folder in your system.
3. Move the `ignite-rest-http` folder from `{gridgain}/libs/optional` to `{gridgain}/libs` to enable the Ignite REST library for the cluster. The library is used by GridGain Control Center for cluster management and monitoring needs.
4. (Optional) Enable required [modules](../../gridgain8-usage/setup.md#enabling-modules).
5. (Optional) Set the `IGNITE_HOME` environment variable or Windows PATH to point to the installation folder and make sure there is no trailing `/` (or `\` for Windows) in the path.
