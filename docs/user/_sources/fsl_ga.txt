FSL Group Analysis
==================
Overview
^^^^^^^^
C-PAC uses `FSL/FEAT <http://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FEAT/UserGuide>`_ to compare findings across groups.

Users create a model file that includes group, phenotypic, and nuisance regressors for each subject, and the data is `run through a General Linear Model (GLM) based on pre-defined comparisons (contrasts) <http://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FEAT/UserGuide#Appendix_A:_Brief_Overview_of_GLM_Analysis>`_.

The following links provide an introduction to how groups are compared using FSL, as well as how to define contrasts.

* http://ccn.ucla.edu/wiki/images/c/c7/FSL_workshop_FEAT_2.pdf

* http://www.fmrib.ox.ac.uk/fslcourse/lectures/feat1_part2.pdf

* http://www.cubric.cf.ac.uk/neuroimaging-training/session5_group.pdf

Configuring CPAC to Run FSL Group Analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: /images/gui/fslga_main.png

* **Run Group Analysis:** Run group analysis using FSL/FEAT.
* **Select Derivatives:** Select which derivatives you would like to include when running group analysis. When including Dual Regression, make sure to correct your P-value for the number of maps you are comparing. When including Multiple Regression SCA, you must have more degrees of freedom (subjects) than there were time series.
* **Models to Run:** Use the + to add FSL Models to be run (or to create new models).
* **Models Contain F-tests:** Set this option to True if any of the models specified above contain F-tests.
* **Z Threshold:** Only voxels with a Z-score higher than this value will be considered significant.
* **Cluster Significance Threshold:** Significance threshold (P-value) to use when doing cluster correction for multiple comparisons.

Specifying Models to Run
""""""""""""""""""""""""


.. figure:: /images/gui/fslga_gui.png

* **Subject List:** Full path to a list of subjects to be included in the model. This should be a text file with one subject per line. Tip 1: A list in this format contaning all subjects run through CPAC was generated along with the main CPAC subject list (see subject_list_group_analysis.txt). Tip 2: An easy way to manually create this file is to copy the subjects column from your Regressor/EV spreadsheet.
* **EV File:** Full path to a .csv file containing EV information for each subject. Tip: A file in this format (containing a single column listing all subjects run through CPAC) was generated along with the main CPAC subject list (see template_phenotypic.csv).
* **Subjects Column Name:** Name of the subjects column in your EV file.
* **EVs to Include:** Specify the names of columns in your EV file that you would like to include in this model. Column names should be separated by commas and appear exactly as they do in your EV file. To include motion parameters calculated by CPAC, click the + button to on the right (and include an empty column of the same name in your EV file).
* **EV Type:** Specify whether each of the EVs in this model should be treated as categorical or continuous. To do this, place a 1 (categorical) or 0 (continuous) in the same list position as the corresponding EV. For example, if the EVs to include were: ``age, sex, diagnosis, mean_fd`` One might specify: ``0,1,1,0``
* **Demean:** Specify whether to demean each of the EVs in this model. To do this, place a 1 (demean) or 0 (don't demean) in the same list position as the corresponding EV. For example, if the EVs to include were: ``age, sex, diagnosis, mean_fd`` One might specify:``1,0,0,1`` Note that only continuous EV's should be demeaned.
* **Contrast File:** Full path to a .csv file containing contrasts to be applied to this model. When specifying EVs in this file: - Continuous EVs should appear the same as their corresponding column name in the EV file. - Categorical EVs must be split into multiple columns (one for each category), with names of the format EVname__N (e.g. diagnosis__1, diagnosis__2, diagnosis__3) If you wish to include F-tests in your model, create a column for each desired F-test, with names in the format f_test_1, f_test_2, etc.
* **Model Group Variances Seperately:** Specify whether FSL should model the variance for each group separately. If this option is enabled, you must specify a grouping variable below.
* **Grouping Variable:** The name of the EV that should be used to group subjects when modeling variances. If you do not wish to model group variances separately, set this value to None.
* **Model Name:** Specify a name for the new model.
* **Output Directory:** Full path to the directory where CPAC should place model files.
* **Model CSV File Name:** In addition to the standard FSL model files, CPAC will output a .csv containing the subjects and EVs specified above. Column names in this file will be the same as in the contrasts file, and will have been demeaned as specified.







