Dashboard
=========

The C-PAC dashboard allows users to schedule and run C-PAC through a graphical interface in a browser.

To launch a local dashboard, run « Details about how to access dashboard »

Technical details
=================
The implementation relies heavily on the ``asyncio`` API, to simplify concurrency. However, it is not a parallel API, meaning that everything is executed in the same thread (and there is no race condition) and the different tasks that are being executed concurrently *must not* block the asyncio execution (e.g. it can have an asyncio.sleep in a task, or an IO function).

We have 6 main parts on this implementation: Scheduler, Backend, Shedule (and its children), Message, Result, and the API.

Beginning with the Schedule. Schedule is a abstraction of the task that should be executed. For C-PAC, we have three tasks:

* DataSettings: A task to generate data configs from a provided data settings;
* DataConfig: A task to schedule a pipeline for the subjects from a data config, spawning new tasks for each participant;
* ParticipantPipeline: A task to execute a pipeline for a single subject.

More technical aspects, such as running containers, are handled by a specialization of the Schedule class: BackendSchedule. The BackendSchedules are specific to a Backend, an interface between Python & the softwares of a specific backend (e.g. Singularity binaries). The Backend must contain the parameters required for the BackendSchedules to properly communicate with the underlying softwares, such as the Docker image to be used or the SSH connection to access a SLURM cluster.

The Scheduler is the central part of this implementation, and maybe the most simple. It stores the Schedules into a tree-like structure. Schedules can spawn new Schedules and manage the Messages received by each Schedule, together with the callbacks associated to a Schedule Message type. When a Schedule is scheduled, the Scheduler will send the Schedule to its Backend, and the Backend will specialize this "naïve" Schedule into a BackendSchedule for that Backend:

.. code-block:: Python

  ParticipantPipelineSchedule + DockerBackend = DockerParticipantPipelineSchedule

This "backend-aware" Schedule (from the superclass BackendSchedule) will then be executed by the Scheduler. The BackendSchedule behave as a Python generator, so the Scheduler simply iterates this object, and the items of this iteration are defined as Messages. The Messages are data classes (i.e. only store data, not methods), to give information for the Scheduler about the execution. The Messages are relayed to Scheduler watchers, which are external agents that provide a callback function for the Scheduler to call when it receives a specific type of Message. For the Spawn Message, the Scheduler schedules a new Schedule, with the parameters contained in the Spawn message.

Specifics of the Docker and Singularity containers are actually the same: they share the same base code for container execution, only differing in the container creation.

When the container is created, three tasks run concurrently for this Schedule: container status, log listener, and file listener. The first yields Messages of type Status, as a ping, so we know the container is running fine. The second connects to the WebSocket (WS) server running in the container, to capture which nodes it has run so far, and yield Messages of type Log. The last one looks in the output directory for logs and crashes, storing the files as Results in the Schedule, and yielding Messages of type Result.
Only the ParticipantPipeline has the second and the third, the others have just the container status Messages.

For SLURM, it starts connecting to the cluster via SSH. It uses the SSH multiplexing connection feature, so the authentication process happens only once, which is a good idea for connections that has a multi-factor authentication layer. After connecting to a cluster, the Backend allocates nodes to execute the Schedules and install a Miniconda & cpac. By using the  cpac.api module, the local cpac communicates with the node cpac via HTTP & <span title="WebSocket">WS<span> to run the Schedules. It uses the same API to gather the results and keep the local Schedule state updated. By default, the Singularity Backend is used by the node cpac to run the Schedules.

The Results are basically files in which it would be too much to transfer via <span title="WebSocket">WS<span>. The API to gather the Results allow to slice the content using HTTP headers (``Content-Range``). It is essential for results that will be incremented during the execution (i.e. logs). Using slice, one does not need to request for the whole file again, but only the part it does not have.
