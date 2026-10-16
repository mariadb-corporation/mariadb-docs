---
description: >-
  Stop the streaming demo, the GridGain cluster, and Control Center containers cleanly while keeping the streamed data for later runs.
---

# Stop the GridGain Streaming Demo

When you're done, stop the demo containers.

## Stop the Demo Containers

1. Stop the application's container:

   ```bash
   docker compose -f docker/ignite-streaming-app.yaml stop
   ```
1. Stop the GridGain cluster's containers:

   ```bash
   docker compose -f docker/ignite-cluster.yaml stop
   ```
1. Stop the Control Center containers:

   ```bash
   docker compose -f docker/control-center.yaml stop
   ```

Using `stop` keeps the containers and their data, so you can resume the demo later with the matching `docker compose -f docker/<docker-compose-file> start` (or `up -d`) commands. The cluster stays activated when you restart it this way.

{% hint style="info" %}
To remove the containers and network instead of just stopping them, use `docker compose -f docker/<docker-compose-file> down`. Each cluster node stores its data in its own anonymous Docker volume tied to its container, so `down` discards that data and the next start begins with an empty cluster. Use `stop` rather than `down` if you want to keep the streamed data between runs.
{% endhint %}

You have completed the GridGain 8 management and monitoring guide. Don't hesitate to share feedback by using the `Documentation Feedback` button in the bottom-right corner of the page. Help us fix issues and expand the tutorial, and let us know which topics you'd like new parts to cover.
