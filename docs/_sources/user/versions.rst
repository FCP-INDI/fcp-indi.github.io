C-PAC versions
==============

See :doc:`Release Notes </user/rnotes>` for information about specific versions of C-PAC. The Docker Hub tags are like ``fcpindi/c-pac:release-${VERSION}${VARIANT}`` where ``${VERSION}`` is either a specific semantic version prefixed with a ``v`` or ``latest`` or ``nightly``, like |example version|

Variants
^^^^^^^^

Primary image
-------------

Non-variant, primary image (no ``${VARIANT}`` or an empty string, e.g. |example version|)

Lite variant
------------

``-lite``, primary image without FreeSurfer for a smaller image for runs that don't need FreeSurfer (e.g., |example version|\ ``-lite``)

ABCD-HCP variant
----------------

``-ABCD-HCP``, image with software dependencies version-matched to `ABCD-HCP BIDS fMRI Pipeline <https://github.com/DCAN-Labs/abcd-hcp-pipeline/blob/e480a8f99534f1b05f37bf44c64827384b69b383/Dockerfile>`_ (e.g., |example version|\ ``-ABCD-HCP``)

fMRIPrep-LTS variant
--------------------

``-fMRIPrep-LTS``, image with software dependencies version-matched to `fMRIPrep LTS <https://reproducibility.stanford.edu/fmriprep-lts#long-term-support-lts>`_ (e.g., |example version|\ ``-fMRIPrep-LTS``)

.. |example version| replace:: ``release-``\ |version as code|
