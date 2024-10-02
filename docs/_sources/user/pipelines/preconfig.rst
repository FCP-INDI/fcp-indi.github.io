Pre-configured Pipelines
========================

human
^^^^^

default: The Default Pipeline
-----------------------------

Pipeline Configuration YAML: `https://github.com/FCP-INDI/C-PAC/blob/main/CPAC/resources/configs/pipeline_config_default.yml <https://github.com/FCP-INDI/C-PAC/blob/main/CPAC/resources/configs/pipeline_config_default.yml>`_

.. note::
   
   C-PAC runs this pipeline by default, and it is not necessary to invoke the `--preconfig` flag to run it.

.. note::

   .. versionchanged:: 1.8.5 

      This pipeline was modified during the v1.8.5 release cycle. |see 1.8.5 rnotes| The previous default pipeline has been preserved as |default-deprecated|_

.. include:: /user/pipelines/desc/default.rst

abcd-options
------------

.. warning::

   :doc:`/user/known-issues/FCP-INDI/C-PAC/2104`

anat-only: Default with Anatomical Preprocessing Only
-----------------------------------------------------

Pipeline Configuration YAML: `https://github.com/FCP-INDI/C-PAC/blob/main/CPAC/resources/configs/pipeline_config_anat-only.yml <https://github.com/FCP-INDI/C-PAC/blob/main/CPAC/resources/configs/pipeline_config_anat-only.yml>`_

Based on the preprocessing decisions of the default pipeline, this preconfiguration allows you to immediately kick off a run with only anatomical preprocessing selected. This includes:

* Brain extraction (via AFNI 3dSkullStrip)
* Tissue segmentation (via FSL FAST)
* Registration to template (via ANTs/ITK)

preproc: Default without Derivatives
------------------------------------

Pipeline Configuration YAML: `https://github.com/FCP-INDI/C-PAC/blob/main/CPAC/resources/configs/pipeline_config_preproc.yml <https://github.com/FCP-INDI/C-PAC/blob/main/CPAC/resources/configs/pipeline_config_preproc.yml>`_

Based on the preprocessing decisions of the default pipeline, this preconfiguration allows you to preprocess all of your data, without launching into calculation of outputs and data derivatives. This includes:

Anatomical:

* Brain extraction (via AFNI 3dSkullStrip)
* Tissue segmentation (via FSL FAST)
* Registration to template (via ANTs/ITK)

Functional:

* Slice-timing correction
* Motion estimation & correction
* Co-registration to structural
* Nuisance correction & filtering
* Registration to template (via ANTs/ITK)

fmriprep-options: fmriprep-Options Pipeline
-------------------------------------------

Pipeline Configuration YAML: `https://github.com/FCP-INDI/C-PAC/blob/main/CPAC/resources/configs/pipeline_config_fmriprep-options.yml <https://github.com/FCP-INDI/C-PAC/blob/main/CPAC/resources/configs/pipeline_config_fmriprep-options.yml>`_

This pipeline is designed to increase reproducibility with the preprocessing results of the fmriprep pipeline package\ :footcite:`fMRI16` produced by the `Poldrack Lab at Stanford University <https://poldracklab.stanford.edu/>`_.

References
**********

.. bibliography::
   :list: bullet

   NiPr20
   Este19

.. footbibliography::

ndmg: Neurodata's 'ndmg-f' Pipeline
-----------------------------------

Pipeline Configuration YAML: `https://github.com/FCP-INDI/C-PAC/blob/main/CPAC/resources/configs/pipeline_config_ndmg.yml <https://github.com/FCP-INDI/C-PAC/blob/main/CPAC/resources/configs/pipeline_config_ndmg.yml>`_

This pipeline is the result of `Neurodata's <https://neurodata.io/>`_ study to converge upon the intersection of pipeline configuration decisions that maximizes discriminability between participants' data, drawing from the connectome graphs produced (labeled 'ndmg_graph' in the C-PAC output directory). This pipeline invokes a minimal set of preprocessing.

Note, the 'ndmg_graph' connectome graph outputs are always produced by C-PAC. This pipeline configuration simply replicates the preprocessing methods described in the paper, linked below.

References
**********

.. bibliography::
   :list: bullet
   :start: continue

   Kiar18
   Neur
   Neur18

rbc-options: ReproBrainChart Options Pipeline
---------------------------------------------

Pipeline Configuration YAML: `https://github.com/FCP-INDI/C-PAC/blob/main/CPAC/resources/configs/pipeline_config_rbc-options.yml <https://github.com/FCP-INDI/C-PAC/blob/main/CPAC/resources/configs/pipeline_config_rbc-options.yml>`_

RBC-options pipeline was built and integrated in C-PAC based on the Reproducible Brain Charts initiative, which aims to aggregate and harmonize phenotypic and neuroimage data to delineate node mechanisms regarding developmental basis of psychopathology in youth and yield reproducible growth charts of brain development\ :footcite:`Hoff21`.

References
**********

.. footbibliography::

non-human primate
^^^^^^^^^^^^^^^^^

monkey: Default with Monkey Preprocessing 
-----------------------------------------

Pipeline Configuration YAML: `https://github.com/FCP-INDI/C-PAC/blob/main/CPAC/resources/configs/pipeline_config_monkey.yml <https://github.com/FCP-INDI/C-PAC/blob/main/CPAC/resources/configs/pipeline_config_monkey.yml>`_

This pipeline is based on the work of Xu et al.\ :footcite:`Xu19` and nhp-ABCD-BIDS-pipeline.\ :footcite:`Stur20`

References
**********

.. bibliography::
   :list: bullet
   :start: continue

   Wang21a
   Rami20

.. footbibliography::

Based on the preprocessing decisions of the default pipeline, this preconfiguration allows you to preprocess all of your macaque data, includes:

Anatomical:

* Brain extraction (via U-Net)
* Tissue segmentation (via ANTs-prior based)
* Registration to template (via ANTs/ITK)

Functional:

* Despike
* Slice-timing correction
* Motion estimation & correction
* EPI N4 Bias Correction
* Brain Extraction (Anatomical-refined)
* Co-registration to structural
* Nuisance correction & filtering
* Registration to template (via ANTs/ITK)
* spatial smoothing

testing
^^^^^^^

benchmark-ANTS: C-PAC Benchmark with ANTs Registration
------------------------------------------------------

Pipeline Configuration YAML: `https://github.com/FCP-INDI/C-PAC/blob/main/CPAC/resources/configs/pipeline_config_benchmark-ANTS.yml <https://github.com/FCP-INDI/C-PAC/blob/main/CPAC/resources/configs/pipeline_config_benchmark-ANTS.yml>`_

The benchmark pipeline has remained mostly unchanged since the project's inception, and is used at the end of each release cycle to ensure the results of C-PAC's key outputs have not changed. It is designed to test a wide range of pipeline options. This pipeline is based on registration-to-template using the ANTs/ITK toolset, as this decision impacts many other aspects of the pipeline further downstream.

benchmark-FNIRT: C-PAC Benchmark with FSL FNIRT Registration
------------------------------------------------------------

Pipeline Configuration YAML: `https://github.com/FCP-INDI/C-PAC/blob/main/CPAC/resources/configs/pipeline_config_benchmark-FNIRT.yml <https://github.com/FCP-INDI/C-PAC/blob/main/CPAC/resources/configs/pipeline_config_benchmark-FNIRT.yml>`_

The benchmark pipeline has remained mostly unchanged since the project's inception, and is used at the end of each release cycle to ensure the results of C-PAC's key outputs have not changed. It is designed to test a wide range of pipeline options. This pipeline is based on registration-to-template using the FSL FLIRT & FNIRT, as this decision impacts many other aspects of the pipeline further downstream.

.. |default-deprecated| replace:: ``default-deprecated``

.. _default-deprecated: https://github.com/FCP-INDI/C-PAC/blob/main/CPAC/resources/configs/pipeline_config_default-deprecated.yml
