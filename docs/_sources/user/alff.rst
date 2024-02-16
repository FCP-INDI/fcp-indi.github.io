Amplitude of Low Frequency Fluctuations (ALFF) and fractional ALFF (f/ALFF)
---------------------------------------------------------------------------

Introduction & Background
^^^^^^^^^^^^^^^^^^^^^^^^^
Slow fluctuations in activity are a fundamental feature of the resting brain, and their presence is key to determining correlated activity between brain regions and defining resting state networks. The relative magnitude of these fluctuations can differ between brain regions and between subjects, and thus may act as a marker of individual differences or dysfunction. **Amplitude of Low Frequency Fluctuations** (ALFF) :footcite:`Zang07` and **fractional Amplitude of Low Frequency Fluctuations** (f/ALFF) :footcite:`Zou08` are related measures that quantify the amplitude of these low frequency oscillations (LFOs).

ALFF is defined as the total power within the frequency range between 0.01 and 0.1 Hz, and thus indexes the strength or intensity of LFO. f/ALFF is defined as the power within the low-frequency range (0.01-0.1 Hz) divided by the total power in the entire detectable frequency range, and represents the relative contribution of specific LFO to the whole frequency range :footcite:`Zuo10`.

Computation and Analysis Considerations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
All computations are performed in a subject's native space, template space, or both in parallel. After transforming voxel time series frequency information into the power domain, calculation of these measures is relatively simple. ALFF is calculated as the sum of amplitudes within a specific low frequency range. f/ALFF is calculated as a fraction of the sum of amplitudes across the entire frequency range detectable in a given signal. For both measures, amplitudes in subject-level maps are transformed into Z-scores to create standardized subject-level maps. For more detail on how CPAC computes these steps, please see :doc:`the ALFF and f/ALFF page of the developer documentation </developer/workflows/alff>`.

Though both ALFF and f/ALFF are sensitive mostly to signal from gray matter, ALFF is more prone to noise from physiological sources, particularly near the ventricles and large blood vessels :footcite:`Zou08,Zuo10`. The figure below (from :footcite:`Zuo10`) shows areas in which ALFF shows higher amplitude than f/ALFF, as well as the relative sensitivity of these measures to gray matter.

.. figure:: /_images/alff_zuo_difference.png

Both ALFF and f/ALFF show moderate to high test-retest reliability in gray matter regions, but reliability for ALFF tends to be higher than for fALFF :footcite:`Zuo10`. As it is more reliable, ALFF may be more sensitive to differences between groups and individuals. The figure below (also from :footcite:`Zuo10`) shows differences in test-retest reliability as measured by Intraclass Correlation (ICC) :footcite:`Shro79`.

.. figure:: /_images/alff_zuo_trt.png

Finally, as these measures require a constant timecourse on which to do frequency and power analyses, they cannot be run on scrubbed data :footcite:`Powe12` in which volumes with excessive movement have been removed.

Applications and Recommendations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ALFF and f/ALFF have been used to uncover differences in amplitude power both between subjects and between conditions. Zang et al. :footcite:`Zang07` found that children with ADHD show reduced ALFF amplitude in some brain areas and increased amplitude in others compared to controls, while Yan and colleagues :footcite:`Yan09` saw increased amplitude in the Default Mode Network during Eyes Open vs. Eyes Closed resting periods. Changes in f/ALFF have also been observed with aging :footcite:`Hu14`.

The increased specificity to the gray matter signal for f/ALFF compared to ALFF may suggest favoring the former, but doing so would come at the cost of reduced test-retest reliability. As such, in order to maximize the reliability across subjects while providing sufficient specificity to examine individual differences, reporting both measures is recommended :footcite:`Zuo10`.

Configuring CPAC to Run ALFF and f/ALFF
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. figure:: /_images/alff_gui.png

#. **ALFF / f/ALFF - [Off, On]:** Calculate Amplitude of Low Frequency Fluctuations (ALFF) and and fractional ALFF (f/ALFF) for all voxels.

#. **f/ALFF High-Pass Cutoff - [decimal]:** Frequency cutoff (in Hz) for the high-pass filter used when calculating f/ALFF.

#. **f/ALFF Low-Pass Cutoff - [decimal]:** Frequency cutoff (in Hz) for the low-pass filter used when calculating f/ALFF

.. include:: /user/pipelines/without_gui.rst

.. literalinclude:: /references/default_pipeline.yml
   :language: YAML
   :start-at: amplitude_low_frequency_fluctuation:
   :end-before: regional_homogeneity:

Surface-based f/ALFF
^^^^^^^^^^^^^^^^^^^^
.. versionadded:: 1.8.7

C-PAC now offers the computation of surface-based ALFF and fALFF. This can be configured in under surface_analysis in the pipeline file. 

.. literalinclude:: /references/default_pipeline.yml
   :language: YAML
   :start-at: surface_analysis:
   :end-before: anatomical_preproc:

References
^^^^^^^^^^

.. footbibliography::
