---
description: >-
  Deploy user code to GridGain 9 cluster nodes as immutable deployment units
  using the CLI, REST API, or manual placement, and manage their lifecycle.
---

# Code Deployment

When working with GridGain, you may need to deploy user code to cluster nodes so that it can be executed across the cluster, as shown in the [Distributed Computing](distributed-computing/about-distributed-computing.md) section.

In GridGain 9 the code is deployed as an immutable *deployment unit* with a unique ID and version.

While there are no strict policies on what a deployment unit can contain, GridGain 9 currently supports compute jobs implemented in Java and .NET.

{% hint style="info" %}
You can invoke compute job execution from any client (.NET, Java, C++, etc. ), but the job itself must be written in Java or .NET.
{% endhint %}

{% hint style="info" %}
The Java examples on this page use the thin client, which requires the `ignite-client` module. For repository and dependency configuration, see [Project Setup and Required Modules](project-setup.md).
{% endhint %}

If you want to use any other programming language in a compute job, you must load that file as part of the job's code. A code file deployed on its own will not be loaded by the JVM and thus cannot be used directly.

The example below demonstrates how to load a script that is packaged within a deployment unit:

```java
public class MyJob implements ComputeJob<String, String> {
    @Override
    public CompletableFuture<String> executeAsync(JobExecutionContext ctx, String arg) {
        Ignite ignite = ctx.ignite();

        /** Full path to the script we want to run */
        final String resPath = "/org/apache/ignite/example/code/deployment/resources/script.sh";

        try (InputStream in = MyJob.class.getResourceAsStream(resPath)) {
            if (in == null) {
                throw new IllegalStateException("Resource not found: " + resPath);
            }

            byte[] script = in.readAllBytes();

            Process p = new ProcessBuilder("sh", "-s", "--", arg)
                    .redirectErrorStream(true)
                    .start();

            try (OutputStream os = p.getOutputStream()) {
                os.write(script);
            }

            String out;
            try (InputStream procOut = p.getInputStream()) {
                out = new String(procOut.readAllBytes(), StandardCharsets.UTF_8).strip();
            }

            int exit = p.waitFor();
            if (exit != 0) {
                throw new RuntimeException("Script exited with code " + exit + ":\n" + out);
            }

            String result = "Node: " + ignite.name()
                    + "\nArg: " + arg
                    + "\nScript output:\n" + out;

            return CompletableFuture.completedFuture(result);
        } catch (Exception e) {
            throw new RuntimeException("Failed to run script", e);
        }
    }
}
```

You can manage deployment units using either [CLI](../reference/cli-tool.md) commands or the [REST API](https://www.gridgain.com/sdk/gridgain9/latest/openapi.html#tag/deployment). Both methods provide the same functionality for deploying, listing, and undeploying code.

## Deploying Units with Folder Structures

{% hint style="info" %}
Currently, only ZIP archives can be deployed via REST.
{% endhint %}

GridGain supports deploying units that contain folder structures packaged as ZIP archives.

You can package complex deployment units consisting of multiple files organized in directories. During deployment, the archive is automatically extracted, and the folder structure is preserved.

To deploy code in this format, package the files into a ZIP archive and deploy it to the cluster. The original directory structure will be retained.

GridGain 9 also supports deploying a folder with subfolders recursively using the CLI. For more details, see [the corresponding section](../reference/cli-tool.md#cluster-unit-deploy) on using the CLI for deployment.

## Deployment Unit Location

By default, nodes store the deployment units in the `{GRIDGAIN_HOME}/work/deployment` directory. This can be changed with the [`ignite.deployment.location`](../reference/configuration/node-configuration-parameters.md#code-deployment-configuration) node configuration parameter.

The deployment units have the following structure:

```
deployment
├─ unit1Id
│  ├─ version1
│  └─ version2
└─ unit2Id
   ├─ version1
   │  ├─ folder1
   │  └─ folder2
   └─ version2
      ├─ folder1
      └─ folder2
```

{% hint style="warning" %}
When deploying the unit to a node that runs on a case-insensitive file system (for example, Windows or MacOS), files in the deployment unit must have unique names regardless of case. For example, `file1.java` and `File1.java` are considered duplicates and cannot both be deployed. For deployment units with directory structures, this rule applies to both files and subdirectories in each directory.
{% endhint %}

Each deployment unit is stored in a separate directory, with each version having its own subdirectory.

## Deploy New Unit

Deploying a new unit requires specifying a unique string ID for the code and a version number.

{% hint style="info" %}
To update the code, deploy a new unit. The new unit can use the same ID as the existing one, but it must have a different version.
{% endhint %}

### Deploy via CLI

When deploying a new unit, use `cluster unit deploy` command with unit's ID and set the following options:

| Parameter | Description |
| --- | --- |
| version | **Required** Deployment unit version in `x.y.z` format. If a unit with the same name and version already exists, a `Unit already exists` error will be thrown. |
| path | **Required** Path to the deployment unit file or directory. It is recommended to use an absolute path. |
| nodes | Defines the target nodes for deployment. Use `ALL` to deploy to every node immediately, `MAJORITY` to deploy to enough nodes for a management group majority (with remaining nodes updated later), or list specific node names (comma-separated) for immediate deployment to those nodes. |

{% hint style="info" %}
You cannot deploy multiple units simultaneously, you need to run `unit deploy` command separately for each file you want to deploy.
{% endhint %}

For example, to deploy to the majority of nodes use the following command:

```bash
cluster unit deploy test-unit --version 1.0.0 --path $ABSOLUTE_PATH_TO_CODE_UNIT --nodes MAJORITY
```

Here `$ABSOLUTE_PATH_TO_CODE_UNIT` refers to the absolute path to the code unit file or directory.

### Deploy via REST

To deploy a new unit via the REST API, send a `POST` request to the code deployment endpoint:

- `/management/v1/deployment/units/{unitId}/{unitVersion}` endpoint to deploy JAR files;
- `/management/v1/deployment/units/zip/{unitId}/{unitVersion}` endpoint to deploy ZIP files.

These endpoints have the following parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| unitId | path | **Required** Unique unit ID. If a deployment unit with this ID does not exist, it is created. |
| unitVersion | path | **Required** Unique version of the deployment unit. If a deployment unit with the specified ID and version already exists, HTTP 409 "Conflict" response is returned. |
| unitContent | file (multipart) | **Required** JAR file to deploy, provided as a file upload via multipart/form-data. |
| deployMode | query | Defines how many nodes the unit will be deployed to. If set to `MAJORITY`, the unit will be deployed to enough nodes to form cluster management group majority. If set to `ALL`, the unit will be deployed to all nodes. Cannot be used with the `initialNodes` parameter. |
| initialNodes | query | The list of names of specific nodes to deploy the unit to. Cannot be used with the `deployMode` parameter. |

For example, you can deploy a new unit to specific nodes in your local cluster as follows:

```bash
curl -X POST 'http://localhost:10300/management/v1/deployment/units/unit/1.0.0?initialNodes=node1,node2' \
  -H "Content-Type: multipart/form-data" \
  -F "unitContent=@/path/to/your/unit.jar"
```

- You can target nodes using either the `deployMode` or `initialNodes` parameter. These options serve the same purpose as the similar CLI parameters, ensuring the unit propagates as needed.

- For additional details see the corresponding [API documentation](https://www.gridgain.com/sdk/gridgain9/latest/openapi.html#tag/deployment).

### Deploy Manually

If necessary, you can deploy a new unit manually by adding your code to the deployment unit storage on the node. Unlike other deployment options, node restart is required to load new deployment units.

To deploy the code:

- Find the [deployment unit location](code-deployment.md#deployment-unit-location) on the node.
- Create a new directory. This directory will be used as the deployment unit ID.
- Create a new subdirectory. This directory will be used as the deployment unit version. You must use [semantic version](https://semver.org/) as its name.
- Add your code to the subdirectory.
- Restart the node to load the new code.

As a result, your directory structure may look like this:

```
deployment
└─ myUnit
  └─ 1.0.0
     └─ [code files]
```

## Getting Unit Information

This section explains how get all deployments on the cluster or on a specific node, view unit details such as status and version, and search or filter deployments by these attributes.

### Get Unit Information via CLI

You can list deployment units using `unit list` command, and inspect what files are included in the deployment unit with the `unit inspect` command.

#### Listing Deployment Units

{% hint style="info" %}
When you run the `unit list` command in the CLI, the output shows a list of deployment units. An asterisk (*) indicates the active version, which is always the highest [semantic version](https://semver.org/), regardless of deployment order.
{% endhint %}

- Use `cluster unit list` command to see all deployed units on the cluster.
- Use `node unit list` command to view only the units on the node where the command is executed.

In these commands, you can:

- Pass the unit's ID to the command to get information for the specific unit:

  ```bash
  cluster unit list test-unit
  ```
- Search units by adding `version` command options:

  ```bash
  cluster unit list test-unit --version 1.0.0
  ```
- Or filter by `status`:

  ```bash
  cluster unit list test-unit --status deployed
  ```

| Parameter | Description |
| --- | --- |
| statuses | Filter units by status.<br><br>• `UPLOADING` - the unit is being deployed to the cluster<br>• `DEPLOYED` - the unit is deployed to the cluster and can be used<br>• `OBSOLETE` - the command to remove unit has been received, but it is still used in some jobs<br>• `REMOVING` - the unit is being removed<br><br>If not specified, deployment units in all statuses will be returned. |

#### Inspecting Deployment Units

Use the `node unit inspect` to get detailed information about the structure of the deployment unit.

```bash
node unit inspect test-unit
```

### Get Unit Information via REST

You can also retrieve deployment unit details via `GET` requests.

- To get information for a specific unit on a node or across the cluster, use `/management/v1/deployment/node/units/{unitId}` and `/management/v1/deployment/cluster/units/{unitId}` respectively.

  ```bash
  curl -X GET 'http://localhost:10300/management/v1/deployment/cluster/units/test-unit/1.0.0'
  ```
- To list all deployment units for the node or across the cluster, use `/management/v1/deployment/node/units` and `/management/v1/deployment/cluster/units` respectively.

  ```bash
  curl -X GET 'http://localhost:10300/management/v1/deployment/cluster/units/'
  ```
- You can further narrow down the search by looking up only deployments with specific versions or statuses.

| Parameter | Type | Description |
| --- | --- | --- |
| unitId | path | **Required** Unique unit ID of the deployment unit. |
| version | query | Unique version of the deployment unit. If not specified, all versions of deployment unit will be returned. |
| statuses | query | Statuses of the deployment units to return. Possible values:<br><br>• `UPLOADING` - the unit is being deployed to the cluster<br>• `DEPLOYED` - the unit is deployed to the cluster and can be used<br>• `OBSOLETE` - the command to remove unit has been received, but it is still used in some jobs<br>• `REMOVING` - the unit is being removed<br><br>If not specified, deployment units in all statuses will be returned. |

## Undeploying Unit

When you no longer need a deployment unit version, you can undeploy it from the cluster.

### Undeploy via CLI

Use the `cluster unit undeploy` command. Provide unit ID and unit `version` to remove.

```bash
cluster unit undeploy test-unit --version 1.0.0
```

- You cannot undeploy all units with the same ID at once, you must remove them by version.

- When you undeploy a unit that has multiple versions, the active code rolls back to the next most recent version, determined by the version number.

### Undeploy via REST

To undeploy a unit from specific nodes, use a `DELETE` request to `/management/v1/deployment/units/{unitId}/{unitVersion}` endpoint.

For instance, to undeploy the same unit from nodes node1 and node2, use the following command:

```bash
curl -X DELETE 'http://localhost:10300/management/v1/deployment/units/test-unit/1.0.0?nodes=node1,node2'
```

When the cluster receives the request, it will delete the specified deployment unit version on all nodes.
If the unit is used in a job, it will instead be moved to the `OBSOLETE` status and removed once it is no longer required.
