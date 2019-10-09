.. C-PAC documentation master file, created by
   sphinx-quickstart on Fri Jul 20 16:32:55 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to C-PAC's Documentation!
=================================

Latest Release: C-PAC v1.5.0 (Oct 9, 2019)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**NEW FEATURES - GENERAL**

* **Phase-Encoding Polarity Distortion Correction (Blip-Up / Blip-Down).** A new option for distortion correction is available! Phase-Encoding Polarity (commonly known as blip-up/blip-down) employs phase-encoding direction-specific EPI field maps to correct for distortion in the direction of the phase-encoding.

* **N4 Bias Field Correction.** The ability to run N4 Bias Field Correction in the anatomical preprocessing pipeline has been added, via ANTs' N4BiasFieldCorrection.

[http://stnava.github.io/ANTs/]

[http://manpages.ubuntu.com/manpages/trusty/man1/N4BiasFieldCorrection.1.html]

* **Non-Local Means (NLM) filtering.** NLM has been integrated into the anatomical preprocessing pipeline, via ANTs DenoiseImage.

[http://stnava.github.io/ANTs/]

[https://manpages.debian.org/experimental/ants/DenoiseImage.1.en.html]

* **Increased Configurability of Output Resolution.** Users can now select write-out resolutions with a finer granularity of values, also allowing for native voxel dimension write-outs.

* **Increased Interpolation Configurability.** Introduced the ability to select a full range of interpolation options for transform application and resampling. LanczosWindowedSinc has been set as the new default for ANTs operations and Sinc for FSL operations.

* **PyPEER Integration.** C-PAC can now prepare your pipeline results directly for Predictive Eye Estimation. PEER is a previously developed support vector regression-based method for retrospectively estimating eye gaze from the fMRI signal in the eye’s orbit.

[https://github.com/ChildMindInstitute/PyPEER]

Evaluating fMRI-Based Estimation of Eye Gaze during Naturalistic Viewing. Jake Son, Lei Ai, Ryan Lim, Ting Xu, Stanley Colcombe, Alexandre Rosa Franco, Jessica Cloud, Stephen LaConte, Jonathan Lisinski, Arno Klein, R. Cameron Craddock, Michael Milham. https://doi.org/10.1101/347765

[https://www.biorxiv.org/content/10.1101/347765v5]

**NEW FEATURES - CROSS-PIPELINE REPRODUCIBILITY**

Several new preprocessing features have been added to C-PAC's pipeline choices, in an ongoing effort to incrementally expand C-PAC's configurability. These methods have been adapted from the niworkflows and fmriprep packages (see appropriate links below).

* **New BOLD Masking option.** A BOLD masking strategy designed by the fmriprep team is now available. The method employs both BET and 3dAutomask for refined BOLD masks. See the User Guide for more information.

[https://fmriprep.readthedocs.io/en/stable/]

[https://fmriprep.readthedocs.io/en/stable/workflows.html#bold-preprocessing]

* **ANTs Brain Extraction.** ANTs Brain extraction has now been integrated as an option for brain extraction. Implementation by the fmriprep team. See the User Guide for more information.

[http://stnava.github.io/ANTs/]

[https://github.com/ANTsX/ANTs/blob/master/Scripts/antsBrainExtraction.sh]

[https://fmriprep.readthedocs.io/en/stable/]

[https://fmriprep.readthedocs.io/en/stable/workflows.html#bold-preprocessing]

* **Increased Segmentation Configurability.** Thresholding options have returned, and new erosion options for anatomical segmentation have been introduced. The erosion implementation was adapted from fmriprep.

[https://fmriprep.readthedocs.io/en/stable/]

[https://fmriprep.readthedocs.io/en/stable/workflows.html#brain-extraction-brain-tissue-segmentation-and-spatial-normalization]

**IMPROVEMENTS**

* Added a selection of Neurodata's Neuroparc atlases to the C-PAC container, and C-PAC now also performs time-series extraction on these atlases by default (in addition to the original defaults).

[https://github.com/neurodata/neuroparc]

[https://neurodata.io/]

* Improved parallelization for ISC and ISFC runs.

* Users can now employ the -monkey option for AFNI 3dSkullStrip for brain extraction, for non-human primate data.

**BUG FIXES**

* Fixed an issue where BIDS-format slice timing information was not being read into 3dTshift properly in some cases.

* Fixed an error preventing Seed-Based Correlation Analysis from running to completion.

* Fixed an error that would cause the pipeline to crash at the smoothing stage if the write-out resolution for functional preprocessed data and the resolution for functional-derived data were different.

* Fixed an issue that would prevent output files from being written to the output directory if nuisance regression was disabled.

* Fixed an issue where ISC and ISFC would not write out the results to the output directory.

**In addition,** the :doc:`C-PAC Docker image and AWS AMI</running>` have both been updated. These provide a quick way to get started without needing to go through the install process.

**And as always, you can contact us here for user support and discussion:**

`https://groups.google.com/forum/#!forum/cpax_forum <https://groups.google.com/forum/#!forum/cpax_forum>`_


The C-PAC Mission
^^^^^^^^^^^^^^^^^

Once a distant goal, discovery science for the human connectome is now a reality. Researchers who previously struggled to obtain neuroimaging data from 20-30 participants are now exploring the functional connectome using data acquired from thousands of participants, made publicly available through the `1000 Functional Connectomes Project and the International Neuroimaging Data-sharing Initiative (INDI) <http://fcon_1000.projects.nitrc.org/>`_. However, in addition to access to data, scientists need access to tools that will facilitate data exploration. Such tools are particularly important for those who are inexperienced with the nuances of fMRI image analysis, or those who lack the programming support necessary for handling and analyzing large-scale datasets.

The Configurable Pipeline for the Analysis of Connectomes (C-PAC) is a configurable, open-source, Nipype-based, automated processing pipeline for resting state functional MRI (R-fMRI) data, for use by both novice and expert users. C-PAC was designed to bring the power, flexibility and elegance of the `Nipype platform <http://nipy.sourceforge.net/nipype/>`_ to users in a plug and play fashion—without requiring the ability to program. Using an easy to read, text-editable configuration file or a graphical user interface, C-PAC users can rapidly orchestrate automated R-fMRI processing procedures, including: 

* standard quality assurance measurements
* standard image preprocessing based upon user specified preferences
* generation of functional connectivity maps (e.g., :doc:`seed-based correlation analyses </sca>`)
* customizable extraction of time-series data
* generation of graphical representations of the connectomes at various scales (e.g., voxel, parcellation unit)
* generation of local R-fMRI measures (e.g., :doc:`regional homogeneity </reho>`, :doc:`voxel-matched homotopic connectivity </vmhc>`, :doc:`frequency amplitude measures </alff>`)

Importantly, C-PAC makes it possible to use a single configuration file to launch a factorial number of pipelines differing with respect to specific processing steps (e.g., spatial/temporal filter settings, global correction strategies, motion correction strategies, group analysis models). Additional noteworthy features include the ability to easily:

* customize C-PAC to handle any systematic directory organization
* specify Nipype distributed processing settings

C-PAC maintains key Nipype strengths, including the ability to:

* interface with different software packages (e.g., FSL, AFNI, ANTS)
* protect against redundant computation and/or storage
* automatically carry out input checking, bug tracking and reporting

Future updates will include more configurability, advanced analytic features (e.g., support vector machines, cluster analysis) and diffusion tensor imaging (DTI) capabilities.

For more information and additional tutorials, check out our `YouTube channel <https://www.youtube.com/channel/UCMhbaa3bF7oQgnAWX6HmyMQ>`_, as well as slides from our previous presentations:

* `CPAC Connectome Analysis in the Cloud <http://www.slideshare.net/CameronCraddock/cpac-connectome-analysis-in-the-cloud>`_
* `Open science resources for 'Big Data' Analyses of the human connectome <http://www.slideshare.net/CameronCraddock/open-science-resources-for-big-data-analyses-of-the-human-connectome>`_
* `Computational approaches for mapping the human connectome <http://www.slideshare.net/CameronCraddock/computational-approaches-for-mapping-the-human-connectome>`_

The C-PAC Team
^^^^^^^^^^^^^^
.. line-block::

   **Primary Development Team:**
   Michael Milham (Founder, Co-Principal Investigator)
   Cameron Craddock (Co-Principal Investigator)
   Steven Giavasis (Lead Developer)
   Hecheng Jin (Developer)
   Xinhui Li (Developer)

   **Project Alumni:**
   Anibal Solon Heinsfeld
   Nanditha Rajamani
   Alison Walensky
   David O'Connor
   Carol Froehlich
   John Pellman
   Amalia MacDonald
   Daniel Clark
   Rosalia Tungaraza
   Daniel Lurie
   Zarrar Shehzad
   Krishna Somandepali
   Aimi Watanabe
   Qingyang Li
   Ranjit Khanuja
   Sharad Sikka
   Brian Cheung
 
   **Other Contributors:**
   Ivan J. Roijals-Miras (Google Summer of Code)
   Florian Gesser (Google Summer of Code)
   Asier Erramuzpe (Google Summer of Code)
   Chao-Gan Yan
   Joshua Vogelstein
   Adriana Di Martino
   F. Xavier Castellanos
   Sebastian Urchs
   Bharat Biswal

Funding Acknowledgements
^^^^^^^^^^^^^^^^^^^^^^^^
Primary support for the work by Michael P. Milham, Cameron Craddock and the INDI team was provided by gifts from Joseph P. Healey and the `Stavros Niarchos Foundation <http://www.snf.org/>`_ to the `Child Mind Institute <http://www.childmind.org/>`_, as well as by `NIMH <http://www.nimh.nih.gov/index.shtml>`_ awards to Dr. Milham (R03MH096321) and F.X. Castellanos (R01MH083246).

User Guide Index
----------------

.. toctree::
   :maxdepth: 2

   1. C-PAC Quickstart <quick>
   2. Specify Your Data <subject_list_config>
   3. Select Your Pipeline <pipeline_config>
   4. Pre-Process Your Data <preprocessing>
   5. Compute Derivatives <derivatives>
   6. All Run Options <running>
   7. Run Group Analysis <group_analysis>
   8. Check Your Outputs <output_dir>
   9. Troubleshoot <help>
   10. Release Notes <rnotes>
   11. Appendix <appendix>
