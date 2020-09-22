C-PAC Quickstart
================

.. include:: quick_overview.rst

.. _cpac-python-package:

.. include:: cpac.rst

For instructions to run in Docker or Singularity without installing cpac (Python package), see :doc:`All Run Options </user/running>`

Default Pipeline
----------------

C-PAC is packaged with a default processing pipeline so that you can get your data preprocessing and analysis started immediately. Just pull the C-PAC Docker container and kick off the container with your data, and you're on your way.

The default processing pipeline performs fMRI processing using four strategies, with and without global signal regression, with and without bandpass filtering.

Anatomical processing begins with conforming the data to RPI orientation and removing orientation header information that will interfere with further processing. A non-linear transform between skull-on images and a 2mm MNI brain-only template are calculated using ANTs [3]. Images are them skull-stripped using AFNI's 3dSkullStrip [5] and subsequently segmented into WM, GM, and CSF using FSL’s fast tool [6]. The resulting WM mask was multiplied by a WM prior map that was transformed into individual space using the inverse of the linear transforms previously calculated during the ANTs procedure. A CSF mask was multiplied by a ventricle map derived from the Harvard-Oxford atlas distributed with FSL [4]. Skull-stripped images and grey matter tissue maps are written into MNI space at 2mm resolution.

Functional preprocessing begins with resampling the data to RPI orientation, and slice timing correction. Next, motion correction is performed using a two-stage approach in which the images are first coregistered to the mean fMRI and then a new mean is calculated and used as the target for a second coregistration (AFNI 3dvolreg [2]). A 7 degree of freedom linear transform between the mean fMRI and the structural image is calculated using FSL’s implementation of boundary-based registration [7]. Nuisance variable regression (NVR) is performed on motion corrected data using a 2nd order polynomial, a 24-regressor model of motion [8], 5 nuisance signals, identified via principal components analysis of signals obtained from white matter (CompCor, [9]), and mean CSF signal. WM and CSF signals were extracted using the previously described masks after transforming the fMRI data to match them in 2mm space using the inverse of the linear fMRI-sMRI transform. The NVR procedure is performed twice, with and without the inclusion of the global signal as a nuisance regressor. The residuals of the NVR procedure are processed with and without bandpass filtering (0.001Hz < f < 0.1Hz), written into MNI space at 3mm resolution and subsequently smoothed using a 6mm FWHM kernel.

Several different individual level analysis are performed on the fMRI data including:

* **Amplitude of low frequency fluctuations (alff) [10]:** the variance of each voxel is calculated after bandpass filtering in original space and subsequently written into MNI space at 2mm resolution and spatially smoothed using a 6mm FWHM kernel.
* **Fractional amplitude of low frequency fluctuations (falff) [11]:** Similar to alff except that the variance of the bandpassed signal is divided by the total variance (variance of non-bandpassed signal.
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

Detailed information about the selection of pre-configured pipelines are :doc:`available here </user/preconfig>`.

.. include:: design_a_pipeline.rst

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

References
----------

1. Gorgolewski, K., Burns, C.D., Madison, C., Clark, D., Halchenko, Y.O., Waskom, M.L., Ghosh, S.S.: Nipype: A flexible, lightweight and extensible neuroimaging data processing framework in python. Front. Neuroinform. 5 (2011). doi:10.3389/fninf.2011.00013

2. Cox, R.W., Jesmanowicz, A.: Real-time 3d image registration for functional mri. Magn Reson Med 42(6), 1014–8 (1999)

3. Avants, B., Epstein, C., Grossman, M., Gee, J.: Symmetric diffeomorphic image registration with cross-correlation: Evaluating automated labeling of elderly and neurodegenerative brain. Medical Image Analysis 12(1), 26–41 (2008). doi:10.1016/j.media.2007.06.004

4. Smith, S.M., Jenkinson, M., Woolrich, M.W., Beckmann, C.F., Behrens, T.E.J., Johansen-Berg, H., Bannister, P.R., Luca, M.D., Drobnjak, I., Flitney, D.E., Niazy, R.K., Saunders, J., Vickers, J., Zhang, Y., Stefano, N.D., Brady, J.M., Matthews, P.M.: Advances in functional and structural mr image analysis and implementation as fsl. NeuroImage 23, 208–219 (2004). doi:10.1016/j.neuroimage.2004.07.051

5. Smith, S.M.: Fast robust automated brain extraction. Human Brain Mapping 17(3), 143–155 (2002). doi:10.1002/hbm.10062

6. Zhang, Y., Brady, M., Smith, S.: Segmentation of brain mr images through a hidden markov random field model and the expectation-maximization algorithm. IEEE Transactions on Medical Imaging 20(1), 45–57 (2001). doi:10.1109/42.906424

7. Greve, D.N., Fischl, B.: Accurate and robust brain image alignment using boundary-based registration. NeuroImage 48(1), 63–72 (2009). doi:10.1016/j.neuroimage.2009.06.060

8. Friston, K.J., Williams, S., Howard, R., Frackowiak, R.S., Turner, R.: Movement-related effects in fmri time-series. Magn Reson Med 35(3), 346–55 (1996)

9. Behzadi, Y., Restom, K., Liau, J., Liu, T.T.: A component based noise correction method (compcor) for bold and perfusion based fmri. NeuroImage 37(1), 90–101 (2007). doi:10.1016/j.neuroimage.2007.04.042

10. Zang, Y.-F., He, Y., Zhu, C.-Z., Cao, Q.-J., Sui, M.-Q., Liang, M., Tian, L.-X., et al. (2007). Altered baseline brain activity in children with ADHD revealed by resting-state functional MRI. Brain & development, 29(2), 83–91.

11. Zou, Q.-H., Zhu, C.-Z., Yang, Y., Zuo, X.-N., Long, X.-Y., Cao, Q.-J., Wang, Y.-F., et al. (2008). An improved approach to detection of amplitude of low-frequency fluctuation (ALFF) for resting-state fMRI: Fractional ALFF. Journal of neuroscience methods, 172(1), 137–141.

12. Zang, Y., Jiang, T., Lu, Y., He, Y., Tian, L., 2004. Regional homogeneity approach to fMRI data analysis. Neuroimage 22, 394-400.

13. Stark, D. E., Margulies, D. S., Shehzad, Z. E., Reiss, P., Kelly, A. M. C., Uddin, L. Q., Gee, D. G., et al. (2008). Regional variation in interhemispheric coordination of intrinsic hemodynamic fluctuations. The Journal of Neuroscience, 28(51), 13754–13764.

14. Buckner RL, Sepulcre J, Talukdar T, Krienen FM, Liu H, Hedden T, Andrews-Hanna JR, Sperling RA, Johnson KA. 2009. Cortical hubs revealed by intrinsic functional connectivity: mapping, assessment of stability, and relation to Alzheimer’s disease. J Neurosci. 29:1860–1873.

15. Lohmann G, Margulies DS, Horstmann A, Pleger B, Lepsien J, Goldhahn D, Schloegl H, Stumvoll M, Villringer A, Turner R. 2010. Eigenvector centrality mapping for analyzing connectivity patterns in fMRI data of the human brain. PLoS One. 5:e10232

16. Tomasi D, Volkow ND. 2010. Functional connectivity density mapping. PNAS. 107(21):9885-9890.

17. C.F. Beckmann, C.E. Mackay, N. Filippini, and S.M. Smith. Group comparison of resting-state FMRI data using multi-subject ICA and dual regression. OHBM, 2009.

18. Smith, S. M., Fox, P. T., Miller, K. L., Glahn, D. C., Fox, P. M., Mackay, C. E., et al. (2009). Correspondence of the brain’s functional architecture during activation and rest. Proceedings of the National Academy of Sciences of the United States of America, 106(31), 13040–13045. doi:10.1073/pnas.0905267106

19. Dosenbach, N. U. F., Nardos, B., Cohen, A. L., Fair, D. a, Power, J. D., Church, J. a, … Schlaggar, B. L. (2010). Prediction of individual brain maturity using fMRI. Science (New York, N.Y.), 329(5997), 1358–61. `http://doi.org/10.1126/science.1194144 <http://doi.org/10.1126/science.1194144>`_

20. Tzourio-Mazoyer, N., Landeau, B., Papathanassiou, D., Crivello, F., Etard, O., Delcroix, N., … Joliot, M. (2002). Automated anatomical labeling of activations in SPM using a macroscopic anatomical parcellation of the MNI MRI single-subject brain. NeuroImage, 15(1), 273–89. `http://doi.org/10.1006/nimg.2001.0978 <http://doi.org/10.1006/nimg.2001.0978>`_

21. Eickhoff, S. B., Stephan, K. E., Mohlberg, H., Grefkes, C., Fink, G. R., Amunts, K., & Zilles, K. (2005). A new SPM toolbox for combining probabilistic cytoarchitectonic maps and functional imaging data. NeuroImage, 25(4), 1325–35. `http://doi.org/10.1016/j.neuroimage.2004.12.034 <http://doi.org/10.1016/j.neuroimage.2004.12.034>`_

22. Harvard-Oxford cortical and subcortical structural atlases, `http://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Atlases <http://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Atlases>`_

23. Lancaster, J. L., Woldorff, M. G., Parsons, L. M., Liotti, M., Freitas, C. S., Rainey, L., … Fox, P. T. (2000). Automated Talairach atlas labels for functional brain mapping. Human Brain Mapping, 10(3), 120–31. Retrieved from `http://www.ncbi.nlm.nih.gov/pubmed/10912591 <http://www.ncbi.nlm.nih.gov/pubmed/10912591>`_

24. Craddock, R. C., James, G. A., Holtzheimer, P. E., Hu, X. P., & Mayberg, H. S. (2011). A whole brain fMRI atlas generated via spatially constrained spectral clustering. Human Brain Mapping, 0(July 2010). `http://doi.org/10.1002/hbm.21333 <http://doi.org/10.1002/hbm.21333>`_
