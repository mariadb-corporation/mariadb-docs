---
description: >-
  Introduction to core Kubernetes concepts relevant to database administrators,
  such as StatefulSets, Persistent Volumes, and Services, and how they apply to
  MariaDB storage and networking.
---

# Kubernetes Overview for MariaDB Users

Kubernetes, or K8s, is software to orchestrate containers. It is released under the terms of an open source license, Apache License 2.0.

Kubernetes was originally developed by Google. Currently it is maintained by the Cloud Native Computing Foundation (CNCF), with the status of Graduated Project.

For information about how to setup a learning environment or a production environment, see [Getting started](https://kubernetes.io/docs/setup/) in Kubernetes documentation.

## Architecture

Kubernetes runs in a **cluster**. A cluster runs a **workload**: a set of servers that are meant to work together (web servers, database servers, etc).

A Kubernetes cluster consists of the following components:

* Nodes run containers with the servers needed by our applications.
* Controllersconstantly check the cluster nodes current state, and compare it with the desired state.
* A Control Plane is a set of different components that store the cluster desired state and take decisions about the nodes. The Control Plane provides an API that is used by the controllers.

For more information on Kubernetes architecture, see [Concepts](https://kubernetes.io/docs/concepts/) and [Kubernetes Components](https://kubernetes.io/docs/concepts/overview/components/) in Kubernetes documentation.

### Nodes

A node is a system that is responsible to run one or more pods. A pod is a set of containers that run a Kubernetes workload or part of it. All containers that run in the same pod are also located on the same node. Usually identical pods run on different nodes for fault tolerance.

For more details, see [Nodes](https://kubernetes.io/docs/concepts/architecture/nodes/) in the Kubernetes documentation.

Every node must necessarily have the following components:

| Component           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `kubelet`           | `kubelet` has a set of `PodSpecs` which describe the desired state of pods. It checks that the current state of the pods matches the desired state. It especially takes care that containers don't crash.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `kube-proxy`        | <p>In a typical Kubernetes cluster, several containers located in different pods need to communicate with other containers within the same pods for performance and fault tolerance reasons. When developing and deploying applications, the IP addresses of these containers are unknown in advance. For instance, an application server may need to connect to a MariaDB instance, but the MariaDB's IP will vary for each pod.</p><p>The primary role of <code>kube-proxy</code> is to manage Kubernetes services. When an application needs to connect to MariaDB, it connects to the MariaDB service instead.</p><p><code>kube-proxy</code> then receives the request and redirects it to a running MariaDB container within the same pod.</p> |
| `Container Runtime` | <p>Kubernetes orchestrates containers within a pod using a container runtime that complies with the Kubernetes Container Runtime Interface (CRI). Approved container runtimes are detailed on the <a href="https://kubernetes.io/docs/setup/production-environment/container-runtimes/">Container Runtimes page</a> of the Kubernetes documentation. Additional details about the CRI can be found on <a href="https://github.com/kubernetes/community/blob/master/contributors/devel/sig-node/container-runtime-interface.md">GitHub</a>.</p><p><em>Initially, Kubernetes defaulted to using Docker as its container runtime. Though now deprecated, Docker images remain viable with any compatible container runtime.</em></p>                   |

### Controllers

Controllers constantly check if there are differences between the pod's current state and their desired state. When differences are found, controllers try to fix them. Each node type controls one or more resource types. Several types of controllers are needed to run a cluster.

Most of the actions taken by the controllers user the API server in the Control Plane. However, this is not necessarily true for custom controllers. Also, some actions cannot be performed via the Control Plane. For example, if some nodes crashed, adding new nodes involves taking actions outside of the Kubernetes cluster, and controllers will have to do this themselves.

It is possible to write custom controllers to perform checks that require knowledge about a specific technology. For example, a MariaDB custom controller may want to check if [replication](../../../ha-and-performance/standard-replication/) is working by issuing [SHOW REPLICA STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-replica-status.md) commands. This logic is specific to the way MariaDB works, and can only be implemented in a customer controller. Custom controllers are usually part of operators.

For more information, see [Controllers](https://kubernetes.io/docs/concepts/architecture/controller/) in the Kubernetes documentation.

### Control Plane

The control plane consists of the following components.

For more information about the control plane, see [Control Plane Components](https://kubernetes.io/docs/concepts/overview/components/) in Kubernetes documentation.

#### API Server

An API Server exposes API functions both internally and externally. It is essential to coordinate Kubernetes components so that they react to node's change of state, and it allows the user to send commands.

The default implementation of the API Server is kube-apiserver. It is able to scale horizontally and to balance the load between its instances.

| Component                  | Description                                                                                                                                                  |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `kube-controller-manager`  | Most controllers run in this component.                                                                                                                      |
| `etcd`                     | Contains all data used by a Kubernetes cluster. Taking regular backups of etcd data is advisable.                                                            |
| `kube-scheduler`           | Decides which node should host a new pod based on criteria like resource requirements.                                                                       |
| `cloud-controller-manager` | Implements logic and API of a cloud provider. Handles requests from the API Server and performs actions specific to a cloud vendor, like creating instances. |

### Clients and Tools

Kubernetes comes with a set of tools that allow us to communicate with the API server and test a cluster.

| Tool       | Description                                                                                                                                                                                    |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `kubectl`  | Enables communication with the API server and allows running commands on a Kubernetes cluster.                                                                                                 |
| `kubeadm`  | Facilitates the creation of a Kubernetes cluster ready to receive commands from kubectl.                                                                                                       |
| `kind`     | Used to create and manage test clusters on a personal machine. It creates a cluster consisting of Docker containers, requiring Docker to be installed. Available on Linux, MacOS, and Windows. |
| `minikube` | Runs a single-node cluster on the local machine. Available on Linux, MacOS, and Windows.                                                                                                       |

## Kubernetes Resources and References

* [Kubernetes website](https://kubernetes.io/).
* [Kubernetes](https://en.wikipedia.org/wiki/Kubernetes) on Wikipedia.
* [Kubernetes organization](https://github.com/kubernetes) on GitHub.
* [The Official MariaDB Operator](https://github.com/mariadb-operator/mariadb-operator)
* [OperatorHub.io](https://operatorhub.io/)
* [Kubernetes Community Forums](https://discuss.kubernetes.io/).
* (video) [MariaDB database clusters on Kubernetes](https://mariadb.org/fest2020/kubernetes/), by Pengfei Ma, at MariaDB Server Fest 2020.
* Series of posts by Anel Husakovic on the MariaDB Foundation blog:
  * [Start MariaDB in K8s](https://mariadb.org/start-mariadb-in-k8s/)
  * [MariaDB & K8s: Communication between containers/Deployments](https://mariadb.org/mariadb-k8s-communication-between-containers-deployments/)
  * [MariaDB & K8s: Create a Secret and use it in MariaDB deployment](https://mariadb.org/mariadb-k8s-create-a-secret-and-use-it-in-mariadb-deployment/)
  * [MariaDB & K8s: Deploy MariaDB and WordPress using Persistent Volumes](https://mariadb.org/mariadb-k8s-deploy-mariadb-and-wordpress-using-persistent-volumes/)
  * [Create statefulset MariaDB application in K8s](https://mariadb.org/create-statefulset-mariadb-application-in-k8s/)
  * [MariaDB replication using containers](https://mariadb.org/mariadb-replication-using-containers/)
  * [MariaDB & K8s: How to replicate MariaDB in K8s](https://mariadb.org/mariadb-k8s-how-to-replicate-mariadb-in-k8s/)

Content initially contributed by [Vettabase Ltd](https://vettabase.com/).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
