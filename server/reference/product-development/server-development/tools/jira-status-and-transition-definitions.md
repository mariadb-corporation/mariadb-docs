---
description: >-
  Explains the various lifecycle statuses and workflow transitions used for
  issue tracking in MariaDB's Jira instance.
---

# Jira - Status and Transition Definitions

Here is the workflow of the MariaDB Server [Jira](jira.md) projects (MDEV and MENT), including how the reviewer and the implementer are assigned when an issue moves into and out of review.

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
* The issue can be closed after it has been in NEEDS FEEDBACK for a month with no activity
* Transitions
  * Provide feedback → OPEN
  * No Feedback → CLOSED

**IN PROGRESS**

* Status employed when the assignee is actively working on the issue
* Denotes that the issue is being actively addressed and moving forward
* Transitions
  * Stop Progress → STALLED
    * We move issues marked “IN PROGRESS” that have had no meaningful updates from the assignee for six weeks to STALLED.
  * Request testing → IN TESTING
  * Needs feedback → NEEDS FEEDBACK
  * Close Issue → CLOSED
  * Request Review → IN REVIEW
    * The transition screen shows the "Assigned for review" field so the reviewer
      can be checked, changed, or filled in if missing.
    * On transition, the current Assignee is saved to "Assigned for implementation",
      and the "Assigned for review" person becomes the Assignee.

**IN REVIEW**

* Status used to request a peer review of an issue, typically involving code evaluation
* Seeking input from another assignee to ensure quality and adherence to standards
* Transitions
  * Redo → STALLED
    * The transition screen shows the "Assigned for implementation" field so the
      implementer can be checked, changed, or filled in if missing.
    * On transition, the current Assignee is saved to "Assigned for review",
      and the "Assigned for implementation" person becomes the Assignee again.
  * Request testing → IN TESTING
  * Approved → APPROVED

**IN TESTING**

* Status employed to initiate testing of completed work, often involving a quality engineer
* Ensuring that the implemented solution meets functional and performance requirements
* Transitions
  * Approved → APPROVED
  * Stop Testing → STALLED
  * Close Issue → CLOSED

**APPROVED**

* Status used when reviewed or tested work has been approved and is ready
  for closure or release follow-up
* Indicates that the issue has passed the required review/testing gate and
  no further implementation changes are expected before final closure
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
