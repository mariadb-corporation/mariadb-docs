---
description: >-
  GridGain's MapReduce API, provided by the ComputeTask interface, lets you split a task into jobs and aggregate their results.
---

# MapReduce API

## Overview

GridGain provides an API for performing simplified MapReduce operations.
The MapReduce pattern is based on the assumption that the task that you
want to execute can be split into multiple jobs (the mapping phase),
with each job executed separately. The results produced by each job are
aggregated into the final results (the reducing phase).

In a distributed system such as GridGain, the jobs are distributed between
the nodes according to the preconfigured [load balancing strategy](load-balancing.md) and the results are aggregated on the node that submitted the task.

The MapReduce pattern is provided by the `ComputeTask` interface.

{% hint style="info" %}
Use `ComputeTask` only when you need fine-grained control over the
job-to-node mapping, or custom fail-over logic. For all other cases you
should use [simple closures](distributed-computing.md#executing-an-igniteclosure).
{% endhint %}

## Understanding Compute Task Interface

The `ComputeTask` interface provides a way to implement custom map and reduce logic. The interface has three methods: `map(...)`, `result()`, and `reduce()`.

The `map()` method should be implemented to create the compute jobs based on the input parameter and map them to worker nodes. The method receives the collection of cluster nodes on which the task is to be run and the task's input parameter. The method returns a map with jobs as keys and mapped worker nodes as values. The jobs are then sent to the mapped nodes and executed there.

The `result()` method is called after completion of each job and returns an instance of `ComputeJobResultPolicy` indicating how to proceed with the task. The method receives the results of the job and the list of all the job results received so far. The method may return one of the following values:

- `WAIT` - wait for all remaining jobs to complete (if any);
- `REDUCE` - immediately move to the reduce step, discarding all the remaining jobs and results not yet received;
- `FAILOVER` - failover the job to another node (see [Fault Tolerance](fault-tolerance.md)).

The `reduce()` method is called during the reduce step, when all the jobs have completed (or the `result()` method returned the `REDUCE` result policy for a particular job). The method receives a list with all completed results and returns the final result of the computation.

## Executing a Compute Task

To execute a compute task, call the `IgniteCompute.execute(...)` method and pass the input parameter for the compute task as the last argument.

{% tabs %}
{% tab title="Java" %}
```java
Ignite ignite = Ignition.start();

IgniteCompute compute = ignite.compute();

int count = compute.execute(new CharacterCountTask(), "Hello Grid Enabled World!");
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
class CharCountComputeJob : IComputeJob<int>
{
    private readonly string _arg;

    public CharCountComputeJob(string arg)
    {
        Console.WriteLine(">>> Printing '" + arg + "' from compute job.");
        this._arg = arg;
    }

    public int Execute()
    {
        return _arg.Length;
    }

    public void Cancel()
    {
        throw new System.NotImplementedException();
    }
}
        

class CharCountTask : IComputeTask<string, int, int>
{
    public IDictionary<IComputeJob<int>, IClusterNode> Map(IList<IClusterNode> subgrid, string arg)
    {
        var map = new Dictionary<IComputeJob<int>, IClusterNode>();
        using (var enumerator = subgrid.GetEnumerator())
        {
            foreach (var s in arg.Split(" "))
            {
                if (!enumerator.MoveNext())
                {
                    enumerator.Reset();
                    enumerator.MoveNext();
                }

                map.Add(new CharCountComputeJob(s), enumerator.Current);
            }
        }

        return map;
    }

    public ComputeJobResultPolicy OnResult(IComputeJobResult<int> res, IList<IComputeJobResult<int>> rcvd)
    {
        // If there is no exception, wait for all job results.
        return res.Exception != null ? ComputeJobResultPolicy.Failover : ComputeJobResultPolicy.Wait;
    }

    public int Reduce(IList<IComputeJobResult<int>> results)
    {
        return results.Select(res => res.Data).Sum();
    }
}

public static void MapReduceComputeJobDemo()
{
    var ignite = Ignition.Start(new IgniteConfiguration
    {
        DiscoverySpi = new TcpDiscoverySpi
        {
            LocalPort = 48500,
            LocalPortRange = 20,
            IpFinder = new TcpDiscoveryStaticIpFinder
            {
                Endpoints = new[]
                {
                    "127.0.0.1:48500..48520"
                }
            }
        }
    });

    var compute = ignite.GetCompute();

    var res = compute.Execute(new CharCountTask(), "Hello Grid Please Count Chars In These Words");

    Console.WriteLine("res=" + res);
}
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

You can limit the execution of jobs to a subset of nodes by using a [cluster group](cluster-groups.md).

## Handling Job Failures

If a node crashes or becomes unavailable during a task execution, all jobs scheduled for the node are automatically sent to another available node (due to the built-in failover mechanism). However, if a job throws an exception, you can treat the job as failed and fail it over to another node for re-execution. To do this, return `FAILOVER` in the `result(...)` method:

```java
@Override
public ComputeJobResultPolicy result(ComputeJobResult res, List<ComputeJobResult> rcvd) {
    IgniteException err = res.getException();

    if (err != null)
        return ComputeJobResultPolicy.FAILOVER;

    // If there is no exception, wait for all job results.
    return ComputeJobResultPolicy.WAIT;
}
```

## Compute Task Adapters

There are several helper classes that provide most commonly used implementations of the `result(...)` and `map(...)` methods.

- `ComputeTaskAdapter` — This class implements the `result()` method to return the `FAILOVER` policy if a job throws an exception and the `WAIT` policy otherwise. It means that this implementation will wait for all jobs to finish with a result.
- `ComputeTaskSplitAdapter` — This class extends `ComputeTaskAdapter` and implements the `map(...)` method to automatically assign jobs to nodes. It introduces a new `split(...)` method that implements the logic of producing jobs based on the input data.

## Distributed Task Session

{% hint style="info" %}
Not available in .NET/C#/C++.
{% endhint %}

For each task, GridGain creates a distributed session that holds information about the task and is visible to the task itself and to all jobs spawned by it. You can use this session to share attributes between jobs. Attributes can be assigned before or during job execution and become visible to other jobs in the same order in which they were set.

{% tabs %}
{% tab title="Java" %}
```java
@ComputeTaskSessionFullSupport
private static class TaskSessionAttributesTask extends ComputeTaskSplitAdapter<Object, Object> {

    @Override
    protected Collection<? extends ComputeJob> split(int gridSize, Object arg) {
        Collection<ComputeJob> jobs = new LinkedList<>();

        // Generate jobs by number of nodes in the grid.
        for (int i = 0; i < gridSize; i++) {
            jobs.add(new ComputeJobAdapter(arg) {
                // Auto-injected task session.
                @TaskSessionResource
                private ComputeTaskSession ses;

                // Auto-injected job context.
                @JobContextResource
                private ComputeJobContext jobCtx;

                @Override
                public Object execute() {
                    // Perform STEP1.
                    // ...

                    // Tell other jobs that STEP1 is complete.
                    ses.setAttribute(jobCtx.getJobId(), "STEP1");

                    // Wait for other jobs to complete STEP1.
                    for (ComputeJobSibling sibling : ses.getJobSiblings())
                        try {
                            ses.waitForAttribute(sibling.getJobId(), "STEP1", 0);
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }

                    // Move on to STEP2.
                    // ...

                    return ... 

                }
            });
        }
        return jobs;
    }

    @Override
    public Object reduce(List<ComputeJobResult> results) {
        // No-op.
        return null;
    }
        
}

```
{% endtab %}
{% tab title="C#/.NET" %}
unsupported
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Compute Task Example

The following example demonstrates a simple character counting application that splits a given string into words and calculates the length of each word in an individual job. The jobs are distributed to all cluster nodes.

{% tabs %}
{% tab title="Java" %}
```java
public class ComputeTaskExample {
    private static class CharacterCountTask extends ComputeTaskSplitAdapter<String, Integer> {
        // 1. Splits the received string into words
        // 2. Creates a child job for each word
        // 3. Sends the jobs to other nodes for processing.
        @Override
        public List<ComputeJob> split(int gridSize, String arg) {
            String[] words = arg.split(" ");

            List<ComputeJob> jobs = new ArrayList<>(words.length);

            for (final String word : words) {
                jobs.add(new ComputeJobAdapter() {
                    @Override
                    public Object execute() {
                        System.out.println(">>> Printing '" + word + "' on from compute job.");

                        // Return the number of letters in the word.
                        return word.length();
                    }
                });
            }

            return jobs;
        }

        @Override
        public Integer reduce(List<ComputeJobResult> results) {
            int sum = 0;

            for (ComputeJobResult res : results)
                sum += res.<Integer>getData();

            return sum;
        }
    }

    public static void main(String[] args) {

        Ignite ignite = Ignition.start();

        IgniteCompute compute = ignite.compute();

        // Execute the task on the cluster and wait for its completion.
        int cnt = compute.execute(CharacterCountTask.class, "Hello Grid Enabled World!");

        System.out.println(">>> Total number of characters in the phrase is '" + cnt + "'.");
    }
}
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp

class CharCountComputeJob : IComputeJob<int>
{
    private readonly string _arg;

    public CharCountComputeJob(string arg)
    {
        Console.WriteLine(">>> Printing '" + arg + "' from compute job.");
        this._arg = arg;
    }

    public int Execute()
    {
        return _arg.Length;
    }

    public void Cancel()
    {
        throw new System.NotImplementedException();
    }
}
        
public class ComputeTaskExample
{
    private class CharacterCountTask : ComputeTaskSplitAdapter<string, int, int>
    {
        public override int Reduce(IList<IComputeJobResult<int>> results)
        {
            return results.Select(res => res.Data).Sum();
        }

        protected override ICollection<IComputeJob<int>> Split(int gridSize, string arg)
        {
            return arg.Split(" ")
                .Select(word => new CharCountComputeJob(word))
                .Cast<IComputeJob<int>>()
                .ToList();
        }
    }

    public static void RunComputeTaskExample()
    {
        var ignite = Ignition.Start(new IgniteConfiguration
        {
            DiscoverySpi = new TcpDiscoverySpi
            {
                LocalPort = 48500,
                LocalPortRange = 20,
                IpFinder = new TcpDiscoveryStaticIpFinder
                {
                    Endpoints = new[]
                    {
                        "127.0.0.1:48500..48520"
                    }
                }
            }
        });

        var cnt = ignite.GetCompute().Execute(new CharacterCountTask(), "Hello Grid Enabled World!");
        Console.WriteLine(">>> Total number of characters in the phrase is '" + cnt + "'.");
    }
}
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
