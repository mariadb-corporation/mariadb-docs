# Observability

This page provides a high-level overview of the Observability functionality in SkySQL.

In order to interact with our Observability APIs, an [API KEY](https://skysqlinc.github.io/skysql-docs/Security/Managing%20API%20keys/) must be generated. Throughout this document, we will refer to it as `{{SKYSQL_API_KEY}}`.

Additionally, you will need the SkySQL Database ID, available by clicking on any of your existing services from the [SkySQL Console](https://app.skysql.com/), and navigating to the Details page. We will Refer to the Database ID as `{{SKYSQL_DATABASE_ID}}` throughout this document.

For the impatient reader, we jump right to the [Integrations section](Observability.md#integrations), then for ones who are building custom instrumentation, we provide a detailed list of [APIs](Observability.md#apis) and their relevant documentation.

## Integrations

### Datadog

Using the [Datadog](https://www.datadoghq.com/) integration, you can instrument Observability metrics from SkySQL into your Datadog account. This integration allows you to monitor and visualize SkySQL metrics alongside other services in your Datadog dashboard.

#### Requirements.

You will need your Datadog API key to set up the integration. We will refer to it as `{{DD_API_KEY}}` throughout this document.

#### Agent Setup.

You will need to configure the Datadog Agent to pull metrics from us. Here is an example of how you can setup the [DataDog Agent](https://docs.datadoghq.com/agent/):

1. Create a local directory for configuration to be mapped to the Docker Container:

```shell
mkdir -p /home/datadog-agent/openmetrics
```

2. Create a `conf.yaml` file in your `openmetrics` directory with:

```yaml
init_config:

instances:
  - openmetrics_endpoint: https://api.skysql.com/observability/v2/metrics
    namespace: {{SKYSQL_DATABASE_ID}}
    extra_headers:
      X-API-KEY: {{SKYSQL_API_KEY}}
    metrics:
      - '.*'
```

3. Send the metrics to the correct DataDog Site. You should refer to [DataDog Site documentation](https://docs.datadoghq.com/getting_started/site/) to determine the correct `SITE PARAMETER` for your account. This resource provides a comprehensive list of Datadog sites and their corresponding `SITE PARAMETER` values, ensuring that your data is sent to the correct regional Datadog instance. We will refer to it as `{{DD_SITE_PARAMETER}}` throughout this document.
4. Run the Datadog Agent Docker Container with the following command:

```shell
docker run -v /home/datadog-agent/openmetrics:/etc/datadog-agent/conf.d/openmetrics.d:ro \
  -e DD_API_KEY={{DD_API_KEY}} -e DD_HOSTNAME="my-agent" -e DD_SITE="{{DD_SITE_PARAMETER}}" \ 
  -e DD_LOG_LEVEL="info" gcr.io/datadoghq/agent:7
```

5. You should see the metrics soon to be available in [DataDog Metrics Explorer](https://app.datadoghq.com/metric/explorer)

#### Testing [SkySQL APIs](Observability.md#apis)

If you can always check if the Observability API is working successfully by calling it directly:

```shell
curl --location 'https://api.skysql.com/observability/v2/metrics' \
--header 'X-API-KEY: {{SKYSQL_API_KEY}}'
```

Detailed documentation on how to interact with our [APIs](Observability.md#apis) follows:

## APIs

To build instrumentation around our [Observability APIs](https://apidocs.skysql.com/#/Observability), we expose the following endpoints:

#### Logs

SkySQL exposes a set of log-related endpoints under `observability/v2/logs`, allowing you to:

* Retrieve logs within a specified date range
* Download log archives
* Query log types and servers
* Manage log retention settings

Refer to the [Observability section of the SkySQL API docs](https://apidocs.skysql.com/#/Observability) for the full list of parameters and responses.

#### Metrics

You can retrieve metrics (in Prometheus-compatible format) from SkySQL using the `observability/v2/metrics` endpoint. To learn more about query parameters and usage, see:

Example:

```shell
curl --location 'https://api.skysql.com/observability/v2/metrics' \
--header 'X-API-KEY: {{SKYSQL_API_KEY}}'
```

Refer to the [Observability section of the SkySQL API docs](https://apidocs.skysql.com/#/Observability) for the full list of parameters and responses.

### API Documentation

For the complete, detailed API reference (including request/response formats, error codes, etc.), please see the official SkySQL API docs here:

* [SkySQL Observability (Logs + Metrics) Endpoints](https://apidocs.skysql.com/#/Observability).
* [Prometheus HTTP API](https://prometheus.io/docs/prometheus/latest/querying/api/).

### Appendix

#### Table A. Key Observability Metric Series

We export the folowing metrics as part of the [metrics](Observability.md#metrics) endpoint:

| Metric                                                       |
| ------------------------------------------------------------ |
| mariadb\_galera\_evs\_repl\_latency\_avg\_seconds            |
| mariadb\_galera\_evs\_repl\_latency\_max\_seconds            |
| mariadb\_galera\_evs\_repl\_latency\_min\_seconds            |
| mariadb\_galera\_status\_info                                |
| mariadb\_global\_status\_aborted\_clients                    |
| mariadb\_global\_status\_aborted\_connects                   |
| mariadb\_global\_status\_buffer\_pool\_pages                 |
| mariadb\_global\_status\_bytes\_received                     |
| mariadb\_global\_status\_bytes\_sent                         |
| mariadb\_global\_status\_commands\_total                     |
| mariadb\_global\_status\_created\_tmp\_disk\_tables          |
| mariadb\_global\_status\_created\_tmp\_files                 |
| mariadb\_global\_status\_created\_tmp\_tables                |
| mariadb\_global\_status\_handlers\_total                     |
| mariadb\_global\_status\_innodb\_data\_read                  |
| mariadb\_global\_status\_innodb\_data\_written               |
| mariadb\_global\_status\_innodb\_num\_open\_files            |
| mariadb\_global\_status\_innodb\_page\_size                  |
| mariadb\_global\_status\_open\_files                         |
| mariadb\_global\_status\_open\_table\_definitions            |
| mariadb\_global\_status\_open\_tables                        |
| mariadb\_global\_status\_opened\_files                       |
| mariadb\_global\_status\_opened\_table\_definitions          |
| mariadb\_global\_status\_opened\_tables                      |
| mariadb\_global\_status\_queries                             |
| mariadb\_global\_status\_questions                           |
| mariadb\_global\_status\_rows\_read                          |
| mariadb\_global\_status\_rows\_sent                          |
| mariadb\_global\_status\_select\_full\_join                  |
| mariadb\_global\_status\_select\_full\_range\_join           |
| mariadb\_global\_status\_select\_range                       |
| mariadb\_global\_status\_select\_range\_check                |
| mariadb\_global\_status\_select\_scan                        |
| mariadb\_global\_status\_slave\_running                      |
| mariadb\_global\_status\_slow\_queries                       |
| mariadb\_global\_status\_sort\_merge\_passes                 |
| mariadb\_global\_status\_sort\_range                         |
| mariadb\_global\_status\_sort\_rows                          |
| mariadb\_global\_status\_sort\_scan                          |
| mariadb\_global\_status\_table\_locks\_immediate             |
| mariadb\_global\_status\_table\_locks\_waited                |
| mariadb\_global\_status\_table\_open\_cache\_hits            |
| mariadb\_global\_status\_table\_open\_cache\_misses          |
| mariadb\_global\_status\_table\_open\_cache\_overflows       |
| mariadb\_global\_status\_threads\_cached                     |
| mariadb\_global\_status\_threads\_connected                  |
| mariadb\_global\_status\_threads\_created                    |
| mariadb\_global\_status\_threads\_running                    |
| mariadb\_global\_status\_uptime                              |
| mariadb\_global\_status\_wsrep\_cert\_deps\_distance         |
| mariadb\_global\_status\_wsrep\_cluster\_conf\_id            |
| mariadb\_global\_status\_wsrep\_cluster\_size                |
| mariadb\_global\_status\_wsrep\_cluster\_status              |
| mariadb\_global\_status\_wsrep\_connected                    |
| mariadb\_global\_status\_wsrep\_flow\_control\_paused        |
| mariadb\_global\_status\_wsrep\_last\_committed              |
| mariadb\_global\_status\_wsrep\_local\_recv\_queue           |
| mariadb\_global\_status\_wsrep\_local\_recv\_queue\_avg      |
| mariadb\_global\_status\_wsrep\_local\_recv\_queue\_max      |
| mariadb\_global\_status\_wsrep\_local\_recv\_queue\_min      |
| mariadb\_global\_status\_wsrep\_local\_send\_queue           |
| mariadb\_global\_status\_wsrep\_local\_send\_queue\_avg      |
| mariadb\_global\_status\_wsrep\_local\_send\_queue\_max      |
| mariadb\_global\_status\_wsrep\_local\_send\_queue\_min      |
| mariadb\_global\_status\_wsrep\_local\_state                 |
| mariadb\_global\_status\_wsrep\_ready                        |
| mariadb\_global\_status\_wsrep\_replicated                   |
| mariadb\_global\_status\_wsrep\_replicated\_bytes            |
| mariadb\_global\_variables\_gtid\_current\_pos               |
| mariadb\_global\_variables\_innodb\_buffer\_pool\_size       |
| mariadb\_global\_variables\_innodb\_log\_buffer\_size        |
| mariadb\_global\_variables\_key\_buffer\_size                |
| mariadb\_global\_variables\_max\_connections                 |
| mariadb\_global\_variables\_open\_files\_limit               |
| mariadb\_global\_variables\_query\_cache\_size               |
| mariadb\_global\_variables\_read\_only                       |
| mariadb\_global\_variables\_table\_open\_cache               |
| mariadb\_info\_schema\_engine\_table\_count\_total           |
| mariadb\_info\_schema\_table\_size                           |
| mariadb\_security\_users\_without\_passwords                 |
| mariadb\_slave\_status\_exec\_master\_log\_pos               |
| mariadb\_slave\_status\_last\_io\_errno                      |
| mariadb\_slave\_status\_last\_sql\_errno                     |
| mariadb\_slave\_status\_read\_master\_log\_pos               |
| mariadb\_slave\_status\_relay\_log\_pos                      |
| mariadb\_slave\_status\_seconds\_behind\_master              |
| mariadb\_slave\_status\_slave\_io\_running                   |
| mariadb\_slave\_status\_slave\_sql\_running                  |
| mariadb\_up                                                  |
| mariadb\_xpand\_activity\_core0                              |
| mariadb\_xpand\_activity\_til                                |
| mariadb\_xpand\_capacity\_disk\_system\_avail\_bytes         |
| mariadb\_xpand\_capacity\_disk\_system\_max\_bytes           |
| mariadb\_xpand\_capacity\_disk\_system\_usage\_ratio         |
| mariadb\_xpand\_capacity\_disk\_total\_usage\_percent        |
| mariadb\_xpand\_cluster\_nodes\_in\_quorum                   |
| mariadb\_xpand\_cluster\_total\_nodes                        |
| mariadb\_xpand\_cluster\_uptime\_seconds                     |
| mariadb\_xpand\_containers\_rows                             |
| mariadb\_xpand\_cpu\_load                                    |
| mariadb\_xpand\_io\_disk\_latency\_seconds                   |
| mariadb\_xpand\_io\_network\_bytes                           |
| mariadb\_xpand\_io\_network\_latency\_seconds                |
| mariadb\_xpand\_memory\_bm\_bytes                            |
| mariadb\_xpand\_memory\_reserved\_bytes                      |
| mariadb\_xpand\_memory\_total\_bytes                         |
| mariadb\_xpand\_memory\_working\_bytes                       |
| mariadb\_xpand\_qps                                          |
| mariadb\_xpand\_rebalancer\_jobs\_queued                     |
| mariadb\_xpand\_rebalancer\_rebalancer\_rebalance            |
| mariadb\_xpand\_rebalancer\_rebalancer\_reprotects           |
| mariadb\_xpand\_rebalancer\_rebalancer\_reranks              |
| mariadb\_xpand\_rebalancer\_rebalancer\_softfail\_reprotects |
| mariadb\_xpand\_rebalancer\_rebalancer\_splits               |
| mariadb\_xpand\_rebalancer\_underprotected\_slices           |
| mariadb\_xpand\_response\_time\_seconds                      |
| mariadb\_xpand\_sessions                                     |
| mariadb\_xpand\_sessions\_time\_in\_state                    |
| mariadb\_xpand\_sessions\_trx\_age                           |
| mariadb\_xpand\_stats\_Com\_alter\_cluster                   |
| mariadb\_xpand\_stats\_Com\_delete                           |
| mariadb\_xpand\_stats\_Com\_delete\_seconds                  |
| mariadb\_xpand\_stats\_Com\_insert                           |
| mariadb\_xpand\_stats\_Com\_insert\_seconds                  |
| mariadb\_xpand\_stats\_Com\_select                           |
| mariadb\_xpand\_stats\_Com\_select\_seconds                  |
| mariadb\_xpand\_stats\_Com\_set\_option                      |
| mariadb\_xpand\_stats\_Com\_show\_slave\_status              |
| mariadb\_xpand\_stats\_Com\_show\_status                     |
| mariadb\_xpand\_stats\_Com\_show\_variables                  |
| mariadb\_xpand\_stats\_Com\_update                           |
| mariadb\_xpand\_stats\_Com\_update\_seconds                  |
| mariadb\_xpand\_stats\_connections                           |
| mariadb\_xpand\_tps                                          |
| mariadb\_xpand\_wals\_avg\_sync\_time\_seconds               |
| maxscale\_modules                                            |
| maxscale\_server\_active\_operations                         |
| maxscale\_server\_adaptive\_avg\_select\_time                |
| maxscale\_server\_connection\_pool\_empty                    |
| maxscale\_server\_connections                                |
| maxscale\_server\_max\_connections                           |
| maxscale\_server\_max\_pool\_size                            |
| maxscale\_server\_persistent\_connections                    |
| maxscale\_server\_reused\_connections                        |
| maxscale\_server\_routed\_packets                            |
| maxscale\_server\_total\_connections                         |
| maxscale\_service\_connections                               |
| maxscale\_threads\_count                                     |
| maxscale\_threads\_current\_descriptors                      |
| maxscale\_threads\_errors                                    |
| maxscale\_threads\_event\_queue\_length                      |
| maxscale\_threads\_hangups                                   |
| maxscale\_threads\_max\_queue\_time                          |
| maxscale\_threads\_reads                                     |
| maxscale\_threads\_stack\_size                               |
| maxscale\_threads\_total\_descriptors                        |
| maxscale\_threads\_writes                                    |
| maxscale\_up                                                 |
| maxscale\_uptime\_seconds                                    |
| process\_resident\_memory\_bytes                             |
