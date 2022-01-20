Random State
============

When performing reproducibility/variability experiments, it is important to isolate sources of variability. One such source is random state.

Users can fix the random state of C-PAC's execution by specifying a random seed. When adding a Node that should accept a user-specified random seed, add

* the |nipype.interfaces.base.core.Interface|_ and the corresponding flags to add/remove to set the random seed, or
* in the case of a :py:class:`CPAC.utils.interfaces.function.Function` Node, the Function node's function and a function to apply to that function definition to set the random seed

to :py:func:`CPAC.pipeline.random_state.seed.random_seed_flags`.

.. autofunction:: CPAC.pipeline.random_state.seed.random_seed_flags

.. autoclass:: nipype.interfaces.base.core.Interface
   :special-members: __init__
   :members:
   :inherited-members:

.. |nipype.interfaces.base.core.Interface| replace:: :py:class:`nipype.interfaces.base.core.Interface`
.. _nipype.interfaces.base.core.Interface: https://nipype.readthedocs.io/en/1.5.1/devel/interface_specs.html