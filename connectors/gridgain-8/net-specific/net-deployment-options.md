---
hidden: true
description: >-
  Deployment options for GridGain.NET applications: full binary package, NuGet,
  single-file, custom, and ASP.NET deployments.
---

# Application Deployment Options

## Overview

GridGain.NET consists of .NET assemblies and Java jar files. The .NET assemblies are referenced by your project and are copied to an output folder during the build automatically. The JAR files should be copied manually. GridGain.NET discovers them via the `IgniteHome` or `JvmClasspath` settings.

## Full Binary Package Deployment

- Copy the whole GridGain distribution package along with your application
- Set the `IGNITE_HOME` environment variable or `IgniteConfiguration.IgniteHome` setting to point to that folder

## NuGet Deployment

Project properties are updated automatically during the GridGain.NET NuGet package installation to copy jar files to the `libs` folder in the output directory (see [Getting Started](https://www.gridgain.com/docs/gridgain8/latest/getting-started/quick-start/dotnet)). Make sure to include that `libs` folder when distributing your binaries.

Make sure `IGNITE_HOME` is not set globally. Normally you don't need to set `IGNITE_HOME` with NuGet, except for ASP.NET deployments (see below).

To exclude jar files from the build output, add the `<ExcludeAssets>build</ExcludeAssets>` [property](https://docs.microsoft.com/en-us/nuget/consume-packages/package-references-in-project-files#controlling-dependency-assets) to the corresponding `<PackageReference>` element in your `.csproj` file. This can be useful for thin client use cases and custom deployments.

## Single File Deployment

GridGain.NET supports [single file deployment](https://docs.microsoft.com/en-us/dotnet/core/deploying/single-file) that is available in .NET Core 3 / .NET 5+.

- Use the `IncludeAllContentForSelfExtract` MSBuild property to include jar files into the single-file bundle, or ship them separately.
- See [Troubleshooting: DllNotFoundException](net-troubleshooting.md#dllnotfoundexception-unable-to-load-shared-library-libcoreclr.so-or-one-of-its-dependencies) for a workaround that is required on .NET 5 with some Ignite versions.

Publish command example:

`dotnet publish --self-contained true -r linux-x64 -p:PublishSingleFile=true -p:IncludeAllContentForSelfExtract=true`

{% code title="MyApp.csproj" %}
```xml
<Project Sdk="Microsoft.NET.Sdk">
...

    <ItemGroup>
      <PackageReference Include="GridGain.Ignite" Version="8.8.2">
          <ExcludeAssets>build</ExcludeAssets>
      </PackageReference>
    </ItemGroup>

</Project>
```
{% endcode %}

## Custom Deployment

The JAR files are located in the `libs` folder of the binary distribution and NuGet package. The minimum set of jars for GridGain.NET is:

- `ignite-core-{VER}.jar`
- `cache-api-1.0.0.jar`
- `ignite-indexing` folder (if SQL queries are used)
- `ignite-spring` folder (if a Spring XML configuration is used)

### Deploying JARs to a default location:

- Copy the JAR files to the `libs` folder next to `Apache.Ignite.Core.dll`
- Do not set the `IgniteConfiguration.JvmClasspath`, `IgniteConfiguration.IgniteHome` properties and `IGNITE_HOME` environment variable

### Deploying jar files to an arbitrary location:

- Copy the JAR files somewhere
- Set the `IgniteConfiguration.JvmClasspath` property to a semicolon-separated string of paths for each jar file
- Do not set the `IGNITE_HOME` environment variable and `IgniteConfiguration.IgniteHome` property

{% code title="IgniteConfiguration.JvmClasspath Example" %}
```bash
c:\ignite-jars\ignite-core-1.5.0.final.jar;c:\ignite-jars\cache-api-1.0.0.jar
```
{% endcode %}

## ASP.NET Deployment

`JvmClasspath` or `IgniteHome` have to be explicitly set when using Ignite in a web environment (IIS and IIS Express), because DDL files are copied to temporary folders, and Ignite can not locate JAR files automatically.

You can set `IgniteHome` like this in ASP.NET environment:

{% code title="C#" %}
```csharp
Ignition.Start(new IgniteConfiguration
{
    IgniteHome = HttpContext.Current.Server.MapPath(@"~\bin\")
});
```
{% endcode %}

Alternatively, `IGNITE_HOME` can be set globally. Add this line at the top of the `Application_Start` method in `Global.asax.cs`:

{% code title="C#" %}
```csharp
Environment.SetEnvironmentVariable("IGNITE_HOME", HttpContext.Current.Server.MapPath(@"~\bin\"));
```
{% endcode %}

Finally, you can use the following method to populate `JvmClasspath`:

{% code title="C#" %}
```csharp
static string GetDefaultWebClasspath()
{
    var dir = HttpContext.Current.Server.MapPath(@"~\bin\libs");

    return string.Join(";", Directory.GetFiles(dir, "*.jar"));
}
```
{% endcode %}

## IIS Application Pool Lifecycle, AppDomains, and GridGain.NET

There is a known problem with IIS. When a web application is restarted due to code changes or a manual restart, the application pool process remains alive, while AppDomain gets recycled.

GridGain.NET automatically stops when AppDomain is unloaded. However, a new domain may be started when old one is still unloading. So the node from the old domain can have an `IgniteConfiguration.IgniteInstanceName` conflict with a node from the new domain.

To fix this issue make sure to either assign a unique `IgniteInstanceName`, or set `IgniteConfiguration.AutoGenerateIgniteInstanceName` property to `true`.

{% tabs %}
{% tab title="Use in C#" %}
```csharp
var cfg = new IgniteConfiguration { AutoGenerateIgniteInstanceName = true };
```
{% endtab %}

{% tab title="web.config" %}
```xml
<igniteConfiguration autoGenerateIgniteInstanceName="true">
  ...
</igniteConfiguration>
```
{% endtab %}
{% endtabs %}

Refer to the [following StackOverflow discussion](http://stackoverflow.com/questions/42961879/how-do-i-retrieve-a-started-ignite-instance-when-a-website-restart-occurs-in-iis/) for more details.
