# MariaDB Cloud Region Choices

## **AWS Regions**

| Region         | Location                 | Available Service Type  |
| -------------- | ------------------------ | ----------------------- |
| ap-northeast-1 | Tokyo, Japan             | Provisioned             |
| ap-northeast-2 | Seoul, South Korea       | Provisioned             |
| ap-southeast-1 | Jurong West, Singapore   | Provisioned             |
| ap-southeast-2 | Sydney, Australia        | Provisioned             |
| ca-central-1   | Montréal, Québec, Canada | Provisioned             |
| eu-central-1   | Frankfurt, Germany       | Provisioned             |
| eu-north-1     | Stockholm, Sweden        | Provisioned             |
| eu-west-1      | Dublin, Ireland          | Provisioned             |
| eu-west-2      | London, England, UK      | Provisioned, Serverless |
| eu-west-3      | Paris, France            | Provisioned             |
| sa-east-1      | São Paulo, Brazil        | Provisioned             |
| us-east-1      | Northern Virginia, USA   | Provisioned             |
| us-east-2      | Ohio, USA                | Provisioned, Serverless |
| us-west-2      | Oregon, USA              | Provisioned             |

## **GCP Regions**

| Region                  | Location                                | Available Service Type   |
| ----------------------- | --------------------------------------- | ------------------------ |
| asia-northeast1         | Tokyo, Japan                            | Provisioned              |
| asia-south1             | Mumbai, India                           | Provisioned              |
| asia-southeast1         | Jurong West, Singapore                  | Provisioned              |
| asia-southeast2         | Jakarta, Indonesia                      | Provisioned              |
| australia-southeast1    | Sydney, Australia                       | Provisioned              |
| europe-north1           | Hamina, Finland                         | Provisioned              |
| europe-west1            | St. Ghislain, Belgium                   | Provisioned              |
| europe-west2            | London, England, UK                     | Provisioned , Serverless |
| europe-west3            | Frankfurt, Germany                      | Provisioned              |
| europe-west4            | Eemshaven, Netherlands                  | Provisioned              |
| europe-west9            | Paris, France                           | Provisioned              |
| northamerica-northeast1 | Montréal, Québec, Canada                | Provisioned              |
| us-central1             | Council Bluffs, Iowa, USA               | Provisioned, Serverless  |
| gcp-us-east1            | Moncks Corner, South Carolina, USA      | Provisioned              |
| us-east4                | Ashburn (Loudoun County), Virginia, USA | Provisioned              |
| us-west1                | The Dalles, Oregon, USA                 | Provisioned              |
| us-west2                | Los Angeles, California, USA            | Provisioned              |
| us-west4                | Las Vegas, Nevada, USA                  | Provisioned              |

## **Azure Regions**

| Region             | Location                 | Available Service Type  |
| ------------------ | ------------------------ | ----------------------- |
| eastus             | Richmond, Virginia, USA  | Provisioned, Serverless |
| eastus2            | Virginia, USA            | Provisioned             |
| westus2            | Seattle, Washington, USA | Provisioned             |
| uksouth            | London, England, UK      | Provisioned             |
| francecentral      | Paris, France            | Provisioned             |
| northeurope        | Dublin, Ireland          | Provisioned, Serverless |
| germanywestcentral | Frankfurt, Germany       | Provisioned             |
| southeastasia      | Jurong West, Singapore   | Provisioned             |

### Availability Zones and Latency Considerations

When deploying a highly available database service, nodes are distributed across multiple Availability Zones (AZs) within your selected region to maximize fault tolerance and protect against datacenter-level failures.

**Standard Replicated Topology:** Because standard Replicated topologies use asynchronous or semi-synchronous replication, deploying replicas across multiple AZs has a negligible impact on primary write latency.

**MariaDB Galera Clusters (Synchronous HA):** When deploying a MariaDB Galera Cluster across multiple AZs, you must account for inter-AZ network latency. Because Galera uses synchronous write-set certification, a transaction is not committed until all nodes in the cluster acknowledge it. The physical distance between Availability Zones in a given region will therefore introduce a slight commit latency to your write transactions.

{% hint style="warning" %}
**Tech Preview Advisory:** MariaDB Galera Clusters are currently available as a _Tech Preview_.
{% endhint %}
