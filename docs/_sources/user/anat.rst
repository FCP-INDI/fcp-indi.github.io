Anatomical Preprocessing
------------------------

.. raw:: html

    <div class="flowchart-container"><object data="../_static/flowcharts/anatomical.svg" type="image/svg+xml"></object></div>

Surface Analysis
^^^^^^^^^^^^^^^^

Surface analysis runs FreeSurfer recon-all and generates CSF, WM, GM masks, pial surface mesh, smoothed surface mesh, spherical surface mesh, white matter surface mesh, sulcal depth surface maps, cortical thickness surface maps and cortical volume surface maps.

Configuring CPAC to run surface analysis:
"""""""""""""""""""""""""""""""""""""""""

.. figure:: /_images/anat_surface.png

#. **FreeSurfer - [On,Off]:** FreeSurfer recon-all. Default is Off.

.. include:: /user/pipelines/without_gui.rst

.. literalinclude:: /references/default_pipeline.yml
   :language: YAML
   :lines: 152-159

Initial Preprocessing
^^^^^^^^^^^^^^^^^^^^^

Initial preprocessing offers methods like `ACPC Alignment <https://doi.org/10.1016/j.neuroimage.2013.04.127>`_ , `non-local means filtering <https://www.iro.umontreal.ca/~mignotte/IFT6150/Articles/Buades-NonLocal.pdf>`_ and `N4 bias field correction <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3071855/>`_ to preprocess anatomical images.

C-PAC provides options for configuring initial preprocessing - users can select:

* `ACPC Alignment <https://github.com/Washington-University/HCPpipelines/blob/master/PreFreeSurfer/scripts/ACPCAlignment.sh>`_
* `ANT's DenoiseImage <https://manpages.debian.org/experimental/ants/DenoiseImage.1.en.html>`_
* `ANT's N4BiasFieldCorrection <http://manpages.ubuntu.com/manpages/trusty/man1/N4BiasFieldCorrection.1.html>`_


Configuring CPAC to run initial preprocessing:
""""""""""""""""""""""""""""""""""""""""""""""

.. figure:: /_images/anat_init_options.png

#. **ACPC Alignment - [On,Off]:** Anterior Commissure - Posterior Comissure (ACPC) alignment. Default is Off. If choose 'on', clicking on the setting icon will bring up a dialog where you can set ACPC alignment parameters.

#. **Non-Local Means Filtering - [On,Off]:** ANTs DenoiseImage. Default is Off.

#. **N4 Bias Field Correction - [On,Off]:** ANTs N4BiasFieldCorrection - a variant of the popular N3 (nonparametric nonuniform normalization) retrospective bias correction algorithm. Default is Off.

.. include:: /user/pipelines/without_gui.rst

.. literalinclude:: /references/default_pipeline.yml
   :language: YAML
   :lines: 197-209

Configuring ACPC Alignment options:
""""""""""""""""""""""""""""""""""""""
**Note:** These options are pre-set for ACPC Alignment's default values. These do not need to be modified unless you are looking to optimize the results of ACPC alignment for your particular dataset.

.. figure:: /_images/acpc_gui.png

#. **ACPC Brain Size - [150]:** ACPC size of brain in z-dimension in mm. Default: 150mm for human data, 70mm for macaque data.
#. **ACPC Aligned Skull Template - [path]:** Skull template to be used for ACPC alignment. It is not necessary to change this path unless you intend to use a non-standard template.
#. **ACPC Aligned Brain Template - [path]:** Brain template to be used for ACPC alignment. For human data, it can be 'None'. It is not necessary to change this path unless you intend to use a non-standard template.

.. include:: /user/pipelines/without_gui.rst

.. literalinclude:: /references/default_pipeline.yml
   :language: YAML
   :lines: 197-198,207-226

Skull-Stripping
^^^^^^^^^^^^^^^
Skull-stripping is the removal of skull and other non-brain tissue like dura and eyes from anatomical images, which could otherwise complicate co-registration and normalization steps.

C-PAC provides options for configuring skull-stripping - users can select:

* AFNI: `3dSkullStrip <https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dSkullStrip.html>`_
* FSL: `BET <https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/BET/UserGuide>`_. Further parameters for each of these tools are configurable.
* niworkflows-ants: `niworkflows's antsBrainExtraction <https://github.com/poldracklab/niworkflows/blob/master/niworkflows/anat/ants.py>`_
* U-Net: U-Net is a Fully Convolutional Network (FCN) for image segmentation. Users can now select this option for brain extraction, especially optimal for non-human primate data.
* Providing their own brain mask for extraction

Configuring CPAC to run Skull-Stripping:
""""""""""""""""""""""""""""""""""""""""

**NOTE:** If providing your own brain mask for extraction, you can leave the following options at default. The skull-stripping tools will not run if a brain mask is found in the data configuration file.

.. figure:: /_images/skullstrip_gui.png

#. **Already skull-stripped - [On,Off]:** If inputs are already skull stripped (i.e. the structural input data is brain-only) then you can toggle this option to off.

#. **Which tool for skull-stripping - [FSL, AFNI, niworkflows-ants]:** Choose if you’d like to use FSL BET, AFNI 3dSkullStrip, or run all options in parallel.

.. include:: /user/pipelines/without_gui.rst

.. literalinclude:: /references/default_pipeline.yml
   :language: YAML
   :lines: 197-198,228-232

Configuring AFNI 3dSkullStrip options:
""""""""""""""""""""""""""""""""""""""
**Note:** These options are pre-set for AFNI 3dSkullStrip's default values. These do not need to be modified unless you are looking to optimize the results of skull-stripping for your particular dataset.

.. figure:: /_images/afni_gui.png

#. **Shrink factor - [0.6]:** Set the threshold value for controlling the brain vs non-brain voxels

#. **Vary shrink factor - [On,Off]:** Vary the shrink factor at every iteration of the algorithm. This prevents the likelihood of surface getting stuck in large pools of CSF before reaching the outer surface of the brain. Default is On.

#. **Shrink factor bottom limit - [0.4]:** The shrink factor bottom limit sets the lower threshold when varying the shrink factor. Default is 0.4, for when edge detection is used (which is On by default),otherwise the default value is 0.4.

#. **Avoid ventricles - [On,Off]:** Avoid ventricles while skull stripping. Default is On.

#. **Number of iterations - [250]:** Set the number of iterations. Default is 250. The number of iterations should depend upon the density of your mesh. Default is 250.

#. **Pushout - [On, Off]:** While expanding, consider the voxels above and not only the voxels below. Default is On.

#. **Touchup - [On,Off]:** Perform touchup operations at the end to include areas not covered by surface expansion.

#. **Fill hole option - [10]:** Give the maximum number of pixels on either side of the hole that can be filled. The default is 10 only if ’Touchup’ is On. Otherwise default is 0.

#. **NN smooth - [72]:** Perform final surface smoothing after all iterations. Default is 20.

#. **Avoid eyes - [On,Off]:** Avoid eyes while skull stripping. Default is On.

#. **Use edge - [On,Off]:** Use edge detection to reduce leakage into meninges. Default is On.

#. **Fractional expansion - [0.1]:** Speed of expansion. Default Value is 0.1

#. **Push to edge - [Off,On]:** Perform aggressive push to edge, this might cause leakage. Default is Off.

#. **Use Skull - [Off, On]:** Use the outer skull to limit expansion of surface into the skull in case of very strong shading artifacts. Use this only if you leakage into the skull.

#. **Perc_init - [0]:** Percentage of segments allowed to intersect surface.It is typically a number between 0 and 0.1, but can include negative values (which implies no testing for intersection). Default is 0.

#. **Max_inter_iter - [4]:** Number of iterations to remove intersection problems. With each iteration, the program automatically increases the amount of smoothing to get rid of intersections. Default is 4.

#. **Fac - [1]:** Multiply input dataset by FAC if range of values is too small. Default value is 1.

#. **blur_fwhm - [2]:** Blur datasets after spatial normalization. Default value is 2.

.. include:: /user/pipelines/without_gui.rst

.. literalinclude:: /references/default_pipeline.yml
   :language: YAML
   :lines: 197-198,228-229,234-298

Configuring FSL BET options:
""""""""""""""""""""""""""""
**Note:** These options are pre-set for FSL BET's default values. These do not need to be modified unless you are looking to optimize the results of skull-stripping for your particular dataset.

.. figure:: /_images/bet_gui.png

#. **Threshold - [0.5]:** Set the threshold value controlling the brain vs non-brain voxels. Default is 0.5

#. **Radius - [0]:** Integer value of head radius. Default is 0.

#. **Vertical gradient - [Off,On]:** Vertical gradient un fractional intensity threshold. Within the range of (-1,1).

#. **Apply threshold - [Off,On]:** Apply thresholding to segmented brain image and mask. Default is Off.

#. **Mask - [Off, On]:** Mask created along with skull stripping. Default option is On.

#. **Mesh - [Off, On]:** Mesh created along with skull stripping. Default is Off.

#. **Skull - [Off,On]:** Create a Skull Image. Default is Off.

#. **Surfaces - [Off, On]:** Get additional skull and scalp surfaces by running bet2 and betsurf. This is mutually exclusive with reduce bias, robust, padding, remove_eyes.

#. **Surfaces outline - [Off, On]:** Create a surface outline image, Default is Off.

#. **Padding - [Off, On]:** Add padding to the end of the image, improving BET. Mutually exclusive functional, reduce_bias, robust, padding, remove_eyes, surfaces.

#. **Reduce bias - [Off, On]:** Reduce bias and cleanup neck. Mutually exclusive with functional, reduce_bias, robust, padding, remove_eyes, surfaces.

#. **Remove eyes - [Off,On]:** Eyes and optic nerve cleanup. Mutually exclusive with functional, reduce_bias, robust, padding, remove_eyes, surfaces.

#. **Robust brain center - [Off, On]:** Robust brain center estimation. Mutually exclusive with functional, reduce_bias, robust, padding, remove_eyes, surfaces.

.. include:: /user/pipelines/without_gui.rst

.. literalinclude:: /references/default_pipeline.yml
   :language: YAML
   :lines: 197-198,228-229,300-339

Configuring niworkflows-ants options:
"""""""""""""""""""""""""""""""""""""
**Note:** These templates are used during niworkflows-ants skull stripping. e.g. OASIS template can be downloaded `here <https://s3-eu-west-1.amazonaws.com/pfigshare-u-files/3133832/Oasis.zip>`_.

.. figure:: /_images/niworkflows-ants_gui.png

#. **niworkflows_ants_template_path:** Set the brain extraction template . e.g. OASIStemplate/T_template0_BrainCerebellumProbabilityMask.nii.gz

#. **niworkflows_ants_mask_path:** Set the brain extraction probability mask. e.g. OASIStemplate/T_template0_BrainCerebellumProbabilityMask.nii.gz

#. **niworkflows_ants_regmask_path:** Set the brain extraction registration mask, used for registration to limit the metric computation to a specific region. e.g. OASIStemplate/T_template0_BrainCerebellumRegistrationMask.nii.gz

.. include:: /user/pipelines/without_gui.rst

.. literalinclude:: /references/default_pipeline.yml
   :language: YAML
   :lines: 197-198,228-229,346-358

Anatomical Registration
^^^^^^^^^^^^^^^^^^^^^^^
In order to compare brain activations between subjects, individual functional and anatomical images must first be transformed to match a common template. The most commonly used template (`MNI152 <http://www.bic.mni.mcgill.ca/ServicesAtlases/ICBM152NLin2009>`_) is maintained by the Montreal Neurological Institute, and is created by combining data from the brains of many different individuals to create an "average" brain. The image below shows how an individual brain is warped to match the shape of the template.

.. figure:: /_images/registration.png

C-PAC provides the option of either using FSL (`FLIRT <http://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FLIRT>`_ and `FNIRT <http://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FNIRT>`_) or `Advanced Normalization Tools (ANTS) <http://stnava.github.io/ANTs/>`_ to register images. Although the use of ANTS requires an extra step during the C-PAC install process, we have found its results to be significantly better than those produced by FSL (a conclusion supported by a `recent systematic analysis by Klein et al. <https://www.ncbi.nlm.nih.gov/pubmed/20123029>`_).

During registration, individual anatomical images are first transformed to match the common template. Then, the functional data for each subject is registered to their own transformed anatomical image. Finally, functional derivative files are transformed to the common template. For more detail on how C-PAC computes these steps, please see the `Registration Page of the developer documentation <http://fcp-indi.github.io/docs/developer/workflows/registration.html>`_.

By default, C-PAC will register subject brains to the MNI152 template included with FSL. Users wishing to register their data to a different template (such as a group specific template) can specify alternative template files.

Configuring CPAC to Run Anatomical Registration
"""""""""""""""""""""""""""""""""""""""""""""""
.. figure:: /_images/anat_reg_gui.png

#. **Anatomical Template Resolution - [1 An integer indicating three same dimensions (e.g., 1mm, 2mm, 3mm, 4mm); 2 A float number indicating three same dimensions (e.g., 3.5mm etc.); 3 Three numbers connected by 'x' indicating three different dimensions (e.g., 2.67mmx2.67mmx3mm etc.)]:** The resolution to which anatomical images should be transformed during registration. This is the resolution at which processed anatomical files will be output.

#. **Anatomical Template (Brain Only) - [path]:** Template to be used during registration. It is not necessary to change this path unless you intend to use a non-standard template.

#. **Anatomical Template (With Skull) - [path]:** Template to be used during registration. It is not necessary to change this path unless you intend to use a non-standard template.

#. **Anatomical to Template Registration Method - [ANTS, FSL, ANTS & FSL]:** Registration method(s) to be used. Options are `ANTS <http://stnava.github.io/ANTs/>`_, `FSL <http://fsl.fmrib.ox.ac.uk/fslcourse/lectures/practicals/reg/>`_, or both.

#. **ANTS skull-on transform - [Off, On]:** Register skull-on anatomical image to template. Calculating the transform with skull-stripped images is reported to be better, but it requires very high-quality skull-stripping. If skull-stripping is imprecise, registration with skull is preferred. Note: This option only affects ANTS due to the fact that FNIRT already uses skull-on images for calculating warps.

#. **Interpolation Method - [Linear, BSpline, LanczosWindowedSinc]:** Interpolation method for writing out transformed anatomical images. ANTS registration tools only. Options are Linear, BSpline, or LanczosWindowedSinc.

#. **ANTs Registration Parameters :** Clicking on the setting icon will bring up a dialog where you can set 'antsRegistration' parameters. 

#. **FNIRT Configuration - [path]:** Configuration file specifying settings used during registration. Required if FSL is selected as the registration method. This file can be found in the :file:`/etc/flirtsch` directory of your FSL install.

#. **FNIRT Reference Mask - [path]:** A reference mask to be used by FNIRT.

#. **Perform linear registration only - [Off, On]:** Whether or not perform only FLIRT.

#. **Interpolation Method - [trilinear, sinc, spline]:** Interpolation method for writing out transformed anatomical images. FSL registration tools only. Options are trilinear, sinc, or spline.

.. include:: /user/pipelines/without_gui.rst

.. literalinclude:: /references/default_pipeline.yml
   :language: YAML
   :lines: 482-600

Anatomical Tissue Segmentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

    <div class="flowchart-container"><object data="../_static/flowcharts/segmentation.svg" type="image/svg+xml"></object></div>

C-PAC uses `FSL/FAST <http://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FAST>`_ to automatically segment brain images into white matter, gray matter, and CSF. This is done using probability maps that contain information about the likelihood that a given voxel will be of a particular tissue type. Users specify a probability threshold such that voxels meeting a minimum probability of being a particular tissue will be classified as such. This results in masks containing voxels of only a single tissue type.

.. figure:: /_images/segmentation.png

The default tissue probability maps (referred to as Prior Probability Maps) used during segmentation are based on information from a large number of brains, and are based on the priors distributed with FSL and are included in the "Image Resource Files" package downloaded during installation. Also, CPAC has thresholding and erosion options for anatomical segmentation to further refine the resulting segmentation tissue masks. Threshold value and erosion proportion can be changeable by user. The erosion implementation is adapted from `fmriprep <https://fmriprep.readthedocs.io/en/stable/>`_.

For more detail on how CPAC computes these steps, please see the `Segmentation Page of the developer documentation <http://fcp-indi.github.io/docs/developer/workflows/seg_preproc.html>`_.

Thresholding options have returned, and new erosion options for anatomical segmentation have been introduced. The erosion implementation was adapted from fmriprep.

If you would like to use different priors, they must first be binarized such that for each voxel the probability for each tissue type is set to either 0% or 100%.

The following bash script will binarize existing priors::

    # Define what kind of priors to generate (gray, white, or csf)
    tissue=gray

    # Define threshold to use when binarizing data
    threshold=0.5

    # Copy existing priors (in this example, from FSL)
    3dcopy $FSL_DIR/data/standard/tissuepriors/avg152T1_${tissue}.hdr avg152T1_${tissue}.nii.gz

    # Binarize image using threshold set above
    fslmaths avg152T1_${tissue}.nii.gz -thr $threshold -bin avg152T1_${tissue}_2mm_bin

In addition, C-PAC offers template-based segmentation options that facilitate nonhuman data processing. Optimal for use with functional-only pipelines commonly used for rodent data, users can now employ a template-based tissue segmentation approach that applies inverse registration transforms to template-space tissue priors.

C-PAC offers ANTs prior-based tissue segmentation, which is optimal for non-human primate segmentations. Users could provide atlas and atlas segmentation images to perform ANTs Prior-based Segmentation.

Configuring CPAC to Run Anatomical Tissue Segmentation
""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. figure:: /_images/seg_gui_1.png

#. **Tissue Segmentation - [On, Off]:** Automatically segment anatomical images into white matter, gray matter, and CSF based on prior probability maps.

#. **Use Priors - [On, Off]:** Whether or not to use template-space tissue priors to refine the binary tissue masks generated by segmentation.

#. **White Matter Prior Probability Map - [path]:** Full path to a binarized White Matter prior probability map. It is not necessary to change this path unless you intend to use non-standard priors.

#. **Gray Matter Prior Probability Map - [path]:** Full path to a binarized Gray Matter prior probability map. It is not necessary to change this path unless you intend to use non-standard priors.

#. **CSF Prior Probability Map - [path]:** Full path to a binarized CSF prior probability map. It is not necessary to change this path unless you intend to use non-standard priors.

#. **FSL-FAST Thresholding - [On, Off]]:** Use FSL-FAST generated binary masks to generate the resulting segmentation tissue masks.

#. **Customized Thresholding - [On,Off]]:** Set the threshold value for tissue probability maps to generate the resulting segmentation tissue masks.

#. **White Matter Threshold Value - [float]:** Set the threshold value for refining the resulting White Matter segmentation tissue mask, if choose Customized Thresholding. The default value is 0.95.

#. **Gray Matter Threshold Value - [float]:** Set the threshold value for refining the resulting Gray Matter segmentation tissue mask, if choose Customized Thresholding. The default value is 0.95.

#. **CSF Threshold Value - [float]:** Set the threshold value for refining the resulting CSF segmentation tissue mask, if choose Customized Thresholding. The default value is 0.95.

#. **Erosion - [On, Off]:** Whether or not to use erosion to erode binarized tissue masks.

#. **Erosion Proportion - [float]:** Set the erosion proportion, if use erosion to erode binarized tissue masks. The default is 0.6.

.. figure:: /_images/seg_gui_2.png

#. **Template Based Segmentation - [EPI Template based, T1 Template based]:** Optimal for use with functional-only pipelines commonly used for rodent data, users can now employ a template-based tissue segmentation approach that applies inverse registration transforms to template-space tissue priors. If choose 'EPI Template based' or 'T1 Template based' as template based segmentation method, please make sure to specify white matter, gray matter, CSF mask paths at below three configurations.

#. **White Matter Binary Mask - [path]:** Full path to a binarized White Matter mask.

#. **Gray Matter Binary Mask - [path]:** Full path to a binarized Gray Matter mask.

#. **CSF Prior Binary Mask - [path]:** Full path to a binarized CSF mask.

.. figure:: /_images/seg_gui_3.png

#. **ANTs Prior-Based Segmentation - [On, Off]:** ANTs Prior-based Segmentation workflow that has shown optimal results for non-human primate data. Generate white matter, gray matter, CSF masks based on antsJointLabelFusion.

#. **The atlas image - [path]:** The atlas image assumed to be used in ANTs Prior-based Segmentation. Clicking on the *+* icon to the right of the box here will bring up a dialog where you can define multiple paths to NifTIs containing the atlas image.  You may add multiple images to the box.  

#. **The atlas segmentation images - [path]:** The number of specified segmentations should be identical to the number of atlas brain images. Clicking on the *+* icon to the right of the box here will bring up a dialog where you can define multiple paths to NifTIs containing the atlas segmentation image.  You may add multiple images to the box.  

#. **CSF Label Value - [integer]:** Label value corresponding to CSF in multiatlas file. It is not necessary to change this values unless your CSF/GM/WM label values are different from `Freesurfer Color Lookup Table. <https://surfer.nmr.mgh.harvard.edu/fswiki/FsTutorial/AnatomicalROI/FreeSurferColorLUT>`_

#. **Left Gray Matter Label Value - [integer]:** Label value corresponding to Left Gray Matter in multiatlas file. It is not necessary to change this values unless your CSF/GM/WM label values are different from `Freesurfer Color Lookup Table. <https://surfer.nmr.mgh.harvard.edu/fswiki/FsTutorial/AnatomicalROI/FreeSurferColorLUT>`_

#. **Right Gray Matter Label Value - [integer]:** Label value corresponding to Right Gray Matter in multiatlas file. It is not necessary to change this values unless your CSF/GM/WM label values are different from `Freesurfer Color Lookup Table. <https://surfer.nmr.mgh.harvard.edu/fswiki/FsTutorial/AnatomicalROI/FreeSurferColorLUT>`_

#. **Left White Matter Label Value - [integer]:** Label value corresponding to Left White Matter in multiatlas file. It is not necessary to change this values unless your CSF/GM/WM label values are different from `Freesurfer Color Lookup Table. <https://surfer.nmr.mgh.harvard.edu/fswiki/FsTutorial/AnatomicalROI/FreeSurferColorLUT>`_

#. **Right White Matter Label Value - [integer]:** Label value corresponding to Right White Matter in multiatlas file. It is not necessary to change this values unless your CSF/GM/WM label values are different from `Freesurfer Color Lookup Table. <https://surfer.nmr.mgh.harvard.edu/fswiki/FsTutorial/AnatomicalROI/FreeSurferColorLUT>`_


.. include:: /user/pipelines/without_gui.rst

.. literalinclude:: /references/default_pipeline.yml
   :language: YAML
   :lines: 361-479

References
^^^^^^^^^^
`AFNI 3dSkullStrip <https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dSkullStrip.html>`_

Smith, Stephen M., `Fast robust automated brain extraction <http://dx.doi.org/10.1002/hbm.10062>`_, Human Brain Mapping 2002, Volume 17 Issue 3, page 143-155.

N. Tustison et al., `N4ITK: Improved N3 Bias Correction <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3071855/pdf/nihms279873.pdf>`_, IEEE Transactions on Medical Imaging, 29(6):1310-1320, June 2010.
