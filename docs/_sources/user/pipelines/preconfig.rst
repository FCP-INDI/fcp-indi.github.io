Pre-configured Pipelines
========================

human
^^^^^

default: The Default Pipeline
-----------------------------

:doc:`Pipeline Configuration YAML </user/pipelines/default>`

.. note::
   
   C-PAC runs this pipeline by default, and it is not necessary to invoke the `--preconfig` flag to run it.

.. note::

   .. versionchanged:: 1.8.5 

      This pipeline was modified during the v1.8.5 release cycle. |see 1.8.5 rnotes| The previous default pipeline has been preserved as |default-deprecated|_

C-PAC is packaged with a default processing pipeline so that you can get your data preprocessing and analysis started immediately. Just pull the C-PAC Docker container and kick off the container with your data, and you're on your way.

The default processing pipeline performs fMRI processing using four strategies, with and without global signal regression, with and without bandpass filtering.

Anatomical processing begins with conforming the data to RPI orientation and removing orientation header information that will interfere with further processing. A non-linear transform between skull-on images and a 2mm MNI brain-only template are calculated using ANTs\ :footcite:`Avan08`. 

.. versionchanged:: 1.8.5

   Images are them skull-stripped using FSL's BET\ :footcite:`Smit02` (was using AFNI's 3dSkullStrip\ :footcite:`Cox96,cite-default-Cox97` prior to v1.8.5. |see 1.8.5 rnotes|) and subsequently segmented into WM, GM, and CSF using FSL's FAST tool\ :footcite:`Zhan01`.

The resulting WM mask was multiplied by a WM prior map that was transformed into individual space using the inverse of the linear transforms previously calculated during the ANTs procedure. A CSF mask was multiplied by a ventricle map derived from the Harvard-Oxford atlas distributed with FSL\ :footcite:`Smit04`. Skull-stripped images and grey matter tissue maps are written into MNI space at 2mm resolution.

Functional preprocessing begins with resampling the data to RPI orientation, and slice timing correction. Next, motion correction is performed using a two-stage approach in which the images are first coregistered to the mean fMRI and then a new mean is calculated and used as the target for a second coregistration (AFNI 3dvolreg\ :footcite:`Cox99`). A 7 degree of freedom linear transform between the mean fMRI and the structural image is calculated using FSL's implementation of boundary-based registration\ :footcite:`Zhan01`. Nuisance variable regression (NVR) is performed on motion corrected data using a 2nd order polynomial, a 24-regressor model of motion\ :footcite:`Fris96`, 5 nuisance signals, identified via principal components analysis of signals obtained from white matter (CompCor\ :footcite:`Behz07`), and mean CSF signal. WM and CSF signals were extracted using the previously described masks after transforming the fMRI data to match them in 2mm space using the inverse of the linear fMRI-sMRI transform. The NVR procedure is performed twice, with and without the inclusion of the global signal as a nuisance regressor. The residuals of the NVR procedure are processed with and without bandpass filtering (0.01Hz < f < 0.1Hz), written into MNI space at 3mm resolution and subsequently smoothed using a 6mm FWHM kernel.

Several different individual level analysis are performed on the fMRI data including:

* **Amplitude of low frequency fluctuations (alff)**\ :footcite:`Zang07`: the variance of each voxel is calculated after bandpass filtering in original space and subsequently written into MNI space at 2mm resolution and spatially smoothed using a 6mm FWHM kernel.
* **Fractional amplitude of low frequency fluctuations (falff)**\ :footcite:`Zou08`: Similar to alff except that the variance of the bandpassed signal is divided by the total variance (variance of non-bandpassed signal).
* **Regional homogeneity (ReHo)**\ :footcite:`Zang04`: a simultaneous Kendall rank correlation is calculated between each voxel's time course and the time courses of the 27 voxels that are face, edge, and corner touching the voxel. ReHo is calculated in original space and subsequently written into MNI space at 2mm resolution and spatially smoothed using a 6mm FWHM kernel.
* **Voxel mirrored homotopic connectivity (VMHC)**\ :footcite:`Star08`: an non-linear transform is calculated between the skull-on anatomical data and a symmetric brain template in 2mm space. Using this transform, processed fMRI data are written in to symmetric MNI space at 2mm and the correlation between each voxel and its analog in the contralateral hemisphere is calculated. The Fisher transform is applied to the resulting values, which are then spatially smoothed using a 6mm FWHM kernel.
* **Weighted and binarized degree centrality (DC)**\ :footcite:`Buck09`: fMRI data is written into MNI space at 2mm resolution and spatially smoothed using a 6mm FWHM kernel. The voxel x voxel similarity matrix is calculated by the correlation between every pair of voxel time courses and then thresholded so that only the top 5% of correlations remain. For each voxel, binarized DC is the number of connections that remain for the voxel after thresholding and weighted DC is the average correlation coefficient across the remaining connections.
* **Eigenvector centrality (EC)**\ :footcite:`Lohm10`: fMRI data is written into MNI space at 2mm resolution and spatially smoothed using a 6mm FWHM kernel. The voxel x voxel similarity matrix is calculated by the correlation between every pair of voxel time courses and then thresholded so that only the top 5% of correlations remain. Weighted EC is calculated from the eigenvector corresponding to the largest eigenvalue from an eigenvector decomposition of the resulting similarity. Binarized EC is the first eigenvector of the similarity matrix after setting the non-zero values in the resulting matrix are set to 1.
* **Local functional connectivity density (lFCD)**\ :footcite:`Toma10`: fMRI data is written into MNI space at 2mm resolution and spatially smoothed using a 6mm FWHM kernel. For each voxel, lFCD corresponds to the number of contiguous voxels that are correlated with the voxel above 0.6 (r>0.6). This is similar to degree centrality, except it only includes the voxels that are directly connected to the seed voxel.
* **10 intrinsic connectivity networks (ICNs) from dual regression**\ :footcite:`Beck09`: a template including 10 ICNs from a meta-analysis of resting state and task fMRI data\ :footcite:`Smit09` is spatially regressed against the processed fMRI data in MNI space. The resulting time courses are entered into a multiple regression with the voxel data in original space to calculate individual representations of the 10 ICNs. The resulting networks are written into MNI space at 2mm and then spatially smoothed using a 6mm FWHM kernel.
* **Seed correlation analysis (SCA)**: preprocessed fMRI data is to match template that includes 160 regions of interest defined from a meta-analysis of different task results\ :footcite:`Dose10`. A time series is calculated for each region from the mean of all intra-ROI voxel time series. A separate functional connectivity map is calculated per ROI by correlating its time course with the time courses of every other voxel in the brain. Resulting values are Fisher transformed, written into MNI space at 2mm resolution, and then spatially smoothed using a 6mm FWHM kernel.
* **Time series extraction**: similar the procedure used for time series analysis, the preprocessed functional data is written into MNI space at 2mm and then time series for the various atlases are extracted by averaging within region voxel time courses. This procedure was used to generate summary time series for the automated anatomic labelling atlas\ :footcite:`Tzou02`, Eickhoff-Zilles atlas\ :footcite:`Eick05`, Harvard-Oxford atlas\ :footcite:`Harv`, Talaraich and Tournoux atlas\ :footcite:`Lanc00`, 200 and 400 regions from the spatially constrained clustering voxel timeseries\ :footcite:`Crad12`, and 160 ROIs from a meta-analysis of task results\ :footcite:`Dose10`. Time series for 10 ICNs were extracted using spatial regression.

References
**********

.. footbibliography::

abcd-options
------------

:doc:`Pipeline Configuration YAML </user/pipelines/abcd-options>`

.. warning::

   :doc:`/user/known-issues/FCP-INDI/C-PAC/2104`

anat-only: Default with Anatomical Preprocessing Only
-----------------------------------------------------

:doc:`Pipeline Configuration YAML </user/pipelines/anat-only>`

Based on the preprocessing decisions of the default pipeline, this preconfiguration allows you to immediately kick off a run with only anatomical preprocessing selected. This includes:

* Brain extraction (via AFNI 3dSkullStrip)
* Tissue segmentation (via FSL FAST)
* Registration to template (via ANTs/ITK)

preproc: Default without Derivatives
------------------------------------

:doc:`Pipeline Configuration YAML </user/pipelines/preproc>`

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

fmriprep-options: fMRIPrep options Pipeline
-------------------------------------------

:doc:`Pipeline Configuration YAML </user/pipelines/fmriprep-options>`

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

:doc:`Pipeline Configuration YAML </user/pipelines/ndmg>`

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

:doc:`Pipeline Configuration YAML </user/pipelines/rbc-options>`

RBC-options pipeline was built and integrated in C-PAC based on the Reproducible Brain Charts initiative, which aims to aggregate and harmonize phenotypic and neuroimage data to delineate node mechanisms regarding developmental basis of psychopathology in youth and yield reproducible growth charts of brain development\ :footcite:`Hoff21`.

References
**********

.. footbibliography::

non-human primate
^^^^^^^^^^^^^^^^^

monkey: Default with Monkey Preprocessing 
-----------------------------------------

:doc:`Pipeline Configuration YAML </user/pipelines/monkey>`

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

:doc:`Pipeline Configuration YAML </user/pipelines/benchmark-ANTS>`

The benchmark pipeline has remained mostly unchanged since the project's inception, and is used at the end of each release cycle to ensure the results of C-PAC's key outputs have not changed. It is designed to test a wide range of pipeline options. This pipeline is based on registration-to-template using the ANTs/ITK toolset, as this decision impacts many other aspects of the pipeline further downstream.

benchmark-FNIRT: C-PAC Benchmark with FSL FNIRT Registration
------------------------------------------------------------

:doc:`Pipeline Configuration YAML </user/pipelines/benchmark-FNIRT>`

The benchmark pipeline has remained mostly unchanged since the project's inception, and is used at the end of each release cycle to ensure the results of C-PAC's key outputs have not changed. It is designed to test a wide range of pipeline options. This pipeline is based on registration-to-template using the FSL FLIRT & FNIRT, as this decision impacts many other aspects of the pipeline further downstream.

.. |default-deprecated| replace:: ``default-deprecated``

.. _default-deprecated: https://github.com/FCP-INDI/C-PAC/blob/main/CPAC/resources/configs/pipeline_config_default-deprecated.yml

.. |see 1.8.5 rnotes| replace:: See :doc:`/user/release_notes/v1.8.5` for details.