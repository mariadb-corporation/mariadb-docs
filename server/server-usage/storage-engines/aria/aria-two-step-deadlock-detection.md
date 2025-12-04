---
description: >-
  Explains Aria's deadlock detection mechanism, which uses a two-step process
  with configurable search depths and timeouts to resolve conflicts.
---

# Aria Two-step Deadlock Detection

## Description

The [Aria](./) storage engine can automatically detect and deal with deadlocks (see the [Wikipedia deadlocks article](https://en.wikipedia.org/wiki/Deadlock)).

This feature is controlled by four configuration variables, two that control the search depth and two that control the timeout.

* [deadlock\_search\_depth\_long](aria-system-variables.md)
* [deadlock\_search\_depth\_short](aria-system-variables.md)
* [deadlock\_timeout\_long](aria-system-variables.md)
* [deadlock\_timeout\_short](aria-system-variables.md)

## How it Works

If Aria is ever unable to obtain a lock, we might have a deadlock. There are two primary ways for detecting if a deadlock has actually occurred. First is to search a wait-for graph (see the [wait-for graph on Wikipedia](https://en.wikipedia.org/wiki/Wait-for_graph)) and the second is to just wait and let the deadlock exhibit itself. Aria Two-step Deadlock Detection does a combination of both.

First, if the lock request cannot be granted immediately, we do a short search of the wait-for graph with a small search depth as configured by the `deadlock_search_depth_short` variable. We have a depth limit because the graph can (theoretically) be arbitrarily big and we don't want to recursively search the graph arbitrarily deep. This initial, short search is very fast and most deadlocks are detected right away. If no deadlock cycles are found with the short search the system waits for the amount of time configured in `deadlock_timeout_short` to see if the lock conflicts are removed and the lock can be granted. Assuming this did not happen and the lock request still waits, the system then moves on to step two, which is a repeat of the process but this time searching deeper using the `deadlock_search_depth_long`. If no deadlock has been detected, it waits `deadlock_timeout_long` and times out.

When a deadlock is detected the system uses a weighting algorithm to determine which thread in the deadlock should be killed and then kills it.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
