---
description: >-
  Explains the various lifecycle statuses and workflow transitions used for
  issue tracking in MariaDB's Jira instance.
---

# Jira - Status and Transition Definitions

Here is the MariaDB Server (MDEV & MENT) [Jira](jira.md) project workflow, including the Dev Owner / reviewer assignment for review transitions.

Note: the workflow diagram is from December 2023 and does not show APPROVED or the Redo rename; flag this for a new screenshot.

**OPEN**

* Status assigned to newly created Jira issues
* Indicates that the issue has been reported and awaits further action
* Transitions
  * Needs feedback → NEEDS FEEDBACK
  * Start progress → IN PROGRESS
  * Close Issue → CLOSED

**CONFIRMED**

* Status applied to validate the existence of a bug type of issue
* Implies that the bug can be consistently reproduced and is scheduled for development
* Transitions
  * Stop Progress → STALLED
  * Request testing → IN TESTING
  * Needs feedback → NEEDS FEEDBACK
  * Close Issue → CLOSED
  * Request Review → IN REVIEW

**NEEDS FEEDBACK**

* Status utilised when progress is contingent on receiving essential feedback
* Feedback requests should be clearly communicated to the designated individual
* Issue can be closed after staying in a month in NEED FEEDBACK with no activity
* Transitions
  * Provide feedback → OPEN
  * No Feedback → CLOSED

**IN PROGRESS**

* Status employed when the assignee is actively working on the issue
* Denotes that the issue is being actively addressed and moving forward
* Transitions
  * Stop Progress → STALLED
    * From the end of 2023, we are moving the issues “IN PROGRESS”, which didn’t get any time to get meaningful updates from the assignee for 6 weeks in this status, to STALLED.
  * Request testing → IN TESTING
  * Needs feedback → NEEDS FEEDBACK
  * Close Issue → CLOSED
  * Request Review → IN REVIEW
    * The transition screen shows the "Assigned for review" field so the reviewer
      can be checked, changed, or filled in if missing.
    * The standard Assignee field is not on this transition screen.
    * On transition, the current Assignee is saved to "Assigned for implementation",
      and the "Assigned for review" person becomes the Assignee.

**IN REVIEW**

* Status used to request a peer review of an issue, typically involving code evaluation
* Seeking input from another assignee to ensure quality and adherence to standards
* Transitions
  * Redo → STALLED
    * The transition screen shows the "Assigned for implementation" field so the
      implementer can be checked, changed, or filled in if missing.
    * The standard Assignee field is not on this transition screen.
    * On transition, the current Assignee is saved to "Assigned for review",
      and the "Assigned for implementation" person becomes the Assignee again.
  * Request testing → IN TESTING
  * Approved → APPROVED
  * Close Issue → CLOSED

**Review follow-up**

**Reviewer acknowledgement**

* When a reviewer is assigned, Jira sends the standard assignment email.
* Within 2 business days (excluding the reviewer's time off), the reviewer must
  either comment with an estimated workload and set the Due Date to when they
  can start, or reassign to a more suitable reviewer (who gets the same 2 days).
* If neither happens, the requester, reviewer, and project manager are notified
  in Slack.
* If the reviewer is off, the notification gives the expected date as
  return date + 2 business days.

**Progress tracking**

* When the Due Date is reached, there is a 2-business-day grace period
  (excluding time off) before progress is checked.
* If the review is underway, the requester gets a Slack update; if not,
  the requester, reviewer, and project manager are notified in Slack and
  asked for a new Due Date.

**Ongoing maintenance**

* For reviews longer than one week, the reviewer updates the Due Date and adds
  a progress comment at least weekly; Jira sends an email reminder if this
  is missing.

**IN TESTING**

* Status employed to initiate testing of completed work, often involving a quality engineer.
* Ensuring that the implemented solution meets functional and performance requirements
* Transitions
  * Approved → APPROVED
  * Stop Testing → STALLED
  * Close Issue → CLOSED

**APPROVED**

* Status used when reviewed or tested work has been approved and is ready
  for closure or release follow-up.
* Indicates that the issue has passed the required review/testing gate and
  no further implementation changes are expected before final closure.
* Transitions
  * Close Issue → CLOSED
  * Reopen Issue → STALLED

**STALLED**

* Status indicating that progress on the issue has been temporarily halted
* Distinguished from the Open status by the presence of prior work on the stalled issue
* Transitions
  * Unconfirm issue → OPEN
  * Request testing → IN TESTING
  * Needs Feedback → NEEDS FEEDBACK
  * Start Progress → IN PROGRESS
  * Close Issue → CLOSED
  * Request Review → IN REVIEW

**CLOSED**

* Status assigned when work on the issue has been finalized
* Signifies that the issue has been successfully resolved and no further action is expected
* In the event that the issue requires reopening, it will revert to the Stalled status
* The resolution is another field that will explain how it has been resolved.
* Transitions
  * Reopen Issue → STALLED

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
