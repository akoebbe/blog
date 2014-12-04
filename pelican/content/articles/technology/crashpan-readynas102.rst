===============================================
Installing Crashplan headless on a ReadyNAS 102
===============================================

:date: 2014-06-29
:summary: Crashplan offers a great online backup solution. Netgear ReadyNAS offers a great home/small office local network storage solution. Here's a how-to on how to set your ReadyNAS as a Crashplan client.
:category: Technology


Crashplan offers a great online backup solution. Netgear ReadyNAS offers a great home/small office local network storage solution. Here's a how-to on how to set your ReadyNAS as a Crashplan client.

------------------------------------
Step 1: Turn on SSH on your ReadyNAS
------------------------------------
In the ReadyNAS admin head over to the "Settings" tab of the "System" section. Make sure that SSH is enabled. If you've never turned it on, you will receive a message basically stating "With great power comes great responsibility". If you're not comfortable with ssh and a linux command line, this may not be the solution for you.

----------------------------------------------
Step 2: Get Crashplan downloaded and installed
----------------------------------------------
Using your favorite ssh client, ssh to your ReadyNAS IP address as "root". The password will be the same as your web interface "admin" password.

Head over to Crashplan's `download page <http://www.code42.com/crashplan/thankyou/?os=linux>`__ and get the current download URL for the linux installer. You can copy the URL from the "restart the download" link on this page. At the time of this writing the current version URL was http://download.code42.com/installs/linux/install/CrashPlan/CrashPlan_3.6.3_Linux.tgz

Run the following command on the ReadyNAS using the current version download URL you found on teh download page.

.. code-block:: bash

    wget http://download.code42.com/installs/linux/install/CrashPlan/CrashPlan_3.6.3_Linux.tgz


Apparently the busybox cpio is not compatible with the Crashplan installer, so we'll need to uninstall the busybox version and install the proper version.

.. code-block:: bash

    apt-get remove busybox-cpio
    apt-get install cpio


We'll need to get a java runtime environment installed on the ReadyNAS since Crashplan is a java application. We'll also need a ARM based java library to use in place of the intel version bundled with Crashplan.

.. code-block:: bash

    apt-get install openjdk-6-jre-headless

Now you have the installer archive downloaded. It's time to decompress and run the installer. (Obviously replace the archive name with the one you downloaded)

.. code-block:: bash

    tar xvzf CrashPlan_3.6.3_Linux.tgz
    cd /CrashPlan-install
    ./install.sh


Answer the EULA and accept all of the defaults. You should get output similar to the following (EULA removed). ::

    Welcome to the CrashPlan Installer.

    Press enter to continue with installation.

    Validating environment...
      detected root permissions
    49036 blocks

    You must review and agree to the EULA before installation.

    Press enter to read the EULA.

    What directory do you wish to install CrashPlan to? [/usr/local/crashplan]

    What directory do you wish to link the CrashPlan executable to? [/usr/local/bin]

    What directory do you wish to store backups in? [/usr/local/var/crashplan]

    What directory contains your SYSV init scripts? [/etc/init.d]

    What directory contains your runlevel init links? [/etc/rc5.d]

    Your selections:
    CrashPlan will install to: /usr/local/crashplan
    And put links to binaries in: /usr/local/bin
    And store datas in: /usr/local/var/crashplan
    Your init.d dir is: /etc/init.d
    Your current runlevel directory is: /etc/rc5.d

    Is this correct? (y/n) [y] y

    Unpacking /./CrashPlan_3.6.3.cpi ...
    49036 blocks
    Starting CrashPlan Engine ... Using standard startup
    OK

    CrashPlan has been installed and the Service has been started automatically.

    Press Enter to complete installation.

    Important directories:
      Installation:
        /usr/local/crashplan
      Logs:
        /usr/local/crashplan/log
      Default archive location:
        /usr/local/var/crashplan

    Start Scripts:
      sudo /usr/local/crashplan/bin/CrashPlanEngine start|stop
      /usr/local/crashplan/bin/CrashPlanDesktop

    You can run the CrashPlan Desktop UI locally as your own user or connect
    a remote Desktop UI to this Service via port-forwarding and manage it
    remotely. Instructions for remote management are in the readme files
    placed in your installation directory:
      /usr/local/crashplan/doc


    To start the Desktop UI:
      /usr/local/bin/CrashPlanDesktop

    Installation is complete. Thank you for installing CrashPlan for Linux.


Now Crashplan comes with a libjtux.so that compiled for intel processors. That's not going to work on our ARM based ReadyNAS, so we'll need to replace it with a ARM based library.

`Download a precompiled version here <{filename}../../static/libjtux.so.gz>`_ and make a backup copy of /usr/local/crashplan/libjtux.so, then decompress the downloaded file and put it in place of the original. Firing up the Crashplan backup engine should now work without dieing.

.. code-block:: bash

    /usr/local/crashplan/bin/CrashPlanEngine start


So far so good. Now we need to configure the client.

------------------------------
Step 3: Headless configuration
------------------------------
Since you have to configure Crashplan via a GUI and the ReadyNAS is headless, we'll need to use a desktop app to attach to the client's backend. So here's the plan: we're going to point the desktop client to a non-standard port, then forward that point (via SSH forwarding) to the correct port on the ReadyNAS. In theory we'll only need to do this to get it set up and shouldn't need to connect to it this way again.

Let's change the port the desktop app is looking for the client backend. We'll need to modify a configuration file for this. Here are the locations for each OS. ::

    Linux (if installed as root): /usr/local/crashplan/conf/ui.properties
    Mac: /Applications/CrashPlan.app/Contents/Resources/Java/conf/ui.properties
    Windows: C:\Program Files\CrashPlan\conf\ui.properties​

In this file we should duplicate the servicePort line, uncomment one of them and set it to 4200... ::

    #servicePort=4243
    servicePort=4200

Now we need to forward our local 4200 port to the ReadyNas's port 4243. We can do this with SSH.

.. code-block:: bash

    ssh -L 4200:localhost:4243 root@[ReadyNAS IP]

Now fire up your desktop app and you should be greeted with the setup process.

--------------------------
Credit where credit is due
--------------------------

Here are the articles and threads I've had loaded in by browser as I was working through this. Some of the above is verbatim from some of these sites.

* http://forum.excito.net/viewtopic.php?f=9&t=3739
* http://www.jonrogers.co.uk/2012/05/crashplan-on-the-raspberry-pi/
* http://www.readynas.com/forum/viewtopic.php?f=4&t=60158

