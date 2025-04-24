C-PAC versions
==============

See :doc:`Release Notes </user/rnotes>` for information about specific versions of C-PAC. The Docker Hub tags are like ``fcpindi/c-pac:release-${VERSION}${VARIANT}`` where ``${VERSION}`` is either a specific semantic version prefixed with a ``v`` or ``latest`` or ``nightly``, like |example version|

Variants
^^^^^^^^

Primary image
-------------

|latest-primary-badge| |nightly-badge|

Non-variant, primary image (no ``${VARIANT}`` or an empty string, e.g. |example version|)

Lite variant
------------

|latest-lite-badge| |nightly-lite-badge|

``-lite``, primary image without FreeSurfer for a smaller image for runs that don't need FreeSurfer (e.g., |example version|\ ``-lite``)

Stale variants
--------------

The following variants were version-matched to other pipelines years ago but have not been recently harmonized.

ABCD-HCP variant
****************

.. versionremoved:: 1.8.7.post1

.. image:: https://img.shields.io/badge/last_published_version-C--PAC_1.8.7_%7C_abcd--hcp--pipeline_0.1.4-yellow
   :target: https://hub.docker.com/layers/fcpindi/c-pac/release-v1.8.7-ABCD-HCP/images/sha256-859bd8b11c38f07f53c75c7d06543bc3f35aa7ec368bb2ac0d9362ba365fe90e

``-ABCD-HCP``, image with software dependencies version-matched to `ABCD-HCP BIDS fMRI Pipeline <https://github.com/DCAN-Labs/abcd-hcp-pipeline/blob/e480a8f99534f1b05f37bf44c64827384b69b383/Dockerfile>`_ version `0.1.4 <https://github.com/DCAN-Labs/abcd-hcp-pipeline/releases/tag/v0.1.4>`_ (e.g., ``release-v1.8.7-ABCD-HCP``)

fMRIPrep-LTS variant
********************

.. versionremoved:: 1.8.7.post1

.. image:: https://img.shields.io/badge/last_published_version-C--PAC_1.8.7_%7C_fMRIPrep--LTS_20.2.1-yellow
   :target: https://hub.docker.com/layers/fcpindi/c-pac/release-v1.8.7-fMRIPrep-LTS/images/sha256-cf30cb0643477f01067db9bd173f425f891644e0c0103cf754e1aa5e2b000938

``-fMRIPrep-LTS``, image with software dependencies version-matched to `fMRIPrep LTS <https://reproducibility.stanford.edu/fmriprep-lts#long-term-support-lts>`_ version `20.2.1 <https://github.com/nipreps/fmriprep/releases/tag/20.2.1>`_ (e.g., ``release-v1.8.7-fMRIPrep-LTS``)

.. |example version| replace:: |version as code|

.. |latest-primary-badge| image:: https://img.shields.io/badge/last_published_version-C--PAC_1.8.7.post1.dev3-green
   :target: https://hub.docker.com/layers/fcpindi/c-pac/release-v1.8.7.post1.dev3/images/sha256-7122e5cbeea5ac68a6f2e79584677ca7bf9cdebcf705536c2b93782074b925e7

.. |latest-lite-badge| image:: https://img.shields.io/badge/last_published_version-C--PAC_1.8.7.post1.dev3-green
   :target: https://hub.docker.com/layers/fcpindi/c-pac/release-v1.8.7.post1.dev3-lite/images/sha256-31ab0fcc90276e5751addee506907a62bcc628e75ce9ab87adee623b961b6a8e

.. |nightly-badge| image:: https://img.shields.io/badge/development_version-C--PAC_nightly-green
   :target: https://hub.docker.com/layers/fcpindi/c-pac/nightly/images/sha256-287cb872b7263e63bbf7770e3cc31b54890fde9af4fe5010f0a99e36fb1bfdf4
         
.. |nightly-lite-badge| image:: https://img.shields.io/badge/development_version-C--PAC_nightly-green
   :target: https://hub.docker.com/layers/fcpindi/c-pac/nightly-lite/images/sha256-dcf70cbe77b4166458b3d40bf9cab9e030b7ad24a06a1ee7e5ed335100f9cbcc
         