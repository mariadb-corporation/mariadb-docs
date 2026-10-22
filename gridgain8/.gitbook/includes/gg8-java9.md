GridGain 8.10 requires Java 17 or later (Java 17, 21, and 25 are supported). To run GridGain:

- Set the `JAVA_HOME` environment variable to point to the Java installation directory.
- Pass specific flags to JVM to make proprietary SDK APIs available. If you use the start-up script `ignite.sh` (or `ignite.bat` for Windows), you do not need to do anything because these flags are already set up in the script. Otherwise, provide the following parameters to the JVM of your application:

```
--add-exports=java.base/jdk.internal.misc=ALL-UNNAMED
--add-exports=java.base/sun.nio.ch=ALL-UNNAMED
--add-exports=java.management/com.sun.jmx.mbeanserver=ALL-UNNAMED
--add-exports=jdk.internal.jvmstat/sun.jvmstat.monitor=ALL-UNNAMED
--add-exports=java.base/sun.reflect.generics.reflectiveObjects=ALL-UNNAMED
--add-opens=java.base/jdk.internal.access=ALL-UNNAMED
--add-opens=java.base/jdk.internal.misc=ALL-UNNAMED
--add-opens=java.base/sun.nio.ch=ALL-UNNAMED
--add-opens=java.base/sun.util.calendar=ALL-UNNAMED
--add-opens=java.management/com.sun.jmx.mbeanserver=ALL-UNNAMED
--add-opens=jdk.internal.jvmstat/sun.jvmstat.monitor=ALL-UNNAMED
--add-opens=java.base/sun.reflect.generics.reflectiveObjects=ALL-UNNAMED
--add-opens=jdk.management/com.sun.management.internal=ALL-UNNAMED
--add-opens=java.base/java.io=ALL-UNNAMED
--add-opens=java.base/java.net=ALL-UNNAMED
--add-opens=java.base/java.nio=ALL-UNNAMED
--add-opens=java.base/java.security.cert=ALL-UNNAMED
--add-opens=java.base/java.util=ALL-UNNAMED
--add-opens=java.base/java.util.concurrent=ALL-UNNAMED
--add-opens=java.base/java.util.concurrent.locks=ALL-UNNAMED
--add-opens=java.base/java.util.concurrent.atomic=ALL-UNNAMED
--add-opens=java.base/java.lang=ALL-UNNAMED
--add-opens=java.base/java.lang.invoke=ALL-UNNAMED
--add-opens=java.base/java.lang.reflect=ALL-UNNAMED
--add-opens=java.base/java.math=ALL-UNNAMED
--add-opens=java.base/java.time=ALL-UNNAMED
--add-opens=java.base/java.text=ALL-UNNAMED
--add-opens=java.base/sun.security.ssl=ALL-UNNAMED
--add-opens=java.base/sun.security.x509=ALL-UNNAMED
--add-opens=java.logging/java.util.logging=ALL-UNNAMED
--add-opens=java.management/sun.management=ALL-UNNAMED
--add-opens=java.desktop/java.awt.font=ALL-UNNAMED
--add-opens=java.sql/java.sql=ALL-UNNAMED
```

{% hint style="info" %}
Other parameters, for example, [Detailed GC Logs](../../tuning-and-troubleshooting/troubleshooting.md#detailed-gc-logs), they may be version-dependent as well.
{% endhint %}

When you run GridGain on Java 17 or later, your GridGain cluster nodes may start successfully and reach `ACTIVE` status, but certain runtime operations can still fail with module access errors, caused by Java 9+ module system restrictions (JPMS). Below is the example of an error you many encounter:

```
java.lang.reflect.InaccessibleObjectException: module java.base does not "opens java.time" to unnamed module
```

To resolve this issue, add the appropriate JVM option (--add-opens) for the module mentioned in the error. For example, for the error above, you would add the following:

```
--add-opens=java.base/java.time=ALL-UNNAMED
```

{% hint style="info" %}
The specific option depends on the object types used by the application.
{% endhint %}

Then, restart each node where you updated access permission.
