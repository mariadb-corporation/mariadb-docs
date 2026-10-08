# MariaDB 5.3 - Asynchronous I/O on Windows with InnoDB

Consider 2 pseudo-code implementation of event handling loop handling IO completion on Windows.

* Using Windows events

```
void io_thread() {
    HANDLE handles = new HANDLE[32];
    ...
    for (;;) {
       DWORD index = WaitForMultipleObjects(handles,32, FALSE);
       DWORD num_bytes;
       // Find file and overlapped structure for the index,
       GetOverlappedResult(file, overlapped, &num_bytes, TRUE);
       // handle io represented by overlapped
   }
```

* I/O Completion port based

```
void io_thread() {
    for (;;) {
       DWORD num_bytes;
       ULONG_PTR key;
       OVERLAPPED *overlapped;
       if (GetQueuedCompletionStatus(io_completion_port, &num_bytes,
            &key, &overlapped, INFINITE)) {
          // handle io represented by overlapped
      }
   }
```

Which one is more efficient ? The right answer is - I/O completion port based. This is because:

1. the number of outstanding events a thread can handle is not restricted by a constant like in the WaitForMultipleObject() case.
2. if there several io\_handler() threads running, they load-balance since every I/O can be "dequeued" by GetQueuedCompletionStatus in any io handler thread. With WaitForMultipleObjects(), the thread that will dequeue the I/O result is predetermined for each I/O.

InnoDB has used asynchronous file I/O on Windows since the dawn of time, probably since NT3.1 . On some reason unknown to me (I can only speculate that Microsoft documentation was not good enough back then), InnoDB has always used method with events, and this lead to relatively complicated designs - if you're seeing "segment" mentioning in os0file.c or fil0fil.c , this is mostly due to the fact that number of events WaitForMultipleObjects() can handle is fixed.

I changed async IO handling for XtraDB in MariaDB5.3 to use completion ports, rather than wait\_multiple technique. The results of a synthetic benchmark are good.

The test that I run was sysbench 0.4 "update\_no\_key"

```
4       16      64      256     1024
mariadb-5.2             17812   22378   23436   7882    6043
mariadb-5.2-fix         19217   24302   25499   25986   25925
mysql-5.5.13            12961   20445   16393   14407   5343
```

I do understand, sysbench it does not resemble anything that real-life load, and I'm ready to admit cheating with durability for this specific benchmark, but this is an equal-opportunity cheating, all 3 versions ran with the same parameters.

What do I refer to as durability cheating:

1. using [innodb\_flush\_log\_at\_trx\_commit=0](../../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md) , which, for me , is ok for many scenarios
2. "Switch off Windows disk flushing" setting, which has the effect of not flushing data in the disk controller (file system caching is not used here anyway). This setting is only recommended for battery backed disks, my own desktop does not have it, of course.

However, if I have not done the above, then I would be measuring the latency of a FlushFileBuffers() in my benchmark, which was not what I wanted. I wanted to stress the asynchronous IO.

And here is the obligatory graph:

## Notes

This is taken from an original Facebook note from Vladislav Vaintroub, and it can be found: [note.php?note\_id=238687382817625](https://www.facebook.com/note.php?note_id=238687382817625)

It is also worth noting a note from Vlad about the graph: "The graph is given for 5.2, because I developed that patch for 5.2. I pushed it into 5.3 though :)"

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
