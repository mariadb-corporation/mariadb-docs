# Installing Sphinx

In order to use the [Sphinx Storage Engine](./), it is necessary to install the Sphinx daemon.

Many Linux distributions have Sphinx in their repositories. These can be used to install Sphinx instead of following the instructions below, but these are usually quite old versions and don't all include API's for easy integration. Ubuntu users can use the updated repository at [sphinxsearch-rel21](https://launchpad.net/~builds/+archive/sphinxsearch-rel21) (see instructions below). Alternatively, download from

## Debian and Ubuntu

Ubuntu users can make use of the repository, as follows:

```bash
sudo add-apt-repository ppa:builds/sphinxsearch-rel21
sudo apt-get update
sudo apt-get install sphinxsearch
```

Alternatively, install as follows:

* The Sphinx package and daemon are named `sphinxsearch`.
* `sudo apt-get install unixodbc libpq5 mariadb-client`
* `sudo dpkg -i sphinxsearch*.deb`
* [Configure Sphinx](configuring-sphinx.md) as required
* You may need to check `/etc/default/sphinxsearch` to see that `START=yes`
* Start with `sudo service sphinxsearch start` (and stop with `sudo service sphinxsearch stop`)

## Red Hat and CentOS

* The package name is `sphinx` and the daemon `searchd`.
* `sudo yum install postgresql-libs unixODBC`
* `sudo rpm -Uhv sphinx*.rpm`
* [Configure Sphinx](configuring-sphinx.md) as required
* `service searchd start`

## Windows

* Unzip and extract the downloaded zip file
* Move the extracted directory to `C:\Sphinx`
* [Configure Sphinx](configuring-sphinx.md) as required
* Install as a service:
  * `C:\Sphinx\bin> C:\Sphinx\bin\searchd --install --config C:\Sphinx\sphinx.conf.in --servicename SphinxSearch`

Once Sphinx has been installed, it will need to be [configured](configuring-sphinx.md).

Full instructions, including details on compiling Sphinx yourself, are available at [current.html](https://sphinxsearch.com/docs/current.html).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
