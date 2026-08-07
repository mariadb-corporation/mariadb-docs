---
description: >-
  Running GridGain Control Center and a GridGain cluster in Kubernetes with TLS
  encryption at every step, from certificate generation to cluster attachment.
---

# Running Control Center and GridGain with Encryption

This topic covers how you can set up GridGain and Control Center with encryption on each step.

## 1. Create Certificate Files

First, generate certificates for all the components: frontend, backend and GridGain nodes. Below is a generation script that creates certificates. Make sure to specify your own data instead of placeholders.

`countryName` value must be a two-letter country code.

{% code title="script.sh" %}
```bash
#!/usr/bin/env bash

set -x

# Certificates password.
PASS=qwerty

# Server.
SERVER_DN="CN=localhost,OU=ID,O=GG,L=Hursley,S=Hants,C=GB"

# ca key config.
cat << EOF > ca_key.conf
[req]
prompt                 = no
distinguished_name     = dn
req_extensions         = req_ext
[ dn ]
countryName            = MyCountry
stateOrProvinceName    = MyState
localityName           = MyLocality
organizationName       = MyCompany
commonName             = localhost
organizationalUnitName = IT
emailAddress           = example@test.local
[ req_ext ]
subjectAltName         = @alt_names
[ alt_names ]
DNS.1                  = localhost
EOF

# ca configuration file
cat << EOF > ca.cnf
[ ca ]
default_ca = CertificateAuthority

[ CertificateAuthority ]
certificate = ./ca.pem
database = ./index.txt
private_key = ./ca.key
new_certs_dir = ./
default_md = sha256
policy = policy_match
serial = ./serial
default_days = 365

[policy_match]
commonName = supplied
EOF

touch index.txt
echo 01 > serial

# Generate CA
openssl req -new -newkey rsa:2048 -nodes -config ca_key.conf -out ca.csr -keyout ca.key
openssl x509 -trustout -signkey ca.key -req -in ca.csr -out ca.pem
keytool -deststorepass ${PASS} -noprompt  -import -file ca.pem -alias CertificateAuthority -keystore trust.jks

# Generate node certificates
keytool -genkey -keyalg RSA -keysize 2048 -alias node -deststorepass ${PASS} -keystore node.jks -noprompt \
 -dname ${SERVER_DN} \
 -storepass ${PASS} \
 -keypass ${PASS}
keytool -deststorepass ${PASS} -certreq -alias node -file node.csr -keystore node.jks
openssl ca -batch -config ca.cnf -out node.pem -infiles node.csr
keytool -deststorepass ${PASS} -import -alias ca -keystore node.jks -file ca.pem -noprompt
keytool -deststorepass ${PASS} -import -alias node -keystore node.jks -file node.pem -noprompt
keytool -importkeystore -srcstoretype JKS -deststoretype PKCS12 -srckeystore node.jks -destkeystore node.p12 -srcstorepass ${PASS} -deststorepass ${PASS} -srcalias node -destalias node -noprompt
openssl pkcs12 -in node.p12 -out ca_odbc.pem -passin pass:${PASS} -nodes

# frontend key config
cat << EOF > frontend.conf
[req]
prompt                 = no
distinguished_name     = dn
req_extensions         = req_ext
[ dn ]
countryName            = MyCountry
stateOrProvinceName    = MyState
localityName           = MyLocality
organizationName       = MyCompany
commonName             = localhost
organizationalUnitName = IT
emailAddress           = example@test.local
[ req_ext ]
subjectAltName         = @alt_names
[ alt_names ]
DNS.1                  = localhost
DNS.2                  = frontend
DNS.3                  = frontend.gridgain-control-center
IP.1                   = 127.0.0.1
EOF

# Generate frontend certificates
openssl genrsa -out frontend.nopass.key 1024
openssl req -new -key frontend.nopass.key -config frontend.conf -out frontend.csr
openssl x509 -req -days 365 -in frontend.csr -CA ca.pem -CAkey ca.key -set_serial 01 -extensions req_ext -extfile frontend.conf -out frontend.crt
openssl pkcs12 -export -in frontend.crt -inkey frontend.nopass.key -passin pass:${PASS} -certfile frontend.crt -out frontend.p12 -passout pass:${PASS}
keytool -importkeystore -srckeystore frontend.p12 -srcstoretype PKCS12 -destkeystore frontend.jks -deststoretype JKS -noprompt -srcstorepass ${PASS} -deststorepass ${PASS}

# backend key config
cat << EOF > backend.conf
[req]
prompt                 = no
distinguished_name     = dn
req_extensions         = req_ext
[ dn ]
countryName            = MyCountry
stateOrProvinceName    = MyState
localityName           = MyLocality
organizationName       = MyCompany
commonName             = localhost
organizationalUnitName = IT
emailAddress           = example@test.local
[ req_ext ]
subjectAltName         = @alt_names
[ alt_names ]
DNS.1                  = localhost
DNS.2                  = backend
DNS.3                  = backend.gridgain-control-center
IP.1                   = 127.0.0.1
EOF

# Generate backend certificates
openssl genrsa -des3 -passout pass:${PASS} -out backend.key 1024
openssl req -new -passin pass:${PASS} -key backend.key -config backend.conf -out backend.csr
openssl x509 -req -days 365 -in backend.csr -CA ca.pem -CAkey ca.key -set_serial 01 -extensions req_ext -extfile backend.conf -out backend.crt
openssl pkcs12 -export -in backend.crt -inkey backend.key -passin pass:${PASS} -certfile backend.crt -out backend.p12 -passout pass:${PASS}
keytool -importkeystore -srckeystore backend.p12 -srcstoretype PKCS12 -destkeystore backend.jks -deststoretype JKS -noprompt -srcstorepass ${PASS} -deststorepass ${PASS}
```
{% endcode %}

As a result of execution, you will get a set of key and certificate files.

## 2. Set up Control Center

Now that you have certificates, configure Control Center to use SSL:

- Create new namespace `gridgain-control-center` in kubernetes.
  - Create Control Center namespace:

    ```bash
    kubectl create namespace gridgain-control-center
    ```
  - Set namespace as current:

    ```bash
    kubectl config set-context --current --namespace=gridgain-control-center
    ```
- Place required certificates in k8s secrets:
  - Create secret for backend:

    ```bash
    kubectl create secret generic certificate-backend --from-file=backend.jks --from-file=trust.jks
    ```
  - Create secret for frontend:

    ```bash
    kubectl create secret generic certificate-frontend --from-file=frontend.nopass.key --from-file=frontend.crt
    ```
- Set up Control Center backend with the following commands:
  - Apply backend configuration: `kubectl apply -f control-center-backend-configmap.yaml`

    {% code title="control-center-backend-configmap.yaml" %}
    ```yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: control-center-backend-config
      namespace: gridgain-control-center
    data:
       application.properties: |-
            server.ssl.enabled=true
            server.ssl.key-store=/opt/gridgain-control-center/tls/backend.jks
            server.ssl.key-store-password=qwerty
            server.ssl.trust-store=/opt/gridgain-control-center/tls/trust.jks
            server.ssl.trust-store-password=qwerty
            server.ssl.key-store-type=jks
            server.ssl.protocol=TLS
            # configure allowed origins according to environment settings
            control.browsers.allowed-origins=https://localhost:8443
            account.globalTeam.enabled=true
            account.globalTeam.attachCluster=true
    ```
    {% endcode %}
  - Create a backend statefulset: `kubectl apply -f control-center-backend-statefulset.yaml`

    {% code title="control-center-backend-statefulset.yaml" %}
    ```yaml
    # An example of a Kubernetes configuration for Control Center pod deployment.
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
          - name: backend-container
            image: gridgain/control-center-backend:2021.12.01
            imagePullPolicy: IfNotPresent
            ports:
            - containerPort: 3000
              protocol: TCP
            volumeMounts:
            - mountPath: /opt/gridgain-control-center/tls
              name: node
              readOnly: true
            - name: config-volume
              mountPath: /opt/gridgain-control-center/application.properties
              subPath: application.properties
            - mountPath: /opt/gridgain-control-center/work
              name: control-center-storage
          volumes:
          - name: config-volume
            configMap:
              name: control-center-backend-config
              items:
              - key: application.properties
                path: application.properties
          - name: node
            secret:
              secretName: certificate-backend
              items:
              - key: backend.jks
                path: backend.jks
              - key: trust.jks
                path: trust.jks
      volumeClaimTemplates:
        - metadata:
            name: control-center-storage
          spec:
            accessModes: [ "ReadWriteOnce" ]
            resources:
              requests:
                storage: 10Gi
    ```
    {% endcode %}
  - Create a backend service: `kubectl apply -f control-center-backend-service.yaml`

    {% code title="control-center-backend-service.yaml" %}
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
       - name: control-center-ssl
         port: 3000
         protocol: TCP
         targetPort: 3000
    ```
    {% endcode %}
- Set up Control Center frontend:
  - Apply the configuration file: `kubectl apply -f control-center-frontend-configmap.yaml`

    {% code title="control-center-frontend-configmap.yaml" %}
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
          listen 8008 default_server;
          server_name _;
          return 301 https://$host$request_uri;
        }

        server {
          listen 8443 ssl;
          server_name _;
          ssl_certificate /etc/nginx/tls/frontend.crt;
          ssl_certificate_key /etc/nginx/tls/frontend.nopass.key;
          # ssl_protocols TLSv1.2;
          ssl_ciphers         HIGH:!aNULL:!MD5;
          ssl_verify_client off;

          set $ignite_console_dir /data/www;

          root $ignite_console_dir;

          error_page 500 502 503 504 /50x.html;

          location / {
            try_files $uri /index.html = 404;
          }

          location /api/v1 {
            proxy_pass https://backend;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_set_header X-Forwarded-Host $http_host;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_pass_header X-XSRF-TOKEN;
          }

          location /agents {
            proxy_pass https://backend;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
            proxy_pass_header X-XSRF-TOKEN;
          }

          location /browsers {
            proxy_pass https://backend;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
            proxy_pass_header X-XSRF-TOKEN;
          }

          location = /50x.html {
            root $ignite_console_dir/error_page;
          }
        }
    ```
    {% endcode %}
  - Apply the deployment configuration: `kubectl apply -f control-center-frontend-deployment.yaml`

    {% code title="control-center-frontend-deployment.yaml" %}
    ```yaml
    # An example of a Kubernetes configuration for Control Center deployment.
    apiVersion: v1
    kind: Pod
    metadata:
     name: control-center-frontend
     namespace: gridgain-control-center
     labels:
       app: frontend
    spec:
     containers:
     - name: frontend-container
       image: gridgain/control-center-frontend:2021.12.01
       imagePullPolicy: IfNotPresent
       ports:
       - containerPort: 8443
         protocol: TCP
       volumeMounts:
       - mountPath: /etc/nginx/control-center.conf
         name: control-center-config
         subPath: control-center.conf
       - mountPath: /etc/nginx/tls
         name: node
         readOnly: true
     volumes:
       - name: control-center-config
         configMap:
           name: control-center-config
           items:
           - key: control-center.conf
             path: control-center.conf
       - name: node
         secret:
           secretName: certificate-frontend
           items:
           - key: frontend.nopass.key
             path: frontend.nopass.key
           - key: frontend.crt
             path: frontend.crt
    ```
    {% endcode %}
  - Create the frontend service: `kubectl apply -f control-center-frontend-service.yaml`

    {% code title="control-center-frontend-service.yaml" %}
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
       - name: control-center-web-ssl
         port: 8443
         protocol: TCP
         targetPort: 8443
    ```
    {% endcode %}

After you complete configuration, check the frontend service with the `kubectl get svc frontend -n gridgain-control-center` command:

```
NAME       TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
frontend   LoadBalancer   10.108.86.236   localhost     8443:30239/TCP   3h7m
```

Now frontend web will be available on `https://{EXTERNAL-IP}:8443` URL.

Get the token for authorization in Control Center from backend logs. You can get them with the `kubectl logs backend-0` command:

```
======================================================================================
  No admin accounts found in Control Center.
  Use the following link to create the first admin:
  https://localhost:3000/auth/signup?adminToken=efe88648-e2ca-4b0d-a50f-a0ed993f7859
======================================================================================
```

## 3. Set up GridGain Cluster

To use SSL on all stages of the connection, you also need a GridGain cluster to run SSL:

- Create the new namespace by using the following commands:
  - `kubectl create namespace gridgain`
  - `kubectl config set-context --current --namespace=gridgain`
- Put required certificates in Kubernetes:
  - `kubectl create secret generic certificate --from-file=node.jks --from-file=trust.jks`
- Deploy the server nodes:
  - Create the gridgain service: `kubectl create -f service.yaml`

    {% code title="service.yaml" %}
    ```yaml
    apiVersion: v1
    kind: Service
    metadata:
      # The name must be equal to TcpDiscoveryKubernetesIpFinder.serviceName
      name: gridgain-service
      # The name must be equal to TcpDiscoveryKubernetesIpFinder.namespace
      namespace: gridgain
      labels:
        app: gridgain
    spec:
      type: LoadBalancer
      ports:
        - name: rest
          port: 8080
          targetPort: 8080
        - name: thinclients
          port: 10800
          targetPort: 10800
      # Optional - remove 'sessionAffinity' property if the cluster
      # and applications are deployed within Kubernetes
      #  sessionAffinity: ClientIP
      selector:
        # Must be equal to the label set for pods.
        app: gridgain
    status:
      loadBalancer: {}
    ```
    {% endcode %}
  - Create a GridGain service account: `kubectl create sa gridgain`
  - Configure cluster role: `kubectl create -f cluster-role.yaml`

    {% code title="cluster-role.yaml" %}
    ```yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: gridgain
      namespace: gridgain
    rules:
    - apiGroups:
      - ""
      resources: # Here are the resources you can access
      - pods
      - endpoints
      verbs: # That is what you can do with them
      - get
      - list
      - watch
    ---
    kind: ClusterRoleBinding
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
      name: gridgain
    roleRef:
      kind: ClusterRole
      name: gridgain
      apiGroup: rbac.authorization.k8s.io
    subjects:
    - kind: ServiceAccount
      name: gridgain
      namespace: gridgain
    ```
    {% endcode %}
  - Configure the node: `kubectl create configmap gridgain-config --from-file=node-configuration.xml`

    {% code title="node-configuration.xml" %}
    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.springframework.org/schema/beans
    http://www.springframework.org/schema/beans/spring-beans.xsd">

        <bean class="org.apache.ignite.configuration.IgniteConfiguration">

            <property name="workDirectory" value="/opt/gridgain/work"/>

            <property name="sslContextFactory">
                <bean class="org.apache.ignite.ssl.SslContextFactory">
                    <property name="keyStoreFilePath" value="/gridgain/tls/node.jks"/>
                    <property name="keyStorePassword" value="qwerty"/>
                    <property name="trustStoreFilePath" value="/gridgain/tls/trust.jks"/>
                    <property name="trustStorePassword" value="qwerty"/>
                </bean>
            </property>

            <property name="dataStorageConfiguration">
                <bean class="org.apache.ignite.configuration.DataStorageConfiguration">
                    <property name="defaultDataRegionConfiguration">
                        <bean class="org.apache.ignite.configuration.DataRegionConfiguration">
                            <property name="persistenceEnabled" value="true"/>
                        </bean>
                    </property>

                    <property name="walPath" value="/opt/gridgain/wal"/>
                    <property name="walArchivePath" value="/opt/gridgain/walarchive"/>
                </bean>

            </property>

            <property name="discoverySpi">
                <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
                    <property name="ipFinder">
                        <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.kubernetes.TcpDiscoveryKubernetesIpFinder">
                            <property name="namespace" value="gridgain"/>
                            <property name="serviceName" value="gridgain-service"/>
                        </bean>
                    </property>
                </bean>
            </property>

        </bean>
    </beans>
    ```
    {% endcode %}
  - Create the stateful set: `kubectl create -f statefulset.yaml`

    {% code title="statefulset.yaml" %}
    ```yaml
    # An example of a Kubernetes configuration for pod deployment.
    apiVersion: apps/v1
    kind: StatefulSet
    metadata:
      # Cluster name.
      name: gridgain-cluster
      namespace: gridgain
    spec:
      # The initial number of pods to be started by Kubernetes.
      replicas: 1
      serviceName: gridgain
      selector:
        matchLabels:
          app: gridgain
      template:
        metadata:
          labels:
            app: gridgain
        spec:
          serviceAccountName: gridgain
          terminationGracePeriodSeconds: 60000
          containers:
            # Custom pod name.
          - name: gridgain-node
            image: gridgain/community:8.8.20
            env:
            - name: OPTION_LIBS
              value: ignite-kubernetes,ignite-rest-http,control-center-agent
            - name: CONFIG_URI
              value: file:///opt/gridgain/config/node-configuration.xml
            - name: JVM_OPTS
              value: "-DIGNITE_WAL_MMAP=false -DIGNITE_WAIT_FOR_BACKUPS_ON_SHUTDOWN=true"
             # if you want to provide the license file via URI, uncomment the following 2 lines
    #        - name: LICENSE_URI
    #          value: http://url_to_license_file
            ports:
            # Ports to open.
            - containerPort: 47100 # communication SPI port
            - containerPort: 47500 # discovery SPI port
            - containerPort: 49112 # JMX port
            - containerPort: 10800 # thin clients/JDBC driver port
            - containerPort: 8080 # REST API
            volumeMounts:
            - mountPath: /opt/gridgain/config
              name: config-vol
            - mountPath: /opt/gridgain/work
              name: work-vol
            - mountPath: /opt/gridgain/wal
              name: wal-vol
            - mountPath: /opt/gridgain/walarchive
              name: walarchive-vol
            - mountPath: /gridgain/tls
              name: node
              readOnly: true
            readinessProbe:
              httpGet:
               path: /ignite?cmd=probe
               port: 8080
              initialDelaySeconds: 5
              failureThreshold: 3
              periodSeconds: 10
              timeoutSeconds: 10
            livenessProbe:
              httpGet:
               path: /ignite?cmd=version
               port: 8080
              initialDelaySeconds: 5
              failureThreshold: 3
              periodSeconds: 10
              timeoutSeconds: 10
    # uncomment the following mount path if you want to provide a license
    # the license must be mounted under this exact path
    #        - mountPath: /opt/gridgain/gridgain-license.xml
    #          subPath: gridgain-license.xml
    #          name: license-vol
          securityContext:
            fsGroup: 2000 # try removing this if you have permission issues
          volumes:
          - name: config-vol
            configMap:
              name: gridgain-config
          - name: node
            secret:
              secretName: certificate
              items:
              - key: node.jks
                path: node.jks
              - key: trust.jks
                path: trust.jks
          # uncomment the following volume if you want to provide a license
    #      - name: license-vol
    #        configMap:
    #          name: gridgain-license
      volumeClaimTemplates:
      - metadata:
          name: work-vol
        spec:
          accessModes: [ "ReadWriteOnce" ]
          resources:
            requests:
              storage: "1Gi" # make sure to provide enough space for your application data
      - metadata:
          name: wal-vol
        spec:
          accessModes: [ "ReadWriteOnce" ]
          resources:
            requests:
              storage: "1Gi"
      - metadata:
          name: walarchive-vol
        spec:
          accessModes: [ "ReadWriteOnce" ]
          resources:
            requests:
              storage: "1Gi"
    ```
    {% endcode %}

## 4. Connect GridGain cluster to Control Center

- Check gridgain pod name with the `kubectl get pods -n gridgain` command:

  ```
  NAME                 READY   STATUS    RESTARTS   AGE
  gridgain-cluster-0   1/1     Running   0          5m56s
  ```
- Get a shell to the running gridgain container:
  - `kubectl exec -it gridgain-cluster-0 -n gridgain -- /bin/bash`
- Inside the container, configure connection to Control Center:
  - `cd /opt/gridgain/bin/`
  - `./management.sh --uri https://frontend.gridgain-control-center:8443 --management-truststore-type jks --management-truststore /gridgain/tls/trust.jks --management-truststore-password qwerty`
  - `exit`

Use the token from the logs to attach cluster with the `kubectl logs gridgain-cluster-0 -n gridgain` command:

```
INFO:

>>> +---------------------------------------------------------------------------------------------------+
>>> | Open the link in a browser to monitor your cluster:
                |
>>> | https://frontend.gridgain-control-center:8443/go/ead0eb2d-a5ef-40e2-9a2e-3b5d98c77ca9             |
>>> +---------------------------------------------------------------------------------------------------+
>>> | If you are already using Control Center, you can add the cluster manually using a one-time token: |
>>> | ead0eb2d-a5ef-40e2-9a2e-3b5d98c77ca9                                                              |
>>> |                                                                                                   |
>>> | NOTE: this token will expire in 5 minutes.                                                        |
>>> | New token can be generated with the following command: management.(sh|bat) --token                |
>>> +---------------------------------------------------------------------------------------------------+
>>> | For more information about connection to GridGain Control Center, please visit:                   |
>>> | https://www.gridgain.com/docs/control-center/latest/connect-gridgain-cluster                      |
>>> +---------------------------------------------------------------------------------------------------+
```
