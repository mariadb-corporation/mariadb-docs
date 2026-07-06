---
description: >-
  Utilize the Event Scheduler in MariaDB Server to automate tasks. Learn how to
  create, manage, and schedule events to execute SQL statements at specified
  intervals or times.
---

# Event Scheduler

{% columns %}
{% column %}
{% content-ref url="events.md" %}
[events.md](events.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
An introduction to creating and managing scheduled events, which are named database objects containing SQL statements to be executed by the Event Scheduler.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="alter-event.md" %}
[alter-event.md](alter-event.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn how to modify the characteristics of an existing event, such as its schedule, body, or enabled status, without dropping and recreating it.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="event-limitations.md" %}
[event-limitations.md](event-limitations.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A list of restrictions associated with the Event Scheduler, including the inability to return result sets and specific date range limitations.
{% endcolumn %}
{% endcolumns %}
