.. _installation:

****************
Installing C-PAC
****************

.. _install_cpac:

Downloading C-PAC
=================

C-PAC is only supported as a container image. To get the latest version of C-PAC, use one of the following commands, depending on your containerization software:

Docker
^^^^^^

.. code:: BASH

   docker pull fcpindi/c-pac:latest

Apptainer / Singularity
^^^^^^^^^^^^^^^^^^^^^^^

.. code:: BASH

   singularity pull C-PAC_latest.sif docker://fcpindi/c-pac:latest

other versions
^^^^^^^^^^^^^^

For a development image of the next release (the latest build of |develop|_), simply replace ``latest`` with ``nightly``.

For branch-specific images, replace ``fcpindi/c-pac`` with ``ghcr.io/fcp-indi/c-pac`` and replace ``latest`` with the appropriate branch-specific tag. You can see the GitHub Actions-generated image tags at https://github.com/FCP-INDI/C-PAC/pkgs/container/c-pac or in the log of the relevent GitHub Actions "Build and test C-PAC job" under the heading "Set tag & Dockerfile".

.. |develop| replace:: ``develop``

.. _develop: https://github.com/FCP-INDI/C-PAC/tree/develop

Replacing C-PAC code in an already-built image
==============================================

If you have made changes to C-PAC that you would like to test without rebuilding the whole image, you can simply bind your code to your container when you launch to override the internal copy of C-PAC like

.. code:: BASH
  
   docker run --rm -it \
     -v ${LOCAL_CPAC_PATH}/CPAC:/code/CPAC \
     -v ${LOCAL_CPAC_PATH}/dev/docker_data/run.py:/code/run.py \
     -v ${LOCAL_CPAC_PATH}/dev/docker_data/run-with-freesurfer.sh:/code/run-with-freesurfer.sh \
     fcpindi/c-pac:latest \
     ${INPUT_BIDS_DIR} ${OUTPUT_DIR} participant

or

.. code:: BASH
  
   singularity run --cleanenv \
     -B ${LOCAL_CPAC_PATH}/CPAC:/code/CPAC \
     -B ${LOCAL_CPAC_PATH}/dev/docker_data/run.py:/code/run.py \
     -B ${LOCAL_CPAC_PATH}/dev/docker_data/run-with-freesurfer.sh:/code/run-with-freesurfer.sh \
     C-PAC_latest.sif \
     ${INPUT_BIDS_DIR} ${OUTPUT_DIR} participant

where ``${LOCAL_CPAC_PATH}`` is the path to the root of your clone of the C-PAC git repository. If you haven't made any changes to the entrypoint scripts (``run.py`` / ``run-with-freesurfer.sh``), then ``${LOCAL_CPAC_PATH}/CPAC:/code/CPAC`` is the only binding you need to replace the in-container C-PAC code with your local copy.

Building a new C-PAC image
==========================

The C-PAC build process makes use of Docker's multi-stage build functionality :footcite:`Mult23` to reduce iteration time. See https://github.com/FCP-INDI/C-PAC/tree/develop/.github for the latest Dockerfiles and GitHub Actions workflow configurations.

For each stage that you don't need to change, you can just pull that stage from GitHub Packages :footcite:`Work23`. If you need to build a stage, you can do so locally by running

.. code:: BASH

   cd ${LOCAL_CPAC_PATH}
   docker build \
     --platform linux/amd64 \
     -f .github/Dockerfiles/${STAGE_DOCKERFILE} \
     -t ghcr.io/fcpindi/c-pac/${STAGE}:${TAG} \
     .

To interactively develop a staging image Dockerfile, attach to a base image in a BASH session. For some staging images, BASH is not installed (e.g., images built ``FROM scratch``, so you may want to interact with a different image than what will ultimately be packaged. The base image in a Dockerfile is defined in the final ``FROM`` instruction. For example

.. code:: BASH

   docker run --rm -it \
     --entrypoint /bin/bash \
     ghcr.io/fcp-indi/c-pac/ubuntu:jammy-non-free

enters a C-PAC staging Ubuntu 22.04 image where you can test installation commands interactively before committing them in a Dockerfile.

References
==========

.. footbibliography::
