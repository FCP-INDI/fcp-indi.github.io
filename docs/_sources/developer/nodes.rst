*****
Nodes
*****

.. rubric:: mem_gb

Nipype Nodes have an parameter ``mem_gb`` that differs from the :ref:`commandline option </user/run/help>` ``--mem_gb``. While the commandline option is a limit, the Node parameter is an estimate of the most memory that Node will consume when run. The Node parameter is not a limit; rather, this value is used to allocate system resources at runtime.

.. autoclass:: nipype.pipeline.engine.nodes.Node
   :members: 
   :special-members: __init__
