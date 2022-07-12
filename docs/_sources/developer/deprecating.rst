Deprecating a version of C-PAC
==============================

In the rare occasion that a version of C-PAC needs to be deprecated, we add |CRITICAL_ALERT.rst| as a runtime warning and rename the deprecated image tag to ``${DEPRECATED_TAG}-DEPRECATED`` and replace the original tag for the deprecated image with an image that only displays |CRITICAL_ALERT.rst|_. For example, ``fcpindi/c-pac:release-v1.8.1-DEPRECATED`` is the tag that would be needed to run v1.8.1 after v1.8.1 was deprecated.

To semiautomatically deprecate a published version of C-PAC, follow these steps:

#. Write a ``CRITICAL ALERT`` (e.g., |CRITICAL ALERT 1.8.4|_) describing the need for the deprecation, the affected versions, and any recommendations. 
#. Include that ``CRITICAL ALERT`` in the GitHub release notes for new version (e.g., |1.8.4 release notes|_).
#. Use |CPAC-Development/deprecate|_ to deprecate the affected version images on Docker Hub. This process requires adequate permissions in the `fcp-indi organization on Docker Hub <https://hub.docker.com/orgs/fcpindi>`_ to ``docker push``.

   #. If you aren't already logged into Docker Hub, ``docker login``.

      In a local clone or copy of |CPAC-Development|_:

   #. Replace the critical alert in |CRITICAL_ALERT.rst|_ with the ``CRITICAL_ALERT`` from step one, above.
   #. Update |cpac_pipeline.py|_ and |run.py|_:
      #. Overwrite the current versions in the |CPAC-Development/deprecate|_ with the versions from the source code of the version of C-PAC to deprecate.
      #. Add

         .. code:: Python

            shutil.copyfile('/CRITICAL_ALERT.rst',
               os.path.join(log_dir, 'CRITICAL_ALERT.rst'))

         to |cpac_pipeline.py|_ after

         .. code:: Python

            if not os.path.exists(log_dir):
               os.makedirs(os.path.join(log_dir))

         (e.g., |cpac_pipeline.py example 1|_) and make sure ``shutil`` is imported before calling that library.

      #. Also in |cpac_pipeline.py|_, update the variable ``execution_info`` to include ``{critical_alert}`` at the end, like |cpac_pipeline.py example 2|_:

         .. code:: Python

            execution_info = """

               End of subject workflow {workflow}

               CPAC run complete:

                  Pipeline configuration: {pipeline}
                  Subject workflow: {workflow}
                  Elapsed run time (minutes): {elapsed}
                  Timing information saved in {log_dir}/cpac_individual_timing_{pipeline}.csv
                  System time of start:      {run_start}
                  System time of completion: {run_finish}

            {critical_alert}
            """

         .. note::

            There are probably at least two definitions of ``execution_info`` that need ``{critical_alert}`` appended to them (e.g., |cpac_pipeline.py example 3|_).

      #. Also in |cpac_pipeline.py|_, define ``critical_alert`` based on the |CRITICAL_ALERT.rst|_ file you already updated (e.g., |cpac_pipeline.py example 4|_):

         .. code:: Python

            with open('/CRITICAL_ALERT.rst', 'r') as critical_alert_file:
               critical_alert = '\n'.join([
                     f'    {line.rstrip()}' for line in critical_alert_file.readlines()])

      #. Also in |cpac_pipeline.py|_, update any calls to ``execution_info.format()`` to populate the string variable ``{critical_alert}`` with the ``critical_alert`` you defined above (e.g., |cpac_pipeline.py example 5|_):

         .. code:: Python

            logger.info(execution_info.format(
               workflow=workflow.name,
               pipeline=c.pipeline_setup['pipeline_name'],
               log_dir=c.pipeline_setup['log_directory']['path'],
               elapsed=(time.time() - pipeline_start_time) / 60,
               run_start=pipeline_start_datetime,
               run_finish=strftime("%Y-%m-%d %H:%M:%S"),
               critical_alert=critical_alert
            ))

      #. In |run.py|_, print the contents of |CRITICAL_ALERT.rst|_, e.g. |run.py example 1|_:

         .. code:: Python

            with open('/CRITICAL_ALERT.rst', 'r') as critical_alert_file:
               critical_alert = critical_alert_file.read()

            print(critical_alert)

   #. From the ``deprecate`` subdirectory, run
   
      .. code:: BASH

         ./build_and_deprecate ${DEPRECATED_TAG} ${RECOMMENDED_MINIMUM_VERSION}

      for each tag (as ``${DEPRECATED_TAG}``) that needs to be deprecated. This script will build the replacement images and push them to Docker Hub, overwriting the original image. See |Docker Hub tags|_ for all C-PAC tags currently published on Docker Hub. ``${RECOMMENDED_MINIMUM_VERSION}`` is the |semver| without any leading ``v``. For example

      .. code:: BASH

         for each TAG in "" -lite -ABCD-HCP -fMRIPrep-LTS
         do
           ./build_and_deprecate release-v1.8.1$TAG 1.8.4
         done

      to deprecate all variants of C-PAC v1.8.1 with recommended mimumum version v1.8.4.

      If the version to be deprecated is already deprecated but the critical alert needs to be updated, that can be done with the same syntax with ``./rebuild_and_deprecate`` (e.g., 
      
      .. code:: BASH

         ./rebuild_and_deprecate release-v1.8.1-lite 1.8.4

      to update the critical alert for ``release-v1.8.1-lite`` and ``release-v1.8.1-DEPRECATED``).

#. Add the critical alert to the release notes of each newly deprecated version, or update the critical alert if one already exists for that version (e.g., |1.8.1 release notes|_).
#. Trigger a rebuild of this documentation for the new version of C-PAC.

.. |1.8.1 release notes| replace:: ``C-PAC/releases/v.1.8.1`` "C-PAC Version 1.8.1 Beta"

.. _1.8.1 release notes: https://github.com/FCP-INDI/C-PAC/releases/tag/v1.8.1

.. |1.8.4 release notes| replace:: ``C-PAC/releases/v.1.8.4`` "C-PAC Version 1.8.4 Beta"

.. _1.8.4 release notes: https://github.com/FCP-INDI/C-PAC/releases/tag/v1.8.4

.. |CRITICAL ALERT 1.8.4| replace:: "Critical Alert for fMRIPrep-Options in C-PAC v1.8.1 - v1.8.3"

.. _CRITICAL ALERT 1.8.4: https://github.com/FCP-INDI/CPAC-Development/blob/028e792/deprecate/CRITICAL_ALERT.rst#critical-alert-for-fmriprep-options-in-c-pac-v181---v183

.. |CRITICAL_ALERT.rst| replace:: ``CRITICAL_ALERT.rst``

.. _CRITICAL_ALERT.rst: https://github.com/FCP-INDI/CPAC-Development/blob/main/deprecate/CRITICAL_ALERT.rst

.. |CPAC-Development| replace:: ``CPAC-Development``

.. _CPAC-Development: https://github.com/FCP-INDI/CPAC-Development

.. |CPAC-Development/deprecate| replace:: ``CPAC-Development/deprecate``

.. _CPAC-Development/deprecate: https://github.com/FCP-INDI/CPAC-Development/tree/028e7929188df99241e8eea78d20d0fd27dbe509/deprecate

.. |cpac_pipeline.py| replace:: ``cpac_pipeline.py``

.. _cpac_pipeline.py: https://github.com/FCP-INDI/CPAC-Development/blob/DEPRECATE/deprecate/cpac_pipeline.py

.. |cpac_pipeline.py example 1| replace:: ``cpac_pipeline.py#L264-L265@bc6081c``

.. _cpac_pipeline.py example 1: https://github.com/FCP-INDI/CPAC-Development/blob/bc6081c/deprecate/cpac_pipeline.py#L264-L265

.. |cpac_pipeline.py example 2| replace:: ``cpac_pipeline.py#L370@bc6081c``

.. _cpac_pipeline.py example 2: https://github.com/FCP-INDI/CPAC-Development/blob/bc6081c/deprecate/cpac_pipeline.py#L370

.. |cpac_pipeline.py example 3| replace:: ``cpac_pipeline.py#L705@bc6081c``

.. _cpac_pipeline.py example 3: https://github.com/FCP-INDI/CPAC-Development/blob/bc6081c/deprecate/cpac_pipeline.py#L705

.. |cpac_pipeline.py example 4| replace:: ``cpac_pipeline.py#L373-L375@bc6081c``

.. _cpac_pipeline.py example 4: https://github.com/FCP-INDI/CPAC-Development/blob/bc6081c/deprecate/cpac_pipeline.py#L373-L375

.. |cpac_pipeline.py example 5| replace:: ``cpac_pipeline.py#L722@bc6081c``

.. _cpac_pipeline.py example 5: https://github.com/FCP-INDI/CPAC-Development/blob/bc6081c/deprecate/cpac_pipeline.py#L722

.. |Docker Hub tags| replace:: fcpindi/c-pac Tags | Docker Hub

.. _Docker Hub tags: https://hub.docker.com/repository/docker/fcpindi/c-pac/tags

.. |run.py| replace:: ``run.py``

.. _run.py: https://github.com/FCP-INDI/CPAC-Development/blob/DEPRECATE/deprecate/run.py

.. |run.py example 1| replace:: ``run.py#L216-L219@bc6081c``

.. _run.py example 1: https://github.com/FCP-INDI/CPAC-Development/blob/bc6081c/deprecate/run.py#L216-L219

.. |semver| raw:: HTML

   <span title="semantic version">semver</span>
