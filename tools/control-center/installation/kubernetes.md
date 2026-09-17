---
description: >-
  Deploying GridGain Control Center in Kubernetes, covering the backend and
  frontend containers, services, ConfigMap, and health probes.
---

# Control Center in Kubernetes

## Create a Kubernetes Project

A Kubernetes project is a Kubernetes namespace with additional configuration properties and enables a community of users to isolate the GridGain Control Center from other applications and users. Additional information on Kubernetes projects can be found [here](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/).

1. Create a new Kubernetes project:

   ```bash
   kubectl create namespace gridgain-control-center
   kubectl config set-context --current --namespace=gridgain-control-center
   ```
2. Once the project is created, you can perform regular project operations such as `kubectl get namespace` to view the full list of projects and `oc status` to view the status of the newly created `gridgain-control-center` project.

{% hint style="info" %}
If you deploy your GridGain cluster in Docker, remember to include the `control-center-agent` optional library to allow it to connect to Control Center. To do this, set the environment variable "OPTION_LIBS=control-center-agent". For more information, see the https://www.gridgain.com/docs/latest/installation-guide/installing-using-docker#enabling-modules
{% endhint %}

## Create the Control Center Backend Container

Create the Control Center backend container. Remember to specify the correct image tag for your version of GridGain Control Center.

### Create the Configuration File

Create the backend container configuration file `control-center-backend-sts.yaml`. See an example below.

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: backend
  namespace: gridgain-control-center
spec:
  replicas: 1
  serviceName: backend
  selector:
    matchLabels:
      app: backend
  template:
    metadata:
      labels:
        app: backend
    spec:
      containers:
        name: backend-container
        image: gridgain/control-center-backend:2024.3
        imagePullPolicy: IfNotPresent
        resources:
          requests:
            ephemeral-storage: "2Gi"
          limits:
            ephemeral-storage: "4Gi"
          ports:
            containerPort: 3000
            protocol: TCP
            name: cc-web
          env:
            name: JVM_OPTS
            value: "-server -Xms1g -Xmx2g -XX:+AlwaysPreTouch -XX:+UseG1GC -XX:+ScavengeBeforeFullGC"
          volumeMounts:
            mountPath: /opt/gridgain-control-center/work
            name: control-center-storage
  volumeClaimTemplates:
    metadata:
      name: control-center-storage
      spec:
        accessModes: [ "ReadWriteOnce" ]
        resources:
          requests:
            storage: 10Gi
```

### Define initContainers in the Configuration File (Optional)

When the persistentVolume is created, its owner is `root`. The default user inside the GridGain container is different, which may cause a permission issue when the container tries to write to the above persistentVolume. To prevent this from happening, you can define initContainers in your configuration file. See an example below.

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: backend
  namespace: gridgain-control-center
spec:
  replicas: 1
  serviceName: backend
  selector:
    matchLabels:
      app: backend
  template:
    metadata:
      labels:
        app: backend
    spec:
      securityContext:
        runAsUser: 10001
        runAsGroup: 10001
        fsGroup: 10001
      initContainers:
        - name: init
          image: alpine
          command: ["sh", "-c", "chown -R 10001:10001 /opt/gridgain-control-center/work"]
          volumeMounts:
            - mountPath: /opt/gridgain-control-center/work
              name: control-center-storage
          securityContext:
            runAsUser: 0
            runAsGroup: 0
      containers:
        - name: backend-container
          image: gridgain/control-center-backend:2023.3.1
          imagePullPolicy: IfNotPresent
          env:
            - name: JVM_OPTS
              value: ""
          volumeMounts:
            - mountPath: /opt/gridgain-control-center/work
              name: control-center-storage
  volumeClaimTemplates:
    - metadata:
        name: control-center-storage
      spec:
        accessModes: [ "ReadWriteOnce" ]
        resources:
          requests:
            storage: 10Gi
```

### Create the Container

Once your configuration file has been created, run the following command to create the container:

```bash
kubectl apply -f control-center-backend-sts.yaml
```

## Create Control Center Backend Service

Create a Kubernetes service to route network traffic to the Control Center backend. The service will act as a LoadBalancer for the Control Center backend.

Create the backend service configuration file `control-center-backend-service.yaml`:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: backend
  namespace: gridgain-control-center
spec:
  type: LoadBalancer
  selector:
    app: backend
  ports:
   - name: control-center-web
     port: 3000
     protocol: TCP
     targetPort: 3000
```

Optionally, to introduce a custom `ignite-config.xml` file:

1. Add the following to the config map:

   ```yaml
   apiVersion: v1
   kind: ConfigMap
   metadata:
     name: control-center-backend-configmap
     labels:
   data:
     ignite-config.xml: |
   <content_of_ignite-config.xml>
   ```
2. Add the ConfigMap name in the `volumes` section of the StatefulSet:

   ```yaml
   volumes:
     - configMap:
          name: control-center-backend-configmap
       name: ignite-config
   ```
3. Mount the config map to a specific path:

   ```yaml
   volumeMounts:
     - mountPath: /opt/gridgain-control-center/config/ignite-config.xml
       name: ignite-config
       subPath: ignite-config.xml
   ```

{% hint style="info" %}
For details on mounting files via a config map, see the official [Kubernetes documentation](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/#populate-a-volume-with-data-stored-in-a-configmap).
{% endhint %}

Run the following command to create the service:

```bash
kubectl apply -f control-center-backend-service.yaml
```

## Create a ConfigMap for Control Center Frontend

A ConfigMap is a key-value store that lives as a Kubernetes object. ConfigMaps allow you to modify application behavior without having to recreate the Docker image.

Before creating the Control Center frontend container, you must first create the ConfigMap.

1. Create the ConfigMap configuration file `control-center-frontend-configmap.yaml`:

   ```yaml
   apiVersion: v1
   kind: ConfigMap
   metadata:
     name: control-center-config
     namespace: gridgain-control-center
   data:
      control-center.conf: |-
       upstream backend {
         server backend:3000;
       }

       server {
         listen 8008;
         server_name _;

         set $ignite_console_dir /data/www;

         root $ignite_console_dir;

         error_page 500 502 503 504 /50x.html;

         location / {
           try_files $uri /index.html = 404;
         }

         location /api/v1 {
           proxy_pass http://backend;
           proxy_set_header X-Forwarded-Proto $scheme;
           proxy_set_header X-Forwarded-Host $http_host;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_pass_header X-XSRF-TOKEN;
         }

         location /agents {
           proxy_pass http://backend;
           proxy_http_version 1.1;
           proxy_set_header Upgrade $http_upgrade;
           proxy_set_header Connection "upgrade";
           proxy_set_header Origin http://backend;
         }

         location /browsers {
           proxy_pass http://backend;
           proxy_http_version 1.1;
           proxy_set_header Upgrade $http_upgrade;
           proxy_set_header Connection "upgrade";
           proxy_set_header Origin http://backend;
           proxy_pass_header X-XSRF-TOKEN;
         }

         location = /50x.html {
           root $ignite_console_dir/error_page;
         }
       }
   ```
2. Apply the Control Center backend configmap to the `gridgain-control-center` project using the following command:

   ```bash
   kubectl apply -f control-center-frontend-configmap.yaml
   ```

## Create the Control Center Frontend Container

After the ConfigMap has been applied to the project, create the Control Center frontend container. Remember to specify the correct image tag for your version of GridGain Control Center.

1. Create the container configuration file `control-center-frontend-deployment.yaml`:

   ```yaml
   # An example of a Kubernetes configuration for Control Center deployment.
   apiVersion: v1
   kind: Deployment
   metadata:
    name: control-center-frontend
    namespace: gridgain-control-center
    labels:
      app: frontend
   spec:
    containers:
    - name: frontend-container
      image: gridgain/control-center-frontend:2023.1
      imagePullPolicy: IfNotPresent
      ports:
      - containerPort: 8008
        protocol: TCP
      volumeMounts:
      - mountPath: /etc/nginx/control-center.conf
        name: control-center-config
        subPath: control-center.conf
    volumes:
      - name: control-center-config
        configMap:
          name: control-center-config
          items:
          - key: control-center.conf
            path: control-center.conf
   ```
2. Run the following command to create the container:

   ```bash
   kubectl apply -f control-center-frontend-deployment.yaml
   ```

## Create Control Center Frontend Service

Create a Kubernetes service to route network traffic to the Control Center frontend service.

1. Create the service configuration file `control-center-frontend-service.yaml`:

   ```yaml
   apiVersion: v1
   kind: Service
   metadata:
     name: frontend
     namespace: gridgain-control-center
   spec:
     type: LoadBalancer
     selector:
       app: frontend
     ports:
      - name: control-center-web
        port: 8008
        protocol: TCP
        targetPort: 8008
   ```
2. Run the following command to create the service which will act as a LoadBalancer for the Control Center frontend service:

   ```bash
   kubectl apply -f control-center-frontend-service.yaml
   ```

## Configure Readiness and Liveness Probes

When running Control Center on Kubernetes, configure readiness and liveness probes for both the backend and frontend containers.

### Backend Probes

The Control Center backend supports service health checks through the following endpoints:

- Readiness: `/actuator/health/readiness`
- Liveness: `/actuator/health/liveness`

Add the probes to the backend container spec:

```yaml
spec:
  template:
    spec:
      containers:
        - name: backend
          livenessProbe:
            httpGet:
              path: /actuator/health/ping
              port: probe-port
              scheme: HTTP
            periodSeconds: 60
            timeoutSeconds: 10
            failureThreshold: 5
            successThreshold: 1
          readinessProbe:
            httpGet:
              path: /actuator/health/readiness
              port: probe-port
              scheme: HTTP
            periodSeconds: 30
            timeoutSeconds: 10
            failureThreshold: 6
            successThreshold: 1
```

### Frontend Probes

For the frontend, a basic HTTP probe against / is typically sufficient:

```yaml
spec:
  template:
    spec:
      containers:
        - name: frontend
          livenessProbe:
            httpGet:
              path: /nginx_status
              port: 8080
              scheme: HTTP
            periodSeconds: 10
            timeoutSeconds: 1
            failureThreshold: 3
            successThreshold: 1
          readinessProbe:
            httpGet:
              path: /nginx_status
              port: 8080
              scheme: HTTP
            periodSeconds: 10
            timeoutSeconds: 1
            failureThreshold: 3
            successThreshold: 1
```

For more details on configuring probes, see the official Kubernetes [documentation](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#configure-probes).

## Set JVM Options

You can additionally set JVM options to improve Control Center performance in high-throughput environments. The example below uses the same configuration as above, but also sets some JVM options:

```yaml
# An example of a Kubernetes configuration for Control Center deployment.
apiVersion: v1
kind: Deployment
metadata:
 name: control-center-frontend
 namespace: gridgain-control-center
 labels:
   app: frontend
spec:
 containers:
 - name: frontend-container
   image: gridgain/control-center-frontend:2023.1
   imagePullPolicy: IfNotPresent
   env:
   - name: JVM_OPTS
     value: "-server -XX:+AggressiveOpts -XX:MaxPermSize=256m"
   ports:
   - containerPort: 8008
     protocol: TCP
   volumeMounts:
   - mountPath: /etc/nginx/control-center.conf
     name: control-center-config
     subPath: control-center.conf
 volumes:
   - name: control-center-config
     configMap:
       name: control-center-config
       items:
       - key: control-center.conf
         path: control-center.conf
```

## Expose the Control Center Frontend Service and Get Routes to the Application

1. Get the deployed Control Center frontend LoadBalancer service IP using the following command:

   ```bash
   $ kubectl get svc frontend
   ```
2. Finally, access the Control Center frontend UI using one of the returned external IPs.

## Create the First Admin Account

If this is your first time launching Control Center, you can create an initial Admin account by using details in the Control Center output. Using the example configurations in this document, the default port of the frontend container will be 8008. The Admin creation URL will look like the following:

```bash
http://<IP of frontend service>:8008/auth/signup?adminToken=<TOKEN ID as listed in log files>
```

## Connect a Cluster

When configuring the cluster to connect to Control Center, remember to use the URL to the frontend service with the correct port. In the above examples, the port is 8008. For example:

```bash
management.sh -uri http://<frontend.gridgain-control-center>:8008/
```

## Next Steps

- [Change Configuration Parameters](../admin-guide/configuration.md) - make sure you [optimize the disk space utilization](../admin-guide/disk-space-optimization.md)
- [Add a License](../getting-started/adding-license.md)
- Connect a [GridGain](../getting-started/connect/connect-gridgain-cluster.md) or [Apache Ignite](../getting-started/connect/connect-ignite-cluster.md) Cluster
