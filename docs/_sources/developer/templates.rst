Templates and Atlases
=====================

Templates and altases included in the C-PAC Docker and Singularity images are maintained in a separate repository: `FCP-INDI/C-PAC_templates <https://github.com/FCP-INDI/C-PAC_templates>`_

Adding a template or atlas to be packaged in C-PAC
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In a branch:

#. For the new file(s), fill in as much of the appropriate table(s) in `README.md <https://github.com/FCP-INDI/C-PAC_templates/blob/main/README.md>`_ as you can. If no appropriate table exists in the README, add one.
#. Rename your file(s) to begin with the "Atlas name" you used in the README table, and use BIDS standard template identifiers :cite:`cite-dev-templates-BIDS22VIIItemplateId` to identify the atlas/template's space if possible
#. Add your file(s) to the appropriate subdirectory of `atlases/label <https://github.com/FCP-INDI/C-PAC_templates/tree/main/atlases/label>`_, adding a new subdirectory if you had to add a new table to the README.

Testing your updates
--------------------

You can use `.github/Dockerfiles/cpac_templates.Dockerfile <https://github.com/FCP-INDI/C-PAC_templates/blob/main/.github/Dockerfiles/cpac_templates.Dockerfile>`_ to build a custom ``cpac_templates`` staging image.

For example

.. code:: BASH
   
   docker build -t cpac_templates:custom -f .github/Dockerfiles/cpac_templates.Dockerfile .  # <-- run in your modified fork or branch of FCP-INDI/C-PAC_templates
   docker run --rm -dit --name=CPACTemplates -v cpac_templates:/cpac_templates ghcr.io/fcp-indi/c-pac_templates:latest  # <-- Start a daemon image with your custom templates
   docker run --rm -it -v --volumes-from CPACTemplates fcpindi/c-pac:nightly $BIDS_DIR $OUTPUTS_DIR participant  # <-- Use C-PAC as usual, but bind the custom /cpac_templates
   docker attach CPACTemplates  # <-- Clean up when you're done
   exit                         # <-- Clean up when you're done


Once your changes have been merged to ``main``, C-PAC will include them in each subsequent build.

.. rubric:: References

.. bibliography::
   :cited:
   :keyprefix: cite-dev-templates-
