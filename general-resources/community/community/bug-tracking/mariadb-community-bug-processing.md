# Bug Processing

This page describes how community bug reports are processed among our products and explains what you need to notice while tracking bugs.

## Commitments

MariaDB does not have any SLA or guaranteed reaction times on bugs in Jira. While we are taking bugs reported by the community very seriously, and aim to provide response and to handle issues as fast as possible, MariaDB does not have a dedicated bug verification team, this activity is performed on the best-effort basis.

To make sure your bug report will be confirmed and moved forward faster, please follow [**the guidelines**](reporting-bugs.md) about creating bug reports.

## Bug Verification Routine

As of today, initial bug processing routine in MariaDB is not strictly formalized. This section describes the de-facto status rather than any policy.

The process is different for bug reports (_Bug_ type in JIRA) vs feature requests (_Task_ type). The process described below is related to bug reports.

### Incoming Queue

All new bug reports go to the waiting list, to be reproduced and confirmed by a member of the team. The bug stays in the queue until one or more of the conditions below are met:

* Bug report is assigned to a developer;
* Bug report gets status 'Confirmed';
* Bug report gets the label 'upstream';
* Bug report is closed (on whatever reason).

With other things equal, bug reports in the queue are initially handled in the FIFO manner; however, there are various factors that make things not equal.

#### Bug Processing Order

First thing that is taken into account is [**Priority**](reporting-bugs.md#priority). It does not mean that everything needs to be filed as Critical; on the contrary, it means that Priority should be chosen wisely. Although a report with higher Priority will be looked at sooner, as soon as it becomes clear that the Priority is set to a higher value than the problem deserves, it will be amended and put back to the queue. However, if the high priority is justified, we will try to process the report as fast as possible.

Another important factor is [**the quality of the report**](reporting-bugs.md) itself.

* If the report is written well and [has all information](reporting-bugs.md#contents-of-a-good-bug-report), including a reproducible test case, it can be verified and moved forward quickly.
* If the report is written clearly enough, but does not have enough information, it will get fast enough first response where we will request the missing details; but the further exchange can take a lot of time until we get everything we need to work on the issue.
* Finally, reports which are written in a tangled and incomprehensible manner get the slowest response time, because even if eventually it turns out that they do have all required information, it is difficult and time-consuming to extract and process, so they can be put aside for some time.

#### First Response

Complete processing of a reported bug can be complicated and time-consuming, especially the reproducing part. We do not want our users to wait for long not knowing if their bug report has even been noticed, we try to provide first response quicker than that.

First response to the bug, which we are trying to provide as quickly as possible, is one of these:

* If we can reproduce the problem based on the information that was provided in the initial description, the report gets the status Confirmed.
* If it is obvious from the initial description that the bug report is a [duplicate](reporting-bugs.md#is-the-bug-already-known) of an existing one, or the problem has already been fixed in later releases or in the upcoming release, or the described behavior is not a bug, or, in very rare cases, it is admitted to be a bug, but it is not going to be fixed, the report gets closed with the corresponding Resolution value and a comment with the explanation.
* If the bug report at least appears to describe a real bug, but we do not have enough information to proceed, we will request the information from the reporter, and the report will go to the [Need feedback](mariadb-community-bug-processing.md#need-feedback-what-is-it-and-how-to-deal-with-it) list.
* If on some reason it is clear from the bug report that it will be very difficult to reproduce based on the information from the user, but there is a reason to believe that the problem can be analyzed by code inspection, the bug report can be assigned to a developer who is an expert in the corresponding area for the analysis.

We realize that "as quickly as possible" is a relative term. The dream scenario is that all reports are responded to in a matter of hours; however, more realistically, it can take a few days, and in some cases, when the team is overly busy with a big upcoming release or some other extraordinary events, it can even be weeks.

### Need Feedback

When a report does not have all the information to reproduce the problem right away (which is quite often the case), we will ask the reporter to provide the missing information. Usually it takes more than one iteration to get everything right, so it is important that you respond to the questions as precisely as you can. Please make sure that you answered **all** questions (or, if you cannot answer some of them, please say so, otherwise we will have to ask again, and more time will be wasted on it).

There is no status "Need Feedback" in our JIRA; instead, we are using the label `need_feedback`. As long as the report has this label, it remains on the "Waiting for feedback" list. The label is set and removed manually by whoever asks for the feedback and receives it; so it can happen that the reporter has provided the response, but it remained unnoticed and the bug keeps waiting. It will be our fault, but human errors happen; it would help a lot if the reporter removed the label along with providing the feedback.

#### E-mail Notifications

This question arises fairly often, so it deserves mentioning.

As already said before, the `need_feedback` label is set and _removed_ manually. JIRA e-mail updates about it can be confusing when you look at them quickly. For example, when someone _removes_ the label, the email looks like this:

```
Elena Stepanova updated MDEV-9791:
----------------------------------
    Labels:   (was: need_feedback)
```

What it says that the `Labels` field has become empty, while before it had been `need_feedback`. People often misread it and ask "What else do you need from me? I've answered your questions". This update means that at the moment we don't need anything, your report is back to the incoming queue, and your feedback will be analyzed as soon as possible. Then, we will possibly ask more questions and set the label again, and the notification will look like this:

```
Elena Stepanova updated MDEV-9801:
----------------------------------
    Labels: need_feedback  (was: )
```

#### Successful Outcome

If the feedback exchange was fruitful and we received enough information to proceed, the bug report will go through the normal [**verification steps**](mariadb-community-bug-processing.md#what-is-done-during-bug-verification).

#### Incomplete Reports

Reports do not stay open on the "Need Feedback" list forever. After a month of waiting, if we do not get a response from the reporter, and still cannot proceed without it, we close the report as **Incomplete** with the corresponding comment. This state is not irreversible: you can still add comments and provide the information even when the report is closed as Incomplete, and it will be re-opened.

#### Worst Case Scenario

Sometimes it happens that after iterations of feedback requests we run out of ideas what else to ask from the reporter, and still could not verify the bug, or that the reporter is willing to collaborate with us, but cannot provide the necessary information on objective reasons (usually when the problem happens on a production instance). In some cases we might close the report as "Cannot reproduce", which we consider our loss; but more often we want to keep it open, in hope that more information arrives, maybe from a different source, and together with this report they will help us get to the bottom of the problem; if it happens so, the report gets assigned to somebody without being confirmed, just so it remains at least on somebody's radar, and it will stay open for a long time. It does not mean it is forgotten, it means that for the time being we hit the wall. You are very welcome to comment on such reports, whenever you think you might have something to add, because this is exactly what we are waiting for.

### Bug Verification

Normally the bug report has to go through the following steps before it is moved forward to fixing:

* the described problem needs to be reproduced;
* it needs to be checked against all active post-Beta versions of MariaDB where it is theoretically applicable (as of the moment of writing this article, it is 5.5, 10.0, 10.1);
* in case it is a relatively recent regression, the guilty change needs to be found;
* the component or functional area should be determined, so that the bug gets assigned to the right person.

After that the bug is ready for fixing.

## Bug Fixing Routine

Sometimes it seems hard to understand from the outside how MariaDB development team chooses which bugs to fix in a particular release, or why some bugs are fixed faster than others, or why critical bugs stay untouched for a long time.

### Sprint Model for Bug Fixing

MariaDB currently uses 1- or 2-week sprint model for server development and bugfixing. It needs a separate article to describe it in more detail, but for bugfixing, in a nutshell it means the following.

* one or two weeks before a scheduled release the team creates a new sprint and evaluates existing bugs which affect this release;
* the selected bugs are added to the new sprint;
* during the active sprint, the developer is supposed to work on the tasks which are part of the sprint, unless a true emergency arises.

There are two important consequences of this model which sometimes cause a confusion:

1. If the current sprint is for one version, e.g. 10.0, and you file a bug for another version, e.g. 10.1, then, even if the bug is really critical, it won't be jumped on right away: it makes no sense, because the 10.1 is not going to be released next week anyway, while 10.0 will be. When the 10.0 sprint finishes, and 10.1 sprint starts, your bug will be picked up for that sprint and fixed then.
2. If the current sprint for 10.1 is already in progress, newly created 10.1 reports normally won't be included into it, unless they are considered so extremely important that the developer is allowed to ignore the sprint plan.

### Bugs Chosen for a Sprint

When a new sprint is created, bugs which affect the scheduled release are evaluated.

* from all such bugs assigned to a developer, each developer chooses bugs he is able to work on during the given time interval;
* bug priority plays the most significant role in this process, but this is not the only factor.
  * `Blocker` bugs must be either fixed or degraded before the release goes out;
  * `Critical` bugs should be chosen above other bugs, except for `Blocker`s;
  * among `Major` bugs,
    * bugs with patches, either external, or upstream, or internal, are usually prioritized above ordinary bug reports;
    * external reports (community reports) are ranked higher than bugs reported by the development team;
    * bugs which can realistically be fixed in the given time interval are chosen more frequently than those that are likely to take several cycles;
    * bugs which affect the reporter in a worse matter get more attention than those that have viable workarounds;
  * `Minor` bugs are usually fixed when there are no more urgent tasks.

## Tracking Progress

If a bug report has passed through verification stage, either being confirmed, or pushed forward to the development-level analysis as is, there can be various updates on it. It is important to understand what they mean.

### JIRA Fields to Watch

All JIRA fields are public, but some of them are mainly used for internal development process, while others are more user-facing. [**This article**](reporting-bugs.md#jira-fields) describes which fields should be populated during the initial report submission. There is a different set of fields important for tracking purposes.

#### Resolution vs. Status

It might come as counter-intuitive, but in the existing JIRA structure, the `Status` field does not mean much for the user, it is mainly used for development and management purposes. On the contrary, the `Resolution` field is entirely user-facing: it does not participate in planning or development. It remains the same 'Unresolved' for the whole life of the report, and is only changed when the bug gets closed, demonstrating the reason why it was closed.

**Resolution**

* `Unresolved` - the bug report remains open, the work has not been finished.
* `Fixed` - the bug has been fixed, see [Fix version/s](mariadb-community-bug-processing.md#fix-versions) and possibly comments to the report for more information. This is almost always a terminal state, we do not re-open fixed bugs even if they later re-appear; please create a new one instead. The only case when it can be re-opened is when the 'Fix version/s' have not been released yet.
* `Duplicate` - the bug report is identical to an already existing open (or recently fixed) report, which will be quoted in the comments and/or links. It is usually a terminal state, unless it is proven later that the report was not a duplicate after all.
* `Not a bug` - the described behavior is not a bug, there will be a comment explaining why. It is usually a terminal state, unless you object and show why it is a bug. If the report is in fact a feature request, then rather than closing it as 'Not a bug', we will switch the type to 'Task'.
* `Incomplete` - we had requested feedback from the user and waited for 1 month, but did not receive it. It is a pseudo-terminal state, the report can be re-opened any time when the requested information is provided.
* `Cannot reproduce` - rather rarely used "resolution", which means we could not find the way to confirm the problem described by the reporter, and ran out of ideas what other information to request from the reporter in order to reproduce it.
* `Won't fix` - another rarely used "resolution", which means that the bug is admitted, but we have no intention to fix it. Usually it happens when the bug only affects old versions, and is not important enough to fix in the old versions; or, when it is related to systems or architectures we don't officially support.

**Status**

* `Open`, `Confirmed` - this distinction is used in our internal queues, but from the user's perspective the difference is slim: setting the bug report to 'Confirmed' does mean that we are satisfied with the information provided in the report, but the user will also know about it from our comments and other updates. Otherwise, bugs in both statuses can be considered for fixing.
* `In Progress`, `Stalled` - different intermediate states of bugs which help developers to filter their lists and management to gather a picture of the current activity. For the user, there is no important difference -- despite the negative semantics, 'Stalled' does not mean that something is wrong with the bug report, only that the developer is not working on it actively at the moment.
* `In review` - means, literally, that a peer review has been requested.
* `Closed` - means that the bug report is closed, on whatever reason. The real reason is in the 'Resolution' field.

#### Fix Versions

This is an important field for progress tracking.\
After the bug is confirmed or otherwise acknowledged, this field is populated with a set of major versions where we intend to fix it. E.g. if the field is set to `10.0 10.1`, it means that at the moment we consider it for fixing in some future 10.0 release (not necessarily the next one), and the bugfix will be merged into the next 10.1 release after that; but we do not consider it for fixing in 5.5, even if it is affected to.

To some extent, you can influence the initial plans: if you see that the fix is not targeted for versions where you think it should be, you can comment on the report, and if you provide convincing arguments and make your case, it can be reconsidered.

The value of the field is not a promise to fix the bug in the mentioned releases. It can be changed both ways: during further analysis, the developer can find out that it can be safely fixed in an earlier release, or, on the contrary, that it cannot be safely fixed in the GA release, and the fix can only go to the next versions which are currently under development.

After the bug is fixed, the value of the field is changed to the exact versions, e.g. `10.0.25 10.1.14`. It means that the patch has been pushed into the 10.0 branch, and will be released with 10.0.25 release; it also means that the patch _will be_ merged to 10.1 tree and released with 10.1.14 release, but it does not mean that it is already in the 10.1 branch.

#### Priority

As the other article says, the [**Priority**](reporting-bugs.md#priority) field serves two purposes. During the initial bug creation, it indicates the importance of the bug report from the user's perspective (in other bug tracking systems it is called 'Severity' or alike). After the bug has been confirmed, the same field is used for development purposes, to prioritize bug fixing (real 'Priority'). While we take into account the reporter's view on the matter, we can change the initial priority both ways, depending on the information we revealed during the problem analysis, versions affected, etc.

The value of the field normally means the following:

* `Blocker` - we currently think that the bug must be fixed before the next release(s) set in the 'Fix version/s' field;
* `Critical` - the bug should be picked up for fixing earlier than any other bugs apart from blockers;
* `Major` - the bug will be present in the main queue for fixing in the upcoming 'Fix version/s', although only a part of such bugs will be fixed in every release;
* `Minor`, `Trivial` - the bugs will be picked up when the assignee does not have more pressing issues for the upcoming release.

Please note that the Priority field only demonstrates our intentions at the moment, it does not guarantee that things will happen according to these intentions.

#### Labels

Labels are mostly used for more convenient filtering and don't carry much importance otherwise. However, there are a few that affect the processing of a bug report:

* `need_feedback` - its role during the initial bug processing was already described [above](mariadb-community-bug-processing.md#need-feedback-what-is-it-and-how-to-deal-with-it). However, after a bug is confirmed and queued for fixing, it should not appear anymore; and even if it's left by mistake, it won't affect the progress.
* `upstream` - the label means that the bug also exists in the upstream version of the corresponding component - normally, in MySQL server or a client program, but can also be in Percona's XtraDB or TokuDB. Normally there should also be a link to the upstream bug report. Setting this label means that we might want to take for a while and see whether the bug is fixed in the upstream version before we fix it in MariaDB directly. It was usual for 5.5, less usual for 10.x where bugfixes, apart from InnoDB, are not merged automatically. The label is still set, but it is more for informational purposes than to affect the priority.
* `upstream-fixed` - the label means that the bug used to exist in the upstream version, but not anymore. It means that there is nothing more to wait; moreover, it might be worth picking up the bug soon and at least evaluating the upstream bugfix.

## Bug Reports with Patches

MariaDB encourages contributors to provide bug fixes; so, bug reports which come with the fixes in general have a quicker turnaround. The bug fix can come in a form of Git pull request, or, in simple cases, as a diff pasted in or attached to the bug report itself.

## Principles for External Bug Reports

There are some basic rules for bugs, particularly for setting the [**Resolution**](mariadb-community-bug-processing.md#resolution) value, which we want to stick to and which might be different from procedures you came across in other projects. It mainly concerns _external_ bugs (those that come from the community), for internal ones we can cut corners more freely.

This all is easier to understand if one remembers that the **Resolution** or its analogues in other bug-tracking systems is a _user-facing_ field, as already mentioned above, and that it relates more to the report, than to the bug itself.

### Duplicate

An older bug report cannot be a duplicate of a newer one, it is nonsensical. The only possible exception is when an older bug has no useful information whatsoever _and_ the reporter does not provide any helpful feedback, while a newer report was not closed as a duplicate right away and got some useful updates. The common example of such exception is when the first report is just an optimized stack trace, no query, no data, nothing to work with, while the second report has a test case. But if the first reporter at least makes an effort to collaborate, the report deserves to be treated with respect.

Bug reports which have essentially different descriptions and/or test cases should not be duplicates. The common example is this: a developer creates a bug saying something like "this and that pieces of code are wrong, it should be so and so"; and then a user files a bug saying "this SQL produces a wrong result on this data set". Even if they are about _the same error in the code_ at the end, they are not duplicate _bug reports_.

Obviously, a report can never be a duplicate of anything private (luckily it does not concern MariaDB server so far, as the bug reports are public).

In general, a bug report is a duplicate of another one if, and only if, the new reporter could find the existing report just by a reasonable [**JIRA search**](reporting-bugs.md#is-the-bug-already-known).

### Cannot Reproduce

A bug report should not be closed as "cannot reproduce" if it was once verified/confirmed, but disappeared in later versions. It's unfair to the reporter, and also dangerous to the product. We should know why a bug stopped being reproducible -- either we find when and how it was fixed (and close the report as "Fixed in version X by a patch for Y"), or we discover that it wasn't in fact fixed, but just masked. The simplest example is a change of execution plan in optimizer: server would crash on a particular query, then due to a change in optimizer it started using a different plan for the same query, so it wouldn't go through the crashing path anymore. The crash is still there, though.

In general, the "cannot reproduce" resolution is a last resort. Usually if we can't reproduce something, it means that either the reporter did not provide required information (and then the resolution should be "Incomplete"), or we don't know what to request from the reporter, and then we should keep thinking, rather than close it. Of course, it happens that the bug is genuinely not reproducible, but it shouldn't be decided lightly.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
