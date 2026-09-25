You can start a GridGain node from the command line using the default configuration or by passing a custom configuration file. You can start as many nodes as you like and they will all automatically discover each other.

Navigate into the `bin` folder of GridGain installation directory from the command shell. Your command might look like this:

{% tabs %}
{% tab title="Unix" %}
```shell
cd {gridgain}/bin/
```
{% endtab %}

{% tab title="Windows" %}
```shell
cd {gridgain}\bin\
```
{% endtab %}
{% endtabs %}

Start a node with a custom configuration file that is passed as a parameter to `ignite.sh|bat` like this:

{% tabs %}
{% tab title="Unix" %}
```shell
./ignite.sh ../examples/config/example-ignite.xml
```
{% endtab %}

{% tab title="Windows" %}
```shell
ignite.bat ..\examples\config\example-ignite.xml
```
{% endtab %}
{% endtabs %}

You will see output similar to this:

```
[08:53:45] Ignite node started OK (id=7b30bc8e)
[08:53:45] Topology snapshot [ver=1, locNode=7b30bc8e, servers=1, clients=0, state=ACTIVE, CPUs=4, offheap=1.6GB, heap=2.0GB]
```

Open another tab from your command shell and run the same command again:

{% tabs %}
{% tab title="Unix" %}
```shell
./ignite.sh ../examples/config/example-ignite.xml
```
{% endtab %}

{% tab title="Windows" %}
```shell
ignite.bat ..\examples\config\example-ignite.xml
```
{% endtab %}
{% endtabs %}

Check the `Topology snapshot` line in the output. Now you have a cluster of two server nodes with more CPUs and RAM available cluster-wide:

```
[08:54:34] Ignite node started OK (id=3a30b7a4)
[08:54:34] Topology snapshot [ver=2, locNode=3a30b7a4, servers=2, clients=0, state=ACTIVE, CPUs=4, offheap=3.2GB, heap=4.0GB]
```

{% hint style="info" %}
By default, `ignite.sh|bat` starts a node with the default configuration file: `config/default-config.xml`.
{% endhint %}
