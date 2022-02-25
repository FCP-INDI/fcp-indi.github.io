Logging
=======

Most C-PAC logging is handled by the built-in Python ``logging`` library. When logging, take care to choose an appropriate ``getLogger`` function or method. While :py:func:`CPAC.utils.monitoring.custom_logging.getLogger` and ``nipype.utils.logger.Logging.getLogger`` each fall back on ``logging.getLogger``,

.. raw:: html

    <div class="flowchart-container"><object data="../_static/flowcharts/getLogger.svg" type="image/svg+xml"></object></div>


each have their own intended use cases.

    Loggers are singletons that are never freed during a script execution, and so creating lots of loggers will use up memory which can’t then be freed.

    -- `Logging Cookbook: Creating a lot of loggers <https://docs.python.org/3/howto/logging-cookbook.html#creating-a-lot-of-loggers>`_

``CPAC.utils.monitoring.custom_logging.getLogger`` will look for a :py:class:`CPAC.utils.monitoring.custom_logging.MockLogger` before falling back on ``logging.getLogger``.

A ``CPAC.utils.monitoring.custom_logging.MockLogger`` can be used in place of a :py:class:`logging.Logger` and deleted from memory when no longer needed. For an example, see how ``missing_log`` is created and deleted in :py:func:`CPAC.pipeline.check_outputs.check_outputs`.

``nipype.utils.logger.Logging.getLogger`` will only consider loggers that are part of the class instance calling the method.

.. autofunction:: CPAC.utils.monitoring.custom_logging.getLogger

.. autoclass:: CPAC.utils.monitoring.custom_logging.MockLogger
   :special-members: __init__
   :members:
   :inherited-members:

.. automethod:: nipype.utils.logger.Logging.getLogger

.. automethod:: nipype.utils.logger.Logging.__init__

.. autofunction:: logging.getLogger
