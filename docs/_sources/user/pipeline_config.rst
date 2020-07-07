Setting Up A Pipeline Configuration
====================================
Overview
--------

This section explains how to create a new pipeline or edit an existing one. If you wish to use one of the pre-configured pipelines that come packaged with C-PAC, you can view the current available library of :doc:`pipelines here </preconfig>`.

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

.. include:: design_a_pipeline.rst

Using a Text Editor
-------------------
From terminal, you can quickly generate a default pipeline configuration YAML file template in the directory you are in::

   cpac utils pipe_config new_template

You can then edit the file as needed, or leave it as the default. If you want to run the analysis from terminal::

   cpac run --pipe_config {path to pipeline config} {path to data config}

Pipeline configuration files, like the data settings and data configuration files discussed in the :doc:`data configuration builder section </subject_list_config>`, are stored as YAML files.  Similarly, each of the parameters used by C-PAC to assemble your pipeline can be specified as key-value pairs, so a pipeline configuration YAML would have multiple lines of the form ``key: value`` like so::

    # Name for this pipeline configuration - useful for identification.
    pipelineName :  pipeline01


    # Directory where CPAC should store temporary and intermediate files.
    workingDirectory :  /home/runs/pipeline01/work


    # Directory where CPAC should write crash logs.
    crashLogDirectory :  /home/runs/pipeline01/crash


    # Directory where CPAC should place run logs.
    logDirectory :  /home/runs/pipeline01/log


    # Directory where CPAC should place processed data.
    outputDirectory :  /home/runs/pipeline01/output

An example of a pipeline configuration YAML file can be found `here <https://raw.githubusercontent.com/FCP-INDI/C-PAC/master/CPAC/resources/configs/pipeline_config_template.yml>`_.  Tables explaining the keys and their potential values can be found on the individual pages for each of the outputs C-PAC is capable of producing.  All pipeline configuration files should have the keys in the :doc:`Output Settings </output_config>` table defined.

Why a list?
'''''''''''
You may notice as you learn about the settings for various outputs that many of the values for C-PAC's configurable settings are stored in lists (i.e., multiple values are separated by commas and surrounded by square brackets).  Such lists containing 1s and 0s (for 'True' and 'False' respectively) allow you to toggle on multiple options at the same time, and branch a pipeline into two different analysis strategies. See the `developer documentation <http://fcp-indi.github.io/docs/developer/workflows/cpac_pipeline.html>`_ for more information about how lists are used in C-PAC.

Configurable Settings
------------------------------

.. raw:: html

    <div class="flowchart-container"><object data="../_static/flowcharts/pipeline-individual.svg" type="image/svg+xml"></object></div>

Data Management and Environment Settings
'''''''''''''''''''''''''''''''''''''''''

* :doc:`Computer Settings <compute_config>`
* :doc:`Output Settings <output_config>`

Pre- and post-processing
'''''''''''''''''''''''''

* :doc:`Anatomical Preprocessing </anat>`
* :doc:`Functional Preprocessing </func>`
* :doc:`Nuisance Corrections </nuisance>`
* :doc:`Time Series Extraction </tse>`
* :doc:`After Warp Settings </after_warp>`

Derivatives
'''''''''''

* :doc:`Seed-based Correlation Analysis (SCA) and Dual Regression </sca>` - Analyze the connectivity between brain regions.
* :doc:`Voxel-mirrored Homotopic Connectivity (VMHC) </vmhc>` - Investigate connectivity between hemispheres.
* :doc:`Amplitude of Low Frequency Fluctuations (ALFF) and fractional ALFF (fALFF) </alff>` - Measure the power of slow fluctuations in brain activity.
* :doc:`Regional Homogeneity (ReHo) </reho>` - Measure the similarity of activity patterns across neighboring voxels.
* :doc:`Network Centrality </centrality>` - Analyze the structure of functional networks.

