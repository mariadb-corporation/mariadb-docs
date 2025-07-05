# Installing MariaDB on IBM Cloud

Get MariaDB on IBM Cloud

You should have an IBM Cloud account, otherwise you can [register here](https://cloud.ibm.com/registration).\
At the end of the tutorial you will have a cluster with MariaDB up and running. IBM Cloud uses Bitnami charts to deploy MariaDB on with helm

1. We will provision a new Kubernetes Cluster for you if, you already have one skip to step **2**
2. We will deploy the IBM Cloud Block Storage plug-in, if already have it skip to step **3**
3. MariaDB deployment

## Step 1 provision Kubernetes Cluster

* Click the Catalog button on the top
* Select Service from the catalog
* Search for Kubernetes Service and click on it

![kubernetes-select](<../../../.gitbook/assets/kubernetes-select (1).png>)

* You are now at the Kubernetes deployment page, you need to specify some details about the cluster
* Choose a plan standard or free, the free plan only has one worker node and no subnet, to provision a standard cluster, you will need to upgrade you account to Pay-As-You-Go
* To upgrade to a Pay-As-You-Go account, complete the following steps:
* In the console, go to Manage > Account.
* Select Account settings, and click Add credit card.
* Enter your payment information, click Next, and submit your information
* Choose classic or VPC, read the [docs](https://cloud.ibm.com/docs/containers?topic=containers-infrastructure_providers) and choose the most suitable type for yourself

![infra-select](<../../../.gitbook/assets/infra-select (1).png>)

* Now choose your location settings, for more information please visit [Locations](https://cloud.ibm.com/docs/containers?topic=containers-regions-and-zones#zones)
* Choose Geography (continent)

![location-geo](<../../../.gitbook/assets/location-geo (1).png>)

* Choose Single or Multizone, in single zone your data is only kept in on datacenter, on the other hand with Multizone it is distributed to multiple zones, thus safer in an unforseen zone failure

![location-avail](<../../../.gitbook/assets/location-avail (1).png>)

* Choose a Worker Zone if using Single zones or Metro if Multizone

![location-worker](<../../../.gitbook/assets/location-worker (1).png>)

* If you wish to use Multizone please set up your account with [VRF](https://cloud.ibm.com/docs/dl?topic=dl-overview-of-virtual-routing-and-forwarding-vrf-on-ibm-cloud) or [enable Vlan spanning](https://cloud.ibm.com/docs/vlans?topic=vlans-vlan-spanning#vlan-spanning)
* If at your current location selection, there is no available Virtual LAN, a new Vlan will be created for you
* Choose a Worker node setup or use the preselected one, set Worker node amount per zone

![worker-pool](<../../../.gitbook/assets/worker-pool (1).png>)

* Choose Master Service Endpoint, In VRF-enabled accounts, you can choose private-only to make your master accessible on the private network or via VPN tunnel. Choose public-only to make your master publicly accessible. When you have a VRF-enabled account, your cluster is set up by default to use both private and public endpoints. For more information visit [endpoints](https://cloud.ibm.com/docs/account?topic=account-service-endpoints-overview).

![endpoints](<../../../.gitbook/assets/endpoints (1).png>)

* Give cluster a name

![name-new](<../../../.gitbook/assets/name-new (1).png>)

* Give desired tags to your cluster, for more information visit [tags](https://cloud.ibm.com/docs/account?topic=account-tag)

![tasg-new](<../../../.gitbook/assets/tasg-new (1).png>)

* Click create

![create-new](<../../../.gitbook/assets/create-new (1).png>)

* Wait for you cluster to be provisioned

![cluster-prepare](<../../../.gitbook/assets/cluster-prepare (1).png>)

* Your cluster is ready for usage

![cluster-done](<../../../.gitbook/assets/cluster-done (1).png>)

## Step 2 deploy IBM Cloud Block Storage plug-in

The Block Storage plug-in is a persistent, high-performance iSCSI storage that you can add to your apps by using Kubernetes Persistent Volumes (PVs).

* Click the Catalog button on the top
* Select Software from the catalog
* Search for IBM Cloud Block Storage plug-in and click on it

![block-search](<../../../.gitbook/assets/block-search (1).png>)

* On the application page Click in the dot next to the cluster, you wish to use
* Click on Enter or Select Namespace and choose the default Namespace or use a custom one (if you get error please wait 30 minutes for the cluster to finalize)

![block-cluster](<../../../.gitbook/assets/block-cluster (1).png>)

* Give a name to this workspace
* Click install and wait for the deployment

![block-storage-create](<../../../.gitbook/assets/block-storage-create (1).png>)

## Step 3 deploy MariaDB

We will deploy MariaDB on our cluster

* Click the Catalog button on the top
* Select Software from the catalog
* Search for MariaDB and click on it

![search](<../../../.gitbook/assets/search (1).png>)

* Please select IBM Kubernetes Service

![target-select](../../../.gitbook/assets/target-select.png)

* On the application page Click in the dot next to the cluster, you wish to use

![cluster-select](<../../../.gitbook/assets/cluster-select (1).png>)

* Click on Enter or Select Namespace and choose the default Namespace or use a custom one

![details-namespace](<../../../.gitbook/assets/details-namespace (1).png>)

* Give a unique name to workspace, which you can easily recognize

![details-name](<../../../.gitbook/assets/details-name (1).png>)

* Select which resource group you want to use, it's for access controll and billing purposes. For more information please visit [resource groups](https://cloud.ibm.com/docs/account?topic=account-account_setup#bp_resourcegroups)

![details-resource](<../../../.gitbook/assets/details-resource (1).png>)

* Give tags to your MariaDB, for more information visit [tags](https://cloud.ibm.com/docs/account?topic=account-tag)

![details-tags](../../../.gitbook/assets/details-tags.png)

* Click on Parameters with default values, You can set deployment values or use the default ones

![parameters](<../../../.gitbook/assets/parameters (1).png>)

* Please set the MariaDB root password in the parameters

![root-password](../../../.gitbook/assets/root-password.png)

* After finishing everything, tick the box next to the agreements and click install

![aggreement-create](<../../../.gitbook/assets/aggreement-create (1).png>)

* The MariaDB workspace will start installing, wait a couple of minutes

![in-progress](<../../../.gitbook/assets/in-progress (1).png>)

* Your MariaDB workspace has been successfully deployed

![done](<../../../.gitbook/assets/done (1).png>)

## Verify MariaDB installation

* Go to [Resources](https://cloud.ibm.com/resources) in your browser
* Click on Clusters
* Click on your Cluster

![resource-select](<../../../.gitbook/assets/resource-select (1).png>)

* Now you are at you clusters overview, here Click on Actions and Web terminal from the dropdown menu

![cluster-main](<../../../.gitbook/assets/cluster-main (1).png>)

* Click install - wait couple of minutes

![terminal-install](<../../../.gitbook/assets/terminal-install (1).jpg>)

* Click on Actions
* Click Web terminal --> a terminal will open up
* Type in the terminal, please change NAMESPACE to the namespace you choose at the deployment setup:

```
$ kubectl get ns
```

![get-ns](<../../../.gitbook/assets/get-ns (1).png>)

```
$ kubectl get pod -n NAMESPACE -o wide
```

![get-pods](../../../.gitbook/assets/get-pods.png)

```
$ kubectl get service -n NAMESPACE
```

![get-service](../../../.gitbook/assets/get-service.png)

* Enter your pod with bash , please replace PODNAME with your mariadb pod's name

```
$ kubectl exec --stdin --tty PODNAME -n NAMESPACE -- /bin/bash
```

![bash](<../../../.gitbook/assets/bash (1).png>)

* After you are in your pod please enter Mariadb and enter your root password after the prompt

```
$ mysql -u root -p
```

![welcome](<../../../.gitbook/assets/welcome (1).png>)

You have succesfully deployed MariaDB IBM Cloud!

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
