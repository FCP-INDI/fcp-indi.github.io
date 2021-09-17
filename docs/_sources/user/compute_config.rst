:orphan:

Computer Settings
-----------------
.. figure:: /_images/compute_gui.png

**Pipeline Name - [text]:** Name for this pipeline configuration - useful for identification.  *Note that including an individual participant's ID code in this will presently cause C-PAC to crash.*

#. **Maximum Memory Per Participant (GB) - [number]:**  The maximum amount of memory each participant's workflow can allocate. Use this to place an upper bound of memory usage. **Warning: 'Memory Per Participant' multiplied by 'Number of Participants to Run Simultaneously' must not be more than the total amount of RAM. Conversely, using too little RAM can impede the speed of a pipeline run. It is recommended that you set this to a value that when multiplied by 'Number of Participants to Run Simultaneously' is as much RAM you can safely allocate.**

#. **Maximum Cores Per Participant - [integer]:** Number of cores (on a single machine) or slots on a node (cluster/grid) per subject. Slots are cores on a cluster/grid node. 'Number of Cores Per Participant' multiplied by 'Number of Participants to Run Simultaneously' must not be greater than the total number of cores. Dedicating more than one core/CPU per participant will direct C-PAC to parallelize the motion correction and time series registration transform application steps, for a speed increase.

#. **Number of Participants to Run Simultaneously - [integer]:** This number depends on computing resources.

#. **Number of Cores for Anatomical Registration (ANTS) - [integer]:** This number depends on computing resources.

#. **FSL directory - [path]:** Full path to the FSL version to be used by CPAC. If you have specified an FSL path in your .bashrc file, this path will be set automatically.

#. **Run CPAC on a Cluster/Grid - [False, True]:** Select False if you intend to run CPAC on a single machine. If set to True, CPAC will attempt to submit jobs through the job scheduler / resource manager selected below.

#. **Resource Manager - [SGE, PBS, SLURM]:** Sun Grid Engine (SGE), Portable Batch System (PBS) or Slurm. Only applies if you are running on a grid or compute cluster.  See the section below entitled `SGE Configuration` for more information on how to set up SGE.

#. **SGE Parallel Environment - [text]:** SGE Parallel Environment to use when running CPAC. Only applies when you are running on a grid or compute cluster using SGE.  See the section below entitled `SGE Configuration` for more information on how to set up SGE.

#. **SGE Queue - [text]:** SGE Queue to use when running CPAC. Only applies when you are running on a grid or compute cluster using SGE.  See the section below entitled `SGE Configuration` for more information on how to set up SGE.

.. include:: /user/pipelines/without_gui.rst

.. literalinclude:: /references/default_pipeline.yml
   :language: YAML
   :lines: 10-11,81-136

Setting up SGE
"""""""""""""""

Preliminaries
^^^^^^^^^^^^^

Before you configure Sun Grid Engine so that it works with C-PAC, you should understand the following concepts:

* **Job Scheduler** - A program that can allocate computational resources in an HPC cluster to jobs based on availability and distribute jobs across nodes. C-PAC can use Sun Grid Engine (SGE) as its job scheduler (and SGE comes pre-configured with C-PAC's `cloud image <cloud>`).

* **Parallel Environment** - A specification for how SGE parallelizes work.  Parallel environments can have limits on the number of CPUs used, whitelists and blacklists that dictate who can use resources, and specific methods for balancing server load during distributed tasks.

* **The Job Queue** - A grouping of jobs that run at the same time.  The queue can be frozen, in which case all jobs that it contains will cease.

* **Head Node** - The primary node of an HPC cluster, to which all other nodes are connected.  The head node will run a job scheduler (such as Sun Grid Engine) to allocate jobs to the other nodes.

* **Worker Node** - A node in an HPC cluster to which tasks are delegated by the head node via a job scheduler.

* **Job Submission Script** - A shell script with a series of commands to be executed as part of the job.  Submission scripts may also include flags that activate functionality specific to the scheduler.

Configuring A Parallel Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The specifics of configuring a parallel environment in SGE more broadly are beyond the scope of this guide (see `Oracle's blog <https://blogs.oracle.com/templedf/entry/configuring_a_new_parallel_environment>`_ for a good primer).  Nevertheless, we will discuss how to configure an environment that is compatible with C-PAC.  To do this, we will first create a file named *mpi_smp.conf* that will appear as follows:

.. code-block:: console

    pe_name            mpi_smp
    slots              999
    user_lists         NONE
    xuser_lists        NONE
    start_proc_args    NONE
    stop_proc_args     NONE
    allocation_rule    $pe_slots
    control_slaves     TRUE
    job_is_first_task  FALSE
    urgency_slots      min
    accounting_summary TRUE

This configuration ensures that:

* All of the cores will be used (assuming your system has fewer than 999 cores; if you are lucky enough to have more than this, the maximum value for this field is 9999999).
* No users are whitelisted or blacklisted and no special hooks or cleanup tasks occur before or after a job.
* All job slots that a C-PAC job submission requests are on the same machine (this ensures that each unique subject's computations are taken care of by the same node and the cores allocated for one of C-PAC's steps are not distributed across different machines).
* SGE has full control over the jobs submitted (in terms of resource scheduling).
* The C-PAC run is not part of a parallel job that would require an awareness of which task was performed first (the subjects can be assigned to nodes in any order).
* An accounting record is written concerning how the job used resources.

To activate this parallel environment and tie it to a job queue named *all.q*, execute the following commands on your cluster's master node:

.. code-block:: console

    qconf -Ap /path/to/mpi_smp.conf
    qconf -mattr queue pe_list "mpi_smp" all.q

You would then set the SGE Parallel Environment to *mpi_smp* and the SGE queue to *all.q* in your pipeline configuration file before starting your C-PAC run.

Additional Links
""""""""""""""""

* `The Sun Grid Engine User Guide <http://www.csb.yale.edu/userguides/sysresource/batch/doc/UserGuide_6.1.pdf>`_
* `Starcluster's Sun Grid Engine Tutorial <http://star.mit.edu/cluster/docs/0.93.3/guides/sge.html>`_
* `Oracle's Parallel Environment Tutorial <https://blogs.oracle.com/templedf/entry/configuring_a_new_parallel_environment>`_
* `University of Tennessee Knoxville's Guide to Using SGE <https://newton.utk.edu/doc/Documentation/UsingTheGridEngine/>`_
