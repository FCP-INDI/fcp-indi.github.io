Continuous Integration
======================

Our continous integration flow relies on GitHub Actions, GitHub Container Registry, CircleCI and Docker Hub. GitHub Actions builds staging images based on changes to Dockerfiles and pushes those images to GitHub Container Registry. On each push, once staging images are built or determined to be up to date, GitHub Actions installs C-PAC into a development image for each variant (standard, lite, fMRIPrep-LTS, and ABCD-HCP). CircleCI runs tests in both Docker and Singularity for each of these images and generates a coverage report if all tests pass. On release, CircleCI also pushes production images to Docker Hub.

.. container:: svg-flowchart

    .. raw:: html
        :file: ../../_static/flowcharts/CI-flow.svg

    `Open image <../../_static/flowcharts/CI-flow.svg>`_

Contents
^^^^^^^^

.. toctree::
   :maxdepth: 2

   regression