Setting Up A Pipeline Configuration
====================================
Overview
--------

This section explains how to create a new pipeline or edit an existing one. If you wish to use one of the pre-configured pipelines that come packaged with C-PAC, you can view the current available library of :doc:`pipelines here </user/pipelines/preconfig>`.

.. _ndmg_atlases:

.. topic:: Neuroparc v1.0: Baseline

  .. include:: /user/ndmg_atlases.rst

There are two ways of setting up or editing a pipeline configuration for C-PAC:

* Using the pipeline configuration interface in the C-PAC GUI
* Using a text editor (useful for remote servers where using the C-PAC GUI is not possible or impractical)

Definitions
'''''''''''
* Workflow
    .. include:: /glossary/workflow.rst
        :start-line: 3
* Pipeline
    .. include:: /glossary/pipeline.rst
        :start-line: 3
* Strategy
    .. include:: /glossary/strategy.rst
        :start-line: 3
* Derivative
    .. include:: /glossary/derivative.rst
        :start-line: 3
* Atlas
    .. include:: /glossary/atlas.rst
        :start-line: 3
* Template
    .. include:: /glossary/template.rst
        :start-line: 3

.. rubric:: Reference

.. bibliography:: /references/glossary.bib
   :style: cpac_docs_style
   :cited:
   :keyprefix: glossary-

.. include:: design_a_pipeline.rst

.. _using_a_text_editor:

Using a Text Editor
-------------------
If you want to base a pipeline on another pipeline configuration YAML file, you can specify

.. code:: YAML

   FROM: /path/to/pipeline.yml

in your pipeline configuration file. You can use the name of a :doc:`preconfigured pipeline </user/pipelines/preconfig>` instead of a filepath if you want to base a configuration file on a preconfigured pipeline. If ``FROM`` is not specified, the pipeline will be based on :doc:`the default pipeline </user/pipelines/default>`.

C-PAC will include all expected keys from the pipeline file specified in ``FROM`` (or the default pipeline if none is specified). Any keys specified in a pipeline configuration file will take precedence over the same key in the ``FROM`` base configuration, but all omitted keys will retain their values from the ``FROM`` base configuration.

From terminal, you can quickly generate a default pipeline configuration YAML file template in the directory you are in::

   cpac utils pipe_config new_template

You can then edit the file as needed. For values that you want to leave at the default, you can either leave the key as-is, or you can remove the key, and C-PAC will automatically use value from the default pipeline configuration (or from the pipeline specified in ``FROM``).

If you want to run the analysis from terminal::

   cpac run --pipe_config {path to pipeline config} {path to data config}

Pipeline configuration files, like the data settings and data configuration files discussed in the :doc:`data configuration builder section </user/subject_list_config>`, are stored as YAML files.  Similarly, each of the parameters used by C-PAC to assemble your pipeline can be specified as nested key-value pairs, so a pipeline configuration YAML would have multiple lines of the form ``key: value`` like so

.. literalinclude:: /references/default_pipeline.yml
   :language: YAML
   :lines: 10-51

An example of a pipeline configuration YAML file can be found :doc:`here </user/pipelines/default>`.  Tables explaining the keys and their potential values can be found on the individual pages for each of the outputs C-PAC is capable of producing. All pipeline setup configuration files should have the keys in the :doc:`Output Settings </user/output_config>` table defined.

String values can include the simplest form of `POSIX parameter expansion <https://pubs.opengroup.org/onlinepubs/009695399/utilities/xcu_chap02.html#tag_02_06_02>` (``${parameter}``). Two special variables are included for these types of parameters:

* ``resolution_for_anat`` will be populated with the value set in ``registration_workflows['anatomical_registration']['resolution_for_anat']``.

* ``func_resolution`` will

  * be populated with the value set in ``registration_workflows['functional_registration']['func_registration_to_template']['output_resolution']['func_preproc_outputs']`` if ``funcreg`` is in the value's key, 

  * be populated with the value set in ``registration_workflows['functional_registration']['func_registration_to_template']['output_resolution']['func_derivative_outputs']`` if ``deriv`` is in the value's key, or

  * raise an exception if neither ``funcreg`` nor ``deriv`` is in the value's key.

If ``FROM`` is defined (see above), any undefined keys will be inferred from the pipeline configuration specified; otherwise, any undefined keys will be inferred from the default pipeline.

Why a list?
'''''''''''
You may notice as you learn about the settings for various outputs that many of the values for C-PAC's configurable settings are stored in lists (i.e., multiple values are separated by commas and surrounded by square brackets).  Such lists containing ``On``s and ``Off``s (for ``True`` and ``False`` respectively) allow you to toggle on multiple options at the same time, and branch a pipeline into two different analysis strategies. See the `developer documentation <http://fcp-indi.github.io/docs/developer/workflows/cpac_pipeline.html>`_ for more information about how lists are used in C-PAC.

Configurable Settings
------------------------------

.. raw:: html

    <div class="flowchart-container"><object data="../_static/flowcharts/pipeline-individual.svg" type="image/svg+xml"></object></div>

Data Management and Environment Settings
'''''''''''''''''''''''''''''''''''''''''

* :doc:`Computer Settings </user/compute_config>`
* :doc:`Output Settings </user/output_config>`

Pre- and post-processing
'''''''''''''''''''''''''

* :doc:`Anatomical Preprocessing </user/anat>`
* :doc:`Functional Preprocessing </user/func>`
* :doc:`Nuisance Corrections </user/nuisance>`
* :doc:`Time Series Extraction </user/tse>`
* :doc:`After Warp Settings </user/after_warp>`

Derivatives
'''''''''''

* :doc:`Seed-based Correlation Analysis (SCA) and Dual Regression </user/sca>` - Analyze the connectivity between brain regions.
* :doc:`Voxel-mirrored Homotopic Connectivity (VMHC) </user/vmhc>` - Investigate connectivity between hemispheres.
* :doc:`Amplitude of Low Frequency Fluctuations (ALFF) and fractional ALFF (fALFF) </user/alff>` - Measure the power of slow fluctuations in brain activity.
* :doc:`Regional Homogeneity (ReHo) </user/reho>` - Measure the similarity of activity patterns across neighboring voxels.
* :doc:`Network Centrality </user/centrality>` - Analyze the structure of functional networks.
