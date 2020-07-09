Setting Up A Pipeline Configuration
====================================
Overview
--------

There are two ways of setting up a pipeline configuration for C-PAC:

* Using the pipeline configuration interface in the C-PAC GUI
* Using a text editor (useful for remote servers where using the C-PAC GUI is not possible or impractical)

Definitions
'''''''''''
* Workflow - A workflow accomplishes a particular processing task (e.g. functional preprocessing, scrubbing, nuisance correction). Each workflow can be turned on or off in the pipeline configuration.  Sometimes a workflow can be set to both on and off, allowing for pipelines to branch.
* Pipeline - A pipeline is a combination of workflows.
* Strategy -  A strategy is a set of preprocessing options. Specifically, a strategy is defined by nuisance corrections and scrubbing settings. Strategies can branch depending on which of these workflows are turned on or off and how they are configured.  Their names are constructed by concatenating the following parameters:
    * Number of principle components calculated by CompCor (if enabled)
    * Nuisance corrections selected.
    * Scrubbing threshold (if enabled)

For instance, :file:`_compcor_ncomponents_5_linear1.motion1.compcor1.SCRUB_0.2` is a strategy with 5 principle components for compcor, linear drift, motion, and compcor corrections applied, and a scrubbing threshold of 0.2 mm.

* Derivative - Derivatives are the results of processing a participant's raw data (i.e., connectivity measures).

Using the GUI
-------------
If the C-PAC GUI is not open already, type the command ``cpac gui`` in a terminal window as you would with the subject list builder.  Then, on the main screen click on *New* next to *Pipelines*.

.. figure:: /_images/main_new_pipeconfig.png

For each of the settings in the lefthand pane, refer to the pages linked to below in the *Configurable Settings* section.

.. figure:: /_images/pipeconfig.png

When you have finished configuring your pipeline, click *Save*. You will be asked to specify a location to save a configuration file containing information about the pipeline, and to specify a name for the pipeline.

Using a Text Editor
-------------------
From terminal, you can quickly generate a default pipeline configuration YAML file template in the directory you are in::

   cpac utils pipe_config new_template

You can then edit the file as needed, or leave it as the default. If you want to run the analysis from terminal::

   cpac run --pipe_config {path to pipeline config} {path to data config}

Pipeline configuration files, like the data settings and data configuration files discussed in the :doc:`data configuration builder section </user/subject_list_config>`, are stored as YAML files.  Similarly, each of the parameters used by C-PAC to assemble your pipeline can be specified as key-value pairs, so a pipeline configuration YAML would have multiple lines of the form ``key: value`` like so::

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

An example of a pipeline configuration YAML file can be found `here <https://raw.githubusercontent.com/FCP-INDI/C-PAC/master/CPAC/resources/configs/pipeline_config_template.yml>`_.  Tables explaining the keys and their potential values can be found on the individual pages for each of the outputs C-PAC is capable of producing.  All pipeline configuration files should have the keys in the :doc:`Output Settings </user/output_config>` table defined.

Why a list?
'''''''''''
You may notice as you learn about the settings for various outputs that many of the values for C-PAC's configurable settings are stored in lists (i.e., multiple values are separated by commas and surrounded by square brackets).  Such lists containing 1s and 0s (for 'True' and 'False' respectively) allow you to toggle on multiple options at the same time, and branch a pipeline into two different analysis strategies. See the `developer documentation <http://fcp-indi.github.io/docs/developer/workflows/cpac_pipeline.html>`_ for more information about how lists are used in C-PAC.

Configurable Settings
------------------------------

Data Management and Environment Settings
'''''''''''''''''''''''''''''''''''''''''

* :doc:`Computer Settings <compute_config>`
* :doc:`Output Settings <output_config>`

Pre- and post-processing
''''''''''''''''''''''''

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

