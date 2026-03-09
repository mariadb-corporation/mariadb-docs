# Bring Your Own Account (BYOA)

Bring Your Own Account (BYOA) allows large enterprises to deploy fully managed MariaDB Cloud databases directly within their own public cloud infrastructure. This deployment model offers the operational simplicity of a managed service while satisfying strict requirements for data sovereignty, compliance, and cloud cost optimization.

With BYOA, the Control Plane (UI, API, Monitoring) remains in MariaDB Cloud, while the Data Plane (Compute, Storage, Backups) resides entirely in your cloud account.

```mermaid
flowchart LR
    %% BIG BLOCK STYLE - Aiven-like Visibility
    %% ---------------------------------------------------------
    classDef control fill:#e3f2fd,stroke:#1565c0,stroke-width:4px,color:#0d47a1,font-size:18px,font-weight:bold,rx:5,ry:5,min-width:180px,padding:15px;
    classDef data fill:#fff3e0,stroke:#e65100,stroke-width:4px,color:#bf360c,font-size:18px,font-weight:bold,rx:5,ry:5,min-width:180px,padding:15px;
    classDef external fill:#f5f5f5,stroke:#616161,stroke-width:2px,font-size:18px,font-weight:bold,min-width:150px;

    %% Actors
    User([DevOps Team]):::external
    App([Application]):::external

    %% 1. CONTROL PLANE (Left)
    subgraph MariaDB_Cloud ["MariaDB Control Plane"]
        direction TB
        Portal["Portal & API"]:::control
        Orch["Orchestrator"]:::control
    end

    %% 2. DATA PLANE (Right)
    subgraph Customer_Cloud ["Your Cloud Account"]
        direction TB
        IAM["IAM Role"]:::data
        
        subgraph VPC ["Your Private VPC"]
            direction TB
            Bastion["Secure Bastion"]:::data
            DB["Database Node"]:::data
        end
    end

    %% CONNECTIONS (Thick & Clear)
    User ==>|"1. Request"| Portal
    Portal ==>|"2. Trigger"| Orch
    
    Orch ==>|"3. Provision"| IAM
    IAM -.->|"Create"| VPC
    
    Orch ===>|"4. Manage (TLS)"| Bastion
    Bastion <==> DB

    App ==>|"5. Connect"| DB
    
    %% Spacer to force width
    Portal ~~~ Orch
```

## How it works

A BYOA environment is a secure, isolated set of resources within your own cloud provider account (Azure, AWS, or Google Cloud) that is managed by MariaDB Cloud.

```mermaid
flowchart LR
    %% Simplified diagram focusing on the 4 steps
    classDef step fill:#e3f2fd,stroke:#1565c0,stroke-width:2px,color:#0d47a1
    classDef resource fill:#fff3e0,stroke:#e65100,stroke-width:2px,color:#bf360c

    subgraph Steps ["Operational Workflow"]
        direction LR
        S1["1. Account Linking<br/>(IAM Handshake)"]:::step
        S2["2. Provisioning<br/>(VM Creation)"]:::step
        S3["3. Management<br/>(Patching/Health)"]:::step
        S4["4. Connectivity<br/>(Private Access)"]:::step
    end
    
    S1 --> S2
    S2 --> S3
    S3 --> S4
```

1. Account Linking: You authorize MariaDB Cloud to access your specific cloud subscription via a secure IAM role or Service Principal with least-privilege permissions.
2. Resource Provisioning: When you create a service, MariaDB Cloud orchestrates the deployment of Virtual Machines, Storage, and Networking directly into your account.
3. Management: MariaDB Cloud monitors health, performs backups, and applies patches automatically, just like a standard managed service.
4. Connectivity: Your applications connect to the database locally within your cloud network (VPC/VNet), ensuring low latency and high security without exposing data to the public internet.



### Why use BYOA?

BYOA is designed for enterprise organizations with specific regulatory or infrastructure requirements:

* Compliance & Data Sovereignty: Since data never leaves your cloud account, you maintain absolute control over data residency. This simplifies meeting strict regulatory standards such as HIPAA, PCI-DSS, and GDPR.
* Cloud Cost Optimization: You pay your cloud provider directly for the underlying infrastructure. This allows you to burn down existing committed spend (e.g., Azure MACC, AWS EDP) and leverage your negotiated enterprise discounts.
* Network Security: Database nodes are deployed into a private VPC/VNet. You can enforce your own security group rules, routing policies, and network isolation without complex peering arrangements.
* Advanced Workloads (PowerPlus): Enables the PowerPlus tier, allowing for advanced topologies like Galera Clusters to run in your own environment.

### Who is eligible for BYOA?

BYOA is an enterprise-grade feature with specific commercial and technical prerequisites:

* Service Tier: Your organization must be on the Power or PowerPlus tier.
* Support Plan: You must have Standard Support with the Remote DBA add-on enabled.
* Contract: Available to customers with annual contracts or minimum spend commitments.

{% hint style="info" %}
For the initial release (Jan 2026), BYOA is available as a Tech Preview on Microsoft Azure. AWS and Google Cloud support will follow in subsequent phases.
{% endhint %}

### BYOA Pricing and Billing

The BYOA setup splits your costs into two separate components. This model ensures transparency and allows you to apply your own cloud credits or reserved instance savings to the infrastructure portion of the cost.

```mermaid
flowchart LR
    %% Styles: Bold fonts, thick borders, distinct colors for clarity
    classDef maria fill:#e8f5e9,stroke:#2e7d32,stroke-width:3px,color:#1b5e20,font-size:16px,font-weight:bold;
    classDef cloud fill:#fff9c4,stroke:#fbc02d,stroke-width:3px,color:#f57f17,font-size:16px,font-weight:bold;
    classDef customer fill:#f5f5f5,stroke:#616161,stroke-width:2px,color:#212121,font-size:16px,font-weight:bold;

    Customer((Customer Organization)):::customer

    subgraph MariaDB_Bill ["Invoice 1: MariaDB Cloud"]
        direction TB
        M_Fees[("Management Fees<br/>Support (Remote DBA)<br/>Software Licenses")]:::maria
    end

    subgraph Cloud_Bill ["Invoice 2: Cloud Provider (AWS/Azure)"]
        direction TB
        C_Infra[("Compute (VMs)<br/>Storage (IOPS/Disk)<br/>Data Transfer")]:::cloud
    end

    %% Flows with thick arrows
    Customer ==>|"Pays Service Fees"| M_Fees
    Customer ==>|"Pays Infrastructure Costs"| C_Infra

    %% Benefit Annotation
    C_Infra -.->|"Apply committed spend<br/>(e.g., EDP / MACC)"| Customer

    %% Subgraph text styling
    style MariaDB_Bill fill:#ffffff,stroke:#2e7d32,stroke-width:2px,color:#2e7d32
    style Cloud_Bill fill:#ffffff,stroke:#fbc02d,stroke-width:2px,color:#f9a825
```

1. MariaDB Cloud Invoice: You receive a bill from MariaDB for the management fee, software licensing, and support.
2. Cloud Provider Invoice: You receive a bill directly from your cloud provider (e.g., Microsoft Azure) for the consumed infrastructure resources (Compute, Storage, Network).

### Get Started

For the Tech Preview (Jan 2026), onboarding is a guided process.

1. Contact Sales: Submit a request via the MariaDB Cloud Portal or contact your account representative to validate eligibility.
2. Onboarding: Our support team will provide the necessary IAM/Service Principal templates and guide you through the account linking process.
3. Deploy: Once linked, "Bring Your Own Account" will appear as a deployment target in your Create Service wizard.
