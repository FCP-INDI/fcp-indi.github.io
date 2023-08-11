Random State
============

When performing reproducibility/variability experiments, it is important to isolate sources of variability. One such source is random state.

Random seed can be set in pipeline config

.. literalinclude:: /references/default_pipeline.yml
   :language: YAML
   :start-at: pipeline_setup:
   :lines: 1

.. literalinclude:: /references/default_pipeline.yml
   :language: YAML
   :start-at: system_config:
   :end-before: # Select Off if you intend to run CPAC on a single machine.

or on the command line with ``--random-seed $SEED``.

Valid options are positive integers up to 2,147,483,647 or the word 'random' (which will set an integer in that range). If not specified, a seed will not be set, and each relevant process will run with an undocumented random seed.

When a seed is set, a ``random.log`` file, including the constant seed and each node the seed was applied to, will be generated in the logging directory.

The following processes currently support this feature:

.. exec::
    from CPAC.pipeline.random_state.seed import random_seed_flags, \
                                                set_up_random_state
    set_up_random_state('random')
    processes = random_seed_flags()
    for interface in processes['interfaces'].keys():
        print(interface._cmd)
    for fxn in processes['functions'].keys():
        print('.'.join([fxn.__module__, fxn.__name__]))
