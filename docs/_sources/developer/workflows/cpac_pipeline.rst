.. _cpac_pipeline:

***************************
C-PAC Pipeline Construction
***************************

Configuration Object
====================

The 'c' variable in cpac_pipeline.py is a `Configuration object <https://github.com/FCP-INDI/C-PAC/blob/v1.6.0/CPAC/utils/configuration.py>`_, which is an abstract representation used to store the options for the pipeline configuration YAML after it is read in by C-PAC.  Each attribute of the Configuration object is a key from the YAML file, with values mirroring the YAML.

Strategy Object
===============

A strategy object represents an individual pipeline.  The number of strategies is determined by how options have been set in the configuration file.  If there is a step where multiple options have been specified, all steps in the pipeline prior to that step will be forked and multiple strategies will created for each option.  The steps where forking can occur are CompCor, nuisance regressor, segmentation and scrubbing.  Each strategy has the following attributes:

* resource pool - a dictionary containing all nodes/workflows used by a strategy.  Keys are descriptors of the node/workflow and values are two-element tuples containing a copy of the node/workflow and the outputspec for that node/workflow.

* leaf_node - the final node/workflow added during the last step of strategy construction.

* leaf_out_file - the outputspec associated with the leaf node.

* name - a list of workflow names

Strategy Construction
======================

cpac_pipeline.py is where the Nipype workflow object for each strategy is constructed via flow control.
To add a new method/technique, add a code block similar to this:

.. code-block:: python

	'''
	Inserting <technique/method>
	'''
	
	new_strat_list = []
	num_strat = 0

	if 1 in c.runTechnique:
		for strat in strat_list:
			# Introduce nodes/workflows here
			try:
				nipype_node=spawn_nipype_node()
			except:
				logger.info('Something went wrong!')
			# Get the necessary inputs from the resource pool and connect to the node/workflow.
			try:
				node, out_file = strat.get_node_from_resource_pool('previous')
				workflow.connect(node, out_file, nipype_node,'inputspec.input')
			except:
				logger.info('Something went wrong!')
			# Add additional options from configuration YAML / config object here using conditional statements.

			# If runTechnique can take multiple values, fork the strategy.
			# This is the off option, so the original strategy is copied into a new one.
			# The new strategy is then updated with the values for a pipeline where the technique is turned on.
			if 0 in c.runTechnique:
				tmp = strategy()
				tmp.resource_pool = dict(strat.resource_pool)
				tmp.leaf_node = (strat.leaf_node)
				tmp.leaf_out_file = str(strat.leaf_out_file)
				tmp.name = list(strat.name)
				# strat now points at the new strategy, rather than the old strategy contained in strat_list
				strat = tmp
				new_strat_list.append(strat) 
			strat.append_name(nipype_node.name)
			strat.update_resource_pool({'output':(output,'outputspec.output')})
			create_log_node(nipype_node,'outputspec.output', num_strat)
			num_strat += 1

	strat_list += new_strat_list

Where `runTechnique` is the name of the YAML configuration key for that method/technique.
