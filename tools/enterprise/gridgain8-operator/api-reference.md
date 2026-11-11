---
description: >-
  Custom Resource Definitions and API fields for the GridGain 8 Kubernetes Operator.
---

# API Reference

## Packages
- [gridgain.gridgain.com/v1](#gridgain.gridgain.com-v1)


## gridgain.gridgain.com/v1

Package v1 contains the GridGainCluster API for gridgain.gridgain.com/v1.

### Resource Types
- [GridGainCluster](#gridgaincluster)



#### CacheExpiryPolicySpec



CacheExpiryPolicySpec configures ModifiedExpiryPolicy on every CacheConfiguration bean
(wildcard template and named caches from spec.caches).



_Appears in:_
- [DefaultCacheConfigurationSpec](#defaultcacheconfigurationspec)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `enabled` _boolean_ | Enabled adds eagerTtl and ModifiedExpiryPolicy to all cache defaults. |  |  |
| `durationSeconds` _integer_ | DurationSeconds is the TTL duration in seconds when Enabled is true.<br />Defaults to 180 when Enabled is true and DurationSeconds is omitted. |  | Minimum: 1 <br /> |


#### ClientServiceSpec



ClientServiceSpec describes the combined REST+thin client Service (Helm: services.default).



_Appears in:_
- [GridGainClusterSpec](#gridgainclusterspec)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `type` _[ServiceType](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#servicetype-v1-core)_ | Type is ClusterIP, NodePort, or LoadBalancer. |  | Enum: [ClusterIP NodePort LoadBalancer] <br /> |
| `sessionAffinity` _[ServiceAffinity](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#serviceaffinity-v1-core)_ | SessionAffinity for the Service. |  | Enum: [None ClientIP] <br /> |
| `annotations` _object (keys:string, values:string)_ | Annotations set on the Service. Clearing this map removes previously applied keys. |  |  |
| `labels` _object (keys:string, values:string)_ | Labels merged onto the Service. Operator identity/selector labels cannot be overridden. |  |  |
| `loadBalancerIP` _string_ | LoadBalancerIP when Type=LoadBalancer (cloud-specific). |  |  |
| `loadBalancerSourceRanges` _string array_ | LoadBalancerSourceRanges restricts ingress when Type=LoadBalancer. |  |  |
| `externalTrafficPolicy` _string_ | ExternalTrafficPolicy when Type is NodePort or LoadBalancer (Cluster or Local). |  | Enum: [Cluster Local] <br /> |
| `clusterIP` _string_ | ClusterIP requests a fixed cluster IP when Type=ClusterIP. |  |  |
| `restNodePort` _integer_ | RestNodePort pins the REST (8080) nodePort when Type is NodePort or LoadBalancer. |  | Maximum: 65535 <br />Minimum: 1 <br /> |
| `thinNodePort` _integer_ | ThinNodePort pins the thin-client (10800) nodePort when Type is NodePort or LoadBalancer. |  | Maximum: 65535 <br />Minimum: 1 <br /> |


#### ClusterAuth



ClusterAuth configures authentication (Helm: auth.enabled, secret-auth.xml).



_Appears in:_
- [GridGainClusterSpec](#gridgainclusterspec)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `enabled` _boolean_ | Enabled turns on passcode authentication and auth.xml materialization. |  |  |
| `serverCredentialId` _string_ | ServerCredentialID selects which PasscodeUser provides the node's credentials (ref server.cred).<br />Defaults to "server" when auth is enabled. The operator uses this user for drain REST and preStop. |  |  |
| `users` _[PasscodeUser](#passcodeuser) array_ | Users defines credentials; at least the server user must exist when Enabled is true (webhook). |  |  |


#### ClusterNetworkPolicySpec



ClusterNetworkPolicySpec configures an optional NetworkPolicy for GridGain pods (Helm: networkPolicy.*).



_Appears in:_
- [GridGainClusterSpec](#gridgainclusterspec)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `enabled` _boolean_ | Enabled creates a NetworkPolicy targeting workload pods (chart: networkPolicy.create). |  |  |
| `name` _string_ | Name overrides metadata.name; defaults to the GridGainCluster name (chart: networkPolicy.name default fullname). |  |  |
| `ingress` _[NetworkPolicyIngressRule](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#networkpolicyingressrule-v1-networking) array_ | Ingress rules (chart: networkPolicy.ingress). |  |  |
| `egress` _[NetworkPolicyEgressRule](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#networkpolicyegressrule-v1-networking) array_ | Egress rules (chart: networkPolicy.egress). |  |  |
| `policyTypes` _[PolicyType](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#policytype-v1-networking) array_ | PolicyTypes selects which rule sections apply; defaults to Ingress and Egress when enabled (chart template). |  |  |




#### ConfigMapMount



ConfigMapMount describes an operator-managed ConfigMap volume (Helm: configMaps.*).



_Appears in:_
- [GridGainClusterSpec](#gridgainclusterspec)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `suffix` _string_ | Suffix is appended to the cluster name to form the ConfigMap name. |  |  |
| `fileKey` _string_ | FileKey is the data key in the ConfigMap. |  |  |
| `mountPath` _string_ | MountPath is the full file path in the container. |  |  |
| `subPath` _string_ | SubPath is the subPath in the volume mount. |  |  |
| `content` _string_ | Content is the file body stored in the ConfigMap. |  |  |


#### DefaultCacheConfigurationSpec



DefaultCacheConfigurationSpec configures shared cache defaults in generated default-config.xml.
Applied to the wildcard (*) template and every named cache from spec.caches.



_Appears in:_
- [GridGainClusterSpec](#gridgainclusterspec)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `expiryPolicy` _[CacheExpiryPolicySpec](#cacheexpirypolicyspec)_ | ExpiryPolicy configures server-side default entry expiry (ModifiedExpiryPolicy).<br />Disabled by default. |  |  |


#### DrainSpec



DrainSpec configures the pre-deletion GridGain drain gate and preStop hook.
See docs/lifecycle.md.



_Appears in:_
- [GridGainClusterSpec](#gridgainclusterspec)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `supplyWaitTimeoutSeconds` _integer_ | SupplyWaitTimeoutSeconds bounds how long the operator waits for a node to<br />finish supplying partitions before deleting its pod. On expiry the gate<br />aborts: the upgrade fails with a recovery token, a scale-down holds the<br />replica count, and the node returns to service unless UndrainOnAbort is<br />false. 0 waits as long as supply runs. Default 3600.<br />The same value caps the preStop supply loop, clamped further by what<br />TerminationGracePeriodSeconds allows — past that, kubelet cuts the hook off<br />and leaves the JVM 2 seconds. | 3600 | Minimum: 0 <br /> |
| `undrainOnAbort` _boolean_ | UndrainOnAbort returns the node to service when the drain gate aborts<br />(POST cmd=drain&action=stop). Default true.<br />false parks the node instead: it stays NotReady indefinitely, which keeps it<br />out of the Service and freezes the PodDisruptionBudget, so node drains,<br />cluster-autoscaler scale-down and the descheduler block on this cluster until<br />a human intervenes. | true |  |
| `shutdownDelaySeconds` _integer_ | ShutdownDelaySeconds is the preStop settle window before SIGTERM, giving work<br />already in flight (a long SQL query, a scan) time to finish. It is not a<br />connection drain: neither the drain command nor leaving the Service endpoints<br />closes established thin-client connections. 0 disables it. Default 30.<br />This value is part of the preStop script, so changing it changes the pod<br />template and triggers a managed rolling upgrade. | 30 | Minimum: 0 <br /> |


#### ExposedServiceSpec



ExposedServiceSpec describes a dedicated single-port Service for REST or the thin client.



_Appears in:_
- [GridGainClusterSpec](#gridgainclusterspec)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `type` _[ServiceType](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#servicetype-v1-core)_ | Type is ClusterIP, NodePort, or LoadBalancer. |  | Enum: [ClusterIP NodePort LoadBalancer] <br /> |
| `sessionAffinity` _[ServiceAffinity](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#serviceaffinity-v1-core)_ | SessionAffinity for the Service. |  | Enum: [None ClientIP] <br /> |
| `annotations` _object (keys:string, values:string)_ | Annotations set on the Service. Clearing this map removes previously applied keys. |  |  |
| `labels` _object (keys:string, values:string)_ | Labels merged onto the Service. Operator identity/selector labels cannot be overridden. |  |  |
| `loadBalancerIP` _string_ | LoadBalancerIP when Type=LoadBalancer (cloud-specific). |  |  |
| `loadBalancerSourceRanges` _string array_ | LoadBalancerSourceRanges restricts ingress when Type=LoadBalancer. |  |  |
| `externalTrafficPolicy` _string_ | ExternalTrafficPolicy when Type is NodePort or LoadBalancer (Cluster or Local). |  | Enum: [Cluster Local] <br /> |
| `clusterIP` _string_ | ClusterIP requests a fixed cluster IP when Type=ClusterIP. |  |  |
| `nodePort` _integer_ | NodePort pins the Service nodePort when Type is NodePort or LoadBalancer. |  | Maximum: 65535 <br />Minimum: 1 <br /> |


#### GridGainCluster



GridGainCluster is the Schema for the gridgainclusters API.





| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `apiVersion` _string_ | `gridgain.gridgain.com/v1` | | |
| `kind` _string_ | `GridGainCluster` | | |
| `metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`. |  |  |
| `spec` _[GridGainClusterSpec](#gridgainclusterspec)_ |  |  |  |


#### GridGainClusterSpec



GridGainClusterSpec defines the desired state of a GridGain 8 cluster (Helm values → CRD).

TLS: only require keystoreSecret when tls.enabled is explicitly true (CEL treats omitted/false as off).



_Appears in:_
- [GridGainCluster](#gridgaincluster)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `replicas` _integer_ | Replicas is the number of GridGain server nodes (Helm: replicaCount).<br />Zero is allowed for scale-to-zero (e.g. SkySQL park/stop). | 1 | Minimum: 0 <br /> |
| `image` _[ImageSpec](#imagespec)_ | Image selects the GridGain container image. |  |  |
| `resources` _[ResourceRequirements](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#resourcerequirements-v1-core)_ | Resources for the GridGain container (Helm: resources). |  |  |
| `persistentVolumes` _[PersistentDataVolume](#persistentdatavolume) array_ | PersistentVolumes declare PVC templates and mounts (Helm: persistence.volumes).<br />When empty or omitted, no PVC templates or persistence mounts are created for the StatefulSet. |  |  |
| `volumePermissions` _[VolumePermissionsSpec](#volumepermissionsspec)_ | VolumePermissions configures optional chown init containers (Helm: persistence.volumePermissions). |  |  |
| `persistentVolumeClaimRetentionPolicy` _[StatefulSetPersistentVolumeClaimRetentionPolicy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#statefulsetpersistentvolumeclaimretentionpolicy-v1-apps)_ | PersistentVolumeClaimRetentionPolicy maps to StatefulSet retention (Helm: persistence.persistentVolumeClaimRetentionPolicy). |  |  |
| `jvmOptions` _string_ | JVMOptions is appended to JVM_OPTS (Helm: jvmOpts; newlines normalized by the controller). |  |  |
| `optionLibs` _string_ | OptionLibs lists GridGain optional modules (Helm: optionLibs). |  |  |
| `igniteWorkDir` _string_ | IgniteWorkDir is IGNITE_WORK_DIR (Helm: igniteWorkDir).<br />When unset with persistentVolumes, the operator sets /persistence. When unset with no persistentVolumes, the env var is omitted; default JVM flags omit any $(IGNITE_WORK_DIR)-based options. |  |  |
| `controlCenterUrl` _string_ | ControlCenterURL sets -Dcontrol.center.agent.uris (Helm: controlCenterUrl). |  |  |
| `metricsEnabled` _boolean_ | MetricsEnabled toggles Prometheus-oriented config in generated default-config (Helm: metrics.enabled). |  |  |
| `persistenceEnabled` _boolean_ | PersistenceEnabled sets persistenceEnabled on the default data region in generated default-config.xml.<br />When true, at least one enabled persistentVolumes entry is required (validating webhook).<br />Native persistence is not fully supported yet; default remains in-memory (false). |  |  |
| `defaultCacheConfiguration` _[DefaultCacheConfigurationSpec](#defaultcacheconfigurationspec)_ | DefaultCacheConfiguration configures shared cache defaults applied to the wildcard (*)<br />template and every named cache in generated default-config.xml. |  |  |
| `caches` _string array_ | Caches lists Ignite cache names to declare in generated default-config.xml.<br />Each name gets a CacheConfiguration bean with the same defaults as the wildcard (*) template<br />(PARTITIONED, backups=0, statisticsEnabled, and optional expiry from defaultCacheConfiguration).<br />Changing this list updates the content-addressed config and triggers a managed rolling upgrade.<br />Removing a name stops declaring it in XML; existing caches in the cluster are not destroyed. |  |  |
| `heapRamPercentage` _integer_ | HeapRAMPercentage is the share of spec.resources.limits.memory allocated to JVM heap (-Xms/-Xmx)<br />when spec.jvmOptions is empty. Also drives DataRegion maxSize budgeting. | 20 | Maximum: 90 <br />Minimum: 1 <br /> |
| `logging` _[LoggingSpec](#loggingspec)_ | Logging configures Log4j2 (Helm: chart files/configmaps/ignite-log4j2.xml or custom). |  |  |
| `auth` _[ClusterAuth](#clusterauth)_ | Auth configures passcode authentication (Helm: auth). |  |  |
| `tls` _[TLSSpec](#tlsspec)_ | TLS configures keystore/truststore wiring (operator extension; not in stock Helm templates). |  |  |
| `license` _[LicenseSpec](#licensespec)_ | License configures EE/UE license mounting (Helm: license). |  |  |
| `clientService` _[ClientServiceSpec](#clientservicespec)_ | ClientService describes the combined non-headless Service for REST and thin clients<br />(Helm: services.default). The controller always creates it as <cluster>-default<br />and a headless Service for discovery; this field only shapes the combined Service. |  |  |
| `restService` _[ExposedServiceSpec](#exposedservicespec)_ | RestService optionally creates a dedicated Service for REST (port 8080) named<br /><cluster>-rest. When omitted, REST is only available on the combined client Service. |  |  |
| `thinClientService` _[ExposedServiceSpec](#exposedservicespec)_ | ThinClientService optionally creates a dedicated Service for the thin client (port 10800)<br />named <cluster>-thin. When omitted, the thin client is only available on the combined<br />client Service. |  |  |
| `podAnnotations` _object (keys:string, values:string)_ | PodAnnotations merged onto the StatefulSet pod template (e.g. prometheus.io/scrape for MOE metrics). |  |  |
| `affinity` _[Affinity](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#affinity-v1-core)_ | Affinity for GridGain pods (Helm: affinity). |  |  |
| `nodeSelector` _object (keys:string, values:string)_ | NodeSelector for GridGain pods (Helm: nodeSelector). |  |  |
| `tolerations` _[Toleration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#toleration-v1-core) array_ | Tolerations for GridGain pods (Helm: tolerations). |  |  |
| `topologySpreadConstraints` _[TopologySpreadConstraint](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#topologyspreadconstraint-v1-core) array_ | TopologySpreadConstraints spread pods across domains (Helm: topologySpreadConstraints). |  |  |
| `priorityClassName` _string_ | PriorityClassName for pods (Helm: priorityClassName). |  |  |
| `podManagementPolicy` _[PodManagementPolicyType](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#podmanagementpolicytype-v1-apps)_ | PodManagementPolicy for the StatefulSet (Helm: podManagementPolicy). |  |  |
| `updateStrategy` _[StatefulSetUpdateStrategy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#statefulsetupdatestrategy-v1-apps)_ | UpdateStrategy for the StatefulSet (Helm: updateStrategy). |  |  |
| `revisionHistoryLimit` _integer_ | RevisionHistoryLimit for the StatefulSet (Helm: revisionHistoryLimit). |  |  |
| `terminationGracePeriodSeconds` _integer_ | TerminationGracePeriodSeconds for pods (Helm: terminationGracePeriodSeconds).<br />When omitted the operator default is 600. That budget covers preStop<br />(one readiness period + 30s thin-client delay) and WAL flush; the operator<br />waits for supply to finish before deleting the pod. See docs/lifecycle.md. |  |  |
| `livenessProbe` _[Probe](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#probe-v1-core)_ | LivenessProbe overrides the default HTTP GET `/ignite?cmd=probe&kind=liveness` on :8080.<br />Omit to use operator defaults (GridGain 8.9.37+). A set value replaces the whole probe. |  |  |
| `readinessProbe` _[Probe](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#probe-v1-core)_ | ReadinessProbe overrides the default HTTP GET `/ignite?cmd=probe&kind=readiness` on :8080.<br />Omit to use operator defaults (GridGain 8.9.37+). A set value replaces the whole probe. |  |  |
| `startupProbe` _[Probe](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#probe-v1-core)_ | StartupProbe overrides the default HTTP GET `/ignite?cmd=probe&kind=liveness` on :8080.<br />Omit to use operator defaults (always applied; GridGain 8.9.37+). A set value replaces the whole probe. |  |  |
| `enableDefaultStartupProbe` _boolean_ | EnableDefaultStartupProbe is deprecated and ignored. Startup probes are always applied<br />when spec.startupProbe is unset, matching liveness and readiness. |  |  |
| `containerPorts` _[ContainerPort](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#containerport-v1-core) array_ | ContainerPorts for the GridGain container (Helm: containerPorts). |  |  |
| `extraEnvVars` _[EnvVar](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#envvar-v1-core) array_ | ExtraEnvVars are appended to the container env (Helm: extraEnvVars). |  |  |
| `extraEnvFromConfigMapRef` _[LocalObjectReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#localobjectreference-v1-core)_ | ExtraEnvFromConfigMapRef references a ConfigMap for additional env (Helm: extraEnvVarsCM). |  |  |
| `extraEnvFromSecretRef` _[LocalObjectReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#localobjectreference-v1-core)_ | ExtraEnvFromSecretRef references a Secret for additional env (Helm: extraEnvVarsSecret). |  |  |
| `podSecurityContext` _[PodSecurityContext](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#podsecuritycontext-v1-core)_ | PodSecurityContext (Helm: podSecurityContext). |  |  |
| `containerSecurityContext` _[SecurityContext](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#securitycontext-v1-core)_ | ContainerSecurityContext (Helm: containerSecurityContext). |  |  |
| `serviceAccount` _[ServiceAccountSpec](#serviceaccountspec)_ | ServiceAccount controls chart-equivalent SA creation and naming (Helm: serviceAccount). |  |  |
| `initContainers` _[Container](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#container-v1-core) array_ | InitContainers are merged after optional volume-permissions inits (Helm: initContainers). |  |  |
| `extraVolumeMounts` _[VolumeMount](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#volumemount-v1-core) array_ | ExtraVolumeMounts for the GridGain container (Helm: extraVolumeMounts). |  |  |
| `extraVolumes` _[Volume](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#volume-v1-core) array_ | ExtraVolumes for the pod (Helm: extraVolumes). |  |  |
| `allowUnsafeCustomConfig` _boolean_ | AllowUnsafeCustomConfig acknowledges spec.mainConfigFrom. Default false: the<br />webhook rejects mainConfigFrom until this is true. When true, the operator<br />mounts the customer XML as-is (no parse, no merge). Join failures,<br />drain/shutdownPolicy mismatches, JVM/data-region conflicts, and in-memory<br />data loss are the customer's responsibility. spec.auth.enabled and<br />spec.tls.enabled cannot be true together with mainConfigFrom. |  |  |
| `mainConfigFrom` _[VolumeSourceConfigMap](#volumesourceconfigmap)_ | MainConfigFrom references an existing ConfigMap to mount as primary Ignite XML (Helm: existingConfigmap).<br />Requires spec.allowUnsafeCustomConfig=true. The operator does not inspect or merge the file.<br />Point CONFIG_URI (spec.extraEnvVars) at the mounted file: spec.mainConfigFrom.path plus the<br />ConfigMap data key. Clusters using this field must set IgniteConfiguration.shutdownPolicy<br />to GRACEFUL themselves. spec.auth.enabled and spec.tls.enabled are refused: the XML owns<br />authentication and TLS. License Secret, log4j2 volume, JVM heap flags, probes and drain<br />still apply to the pod; beans that live only in generated default-config.xml do not. |  |  |
| `customConfigMaps` _[ConfigMapMount](#configmapmount) array_ | CustomConfigMaps are operator-managed ConfigMap mounts (Helm: configMaps inline map). |  |  |
| `podDisruptionBudget` _[PDBSpec](#pdbspec)_ | PodDisruptionBudget limits voluntary disruption (operator addition). |  |  |
| `networkPolicy` _[ClusterNetworkPolicySpec](#clusternetworkpolicyspec)_ | NetworkPolicy restricts traffic to GridGain pods when enabled (Helm: networkPolicy). |  |  |
| `upgrade` _[UpgradeSpec](#upgradespec)_ | Upgrade configures operator-managed partitioned rolling upgrades (default: enabled). |  |  |
| `drain` _[DrainSpec](#drainspec)_ | Drain configures the GridGain drain gate the operator runs before it deletes a<br />pod, and the preStop hook that backs it. Its own block rather than a part of<br />spec.upgrade: the same gate runs for scale-down and recovery, which are not<br />upgrades, and preStop runs on every deletion path. |  |  |


#### ImageSpec



ImageSpec selects the GridGain container image (Helm: image.*).



_Appears in:_
- [GridGainClusterSpec](#gridgainclusterspec)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `registry` _string_ | Registry is the image registry (e.g. docker.io). |  |  |
| `repository` _string_ | Repository is the image repository path (e.g. gridgain/community). |  |  |
| `tag` _string_ | Tag is the image tag. If empty, the operator applies a default tied to the supported GridGain 8 line.<br />Operator default probes require GridGain 8.9.37 or newer. |  |  |
| `pullPolicy` _[PullPolicy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#pullpolicy-v1-core)_ | PullPolicy is the image pull policy. |  |  |
| `pullSecrets` _[LocalObjectReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#localobjectreference-v1-core) array_ | PullSecrets are references to registry pull secrets. |  |  |


#### LicenseSpec



LicenseSpec configures GridGain license mounting (Helm: license.*).
Set either inlineXml or fromSecret+secretKey, not both (enforced by validating webhook).



_Appears in:_
- [GridGainClusterSpec](#gridgainclusterspec)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `mountPath` _string_ | MountPath is the directory inside the container where the license Secret is mounted<br />(no subPath; default /opt/gridgain/license). The license file appears at<br /><mountPath>/<secretKey> (or <mountPath>/gridgain-license.xml for inline licenses).<br />Legacy file-style values ending in .xml/.lic are remapped to the default directory. |  |  |
| `inlineXml` _string_ | InlineXML is raw license XML stored in an operator-managed Secret (`<cluster>-license`, key gridgain-license.xml). |  |  |
| `fromSecret` _[LocalObjectReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#localobjectreference-v1-core)_ | FromSecret references an existing Secret; use with secretKey (Helm: license.useExisting). |  |  |
| `secretKey` _string_ | SecretKey is the key within FromSecret (Helm: useExisting.secretkey). |  |  |


#### LoggingSpec



LoggingSpec configures GridGain logging (Helm: ignite-log4j2 / custom mounts).
The embedded default uses Log4j2 JsonLayout. Jackson for that layout comes from
ignite-rest-http, which is in the operator's default optionLibs. If spec.optionLibs
omits ignite-rest-http while the embedded default is in use, the node starts without
a working log layout.



_Appears in:_
- [GridGainClusterSpec](#gridgainclusterspec)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `log4j2Xml` _string_ | Log4j2XML is raw Log4j2 XML embedded in a ConfigMap the operator manages.<br />Prefer a small config; for large files use ConfigMapRef instead. |  |  |
| `configMapRef` _[LocalObjectReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#localobjectreference-v1-core)_ | ConfigMapRef references an existing ConfigMap whose key holds log4j2.xml. |  |  |
| `configMapKey` _string_ | ConfigMapKey is the key within ConfigMapRef (default: ignite-log4j2.xml). |  |  |
| `disableEmbeddedLog4j2` _boolean_ | DisableEmbeddedLog4j2 skips mounting chart-default ignite-log4j2.xml when no Log4j2XML or ConfigMapRef is set.<br />Use only if the image supplies logging or you mount log4j2 via customConfigMaps. |  |  |


#### PDBSpec



PDBSpec configures PodDisruptionBudget (not in Helm chart; operator adds HA).



_Appears in:_
- [GridGainClusterSpec](#gridgainclusterspec)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `enabled` _boolean_ | Enabled creates a PDB targeting the StatefulSet pods. |  |  |
| `minAvailable` _[IntOrString](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#intorstring-intstr-util)_ | MinAvailable is a count or percentage (e.g. "50%") — mutually exclusive with MaxUnavailable in the controller. |  | XIntOrString: \{\} <br /> |
| `maxUnavailable` _[IntOrString](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#intorstring-intstr-util)_ | MaxUnavailable is a count or percentage — mutually exclusive with MinAvailable in the controller. |  | XIntOrString: \{\} <br /> |


#### PasscodeUser



PasscodeUser is one user entry for passcode authentication (Helm: auth.users.*).



_Appears in:_
- [ClusterAuth](#clusterauth)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `credentialId` _string_ | CredentialID is the Spring bean id suffix (e.g. server -> server.cred in chart examples). |  | MinLength: 1 <br /> |
| `username` _string_ | Username is the GridGain username. |  | MinLength: 1 <br /> |
| `passwordSecret` _[SecretKeySelector](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#secretkeyselector-v1-core)_ | PasswordSecret selects the Secret key containing the password. |  |  |
| `permissions` _string_ | Permissions is the permission expression string as in Helm (e.g. "\{defaultAllow:true\}").<br />Required for each auth.users entry (ACL map in default-config). Webhook also rejects whitespace-only values. |  | MinLength: 1 <br /> |


#### PersistentDataVolume



PersistentDataVolume describes one persisted volume for StatefulSet pods (Helm: persistence.volumes.*).



_Appears in:_
- [GridGainClusterSpec](#gridgainclusterspec)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `name` _string_ | Name is the volume name (PVC template name for new claims). |  | MinLength: 1 <br /> |
| `enabled` _boolean_ | Enabled, when false, omits this volume entirely. |  |  |
| `mountPath` _string_ | MountPath is where the volume is mounted in the GridGain container. |  | MinLength: 1 <br /> |
| `subPath` _string_ | SubPath within the volume to mount (optional). |  |  |
| `existingClaim` _string_ | ExistingClaim references a PVC by name shared or pre-provisioned per your policy.<br />If set, no per-pod PVC template is created for this volume. |  |  |
| `storageClassName` _string_ | StorageClassName for the volume claim template (optional). |  |  |
| `accessModes` _[PersistentVolumeAccessMode](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#persistentvolumeaccessmode-v1-core) array_ | AccessModes for the volume claim template. |  |  |
| `size` _[Quantity](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#quantity-resource-api)_ | Size is the requested storage size for new PVCs (e.g. 8Gi). |  |  |
| `selector` _[LabelSelector](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#labelselector-v1-meta)_ | Selector for binding to existing PVs (claim template). |  |  |
| `annotations` _object (keys:string, values:string)_ | Annotations added to generated PVCs. |  |  |
| `labels` _object (keys:string, values:string)_ | Labels added to generated PVCs. |  |  |


#### ServiceAccountSpec



ServiceAccountSpec mirrors Helm serviceAccount.* (chart default: create=true).



_Appears in:_
- [GridGainClusterSpec](#gridgainclusterspec)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `create` _boolean_ | Create requests a dedicated ServiceAccount managed by the operator (Helm: serviceAccount.create).<br />When omitted, behavior matches Helm default true. |  |  |
| `name` _string_ | Name overrides the generated account name when non-empty. |  |  |
| `automountServiceAccountToken` _boolean_ | AutomountServiceAccountToken maps to pod.spec.automountServiceAccountToken. |  |  |
| `annotations` _object (keys:string, values:string)_ | Annotations on the ServiceAccount. |  |  |


#### ServiceExposureSpec



ServiceExposureSpec is the shared shape of a client-facing Service
(type, metadata, and LoadBalancer/NodePort settings).



_Appears in:_
- [ClientServiceSpec](#clientservicespec)
- [ExposedServiceSpec](#exposedservicespec)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `type` _[ServiceType](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#servicetype-v1-core)_ | Type is ClusterIP, NodePort, or LoadBalancer. |  | Enum: [ClusterIP NodePort LoadBalancer] <br /> |
| `sessionAffinity` _[ServiceAffinity](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#serviceaffinity-v1-core)_ | SessionAffinity for the Service. |  | Enum: [None ClientIP] <br /> |
| `annotations` _object (keys:string, values:string)_ | Annotations set on the Service. Clearing this map removes previously applied keys. |  |  |
| `labels` _object (keys:string, values:string)_ | Labels merged onto the Service. Operator identity/selector labels cannot be overridden. |  |  |
| `loadBalancerIP` _string_ | LoadBalancerIP when Type=LoadBalancer (cloud-specific). |  |  |
| `loadBalancerSourceRanges` _string array_ | LoadBalancerSourceRanges restricts ingress when Type=LoadBalancer. |  |  |
| `externalTrafficPolicy` _string_ | ExternalTrafficPolicy when Type is NodePort or LoadBalancer (Cluster or Local). |  | Enum: [Cluster Local] <br /> |
| `clusterIP` _string_ | ClusterIP requests a fixed cluster IP when Type=ClusterIP. |  |  |


#### TLSSpec



TLSSpec configures TLS for GridGain inter-node and client transports (operator extension beyond chart defaults).



_Appears in:_
- [GridGainClusterSpec](#gridgainclusterspec)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `enabled` _boolean_ | Enabled requests TLS material to be wired into generated configuration. |  |  |
| `keystoreSecret` _[LocalObjectReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#localobjectreference-v1-core)_ | KeystoreSecret references a Secret containing keystore data (keys implementation-specific in controller). |  |  |
| `keystoreKey` _string_ | KeystoreKey is the key within KeystoreSecret (default keystore.jks). |  |  |
| `keystoreType` _string_ | KeystoreType is passed to Ignite SslContextFactory (e.g. JKS, PKCS12); omit to use Ignite default. |  |  |
| `keystorePasswordSecret` _[SecretKeySelector](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#secretkeyselector-v1-core)_ | KeystorePasswordSecret supplies the keystore password via env GRIDGAIN_TLS_KEYSTORE_PASSWORD (Spring SpEL in generated XML). |  |  |
| `truststoreSecret` _[LocalObjectReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#localobjectreference-v1-core)_ | TruststoreSecret references a Secret containing trust material. |  |  |
| `truststoreKey` _string_ | TruststoreKey is the key within TruststoreSecret (default truststore.jks). |  |  |
| `truststoreType` _string_ | TruststoreType is passed to Ignite SslContextFactory when truststore is set. |  |  |
| `truststorePasswordSecret` _[SecretKeySelector](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#secretkeyselector-v1-core)_ | TruststorePasswordSecret supplies the truststore password via env GRIDGAIN_TLS_TRUSTSTORE_PASSWORD. |  |  |






#### UpgradeRecoveryAction

_Underlying type:_ _string_

UpgradeRecoveryAction is a one-shot recovery command after a failed upgrade.

_Validation:_
- Enum: [retry retryUntilReady rollback]

_Appears in:_
- [UpgradeRecoverySpec](#upgraderecoveryspec)

| Field | Description |
| --- | --- |
| `retry` |  |
| `retryUntilReady` |  |
| `rollback` |  |


#### UpgradeRecoverySpec



UpgradeRecoverySpec acknowledges a recovery action with a deterministic token from status.



_Appears in:_
- [UpgradeSpec](#upgradespec)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `action` _[UpgradeRecoveryAction](#upgraderecoveryaction)_ | Action selects retry, retryUntilReady, or rollback. |  | Enum: [retry retryUntilReady rollback] <br /> |
| `token` _string_ | Token must match status.upgrade.recoveryToken. |  |  |


#### UpgradeSpec



UpgradeSpec configures operator-managed rolling upgrades.



_Appears in:_
- [GridGainClusterSpec](#gridgainclusterspec)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `enabled` _boolean_ | Enabled requests operator-managed partitioned rollout. Default true when omitted. | true |  |
| `nodeTimeoutSeconds` _integer_ | NodeTimeoutSeconds is the per-node readiness timeout during Rolling. Default 600. | 600 | Minimum: 1 <br /> |
| `allowSingleReplicaRoll` _boolean_ | AllowSingleReplicaRoll permits destructive rolls when replicas is 1. Default false. |  |  |
| `retryBackoffCapSeconds` _integer_ | RetryBackoffCapSeconds caps exponential backoff during retryUntilReady. Default 300. | 300 | Minimum: 1 <br /> |
| `maxRetries` _integer_ | MaxRetries limits retryUntilReady attempts; 0 means unlimited. Default 0. |  |  |
| `recovery` _[UpgradeRecoverySpec](#upgraderecoveryspec)_ | Recovery is a one-shot action when status.upgrade.phase is Failed.<br />The operator never clears this field (GitOps-safe); it is inert outside Failed,<br />and the per-failure token prevents a stale block from acknowledging a later failure. |  |  |


#### VolumePermissionsSpec



VolumePermissionsSpec matches Helm's persistence.volumePermissions init container.



_Appears in:_
- [GridGainClusterSpec](#gridgainclusterspec)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `enabled` _boolean_ | Enabled runs an init container to chown persistence paths. |  |  |
| `image` _string_ | Image for the init container (default set in controller). |  |  |
| `resources` _[ResourceRequirements](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#resourcerequirements-v1-core)_ | Resources for the init container. |  |  |
| `securityContext` _[SecurityContext](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.35/#securitycontext-v1-core)_ | SecurityContext for the init container. |  |  |


#### VolumeSourceConfigMap



VolumeSourceConfigMap references a ConfigMap and mount path (Helm: existingConfigmap).



_Appears in:_
- [GridGainClusterSpec](#gridgainclusterspec)

| Field | Description | Default | Validation |
| --- | --- | --- | --- |
| `name` _string_ |  |  |  |
| `path` _string_ |  |  |  |


