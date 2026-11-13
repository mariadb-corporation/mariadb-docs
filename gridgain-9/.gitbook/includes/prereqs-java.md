{% tabs %}
{% tab title="9.2" %}
GridGain 9.2 requires Java 21 or later. The server and CLI tool start scripts refuse to start on an older Java version, and the Windows MSI installer refuses to install. The DEB and RPM packages do not check the Java version when you install them. Other Java vendors are supported, but may have minor discrepancies in performance or stability.
{% endtab %}

{% tab title="9.1" %}
GridGain is tested on Oracle JDK 11, 17, 21, and 25 (LTS), as well as JDK 26 (STS). Other Java vendors are supported, but may have minor discrepancies in performance or stability.

Short-term support (STS) Java versions are supported only until the next STS release, Long-term support (LTS) versions are not affected by this policy.
{% endtab %}
{% endtabs %}
