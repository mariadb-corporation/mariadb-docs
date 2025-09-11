# Install mariadb-import

SkySQL customers can import data into a SkySQL service using the `mariadb-import` utility:

- The `mariadb-import` utility provides a command-line interface (CLI)
- The `mariadb-import` utility can import data from TSV and CSV files
- The `mariadb-import` utility is available for Linux and Windows
- The `mariadb-import` utility supports [many command-line options](https://mariadb.com/docs/server/ref/mdb/cli/mariadb-import/)

# Installation

Installation of MariaDB Import varies by operating system.

### **CentOS / RHEL**

1. Configure YUM package repositories:
    
    ```bash
    sudo yum install wget  
    wget https://downloads.mariadb.com/MariaDB/mariadb_repo_setup
    echo "935944a2ab2b2a48a47f68711b43ad2d698c97f1c3a7d074b34058060c2ad21b mariadb_repo_setup" \
        | sha256sum -c -
    chmod +x mariadb_repo_setup   
    sudo ./mariadb_repo_setup --mariadb-server-version="mariadb-10.6"
    ```
    
2. Install MariaDB Import and package dependencies:
    
    ```bash
    sudo yum install MariaDB-client
    ```
    

### **Debian / Ubuntu**

1. Configure APT package repositories:
    
    ```bash
    sudo apt install wget
    wget https://downloads.mariadb.com/MariaDB/mariadb_repo_setup
    echo "935944a2ab2b2a48a47f68711b43ad2d698c97f1c3a7d074b34058060c2ad21b mariadb_repo_setup" \
        | sha256sum -c -
    chmod +x mariadb_repo_setup
    sudo ./mariadb_repo_setup --mariadb-server-version="mariadb-10.6"
    sudo apt update
    ```
    
2. Install MariaDB Import and package dependencies:
    
    ```bash
    sudo apt install mariadb-client
    ```
    

### **SLES**

1. Configure ZYpp package repositories:
    
    ```bash
    sudo zypper install wget
    wget https://downloads.mariadb.com/MariaDB/mariadb_repo_setup
    $ echo "935944a2ab2b2a48a47f68711b43ad2d698c97f1c3a7d074b34058060c2ad21b mariadb_repo_setup" \
        | sha256sum -c -
    chmod +x mariadb_repo_setup
    sudo ./mariadb_repo_setup --mariadb-server-version="mariadb-10.6"
    ```
    
2. Install MariaDB Import and package dependencies:
    
    ```bash
    sudo zypper install MariaDB-client
    ```
    

### **Windows**

1. Access [MariaDB Downloads](https://mariadb.com/downloads/community/community-server/) for MariaDB Community Server.
2. In the "Version" dropdown, select the version you want to download.
3. In the "OS" dropdown, select "MS Windows (64-bit)".
4. Click the "Download" button to download the MSI package.
5. When the MSI package finishes downloading, run it.
6. On the first screen, click "Next" to start the Setup Wizard.
7. On the second screen, click the license agreement checkbox, and then click "Next".
8. On the third screen, select the components you want to install. If you only want the standard MariaDB Client tools:
    - Deselect "Database instance".
    - Deselect "Backup utilities".
    - Deselect "Development Components".
    - Deselect "Third party tools".
    - When only "Client programs" is selected, click "Next".
9. On the next screen, click "Install".
10. When the installation process completes, click "Finish".

# Import Data

The procedure to import data depends on the operating system.

### **Linux**

1. Determine the [connection parameters](<../../Connecting to Sky DBs/>) for your SkySQL service.
2. Use MariaDB Import with the connection information to import the data from the TSV or CSV file into your SkySQL database service:
    
    
    ```bash
    mariadb-import --host FULLY_QUALIFIED_DOMAIN_NAME --port TCP_PORT \
          --user DATABASE_USER --password \
          --ssl-verify-server-cert \
          --ssl-ca ~/PATH_TO_PEM_FILE \
          --local \
          --ignore-lines=1 \
          accounts contacts.tsv
    ```
    
    - Replace `FULLY_QUALIFIED_DOMAIN_NAME` with the Fully Qualified Domain Name of your service
    - Replace `TCP_PORT` with the read-write or read-only port of your service
    - Replace `DATABASE_USER` with the default username for your service, or the username you created
    - Replace `~/PATH_TO_PEM_FILE` with the path to the certificate authority chain (.pem) file
    - If your file is a CSV file, rather than a TSV file, specify `-fields-terminated-by=,`
    - Specify the database name as the first argument (from above, `accounts`)
    - The table name is extracted from the TSV or CSV file's basename (from above, `contacts`)
3. After the command is executed, you will be prompted for a password. Enter the default password for your default user, the password you set for the default user, or the password for the database user you created.

### **Windows**

1. Fix your executable search path.
    
    On Windows, MariaDB Import is not typically found in the executable search path by default. You must find its installation path, and add that path to the executable search path:
    
    ```bash
    SET "PATH=C:\Program Files\MariaDB 10.6\bin;%PATH%"
    ```
    
2. Determine the [connection parameters](<../../Connecting to Sky DBs/>) for your SkySQL service.
3. Use MariaDB Import with the connection information to import the data from the TSV or CSV file into your SkySQL database service:
    
    ```bash
    mariadb-import --host FULLY_QUALIFIED_DOMAIN_NAME --port TCP_PORT \
          --user DATABASE_USER --password \
          --ssl-verify-server-cert \
          --ssl-ca ~/PATH_TO_PEM_FILE \
          --local \
          --ignore-lines=1 \
          accounts contacts.tsv
    ```
    
    - Replace `FULLY_QUALIFIED_DOMAIN_NAME` with the Fully Qualified Domain Name of your service
    - Replace `TCP_PORT` with the read-write or read-only port of your service
    - Replace `DATABASE_USER` with the default username for your service, or the username you created
    - Replace `~/PATH_TO_PEM_FILE` with the path to the certificate authority chain (.pem) file
    - If your file is a CSV file, rather than a TSV file, specify `-fields-terminated-by=,`
    - Specify the database name as the first argument (from above, `accounts`)
    - The table name is extracted from the TSV or CSV file's basename (from above, `contacts`)
4. After the command is executed, you will be prompted for a password. Enter the default password for your default user, the password you set for the default user, or the password for the database user you created.

### **MariaDB Import 10.3 and Older**

The instructions provided above are written for MariaDB Import 10.4 and later, which uses the binary filename of `mariadb-import`.

For MariaDB Import 10.3 and older, the binary filename was `mysqlimport`. The instructions can be adapted for MariaDB Import 10.3 and older by executing `mysqlimport` rather than `mariadb-import`.