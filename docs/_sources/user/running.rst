Running C-PAC
==============
Overview
--------

As with configuring the subject list, pipeline configuration, and group analysis files, execute a C-PAC run by using C-PAC's command line interface.

In addition to running C-PAC traditionally on your own local computer or on a server, there are three other avenues through which you can run C-PAC without going through the install process:

.. include:: /user/run/without_installing.rst

More details of these options are available below.

If you re-run C-PAC with an output directory containing a working directory (from the runtime flag ``--save-working-dir``), C-PAC will use that working directories contents in the re-run. If you try to re-run on an output directory with a saved working directory from a different version of C-PAC than the one that you're currently running, differences in the working directory could cause problems.

.. note::

    C-PAC migrated from Python 2 to Python 3 in v1.6.2 (see `release notes <rnotes>`_). If your working directory contains Python 2 pickles from an older version of C-PAC and you want to continue to use this working directory, run::

        cpac utils repickle /path/to/working_dir

    or::

         docker run -i --rm --user $(id -u):$(id -g) -v /path/to/working_dir:/working fcpindi/c-pac:latest /bids_dir /outputs cli -- utils repickle /working

    or::

         singularity run C-PAC_latest.sif /bids_dir /outputs cli -- utils repickle /path/to/working_dir

    before running C-PAC ≥ v1.6.2

.. seealso::

    :ref:`Common Issue: I'm re-running a pipeline, but I am receiving many crashes <working_dir_crashes>`

.. include:: /user/cpac.rst

On the AWS Cloud
----------------

The C-PAC team has released an Amazon Marketplace AMI, making it easier for researchers to use C-PAC in the cloud.  You can use the AMI to either launch a single machine for basic runs or create a high performance computing (HPC) cluster using Starcluster.  Clusters can be dynamically scaled up as your computational needs increase.  Detailed explanations of cloud computing and HPC are beyond the scope of this documentation, but we will define a few key terms before we start.  If these terms are familiar, you may skip them and proceed to later sections.

* **Amazon Machine Instance (AMI)** - A disk image of an operating system and any additional installed software that can be used to create a virtual machine.

* **Instance** - A single running virtual machine whose initial state is based on the AMI that it is launched from.  Instances can be classified as spot instances or on-demand instances.  On-demand instances are reliably created the moment they are requested for a fixed rate.  Spot instances are created based on whether or not a bid that you set is accepted by Amazon.  They can be significantly cheaper than on-demand instances, but are only created when Amazon accepts your bid.

* **Instance Type** - The hardware specification for a given instance. A list of the instance types made available by Amazon may be found `here <http://aws.amazon.com/ec2/instance-types>`__.

* **Terminated Instance** - An instance is considered terminated when its resources have been completely freed up for use by others in the Amazon cloud.  Any data on a terminated instance that is not relocated to persistent storage such as EBS (see below) will be completely discarded.  Instance termination is the virtual equivalent of throwing out a physical server.  When you have terminated an instance, you are no longer paying for it.  Note that by default, instances do not have persistent storage attached to them- you will need to configure persistent storage when you set up the instance.

* **Stopped Instance** - An instance is considered stopped when it is not active, but its resources are still available for future use whenever you choose to reactivate it.  Stopping an instance is the virtual equivalent of turning a computer off or putting it in hibernate mode.  When you stop an instance, you continue to pay for the storage associated with it (i.e., the main and other volumes attached to it), but not for the instance itself.  You should stop an instance when the analyses you are working on are not fully done and you would like to preserve the current state of a running instance.

* **Simple Storage Service (S3)** - A form of storage offered by Amazon.  S3 is not intended to be directly attached to instances since it lacks a filesystem, but it can be used to archive large datasets.  Amazon provides tools for uploading data to S3 'buckets' where it can be stored.  It is less costly than EBS.

* **Elastic Block Storage (EBS)** - A form of persistent storage offered by Amazon for use with instances.  When you have terminated an instance, items stored in an EBS volume can be accessed by any future instances that you start up.

* **EC2 Instance Store** - A form of temporary storage that comes included with some instance types.  Instance store volumes must be added manually before launching an instance, and all files stored on them will be lost when the instance is terminated.  The instance store is typically mounted at ``/mnt``.

Lastly, it would be important to review any terms related to :doc:`the Sun Grid Engine job scheduler <compute_config>`.

Creating AWS Access and Network Keys
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before you can create a single C-PAC machine or a C-PAC HPC cluster, you must first generate credentials that will allow you to log into any AWS instance that you create.  The following steps will walk you through the process of creating all the necessary credentials and encryption keys that you will need.

#. Go to http://aws.amazon.com/console/

#. Click the `Sign in to the AWS Console` button

#. Enter your e-mail address and password.  If you do not already have an account, enter your e-mail address, select `I am a new user.` and click the `Sign in` button.  Provide Amazon with the information (e-mail address, payment method) needed to create your account.

#. Amazon has different regions that it hosts its web services from (e.g. Oregon, Northern Virginia, Tokyo). In the upper right-hand corner there will be a region that you are logged into next to your user name. Change this to your preferred region.  The Marketplace AMI is available in all regions, although public AMIs (non-Marketplace AMIs shared from personal accounts) may not be.

#. Click on your name in the upper right corner and navigate to `Security Credentials`.  Accept the disclaimer that appears on the page.

#. Click on `Access Keys` and click on the blue `Create New Access Key` button.  Click `Download Key File` and move the resulting csv file to a safe and memorable location on your hard drive.

#. Click on the box in the upper left corner of AWS.  Click on `EC2`.  Click on `Key Pairs` in the left-hand column.

#. Click on the blue `Create Key Pair` button. Give your key an appropriate name and click on the blue `Create` button.  A .pem file will now save to disk.  Move this file to a safe and memorable location on your hard drive.

#. On your local drive, open a terminal and run the following command: ``chmod 400 /path/to/pem/file``

Starting a Single C-PAC Instance via the AWS Console
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now that you have generated the access keys and a pem file, you may launch a single instance via Amazon's web interface by following the steps below.  If you are planning on processing many subjects or obtaining computationally-intensive derivatives (such as network centrality), you should use Starcluster instead.

#. In the left-hand column under the `INSTANCES` header in the AWS console, click `Instances`. This is a dashboard of all instances you currently have running in the AWS cloud. Click the blue `Launch Instance` button.

#. On the left-hand side of the new page, click on the `Amazon Marketplace` tab and search `c-pac` in the search text box.

#. Click the blue `Select` button next to the C-PAC AMI.  Click the blue `Continue` button on the next screen.

#. Now choose the instance type that you would like to use.  Note that C-PAC requires at least 8 GB of RAM- the m3.xlarge instance type has 15 GB of RAM and 4 CPUs and functions well with C-PAC for small runs and experimentation.  This instance type is equivalent to a standard desktop machine in terms of processing power. To select this type, click on the `General purpose` tab and click the box next to `m3.xlarge`.  Then, click the `Next: Configure Instance Details` button.  Note that for most larger runs you will want to choose a more powerful instance type, such as c3.4xlarge or c3.8xlarge.

#. The details page can be used to request spot instances, as well as other functionality (including VPN, VPC options). For a basic run you do not need to change anything, although you can tailor it according to your future needs. Hovering over the 'i' icons on this page will give you more insight into the options available.  When done, click `Next: Add Storage.`

#. On the storage page, you can allocate space for the workstation, such as user and system directories.  This is where you can attach instance store volumes if your instance type comes with them.  To do this, click the `Add New Volume` button and select the instance store via the dropdown menu in the `Type` column.  You may need to do this multiple times if your instance comes with multiple instance stores.  If you want the files stored on the root volume to be kept after the instance is terminated, uncheck the box below the `Delete on Termination` column.  Note that persistent storage for the datasets can be allocated and attached as described in a later section. Click `Next: Tag Instance`.

#. On this page you can tag the instance with metadata (e.g., details related to the specific purpose for the instance).  Tags are key-value pairs, so any contextual data that can be encapsulated in this format can be saved. Click `Next: Configure Security Group`.

#. On this page, you can modify who has access to the instance. The AMI defaults allow remote access from anywhere. If you would like to customize security to allow only a certain set of IP addresses and users access to the instance, you can do so here. If you find that custom settings, such as using the `My IP` setting or specifying a range of IP addresses, do not work, consult with your institution's network administrator to make sure that you are entering settings correctly.  Click `Review and Launch` when you are done.

#. This final page summarizes the instance details you are about to launch. You might receive some warnings as a result of security or the instance type not being in the free tier.  These warnings can be ignored.

#. Click the `Launch` button. A dialogue box will ask you to choose a key pair for the instance. Every instance requires a key pair in order for you to securely log in and use it. Change the top drop down menu bar to `Choose an existing key pair` and select the key pair you created in the `Creating AWS Access and Network Keys` section in the other drop down menu.  Check the acknowledgement check box and click the blue `Launch Instances` button.

#. You can click the `View Instances` blue button on the lower right of the page after to watch your new instance start up in the instance console.

#. When the `Instance State` column reads `running` and the `Status Checks` column reads `2/2`, the instance should be active. Click on the row for the new instance.  In the bottom pane, take note of the values for the `Instance ID`, `Public DNS`, and `Availability zone` fields under the `Description` tab.

Attaching Persistent EBS Storage to an Instance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Once your instance is up and running, you can create a persistent storage volume for your data and results.  In the left-hand column under the `ELASTIC BLOCK STORE` header in the AWS console, click `Volumes`. This is a dashboard of all volumes that you currently have stored in EBS. Click the blue `Create Volume` button.

#. Change the size field in the proceeding dialogue to have enough space to encompass the amount of data you expect to store.  A single volume can be as small as 1 GB or as large as 16 TB.  Change the availability zone to match the zone from your instance's `Description` tab.

#. Click the checkbox next to the newly-created volume.  Click `Actions` followed by `Attach Volumes`.  Enter the `Instance ID` from the instance's `Description` tab in the `Instance` field.  The `Device` field should fill itself automatically and should be of the form `/dev/sdb` or similar.  Note the letter used after the `sd`.  Click the blue `Attach` button.

#. Execute the following command from the terminal to make it so that your instance can see the volume (replace the letter `b` at the end of `/dev/xvdb` with the letter from the previous step).

.. code-block:: console

    ssh -i /path/to/pem/file ubuntu@<Public Domain Name> 'sudo mkfs -t ext4 /dev/xvdb && sudo mount /dev/xvdb /media/ebs

To use this volume with future instances, you may attach it to the instance using the AWS console and then use this command:

.. code-block:: console

    ssh -i /path/to/pem/file ubuntu@<Public Domain Name> 'sudo mount /dev/xvdb /media/ebs'

Note that the creation of a persistent volume is heavily automated in Starcluster, so if you will be creating many different persistent volumes you should use Starcluster instead.

Accessing Your Instance
^^^^^^^^^^^^^^^^^^^^^^^

There are now two different means of accessing the instance.  Either through X2Go (a desktop GUI-based session) or through ssh (a command line session).

ssh
'''

#. Open a terminal and type ``ssh -i /path/to/pem/file ubuntu@<Public Domain Name>``.

#. Type `yes` when asked if you trust the source.

X2Go
''''

#. Install the X2Go client using the instructions `here <http://wiki.x2go.org/doku.php/doc:installation:x2goclient>`__.

#. Open X2go and create a new session.

#. For `Host:`, enter the Public DNS from earlier.

#. For `Login:` enter `ubuntu`.

#. `SSH port:` should be `22`.

#. For `Use RSA/DSA key for ssh connection:`, select the key you generated for the instance.

#. Select `LXDE` for `Session` and click `OK`.

When you are done, your session configuration should look similar to the following:

.. figure:: /_images/cloud_x2go.png

Note: If X2Go does not work on your computer, you can add the ``-X`` flag to the ssh command to enable X11 port forwarding (i.e., the ssh command would be ``ssh -X -i /path/to/pem/file ubuntu@<Public Domain Name>``).  X11 port forwarding is very slow compared to X2Go, however, so it is recommended that you troubleshoot X2Go further before turning to this option.

Uploading Data to Your Instance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To upload data to your newly-created AWS instance, you can run the following command on the computer containing your data:

.. code-block:: console

    scp -r -i /path/to/pem/key /path/to/data ubuntu@<Public Domain Name>:/path/to/server/directory

If you have configured persistent storage, you will want to ensure that `/path/to/server/directory` is pointing to the mount point for the persistent storage.  If you followed the instructions above or the instructions in the Starcluster section below, the mount point should be `/media/ebs`.

Starting a C-PAC HPC Cluster via Starcluster
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Starcluster is suggested for more sophisticated C-PAC runs.  Using Starcluster, you can parallelize your analyses by distributing subjects across multiple nodes in an HPC cluster.  The following section describes how to install and configure Starcluster to work with C-PAC, dynamically add nodes to your cluster and leverage C-PAC's grid functionality.

Installing Starcluster
''''''''''''''''''''''

If you have pip installed, Starcluster can be installed via:

.. code-block:: console

    pip install starcluster

Note that if you are using a \*nix-based OS and you are not using an environment such as Miniconda, you will need to run the above command with ``sudo``.

If you do not have pip installed, see the `Official Starcluster Installation Instructions <http://star.mit.edu/cluster/docs/latest/installation.html>`__ for alternative installation methods.

Installing the C-PAC Starcluster Plug-ins
'''''''''''''''''''''''''''''''''''''''''

The C-PAC Starcluster plug-ins configure the SGE environment that C-PAC uses and ensure that storage space is writable.  From the terminal, download the C-PAC Starcluster plug-ins and install them by running the following commands:

.. code-block:: console

    cd /tmp
    git clone https://github.com/FCP-INDI/CPAC_CLOUD
    cd CPAC_CLOUD/sc_plugins
    mv *.py ~/.starcluster/plugins

Creating and Editing Your Configuration File
''''''''''''''''''''''''''''''''''''''''''''

Now you will need to create a Starcluster configuration file so that Starcluster can use your keys and know which instance types you would like to use.  To begin, type ``starcluster help`` and select option 2.

Fill in the AWS access keys from the CVS file that you created in the `Creating AWS Access and Network Keys` section::

    [aws info]
    AWS_ACCESS_KEY_ID = <Your Acces Key>
    AWS_SECRET_ACCESS_KEY = <Your Secret Key>

You do not need to define the ``AWS_USER_ID`` field unless you want to create custom AMIs based off the C-PAC AMI.  The public C-PAC AMI is available in us-east-1, so you should not change the value of ``AWS_REGION_NAME``.

Point your key definition to the pem file you generated in the `Creating AWS Access and Network Keys` section::

    [key cpac_key]
    KEY_LOCATION=/path/to/pem/file

Find the image ID for the C-PAC AMI by logging into the AWS Console using your favorite web browser.  Make sure that you are in the `N. Virginia` region.  Navigate to the EC2 service click `Images` -> `AMIs`.  Then click `Owned by Me` in the upper left corner and switch it to `Public images`.  Search for 'CPAC'.  Select the version of C-PAC that you wish to use and look in the lower pane for the `AMI ID` field.

Add the following cluster definition to your configuration file::

    [cluster cpac_cluster]
    KEYNAME = cpac_key
    PLUGINS = cpac_sge, mnt_config
    CLUSTER_SIZE = 1
    CLUSTER_SHELL = bash
    NODE_IMAGE_ID = <Image ID>
    MASTER_INSTANCE_TYPE = t2.medium
    NODE_INSTANCE_TYPE = c3.8xlarge

You can customize this to have additional nodes or use different instance types as per your needs.  Note that you can always add nodes later using Starcluster from the command line.  If you wish to use spot instances rather than on-demand instances, then add the following line to the cluster definition::

    SPOT = <bidding_price>

Also add the following two plug-in definitions for the C-PAC Starcluster plug-ins::

    [plugin cpac_sge]
    setup_class = cpac_sge.PEInstaller
    pe_url = https://raw.githubusercontent.com/FCP-INDI/CPAC_CLOUD/master/mpi_smp.conf

    [plugin mnt_config]
    setup_class = mnt_perm.MntPermissions

Attaching Persistent Storage to Your Cluster
''''''''''''''''''''''''''''''''''''''''''''

By default, the cluster will have an EBS-backed root volume and, if available, an instance store volume mounted at ``/mnt``.  Neither of these volumes are persistent and they will be destroyed when the cluster terminates. A shared directory mounted at `/home` on the head node can be used across nodes. If you need more storage than what is available on the head node or if you want to keep your data after the cluster is terminated, you will need to create a new volume that can be attached to all nodes in the cluster.  To do so, begin by creating an EBS-backed volume:

.. code-block:: console

   starcluster createvolume --shutdown-volume-host <volume_size_in_gigabytes> <region> -I t2.micro -i <Image ID>

Type ``starcluster listvolumes`` and get the `volume-id` for the volume that you just created.  Open up your Starcluster configuration file and add the following volume definition::

    [volume cpac_volume]
    VOLUME_ID = <Volume ID>
    MOUNT_PATH = /media/ebs

Append the following line to your `cpac_cluster` definition::

    VOLUMES = cpac_volume

The `Starcluster documentation <http://star.mit.edu/cluster/docs/latest/manual/volumes.html>`__ explains how to perform other operations such as resizing and removing volumes.

Starting the C-PAC Head Node
'''''''''''''''''''''''''''''

To start up the head node on your C-PAC HPC cluster, use the following Starcluster command (with substitutions where necessary):

.. code-block:: console

    starcluster start -c cpac_cluster <cluster_name>

Adding Additional Nodes
'''''''''''''''''''''''

To add additional nodes to your C-PAC HPC cluster, use the following Starcluster command (with substitutions where necessary):

.. code-block:: console

    starcluster addnode -n <number_of_nodes_to_add> <cluster_name>

Accessing the Head Node
'''''''''''''''''''''''

If you wish to access the head node, type the following command:

.. code-block:: console

    starcluster sshmaster -X -u ubuntu <cluster_name>

If you only wish to access the command line interface, you may omit the `-X` flag:

.. code-block:: console

    starcluster sshmaster -u ubuntu <cluster_name>

You may also use the instructions for X2Go from the `Starting a Single C-PAC Instance via the AWS Console` section to access the head node via a graphical shell.  To do so, obtain the public DNS for the head node by typing ``starcluster listclusters``.  The public DNS will be in the last column of the row labeled `master`.

Using C-PAC to Submit an SGE Job
'''''''''''''''''''''''''''''''''

C-PAC performs the heavy lifting of creating an SGE job submission script and submitting it to the SGE job scheduler seamlessly.

**Via the shell:**

#. Open your pipeline configuration YAML file in your preferred text editor.
#. Change the ``runOnGrid`` field to a value of ``True``.
#. Make sure that the ``resourceManager`` field is set to ``SGE``.
#. Set the ``parallelEnvironment`` field to ``mpi_smp``.
#. Execute the following command to run your pipeline.

.. code-block:: console

    cpac_run.py /path/to/pipeline_config.yml /path/to/CPAC_subject_list.yml

Checking on SGE Jobs
'''''''''''''''''''''

Once you are done submitting the job, you can check its status by typing ``qstat``.  This command will produce output that looks similar to the following::

    job-ID  prior   name       user         state submit/start at     queue                          slots ja-task-ID
    -----------------------------------------------------------------------------------------------------------------
          1 0.55500 submit_201 ubuntu       r     06/05/2015 20:42:13 all.q@master                       1 1
          1 0.55500 submit_201 ubuntu       r     06/05/2015 20:42:13 all.q@node001                      1 2
          2 0.55500 submit_201 ubuntu       r     06/05/2015 20:42:58 all.q@node002                      1 1
          2 0.00000 submit_201 ubuntu       qw    06/05/2015 20:42:47                                    1 2

The `job-ID` is a number assigned to your job when it is submitted to the scheduler.  The `state` of the job can be represented by one of several values: `r` means that the job is running, `qw` means that the job is queued and waiting, and `E` means that an error has occurred. The `queue` column indicates on which nodes of your cluster the C-PAC job is being executed.

If an error has occurred on any of the nodes while your pipeline executes, you should check the `cluster_temp_files` directory that was created in the directory from which you ran C-PAC.  This will contain copies of the job submission scripts that C-PAC generated to start your job.  It will also contain files containing the standard out and error messages for a given job.  You should check these first to determine what may have caused the error.  If these files do not help you determine what may have caused the error, feel free to ask for :doc:`help </user/help>` on the C-PAC forum.

Terminating a Starcluster Instance
''''''''''''''''''''''''''''''''''

When you are done and have exited from your cluster, the following command will terminate the cluster:

.. code-block:: console

    starcluster terminate <cluster_name>

If you receive an error from Starcluster while trying to terminate the instance, the following command will force Starcluster to terminate your cluster:

.. code-block:: console

    starcluster terminate -f <cluster_name>

**Warning:** If you are not using persistent storage (see `Attaching Persistent Storage to Your Cluster`) then all of your data will be lost upon termination of the cluster.  You will need to copy your data to another drive if you wish to keep it.

Additional Links
^^^^^^^^^^^^^^^^

* `The StarCluster User Manual <http://star.mit.edu/cluster/docs/latest/manual/index.html>`__
* `Getting Started with AWS <http://docs.aws.amazon.com/gettingstarted/latest/awsgsg-intro/gsg-aws-intro.html>`__

With OpenNeuro
--------------------------
The `OpenNeuro <https://openneuro.org>`__ project is an initiative to provide easy access to public neuroimaging datasets and the ability to quickly run analysis pipelines on these datasets directly through a web interface. C-PAC is available as an app on OpenNeuro, and more information on running apps on the platform is available `here <https://openneuro.org/faq>`_.
