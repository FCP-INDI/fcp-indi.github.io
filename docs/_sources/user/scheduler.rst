Scheduling and Progress Tracking
================================

.. raw:: html

    <div class="flowchart-container"><object data="../_static/flowcharts/scheduler.svg" type="image/svg+xml"></object></div>

During pipeline execution, we want to monitor each node's execution. WebSocket (WS) allows the server to push information to the connected clients, essential in an asynchronous setup.

When starting a run with the ``--monitoring`` flag, the execution hangs until the WebSocket connects. This is preferred so no data is lost (i.e. C-PAC starts running before the WS connects).

If running the :ref:`cpac Python package <cpac-python-package>`, cpac will automatically find an available port on which to connect. If running a Docker container directly, you must expose any ports used for monitoring. The default WebSocket monitoring port is ``8080``.

For example, you can run

.. code-block:: BASH

  cpac run /path/to/BIDS_directory /path/to/outputs participant --monitoring

or

.. code-block:: BASH

  docker run \
    -it --rm -p 8080:8080 \
    -v /path/to/BIDS_directory:/bids_dir \
    -v /path/to/outputs:/outputs \
    fcpindi/c-pac:latest \
    /bids_dir /outputs participant \
    --monitoring

or

.. code-block:: BASH

  singularity run \
    -B /path/to/BIDS_directory:/bids_dir \
    -B /path/to/outputs:/outputs \
    fcpindi_c-pac.simg \
    /bids_dir /outputs participant \
    --monitoring

.. note::

  Singularity requires the ``--fakeroot`` option to use ``network-args.portmap``. If ``--fakeroot`` gives an error like

  .. code-block:: BASH

    ERROR  : Failed to create container namespaces

  .. include:: /user/help.rst
      :start-after: .. unprivileged_userns_clone_start
      :end-before: .. unprivileged_userns_clone_end

Once your container starts running, C-PAC should log some setup information and then pause on the message

.. code-block:: BASH

 [Waiting for monitoring websocket to connect]

One WebSocket monitoring tool is `WebSocat <https://github.com/vi/websocat#installation>`_. To use WebSocat to monitor, run

.. code-block:: BASH

 websocat ws://127.0.0.1:8080/log

(replacing ``8080`` with whatever port you're using) in a terminal. C-PAC will start running and WebSocat will display realtime monitoring messages.
