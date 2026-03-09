---
description: >-
  Specific instructions and requirements for configuring a Buildbot worker on
  macOS systems.
---

# Buildbot Setup for macOS

## Setting up a Buildbot Slave on macOS

Install buildbot-slave using [macports](https://www.macports.org/) or buildbot from [fink](https://www.finkproject.org/) (if you use old version of `buildbot`/`buildbot-slave`, you should use the `buildbot` command instead of `buildslave-2.6` in the following instructions).

Add user buildbot. Make sure that you do not have a buildbot user and group on your system:

```bash
# Check for group with id 101
id -g -nr 101

# Check for user with id 101
id -u -nr 101
```

If you do not have the group and user buildbot, then create the group and the user buildbot:

```bash
# Create group buildbot with group id 101
GROUP="buildbot"
dscl . create /groups/$GROUP
dscl . create /groups/$GROUP name $GROUP
dscl . create /groups/$GROUP passwd "*"
dscl . create /groups/$GROUP gid 101

# Create user buildbot with id 101
BUILDSLAVE_HOME=/var/lib/buildslave
USER=buildbot
mkdir -p $BUILDSLAVE_HOME
dscl . -create /Users/$USER
dscl . -create /Users/$USER RealName "Buildbot slave"
dscl . -create /Users/$USER NFSHomeDirectory $BUILDSLAVE_HOME
dscl . -create /Users/$USER UserShell /bin/bash
dscl . -create /Users/$USER UniqueID 101
dscl . -create /Users/$USER PrimaryGroupID 101
chown 101:101 $BUILDSLAVE_HOME
```

To hide the user use:

```bash
defaults write /Library/Preferences/com.apple.loginwindow HiddenUsersList -array-add buildbot
```

Prepare the environment:

```bash
sudo -i -u buildbot
buildslave-2.6 create-slave --usepty=0 maria-slave hasky.askmonty.org:9989 <slavename> <passwd>
bzr init-repo maria-slave/<slavedirectory>
$EDITOR maria-slave/info/admin
$EDITOR maria-slave/info/host
logout
```

Buildbot can be started/stopped manually with these commands (it's a good idea to start and stop it to see if it is set up correctly). If you installed buildbot from [fink](https://www.finkproject.org/), please make sure that the buildbot user is using the environment settings. Your .profile should contain following line:

```bash
sudo - buildbot
more .profile
test -r /sw/bin/init.sh && . /sw/bin/init.sh
```

```bash
sudo -i -u buildbot
buildslave-2.6 start maria-slave
buildslave-2.6 stop maria-slave
logout
```

In order to make buildbot start on system boot, you'll need to create a `/Library/LaunchDaemons/net.sourceforge.buildbot.plist` file with the following contents (modified example from buildbot wiki):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
    <dict>
 	<key>StandardOutPath</key>
 	<string>twistd.log</string>
 	<key>StandardErrorPath</key>
 	<string>twistd-err.log</string>
 	<key>EnvironmentVariables</key>
 	<dict>
 		<key>PATH</key>
 		<string>/opt/local/bin:/sbin:/usr/sbin:/bin:/usr/bin</string>
 		<key>PYTHONPATH</key>
 		<string>/opt/local/lib/python2.5/site-packages</string>
 	</dict>
 	<key>GroupName</key>
 	<string>daemon</string>
 	<key>KeepAlive</key>
 	<dict>
 		<key>SuccessfulExit</key>
 		<false/>
 	</dict>
 	<key>Label</key>
 	<string>net.sourceforge.buildbot.slave.test</string>
 	<key>ProgramArguments</key>
 	<array>
 		<string>/opt/local/bin/buildslave-2.6</string>
 		<string>start</string>
 		<string>--nodaemon</string>
 		<string>maria-slave</string>
 	</array>
 	<key>RunAtLoad</key>
 	<true/>
 	<key>UserName</key>
 	<string>buildbot</string>
 	<key>WorkingDirectory</key>
 	<string>/var/lib/buildslave/</string>
    </dict>
</plist>
```

If you installed buildbot from [fink](https://www.finkproject.org/), you can edit and copy the `plist` file:

```bash
$EDITOR /sw/share/doc/buildbot-py26/contrib/os-x/net.sourceforge.buildbot.slave.plist
```

Your `plist` file should similar to this one after editing:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd 
">
<plist version="1.0">
<dict>
         <key>Label</key>
         <string>net.sourceforge.buildbot.slave</string>

         <!-- Change this to the user you want to run buildbot as -->
         <key>UserName</key>
         <string>buildbot</string>

         <!-- Change this to your buildbot working directory -->
         <key>WorkingDirectory</key>
         <string>/Volumes/MiniHD2/ServiceData/buildslave/maria-slave</string>
        
         <key>EnvironmentVariables</key>
         <dict>
                 <key>PATH</key>
                 <string>/sw/bin:/sw/sbin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin</string>
         </dict>

         <key>ProgramArguments</key>
         <array>
                 <string>/sw/bin/twistd</string>
                 <string>--nodaemon</string>
                 <string>--python=buildbot.tac</string>
                 <string>--logfile=buildbot.log</string>
                 <string>--prefix=slave</string>
         </array>

         <key>KeepAlive</key>
         <dict>
                 <key>SuccessfulExit</key>
                 <false/>
         </dict>

         <key>RunAtLoad</key>
         <true/>

</dict>
</plist>
```

```bash
sudo cp /sw/share/doc/buildbot-py26/contrib/os-x/net.sourceforge.buildbot.slave.plist /Library/LaunchDaemons/
```

{% hint style="warning" %}
You have to start your build slave via `launchd`, otherwise you will run into several problems. For further details, please refer to [Using Launchd](https://buildbot.net/trac/wiki/UsingLaunchd).
{% endhint %}

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
