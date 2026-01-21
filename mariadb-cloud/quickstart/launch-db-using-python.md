# Launch DB Using Python

The Python example below shows how to launch a DB service and connect to it using the MariaDB Cloud DBaaS API.

You need to configure the following environment variables:&#x20;

* &#x20;`API_KEY`&#x20;
* &#x20;`SKYSQL_CLIENT_IP`&#x20;

{% stepper %}
{% step %}
### **Generate API Key**

1. Go to [MariaDB Cloud API Key management page](https://app.skysql.com/user-profile/api-keys) and generate an API key.
2.  Export the value from the token field to an environment variable API\_KEY:

    ```bash
    export API_KEY='... key data ...'
    ```

    The `API_KEY` environment variable will be used in the subsequent steps.

Check any existing services:

```bash
 curl --request GET 'https://api.skysql.com/provisioning/v1/services' \
    --header "X-API-Key: $API_KEY"
```
{% endstep %}

{% step %}
### **Determine the Client IP Address**

When your new service is created, your client can only connect through the service's firewall if the client IP address is in the service's IP allowlist.

Before creating the new service, determine the public IP address of your client host and save it to the `SKYSQL_CLIENT_IP` environment variable.

If you are not sure of your public IP address, you can use a lookup service, such as `checkip.amazonaws.com`:

```bash
export SKYSQL_CLIENT_IP=`curl -sS checkip.amazonaws.com`
```
{% endstep %}

{% step %}
### **Create the Service Using Python**

The following Python script has been tested with Python 3.11

```python
import os
import time
import requests
import json
import sys
import argparse
import mysql.connector
from mysql.connector import Error

# Set your API key and client IP
API_KEY = os.getenv('API_KEY')
CLIENT_IP = os.getenv('SKYSQL_CLIENT_IP')
## Name of the service to be created
SKYDB_SERVICE_NAME = 'my-first-skysql-db'

# Headers for the API requests
headers = {
    'Content-Type': 'application/json',
    'X-API-Key': API_KEY
}

# Function to launch a MariaDB Cloud DB service
def launch_skysql_db():
    url = "https://api.skysql.com/provisioning/v1/services"
    payload = {
        "service_type": "transactional",
        "topology": "es-single",
        "provider": "gcp",
        "region": "us-central1",
        "architecture": "amd64",
        "size": "sky-2x8",
        "storage": 100,
        "nodes": 1,
        "name": f"{SKYDB_SERVICE_NAME}",
        "ssl_enabled": True,
        "allow_list": [
            {
                "comment": "Describe the IP address",
                "ip": f"{CLIENT_IP}/32"
            }
        ]
    }
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"Failed to launch MariaDB Cloud DB service: {e}")
        return None


# Function to monitor the status of the service
def monitor_status(service_id):
    url = f"https://api.skysql.com/provisioning/v1/services/{service_id}"
    while True:
        response = requests.get(url, headers=headers)
        status = response.json().get('status')
        if status == 'ready':
            print("Service is ready.. ")
            print(response.json())
            return response.json()
        print("Service launch started .. will wait for 30 secs and check again...")
        time.sleep(30)

# Function to test the connection to the service
def test_connection(connection_properties):
    try:
        connection = mysql.connector.connect(
            host=connection_properties['host'],
            user=connection_properties['user'],
            password=connection_properties['password'],
        )
        if connection.is_connected():
            print("Connection successful")
            connection.close()
    except Error as e:
        print(f"Error: {e}")


# Function to fetch security credentials for the service
def fetch_credentials(service_id):
    url = f"https://api.skysql.com/provisioning/v1/services/{service_id}/security/credentials"
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch credentials: {e}")
        return None


# Main function to execute the steps
def main():
    # Step 0: Parse command-line arguments
    parser = argparse.ArgumentParser(description="Launch MariaDB Cloud DB or use an existing service")
    parser.add_argument('--service_id', type=str, help="Optional service ID to skip launching a new service")
    args = parser.parse_args()

    # Step 1: Either use the provided service_id or launch a new MariaDB Cloud DB
    if args.service_id:
        print(f"Using provided service ID: {args.service_id}")
        service_id = args.service_id
    else:
        service_response = launch_skysql_db()

        # Check if the response status code is within the 2xx range (success)
        if not (200 <= service_response.status_code < 300):
            print("Failed to launch MariaDB Cloud DB service")
            print(service_response.json())  # Print detailed error message
            return

        service_json = service_response.json()
        service_id = service_json.get('id')

        if not service_id:
            print("Service launched, but could not retrieve service ID")
            return

    # Step 2: Monitor the status until 'ready'
    service_details = monitor_status(service_id)
    if not service_details:
        print("Service did not become ready")
        return

    # Step 3: Obtain the connection properties (FQDN and port)
    fqdn = service_details.get('fqdn')
    ports = service_details['endpoints'][0]['ports']
    
    # Find the port where name is 'readwrite'
    readwrite_port = next((port['port'] for port in ports if port['name'] == 'readwrite'), None)

    if not fqdn or not readwrite_port:
        print("Failed to retrieve FQDN or port information.")
        return

    # Step 4: Obtain the default credentials (username and password)
    credentials = fetch_credentials(service_id)
    
    if not credentials:
        print("Failed to retrieve credentials")
        return

    connection_properties = {
        'host': fqdn,
        'port': readwrite_port,
        'user': credentials.get('username'),
        'password': credentials.get('password'),
    }

    # Step 5: Test the connection to the DB
    test_connection(connection_properties)
if __name__ == "__main__":
    main()
```
{% endstep %}
{% endstepper %}
