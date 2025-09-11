# Serverless

SkySQL Serverless is the first true serverless database solution for the MySQL and MariaDB ecosystem, uniquely built to meet the dynamic demands of modern applications. SkySQL Serverless combines instant scalability with cost efficiency, scaling down to zero when idle—saving you from paying for unused capacity. When workloads resume, Serverless service is ready in milliseconds, ensuring a seamless, uninterrupted experience for applications and users.

### True Serverless Experience
- **Instant Launch**: Databases ready in milliseconds using pre-fabricated micro databases
- **Scale to Zero**: Complete resource deallocation during idle periods
- **Immediate Cold Start**: No delays during initialization

### Cloud-Native Architecture
- **No Forking**: Built on proven open-source MariaDB/MySQL without modifications
- **Kubernetes-Native**: Leverages custom controllers for fine-grained resource control
- **Multi-Cloud**: Deploy across AWS, Azure, and Google Cloud Platform

### Intelligent Scaling
- **Vertical Auto-Scaling**: CPU and memory adjustments in real-time
- **Horizontal Scaling**: Transparent live migrations for unlimited growth
- **Storage Auto-Scaling**: Dynamic storage expansion based on usage patterns

## Free Developer Tier

Every SkySQL account includes a perpetually free serverless database perfect for:
- Development and testing environments
- Learning and experimentation
- Proof-of-concept projects
- Small applications with intermittent usage

**Specifications:**
- 0.5 vCPU baseline
- 2GB memory baseline
- Auto-scaling up to 2 SCUs (SkySQL Compute Units)
- No time limits or restrictions

## Architecture Highlights

### Compute-Storage Approach
SkySQL takes a different approach from services like AWS Aurora:
- **Preserves Open Source**: No modifications to the mature InnoDB storage engine
- **Native Kubernetes**: Uses standard Kubernetes volume management
- **No Hidden Costs**: Transparent pricing without surprise IOPS charges

### Intelligent Proxy System
- **Always-On Connections**: Applications stay connected even when database scales to zero
- **Session State Management**: Preserves variables, prepared statements, and transaction state
- **Transparent Failover**: Automatic recovery from failures without application impact

### Buffer Pool Management
- **Performance Consistency**: Maintains cache hit ratios during scaling operations
- **Automatic Hydration**: Reloads frequently accessed data after scaling events
- **SSD Offloading**: Temporarily stores hot pages during scale-down operations

## Supported Workloads

SkySQL Serverless is designed to handle diverse workload types:

### Transactional Workloads (OLTP)
- High-frequency, low-latency operations
- ACID compliance and data consistency
- Connection pooling and session management

### Analytical Workloads (OLAP)
- Complex queries and reporting
- Integration with MariaDB ColumnStore
- On-demand analytics processing

### Semantic Search
- Vector database capabilities
- AI/ML application support
- Natural language query processing

## Getting Started

1. **[Create Account](https://app.skysql.com)** - Sign up for your free SkySQL account
2. **[Launch Service](../Quickstart/README.md)** - Follow our quickstart guide
3. **[Connect Application](../Connecting%20to%20SkySQL%20DBs/)** - Integrate with your applications
4. **[Monitor Performance](../Observability.md)** - Use built-in monitoring tools

