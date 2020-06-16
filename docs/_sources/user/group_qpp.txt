Quasi-Periodic Patterns (QPP)
-----------------------------

Introduction and Background
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Quasi-Periodic Patterns are described as dominant spatio-temporal patterns that might recur throughout imaged time-series (Keilholz et al. 2014). The algorithm designed to detect these patterns by Majeed et al. (2009) has been implemented in Python as part of the C-PAC package.

The QPP algorithm produces both a "template", a characteristic single instance of the QPP, and a time course corresponding to the QPP, in the functional data.
The templates generated are useful to compare the QPP's timings and spatial extent across different subjects, while the time course of the QPP strength is useful to compare to other physiological signals (Majeed et al. 2009, Yousefi et al. 2018).
The optimal template is chosen from the given templates by summation of the values of its sliding correlation at local maxima, which are above a certain threshold (provided by the user) at the final iteration.
The template with the highest sum is designated as the most representative QPP.
Selected in this way, the most representative QPP is guaranteed to have high correlation and large numbers of occurrences relative to other templates (Yousefi et al. 2018).

Computation and Analysis Consideration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
While QPP can be performed at an individual level, group QPP can provide far more significant results to compare and regress with other physiological signals.
Computation of QPP involves extracting the time courses of multiple participants and concatenating them, producing one large 4-dimensional dataset.
This data is scanned with a fixed Window Length (WL) starting at random time points to find repeating patterns within the functional data.
This is then repeated several times, based on the user's input, to produce a template and the correlating time course.
The template is therefore an average of the segments of each scan with length WL.

It is important to note that QPP is computationally intensive, efficiency is important to keep in mind when using a large amount of subjects (> 500). It might take around 15 minutes to run such a large extent of subjects. 

Configuring QPP
^^^^^^^^^^^^^^^

Using the GUI
^^^^^^^^^^^^^
.. figure:: /_images/qpp_settings.png

#. **Run QPP - [Off, On]:** Run Quasi-Periodic Pattern analysis.

#. **Scan Inclusion (optional) - list of scans or None:** Include specific scans in your analysis. If you choose this option, only these scans will be included in performing concatenation of the time courses.

#. **Session Inclusion (optional) - list of sessions or None:** Include specific sessions in your analysiS. If you choose this option, only these sessions will be included in performing concatenation of the time courses.

#. **Scan/Sessions Stratification: ["Session and Scan", "Session", "Scan", "None"]:** This represents the grouping stratergy for concatenating the time courses to generate the input for QPP. This will run QPP for each session, (which may contain multiple scans within it) if 'Sessions' is selected. It will run QPP for each included scans, (which may contain multiple sessions within it) if 'Scans' is selected. If no grouping strategy is selected(None), then it will not group by sessions or scans, and will run once for all sessions and all scans.

#. **Window Length - [integer]:** The window length that is used to search the time course for some patterns.

#. **Permutations - [integer]:** The window length that is used to search the time course for some patterns.

#. **Initial Correlation Threshold: [number]:** This represents the early threshold for determining the peaks/signals representing a important 

#. **Final Correlation Threshold: [number]:** This represents the early threshold for determining the peaks/signals representing a important 

#. **Number of iterations to use initial correlation threshold: [number]:** This represents the early threshold for determining the peaks/signals representing a important 

#. **Maximum number of iterations: [number]:** This represents the early threshold for determining the peaks/signals representing a important 

Configuration Using a YAML File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To configure QPP options within a YAML file, add the following lines to your file (with appropriate substitutions for paths):

.. code-block:: yaml

   runQPP :  [1]

   qpp_scan_inclusion :  
   qpp_session_inclusion :  
   qpp_stratification : None

   qpp_permutations:  100
   qpp_window:  30

   qpp_initial_threshold: 0.2
   qpp_final_threshold: 0.3
   qpp_initial_threshold_iterations :  20

   qpp_iterations :  15

References:
^^^^^^^^^^^

Keilholz SD et al. `Quasi-periodic patterns (QPP): large-scale dynamics in resting state fMRI that correlate with local infraslow electrical activity <http://doi.org/10.1016/j.neuroimage.2013.09.029>`_. Neuroimage (2014).

Majeed W et al. `Spatiotemporal dynamics of low frequency fluctuations in BOLD fMRI of the rat <http://doi.org/10.1002/jmri.21848>`_. J Magn Reson Imaging (2009).

Yousefi et al. `Quasi Periodic Patterns of Intrinsic Brain activity in Individuals and their relationship with global signals <http://doi.org/10.1016/j.neuroimage.2017.11.043>`_. Neuroimage (2018).
