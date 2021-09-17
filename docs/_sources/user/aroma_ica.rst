ICA-AROMA (Independent Component Analysis - Automatic Removal of Motion Artifacts)
----------------------------------------------------------------------------------

INTRODUCTION
^^^^^^^^^^^^

Motion artifacts, when induced in fMRI can cause true effects to be classified into noise, or correlate motion artifacts to true effects.While most methods for dealing with the artifacts may result in reduction of temporal freedom or destroy autocorrelation structure, and such drawbacks can be overcome by using AROMA-ICA().
ICA-AROMA concerns a data-driven method to identify and remove motion-related independent components from fMRI data.To that end it exploits a small, but robust set of theoretically motivated features, preventing the need for classifier re-training and therefore providing direct and easy applicability. 


COMPUTATION AND ANALYSIS CONSIDERATION:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This method uses an ICA-based strategy for Automatic Removal of Motion Artifacts (ICA-AROMA) that uses a small (n=4), but robust set of theoretically motivated temporal and spatial features. Our strategy does not require classifier re-training, retains the data's autocorrelation structure and largely preserves temporal degrees of freedom.ICA-AROMA identified motion components with high accuracy and robustness as illustrated by leave-N-out cross-validation.(Pruim R1 et.al.,NeuroImage,2015). C-PAC's implementation of Aroma-ICA involves using the nipype's interface to the package developed in FSL (https://github.com/maartenmennes/ICA-AROMA). The output directory includes the denoised file along with the melodic directory, statistics and other feature classification texts. The movement parameters necessary for running this script is obtained using FSL's McFLIRT, and the mask file is obtained using FSL's BET (as per suggestion). 

INSTALLING AROMA-ICA:
^^^^^^^^^^^^^^^^^^^^^

To run AROMA-ICA using C-PAC, it is essential to download and set up AROMA-ICA in your system. This can be accomplished by::

 mkdir -p /opt/ICA-AROMA
 curl -sSL "https://github.com/rhr-pruim/ICA-AROMA/archive/v0.4.3-beta.tar.gz" | tar -xzC /opt/ICA-AROMA --strip-components 1
 chmod +x /opt/ICA-AROMA/ICA_AROMA.py


CONFIGURING C-PAC TO RUN AROMA-ICA:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: /_images/ICA-AROMA_gui.png

#. **Run Aroma-ICA:** Choose "On" to run Aroma-ICA.

#. **Denoise type:** Choose between 'nonaggr' for non-aggressively denoised file and 'aggr' aggressively denoised file.


CONFIGURING AROMA-ICA USING A YAML FILE:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following nested key/value pairs that will be set to these defaults if not defined in your :doc:`pipeline configuration YAML </user/pipelines/pipeline_config>`:

.. literalinclude:: /references/default_pipeline.yml
   :language: YAML
   :start-at: nuisance_corrections:
   :end-before: 2-nuisance_regression:

EXTERNAL RESOURCES:
^^^^^^^^^^^^^^^^^^^
     
   * AROMA-ICA python script: https://github.com/maartenmennes/ICA-AROMA

REFERENCES:
^^^^^^^^^^^

   * Neuroimage. 2015 May 15;112:267-277. doi: 10.1016/j.neuroimage.2015.02.064. Epub 2015 Mar 11.

   * https://github.com/maartenmennes/ICA-AROMA/blob/master/Manual.pdf








 

