---
description: >-
  Ways to install and deploy GridGain 9, from ZIP archives and packages to
  Docker, Kubernetes, and cloud marketplace images.
---

# Installation

This section covers the available ways to install and deploy GridGain 9. Choose the method that fits your environment — ZIP archive, DEB or RPM package, Docker, Kubernetes, or a cloud marketplace image — and follow the corresponding guide.

{% columns %}
{% column %}
{% content-ref url="installing-using-zip.md" %}
[Installing Using ZIP Archive](installing-using-zip.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Install the GridGain 9 database and CLI tool from the distributed ZIP archives, then start a node.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="installing-deb-rpm.md" %}
[Installing DEB or RPM Package](installing-deb-rpm.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Install GridGain 9 from DEB or RPM packages and run it as a service or a stand-alone process.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="installing-using-docker.md" %}
[Installing Using Docker](installing-using-docker.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Run GridGain 9 in Docker containers, including the server and dedicated CLI images, and start a cluster with Docker Compose.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="installing-on-kubernetes.md" %}
[Installing on Kubernetes](installing-on-kubernetes.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Deploy a GridGain 9 cluster on Kubernetes with ConfigMaps, a StatefulSet, and an initialization job, and configure logging, probes, and autoscaling.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="installing-with-helm.md" %}
[Installing with Helm Chart](installing-with-helm.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Deploy, configure, update, and uninstall a GridGain 9 cluster on Kubernetes using the GridGain Helm chart.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="software-identification.md" %}
[Software Identification (SWID)](software-identification.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand the Software Identification (SWID) tags that GridGain 9 distributions ship, where they are located, and the fields they carry.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="aws/" %}
[AWS](aws/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Deploy GridGain 9 on Amazon Web Services using the GridGain 9 AMI or the GridGain Terraform module.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="gcp/" %}
[GCP](gcp/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Deploy GridGain 9 on Google Cloud Platform using the GridGain 9 GCP OS image or the GridGain Terraform module.
{% endcolumn %}
{% endcolumns %}
