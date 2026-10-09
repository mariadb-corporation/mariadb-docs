---
description: >-
  Bring Your Own Cloud (BYOC) deploys MariaDB Cloud's data plane in your own
  AWS, GCP, or Azure account while the control plane (Portal, API, monitoring)
  stays in MariaDB Cloud.
---

# Bring Your Own Cloud (BYOC)

Bring Your Own Cloud (BYOC) allows large enterprises to deploy fully managed MariaDB Cloud databases directly within their own public cloud infrastructure. This deployment model offers the operational simplicity of a managed service while satisfying strict requirements for data sovereignty, compliance, and cloud cost optimization.

With BYOC, the Control Plane (UI, API, Monitoring) remains in MariaDB Cloud, while the Data Plane (Compute, Storage, Backups) resides entirely in your cloud account.

```mermaid
%%{init: {"themeVariables": {"edgeLabelBackground": "#eef2ff"}}}%%
flowchart LR
    accTitle: BYOC control plane and data plane
    accDescr {
        A left-to-right diagram of two groups and two outside actors. The MariaDB
        Cloud Control Plane group holds Portal and API, Orchestrator and Secure
        Bastion. The Your Cloud Account Data Plane group holds an IAM Role /
        Service Account and a nested group, Your Private VPC, which holds a
        Database Node and Storage. The DevOps Team and the Application are outside
        both groups. Five numbered arrows: 1 Request, from the DevOps Team to
        Portal and API. 2 Trigger, from Portal and API to the Orchestrator. 3
        Provision, from the Orchestrator to the IAM Role / Service Account. 4
        Manage (TLS), from the Secure Bastion to the Database Node. 5 Connect
        (private), from the Application to the Database Node. Three arrows are not
        numbered: a dotted arrow labelled creates, from the IAM Role / Service
        Account to Your Private VPC, a dotted arrow labelled internal, from the
        Orchestrator to the Secure Bastion, and a two-way arrow between the
        Database Node and Storage.
    }
    classDef control fill:#e3f2fd,stroke:#1565c0,stroke-width:2px,color:#0d47a1;
    classDef data fill:#fff3e0,stroke:#e65100,stroke-width:2px,color:#bf360c;
    classDef external fill:#eceff1,stroke:#546e7a,stroke-width:1px,color:#263238;

    User([DevOps Team]):::external
    App([Application]):::external

    subgraph CP ["MariaDB Cloud — Control Plane"]
        direction TB
        Portal["Portal and API"]:::control
        Orch["Orchestrator"]:::control
        Bastion["Secure Bastion"]:::control
    end

    subgraph CU ["Your Cloud Account — Data Plane"]
        direction TB
        IAM["IAM Role /<br/>Service Account"]:::data
        subgraph VPC ["Your Private VPC"]
            direction TB
            DB[("Database Node")]:::data
            Storage[("Storage")]:::data
        end
    end

    User -->|"1 Request"| Portal
    Portal -->|"2 Trigger"| Orch
    Orch -->|"3 Provision"| IAM
    IAM -.->|"creates"| VPC
    Orch -.->|"internal"| Bastion
    Bastion -->|"4 Manage (TLS)"| DB
    App -->|"5 Connect (private)"| DB
    DB <--> Storage
    linkStyle default color:#111111
```

## How it works

A BYOC environment is a secure, isolated set of resources within your own cloud provider account (Azure, AWS, or Google Cloud) that is managed by MariaDB Cloud.

```mermaid
flowchart LR
    accTitle: BYOC setup in four steps
    accDescr {
        A left-to-right sequence of four steps joined by arrows. Step 1, Account
        Linking (IAM handshake), leads to step 2, Provisioning (Compute, storage,
        network). Step 2 leads to step 3, Management (Patching and health). Step 3
        leads to step 4, Connectivity (Private access).
    }
    classDef step fill:#e3f2fd,stroke:#1565c0,stroke-width:2px,color:#0d47a1;

    S1["1. Account Linking<br/>IAM handshake"]:::step
    S2["2. Provisioning<br/>Compute, storage, network"]:::step
    S3["3. Management<br/>Patching and health"]:::step
    S4["4. Connectivity<br/>Private access"]:::step

    S1 --> S2 --> S3 --> S4
```

1. Account Linking: You authorize MariaDB Cloud to access your specific cloud subscription via a secure IAM role or Service Principal with least-privilege permissions.
2. Resource Provisioning: When you create a service, MariaDB Cloud orchestrates the deployment of Virtual Machines, Storage, and Networking directly into your account.
3. Management: MariaDB Cloud monitors health, performs backups, and applies patches automatically, just like a standard managed service.
4. Connectivity: Your applications connect to the database locally within your cloud network (VPC/VNet), ensuring low latency and high security without exposing data to the public internet.



### Why use BYOC?

BYOC is designed for enterprise organizations with specific regulatory or infrastructure requirements:

* Compliance & Data Sovereignty: Since data never leaves your cloud account, you maintain absolute control over data residency. This simplifies meeting strict regulatory standards such as HIPAA, PCI-DSS, and GDPR.
* Cloud Cost Optimization: You pay your cloud provider directly for the underlying infrastructure. This allows you to burn down existing committed spend (e.g., Azure MACC, AWS EDP) and leverage your negotiated enterprise discounts.
* Network Security: Database nodes are deployed into a private VPC/VNet. You can enforce your own security group rules, routing policies, and network isolation without complex peering arrangements.
* Advanced Workloads (PowerPlus): Enables the PowerPlus tier, allowing for advanced topologies like Galera Clusters to run in your own environment.

### Who is eligible for BYOC?

BYOC is an enterprise-grade feature with specific commercial and technical prerequisites:

* Service Tier: Your organization must be on the Power or PowerPlus tier.
* Support Plan: You must have Standard Support with the Remote DBA add-on enabled.
* Contract: Available to customers with annual contracts or minimum spend commitments.

{% hint style="info" %}
BYOC is a Tech Preview, currently available on Amazon Web Services and Microsoft Azure. Google Cloud support is coming soon.
{% endhint %}

### BYOC Pricing and Billing

The BYOC setup splits your costs into two separate components. This model ensures transparency and allows you to apply your own cloud credits or reserved instance savings to the infrastructure portion of the cost.

```mermaid
%%{init: {"themeVariables": {"edgeLabelBackground": "#eef2ff"}}}%%
flowchart LR
    accTitle: BYOC costs split across two invoices
    accDescr {
        Your Organization sends two arrows. An arrow labelled service fees leads
        to a box in the group Invoice 1, MariaDB Cloud, which lists Management
        fee, Support (Remote DBA) and Software licenses. An arrow labelled
        infrastructure costs leads to a box in the group Invoice 2, Your Cloud
        Provider, which lists Compute, Storage and Data transfer. A dotted arrow
        labelled apply committed spend and discounts leads from the Invoice 2 box
        back to Your Organization.
    }
    classDef maria fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#1b5e20;
    classDef cloud fill:#fff8e1,stroke:#f9a825,stroke-width:2px,color:#f57f17;
    classDef customer fill:#eceff1,stroke:#546e7a,stroke-width:1px,color:#263238;

    Customer(("Your<br/>Organization")):::customer

    subgraph B1 ["Invoice 1 — MariaDB Cloud"]
        M["Management fee<br/>Support (Remote DBA)<br/>Software licenses"]:::maria
    end

    subgraph B2 ["Invoice 2 — Your Cloud Provider"]
        C["Compute<br/>Storage<br/>Data transfer"]:::cloud
    end

    Customer -->|"service fees"| M
    Customer -->|"infrastructure costs"| C
    C -.->|"apply committed spend and discounts"| Customer
    linkStyle default color:#111111
```

1. MariaDB Cloud Invoice: You receive a bill from MariaDB for the management fee, software licensing, and support.
2. Cloud Provider Invoice: You receive a bill directly from your cloud provider for the consumed infrastructure resources (Compute, Storage, Network).

### Get Started

For the Tech Preview, onboarding is a guided process.

1. Contact Sales: Submit a request via the MariaDB Cloud Portal or contact your account representative to validate eligibility.
2. Onboarding: Our support team will provide the necessary IAM/Service Principal templates and guide you through the account linking process.
3. Deploy: Once linked, "Bring Your Own Cloud" will appear as a deployment target in your Create Service wizard.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
