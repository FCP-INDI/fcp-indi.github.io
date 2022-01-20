Random State
============

When performing reproducibility/variability experiments, it is important to isolate sources of variability. One such source is random state.

Users can fix the random state of C-PAC's execution by specifying a random seed. When adding a Node that should accept a user-specified random seed, add

* the :py:class:`nipype.interfaces.base.core.Interface` and the corresponding flags to add/remove to set the random seed, or
* in the case of a :py:class:`CPAC.utils.interfaces.function.Function` Node, the Function node's function and a function to apply to that function definition to set the random seed

to :py:function:`CPAC.pipeline.random_state.seed.random_seed_flags`.

.. py:function:: CPAC.pipeline.random_state.seed.random_seed_flags
