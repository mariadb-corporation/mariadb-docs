
MariaDB Client is available for all major operating systems.


## 1. Installation
Installation of MariaDB Client varies by operating system.

### MacOS

1. Install Homebrew if you don't have it already:

    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

2. Install MariaDB Client:

    ```bash
    brew install mariadb
    ```

3. Verify the installation:

    ```bash
    mariadb --version
    ```

### CentOS / RHEL

1. Configure YUM package repositories:

    ```bash 
    sudo yum install wget
    wget https://downloads.mariadb.com/MariaDB/mariadb_repo_setup
    echo "30d2a05509d1c129dd7dd8430507e6a7729a4854ea10c9dcf6be88964f3fdc25 mariadb_repo_setup" \
        | sha256sum -c -

    chmod +x mariadb_repo_setup

    sudo ./mariadb_repo_setup --mariadb-server-version="mariadb-10.11"
    ```

2. Install MariaDB Client and package dependencies:

    ```shell 
    sudo yum install MariaDB-client
    ```

### Debian / Ubuntu

1. Configure APT package repositories:

    ``` shell
    sudo apt install wget

    wget https://downloads.mariadb.com/MariaDB/mariadb_repo_setup

    echo "30d2a05509d1c129dd7dd8430507e6a7729a4854ea10c9dcf6be88964f3fdc25 mariadb_repo_setup" \
        | sha256sum -c -

    chmod +x mariadb_repo_setup

    sudo ./mariadb_repo_setup --mariadb-server-version="mariadb-10.11"

    sudo apt update
    ```

2. Install MariaDB Client and package dependencies:

    ```shell 
    sudo apt install mariadb-client
    ```

### SLES

1. Configure ZYpp package repositories:

    ```shell
    sudo zypper install wget

    wget https://downloads.mariadb.com/MariaDB/mariadb_repo_setup

    echo "30d2a05509d1c129dd7dd8430507e6a7729a4854ea10c9dcf6be88964f3fdc25 mariadb_repo_setup" \
        | sha256sum -c -

    chmod +x mariadb_repo_setup

    sudo ./mariadb_repo_setup --mariadb-server-version="mariadb-10.6"
    ```

2. Install MariaDB Client and package dependencies:
    ```shell 
    sudo zypper install MariaDB-client
    ```

### Windows

1. Access [MariaDB Downloads](https://mariadb.com/downloads/community/community-server/) for MariaDB Community Server.

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

    When only "Client programs" is selected, click "Next".

9. On the next screen, click "Install".

10. When the installation process completes, click "Finish".

## 2. Connect

### Linux

1. Determine the connection parameters for your SkySQL service.

2. Use your connection parameters in the following command line:

    ```shell 
    mariadb --host dbpwf03798702.sysp0000.db1.skysql.com --port 3306 \
        --user dbpwf03798702 -p --ssl-verify-server-cert
    ```

    - Replace 'dbpwf03798702.sysp0000.db1.skysql.com' with the Fully Qualified Domain Name of your service.

    - You can use 3307 for the port if running with Replicas. This is the read-only port of your service.

    - Replace the user name with the one for your service. 

3. After the command is executed, you will be prompted for the password of your database user account. Enter the default password for your default user, the password you set for the default user, or the password for the database user you created.

### Windows

1. Fix your executable search path.

2. On Windows, MariaDB Client is not typically found in the executable search path by default. You must find its installation path, and add that path to the executable search path:

    ```shell 
    SET "PATH=C:\Program Files\MariaDB 10.6\bin;%PATH%"
    ```

3. Use your connection parameters in the following command line:

    ```shell 
    mariadb --host dbpwf03798702.sysp0000.db1.skysql.com --port 3306 \
        --user dbpwf03798702 -p --ssl-verify-server-cert
    ```

    - Replace 'dbpwf03798702.sysp0000.db1.skysql.com' with the Fully Qualified Domain Name of your service.

    - You can use 3307 for the port if running with Replicas. This is the read-only port of your service.

    - Replace the user name with the one for your service. 

4. After the command is executed, you will be prompted for the password of your database user account. Enter the default password for your default user, the password you set for the default user, or the password for the database user you created.
