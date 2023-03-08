Templates and Atlases
=====================

Templates and altases included in the C-PAC Docker and Singularity images are maintained in a separate repository: `FCP-INDI/C-PAC_templates <https://github.com/FCP-INDI/C-PAC_templates>`_ and packaged in a |staging image|_.

Adding a template or atlas to be packaged in C-PAC
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In a branch:

#. For the new file(s), fill in as much of the appropriate table(s) in |README.md|_ as you can. If no appropriate table exists in the ``README``, add one.
#. If you had add a new table to the ``README``, add a matching subdirectory under |atlases/label|_.
#. Rename your file(s) to begin with the "Atlas name" you used in the ``README`` table, and use BIDS standard template identifiers :cite:`cite-dev-templates-BIDS22VIIItemplateId` to identify the atlas/template's space if possible.
#. Add your file(s).

   * If your file(s) are available from a reliable source,

     #. If they're available in a reliable, web-accessible Docker image, `use that image as a staging image <https://docs.docker.com/develop/develop-images/multistage-build/>`_ and ``COPY`` the files directly from , e.g.

        .. code:: Dockerfile

          COPY --from=ghcr.io/fcp-indi/c-pac/neuroparc:v1.0-human /ndmg_atlases /ndmg_atlases

     #. If they're avilable in a GitHub repository,

        #. Clone into the ``GitHubPipelines`` staging image, `e.g. <https://github.com/FCP-INDI/C-PAC_templates/blob/9b33a4f1/.github/Dockerfiles/cpac_templates.Dockerfile#L6-L19>`_,

           .. literalinclude:: /references/cpac_templates.Dockerfile
              :language: Dockerfile
              :lines: 6,19

        #. Copy or move relevant files to a directory that does not contain any unnecessary files, `e.g. <https://github.com/FCP-INDI/C-PAC_templates/blob/9b33a4f1/.github/Dockerfiles/cpac_templates.Dockerfile#L7-L25>`_

           .. literalinclude:: /references/cpac_templates.Dockerfile
              :language: Dockerfile
              :lines: 7-18,20-25

   * Otherwise, your file(s) to the appropriate subdirectory of |atlases/label|_ in your branch.
#. If adding to a directory not already being copied from the ``GitHubPipelines`` staging image to the final templates image, add a ``COPY`` command to copy the files over, `e.g. <https://github.com/FCP-INDI/C-PAC_templates/blob/9b33a4f1/.github/Dockerfiles/cpac_templates.Dockerfile#L39-L40>`_,

   .. literalinclude:: /references/cpac_templates.Dockerfile
      :language: Dockerfile
      :lines: 39-40

If your template or atlas is in a different path
------------------------------------------------
If you're adding your template or atlas to the |staging image|_ in a location other than ``/cpac_templates/``, update both the `Bionic Beaver staging image <https://github.com/FCP-INDI/C-PAC/blob/6ab438f7/.github/Dockerfiles/Ubuntu.bionic-non-free.Dockerfile#L153-L156>`_ and the `Xenial Xerus staging image <https://github.com/FCP-INDI/C-PAC/blob/6ab438f752de1de764378ffc73a423cfa36c4b44/.github/Dockerfiles/Ubuntu.xenial-20200114.Dockerfile#L163-L166>`_ to ``COPY`` your files from the |staging image|_ to each Ubuntu staging image, e.g.,

   .. literalinclude:: /references/Ubuntu.bionic-non-free.Dockerfile
      :language: Dockerfile
      :lines: 153-156


Testing your updates
--------------------

You can use `.github/Dockerfiles/cpac_templates.Dockerfile <https://github.com/FCP-INDI/C-PAC_templates/blob/main/.github/Dockerfiles/cpac_templates.Dockerfile>`_ to build a custom |staging image|_, e.g.,

.. code:: BASH

   docker build -t cpac_templates:custom -f .github/Dockerfiles/cpac_templates.Dockerfile .  # <-- run in your modified fork or branch of FCP-INDI/C-PAC_templates
   docker run --rm -dit \
     --name=CPACTemplates \
     -v cpac_templates:/cpac_templates \
     ghcr.io/fcp-indi/c-pac_templates:latest  # <-- Start a daemon image with your custom templates
   docker run --rm -it \
     --volumes-from CPACTemplates \
     fcpindi/c-pac:nightly $BIDS_DIR $OUTPUTS_DIR participant  # <-- Use C-PAC as usual, but bind the custom /cpac_templates
   docker attach CPACTemplates  # <-- Clean up when you're done
   exit                         # <-- Clean up when you're done


.. note::

   When you use ``--volumes-from`` to bind a directory that already exists in the image, the container will only be able to see the content from the bound daemon container, not any of the files in the original image. You can bind specific files instead of their parent directories to make files from the bound daemon container available in an existing directory in a container.

Once your changes have been merged to |main|_, C-PAC will include them in each subsequent build.

References
^^^^^^^^^^

.. bibliography::
   :cited:
   :keyprefix: cite-dev-templates-

.. hyperlink formatting

.. |atlases/label| replace:: ``atlases/label``

.. _atlases/label: https://github.com/FCP-INDI/C-PAC_templates/tree/main/atlases/label

.. |main| replace:: ``main``

.. _main: https://github.com/FCP-INDI/C-PAC_templates/tree/main

.. |README.md| replace:: ``README.md``

.. _README.md: https://github.com/FCP-INDI/C-PAC_templates/blob/main/README.md

.. |staging image| replace:: ``c-pac_templates`` staging image

.. _staging image: https://github.com/FCP-INDI/C-PAC_templates/pkgs/container/c-pac_templates
