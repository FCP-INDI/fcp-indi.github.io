.. _cpac_pipeline:



************
cpac_pipeline
************

Configuration Object
====================

The 'c' variable in cpac_pipeline.py is a `Configuration object <https://github.com/FCP-INDI/C-PAC/blob/master/CPAC/utils/configuration.py>`_, which is an abstract representation used to store the options for the pipeline configuration YAML after it is read in by C-PAC.

Pipeline Strategy Construction
==============================

cpac_pipeline.py is where the Nipype workflow object for each pipeline strategy is constructed via flow control.  The number of pipeline strategies (i.e., forks of a base workflow object)  is determined by CompCor, nuisance regressor, segmentation and scrubbing options.  

To add a new method/technique, add a code block similar to this:

.. code-block:: python

	'''
	Inserting <technique/method>
	'''
	
	new_strat_list = []
	num_strat = 0

	if 1 in c.runTechnique:
		for strat in strat_list:
			<make nodes here>
			<add additional options from configuration YAML / config object here using conditional statements>
			<get previous step from resource pool and connect nodes to workflow>
			num_strat += 1
		strat_list += new_strat_list
		num_strat = 0

Where `runTechnique` is the name of the YAML configuration key for that method/technique.
