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

.. |Docker Hub tags| replace:: fcpindi/c-pac Tags | Docker Hub

.. _Docker Hub tags: https://hub.docker.com/repository/docker/fcpindi/c-pac/tags

.. |semver| raw:: HTML

   <span title="semantic version">semver</span>
