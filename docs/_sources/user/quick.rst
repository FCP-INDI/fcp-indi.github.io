C-PAC Quickstart
================

.. include:: quick_overview.rst

.. _cpac-python-package:

.. include:: cpac.rst

For instructions to run C-PAC in Docker or Singularity without installing cpac (Python package), see :doc:`All Run Options </user/running>`

.. include:: brainlife.io_app.rst

Default Pipeline
----------------

C-PAC is packaged with a default processing pipeline so that you can get your data preprocessing and analysis started immediately. Just pull the C-PAC Docker container and kick off the container with your data, and you're on your way.

The default processing pipeline performs fMRI processing using four strategies, with and without global signal regression, with and without bandpass filtering.

.. warning::

   :doc:`/user/known-issues/FCP-INDI/C-PAC/2152`

Anatomical processing begins with conforming the data to RPI orientation and removing orientation header information that will interfere with further processing. A non-linear transform between skull-on images and a 2mm MNI brain-only template are calculated using ANTs [3]. Images are them skull-stripped using AFNI's 3dSkullStrip [5] and subsequently segmented into WM, GM, and CSF using FSL’s fast tool [6]. The resulting WM mask was multiplied by a WM prior map that was transformed into individual space using the inverse of the linear transforms previously calculated during the ANTs procedure. A CSF mask was multiplied by a ventricle map derived from the Harvard-Oxford atlas distributed with FSL [4]. Skull-stripped images and grey matter tissue maps are written into MNI space at 2mm resolution.

Functional preprocessing begins with resampling the data to RPI orientation, and slice timing correction. Next, motion correction is performed using a two-stage approach in which the images are first coregistered to the mean fMRI and then a new mean is calculated and used as the target for a second coregistration (AFNI 3dvolreg [2]). A 7 degree of freedom linear transform between the mean fMRI and the structural image is calculated using FSL’s implementation of boundary-based registration [7]. Nuisance variable regression (NVR) is performed on motion corrected data using a 2nd order polynomial, a 24-regressor model of motion [8], 5 nuisance signals, identified via principal components analysis of signals obtained from white matter (CompCor, [9]), and mean CSF signal. WM and CSF signals were extracted using the previously described masks after transforming the fMRI data to match them in 2mm space using the inverse of the linear fMRI-sMRI transform. The NVR procedure is performed twice, with and without the inclusion of the global signal as a nuisance regressor. The residuals of the NVR procedure are processed with and without bandpass filtering (0.001Hz < f < 0.1Hz), written into MNI space at 3mm resolution and subsequently smoothed using a 6mm FWHM kernel.

.. warning::

   :doc:`/user/known-issues/FCP-INDI/C-PAC/2152`

Several different individual level analysis are performed on the fMRI data including:

* **Amplitude of low frequency fluctuations (alff) [10]:** the variance of each voxel is calculated after bandpass filtering in original space and subsequently written into MNI space at 2mm resolution and spatially smoothed using a 6mm FWHM kernel.
* **Fractional amplitude of low frequency fluctuations (falff) [11]:** Similar to alff except that the variance of the bandpassed signal is divided by the total variance (variance of non-bandpassed signal.
.. warning::

   :doc:`/user/known-issues/FCP-INDI/C-PAC/2152`
* **Regional homogeniety (ReHo) [12]:** a simultaneous Kendalls correlation is calculated between each voxel's time course and the time courses of the 27 voxels that are face, edge, and corner touching the voxel. ReHo is calculated in original space and subsequently written into MNI space at 2mm resolution and spatially smoothed using a 6mm FWHM kernel.
* **Voxel mirrored homotopic connectivity (VMHC) [13]:** an non-linear transform is calculated between the skull-on anatomical data and a symmetric brain template in 2mm space. Using this transform, processed fMRI data are written in to symmetric MNI space at 2mm and the correlation between each voxel and its analog in the contralateral hemisphere is calculated. The Fisher transform is applied to the resulting values, which are then spatially smoothed using a 6mm FWHM kernel.
* **Weighted and binarized degree centrality (DC) [14]:** fMRI data is written into MNI space at 2mm resolution and spatially smoothed using a 6mm FWHM kernel. The voxel x voxel similarity matrix is calculated by the correlation between every pair of voxel time courses and then thresholded so that only the top 5% of correlations remain. For each voxel, binarized DC is the number of connections that remain for the voxel after thresholding and weighted DC is the average correlation coefficient across the remaining connections.
* **Eigenvector centrality (EC) [15]:** fMRI data is written into MNI space at 2mm resolution and spatially smoothed using a 6mm FWHM kernel. The voxel x voxel similarity matrix is calculated by the correlation between every pair of voxel time courses and then thresholded so that only the top 5% of correlations remain. Weighted EC is calculated from the eigenvector corresponding to the largest eigenvalue from an eigenvector decomposition of the resulting similarity. Binarized EC, is the first eigenvector of the similarity matrix after setting the non-zero values in the resulting matrix are set to 1.
* **Local functional connectivity density (lFCD) [16]:** fMRI data is written into MNI space at 2mm resolution and spatially smoothed using a 6mm FWHM kernel. For each voxel, lFCD corresponds to the number of contiguous voxels that are correlated with the voxel above 0.6 (r>0.6). This is similar to degree centrality, except only voxels that it only includes the voxels that are directly connected to the seed voxel.
* **10 intrinsic connectivity networks (ICNs) from dual regression [17]:** a template including 10 ICNs from a meta-analysis of resting state and task fMRI data [18] is spatially regressed against the processed fMRI data in MNI space. The resulting time courses are entered into a multiple regression with the voxel data in original space to calculate individual representations of the 10 ICNs. The resulting networks are written into MNI space at 2mm and then spatially smoothed using a 6mm FWHM kernel.
* **Seed correlation analysis (SCA):** preprocessed fMRI data is to match template that includes 160 regions of interest defined from a meta-analysis of different task results [19]. A time series is calculated for each region from the mean of all intra-ROI voxel time series. A separate functional connectivity map is calculated per ROI by correlating its time course with the time courses of every other voxel in the brain. Resulting values are Fisher transformed, written into MNI space at 2mm resolution, and then spatial smoothed using a 6mm FWHM kernel.
* **Time series extraction:** similar the procedure used for time series analysis, the preprocessed functional data is written into MNI space at 2mm and then time series for the various atlases are extracted by averaging within region voxel time courses. This procedure was used to generate summary time series for the automated anatomic labelling atlas [20], Eickhoff-Zilles atlas [21], Harvard-Oxford atlas [22], Talaraich and Tournoux atlas [23], 200 and 400 regions from the spatially constrained clustering voxel timeseries [24], and 160 ROIs from a meta-analysis of task results [19]. Time series for 10 ICNs were extracted using spatial regression.

Pre-configured Pipelines
------------------------

In addition to the default pipeline, C-PAC comes packaged with a growing library of pre-configured pipelines that are ready to use. They can be invoked when running C-PAC using the ``--preconfig`` flag detailed above.

Detailed information about the selection of pre-configured pipelines are :doc:`available here </user/pipelines/preconfig>`.

.. include:: pipelines/design_a_pipeline.rst

Acknowledgments
---------------

We currently have a publication in preparation, in the meantime please cite our poster from INCF:

.. code-block:: console

	Craddock C, Sikka S, Cheung B, Khanuja R, Ghosh SS, Yan C, Li Q, Lurie D, Vogelstein J, Burns R, Colcombe S,
	Mennes M, Kelly C, Di Martino A, Castellanos FX and Milham M (2013). Towards Automated Analysis of Connectomes:
	The Configurable Pipeline for the Analysis of Connectomes (C-PAC). Front. Neuroinform. Conference Abstract:
	Neuroinformatics 2013. doi:10.3389/conf.fninf.2013.09.00042

	@ARTICLE{cpac2013,
	    AUTHOR={Craddock, Cameron  and  Sikka, Sharad  and  Cheung, Brian  and  Khanuja, Ranjeet  and  Ghosh, Satrajit S
	        and Yan, Chaogan  and  Li, Qingyang  and  Lurie, Daniel  and  Vogelstein, Joshua  and  Burns, Randal  and
	        Colcombe, Stanley  and  Mennes, Maarten  and  Kelly, Clare  and  Di Martino, Adriana  and  Castellanos,
	        Francisco Xavier  and  Milham, Michael},
	    TITLE={Towards Automated Analysis of Connectomes: The {Configurable Pipeline for the Analysis of Connectomes (C-PAC)}},
	    JOURNAL={Frontiers in Neuroinformatics},
	    YEAR={2013},
	    NUMBER={42},
	    URL={http://www.frontiersin.org/neuroinformatics/10.3389/conf.fninf.2013.09.00042/full},
	    DOI={10.3389/conf.fninf.2013.09.00042},
	    ISSN={1662-5196}
	}
