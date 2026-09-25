---
description: >-
  Control how jobs are scheduled for processing on each node by configuring the CollisionSpi with FIFO or priority ordering.
---

# Job Scheduling

When jobs arrive at the destination node, they are submitted to a thread pool and scheduled for execution in random order. However, you can change job ordering by configuring `CollisionSpi`. The `CollisionSpi` interface provides a way to control how jobs are scheduled for processing on each node.

GridGain provides several implementations of the `CollisionSpi` interface:

- `FifoQueueCollisionSpi` — simple FIFO ordering in multiple threads. This implementation is used by default;
- `PriorityQueueCollisionSpi` — priority ordering;
- `JobStealingFailoverSpi` — use this implementation to enable [job stealing](load-balancing.md#job-stealing).

To enable a specific collision spi, change the `IgniteConfiguration.collisionSpi` property.

## FIFO Ordering

`FifoQueueCollisionSpi` provides FIFO ordering of jobs as they arrive. The jobs are executed in multiple threads. The number of threads is controlled by the `parallelJobsNumber` parameter. The default value equals 2 times the number of processor cores.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">

    <property name="collisionSpi">
        <bean class="org.apache.ignite.spi.collision.fifoqueue.FifoQueueCollisionSpi">
            <!-- Execute one job at a time. -->
            <property name="parallelJobsNumber" value="1"/>
        </bean>
    </property>

</bean>
```
{% endtab %}
{% tab title="Java" %}
```java
FifoQueueCollisionSpi colSpi = new FifoQueueCollisionSpi();

// Execute jobs sequentially, one at a time,
// by setting parallel job number to 1.
colSpi.setParallelJobsNumber(1);

IgniteConfiguration cfg = new IgniteConfiguration();

// Override default collision SPI.
cfg.setCollisionSpi(colSpi);

// Start a node.
Ignite ignite = Ignition.start(cfg);
```
{% endtab %}
{% tab title="C#/.NET" %}
unsupported
{% endtab %}
{% endtabs %}

## Priority Ordering

Use `PriorityQueueCollisionSpi` to assign priorities to individual jobs, so that jobs with higher priority are executed ahead of lower priority jobs. You can also specify the number of threads to process jobs.

{% hint style="info" %}
Job and task priority configuration must be the same for all nodes in cluster.
{% endhint %}

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">

    <property name="collisionSpi">
        <bean class="org.apache.ignite.spi.collision.priorityqueue.PriorityQueueCollisionSpi">
            <!-- Change the parallel job number if needed. 
                 Default is number of cores times 2. -->
            <property name="parallelJobsNumber" value="5"/>

            <!-- Change the attribute key for tasks.
                 This key is used to look up task priorities from task context.
                 By default, "grid.task.priority" is used. -->
            <property name="priorityAttributeKey" value="grid.task.priority"/>

            <!-- Change the attribute key for jobs.
                 This key is used to look up job priorities from job context.
                 By default, "grid.job.priority" is used. -->
            <property name="jobPriorityAttributeKey" value="grid.job.priority"/>

            <!-- Set the default job priority.
                 By default is set to 0. -->
            <property name="defaultPriority" value="10"/>
        </bean>
    </property>

</bean>
```
{% endtab %}
{% tab title="Java" %}
```java
PriorityQueueCollisionSpi colSpi = new PriorityQueueCollisionSpi();

// Change the parallel job number if needed.
// Default is number of cores times 2.
colSpi.setParallelJobsNumber(5);

// Change the attribute key for tasks.
// This key is used to look up task priorities from task context.
// By default, "grid.task.priority" is used.
colSpi.setPriorityAttributeKey("grid.task.priority");

// Change the attribute key for jobs.
// This key is used to look up job priorities from job context.
// By default, "grid.job.priority" is used.
colSpi.setJobPriorityAttributeKey("grid.job.priority");

// Set the default job priority.
// By default is set to 0.
colSpi.setDefaultPriority(10);

IgniteConfiguration cfg = new IgniteConfiguration();

// Override default collision SPI.
cfg.setCollisionSpi(colSpi);

// Start a node.
Ignite ignite = Ignition.start(cfg);
```
{% endtab %}
{% tab title="C#/.NET" %}
unsupported
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

### Changing specific task priority

Task priorities are set in the [task session](map-reduce.md#distributed-task-session) via the `grid.task.priority` attribute. To change it, the task`s class must have the `@ComputeTaskSessionFullSupport` annotation. If no priority is assigned to a task, the default priority of 0 is used.

{% tabs %}
{% tab title="Java" %}
```java
@ComputeTaskSessionFullSupport
public class MyUrgentTask extends ComputeTaskSplitAdapter<Object, Object> {
    // Auto-injected task session.
    @TaskSessionResource
    private ComputeTaskSession taskSes = null;

    @Override
    protected Collection<ComputeJob> split(int gridSize, Object arg) {
        // Set high task priority.
        taskSes.setAttribute("grid.task.priority", 10);

        List<ComputeJob> jobs = new ArrayList<>(gridSize);

        for (int i = 1; i <= gridSize; i++) {
            jobs.add(new ComputeJobAdapter() {

                @Override
                public Object execute() throws IgniteException {

                    //your implementation goes here

                    return null;
                }
            });
        }

        // These jobs will be executed with higher priority.
        return jobs;
    }

    @Override
    public Object reduce(List<ComputeJobResult> results) throws IgniteException {
        return null;
    }
}
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
namespace dotnet_helloworld
{
    public class JobScheduling
    {
        public void Priority()
        {
            // PriorityQueueCollisionSpi must be configured in the Spring XML configuration file ignite-helloworld.xml
            var cfg = new IgniteConfiguration
            {
                SpringConfigUrl = "ignite-helloworld.xml"
            };

            // Start a node.
            using var ignite = Ignition.Start(cfg);
        }

        // Compute tasks must be annotated with the ComputeTaskSessionFullSupport attribute to support distributing the task's session attributes to compute jobs that the task creates.
        [ComputeTaskSessionFullSupport]
        public class MyUrgentTask : ComputeTaskSplitAdapter<int, bool, bool>
        {
            // Auto-injected task session.
            [TaskSessionResource] private IComputeTaskSession _taskSes;

            protected override ICollection<IComputeJob<bool>> Split(int gridSize, int arg)
            {
                // Set high task priority.
                _taskSes.SetAttribute("grid.task.priority", 10);

                var jobs = new List<IComputeJob<bool>>(gridSize);

                for (var i = 1; i <= gridSize; i++)
                {
                    jobs.Add(new MyUrgentJob());
                }

                // These jobs will be executed with higher priority.
                return jobs;
            }

            public override bool Reduce(IList<IComputeJobResult<bool>> results) => results.All(r => r.Data);
        }

        private class MyUrgentJob : ComputeJobAdapter<bool>
        {
            public override bool Execute() => true;
        }
    }
}
```
{% endtab %}
{% endtabs %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
