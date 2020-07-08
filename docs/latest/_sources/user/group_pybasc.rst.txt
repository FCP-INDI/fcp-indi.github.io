Bootstrapped Analysis of Stable Clusters (PyBASC)
=================================================
Overview
^^^^^^^^

Bootstrapped Analysis of Stable Clusters (BASC) is a boot-strapping technique based on the following work:

#. Garcia-Garcia, M., Nikolaidis, A., Bellec, P., Craddock, R. C., Cheung, B., Castellanos, F. X., & Milham, M. P. (2017). Detecting stable individual differences in the functional organization of the human basal ganglia. NeuroImage.

#. Bellec, P., Rosa-Neto, P., Lyttelton, O. C., Benali, H., & Evans, A. C. (2010). Multi-level bootstrap analysis of stable clusters in resting-state fMRI. Neuroimage, 51(3), 1126-1139.

#. Bellec, P., Marrelec, G., & Benali, H. (2008). A bootstrap test to investigate changes in brain connectivity for functional MRI. Statistica Sinica, 1253-1268.

When running BASC, C-PAC employs the Python-based PyBASC package implemented and maintained by Aki Nikolaidis: `https://github.com/AkiNikolaidis/PyBASC <https://github.com/AkiNikolaidis/PyBASC>`_.

PyBASC allows users to create individual and group level clustering solutions and compare the reliability and reproducibility of these clustering solutions across a wide variety of methods. C-PAC makes it easy to directly supply the preprocessed functional timeseries of your participants directly into PyBASC, for each nuisance strategy, session, and scan you have in your pipeline output folder.

From terminal
-------------

Similar to the pipeline configuration YAML file, the group configuration YAML file allows you to configure your runs with key-value combinations. From terminal, you can quickly generate a default group configuration YAML file template in the directory you are in: ::

    cpac utils group_config new_template

This will generate a group configuration file that you can then modify to make your selections. See below: ::

	# General Group-Level Analysis Settings
	##############################################################################

	# The main input of group-level analysis- the output directory of your individual-level analysis pipeline run (pre-processing & derivatives for each participant). This should be a path to your C-PAC individual-level run's pipeline folder, which includes the sub-directories labeled with the participant IDs.
	pipeline_dir: /path/to/output_dir


	# (Optional) Full path to a list of participants to be included in the model. You can use this to easily prune participants from your model. In group-level analyses involving phenotype files, this allows you to prune participants without removing them from the phenotype CSV/TSV file. This should be a text file with one subject per line. An easy way to manually create this file is to copy the participant ID column from your phenotype file.
	participant_list: None


	# Full path to the directory where CPAC should place group-level analysis outputs and any applicable statistical model files.
	output_dir: /path/to/output/dir


	#Much like the working directory for individual-level analysis, this is where the intermediate and working files will be stored during your run. This directory can be deleted later on. However, saving this directory allows the group analysis run to skip steps that have been already completed, in the case of re-runs.
	work_dir: /path/to/work/dir


	#Where to write out log information for your group analysis run.
	log_dir: /path/to/log/dir


	# The path to your FSL installation directory. This can be left as 'FSLDIR' to grab your system's default FSL installation. However, if you prefer to use a specific install of FSL, you can enter the path here.
	FSLDIR: FSLDIR


	# Bootstrap Analysis of Stable Clusters (BASC) - via PyBASC
	##############################################################################

	# Run Bootstrap Analysis of Stable Clusters
	run_basc :  [1]


	# If there are multiple series or scans in any of the pipeline outputs for which PyBASC is being run, and you only want to run for some of them, you can list them here - scan labels separated by commas (ex. 'rest_run-1, rest_run-3').
	# If nothing is listed, all available pipelines will be run.
	basc_scan_inclusion :  None


	# The resolution to run PyBASC with.
	basc_resolution :  4mm


	# Maximum amount of processors to use while performing BASC.
	basc_proc :  2


	# Maximum amount of RAM (in GB) to be used when running BASC.
	basc_memory :  4


	# Standard FSL Skull Stripped Template.
	template_brain_only_for_func :  $FSLDIR/data/standard/MNI152_T1_${basc_resolution}_brain.nii.gz


	# Full path to a mask file to be used when running BASC. Voxels outside this mask will be excluded from analysis. This is the region that you’d like to parcellate.
	# If you do not wish to use a mask, set this field to None.
	# Note: BASC is very computationally intensive, we strongly recommend you limit your analysis to specific brain areas of interest.
	basc_roi_mask_file :  None


	# If cross clustering is enabled, then clustering of the first region will be calculated based on pairwise similarity between the timeseries of the ROI Mask File, and this second ROI.
	basc_cross_cluster_mask_file :  None


	# The metric used to compare similarity between voxel timeseries.
	# Options: ['correlation', 'euclidean', 'cityblock', 'cosine']
	basc_similarity_metric_list :  ['correlation']


	# How many times individual level circular block bootstrapping of the timeseries will be applied.
	basc_timeseries_bootstrap_list :  100


	# Number of bootstraps to apply to the original dataset.
	basc_dataset_bootstrap_list :  30


	# Number of clusters to create during clustering at both the individual and group levels.
	basc_n_clusters_list :  2


	# The similarity threshold at which the similarity matrices will be set to 0.
	basc_affinity_thresh : [0.0]


	# This is the amount of feature agglomeration that will be applied. Smaller values mean more feature agglomeration.
	basc_output_sizes :  800


	# If set to true, then the ROI Mask file parcellation will be based on the similarity between ROI Mask file voxels based on their connectivity to each voxel in ROI mask file for cross-clustering.
	basc_cross_cluster :  True


	# This parameter determines the width of the time window used in the circular block bootstrap.
	basc_blocklength_list :  1


	# If this is set to true, the all individuals will have feature agglomeration applied together, resulting in the same mapping across subjects. Use this only when memory demands limit ability to process ROIs with a high number of voxels.
	basc_group_dim_reduce :  False

Once you have made your selections, you can run PyBASC from the command-line with this command::

    cpac group basc /path/to/group_config.yml


