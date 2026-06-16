C-PAC Quickstart
================

.. include:: quick_overview.rst

.. _cpac-python-package:

.. include:: cpac.rst

For instructions to run C-PAC in Docker or Singularity without installing cpac (Python package), see :doc:`All Run Options </user/running>`

.. include:: brainlife.io_app.rst

Default Pipeline
----------------

.. include:: /user/pipelines/desc/default.rst

Pre-configured Pipelines
------------------------

In addition to the default pipeline, C-PAC comes packaged with a growing library of pre-configured pipelines that are ready to use. They can be invoked when running C-PAC using the ``--preconfig`` flag detailed above.

Detailed information about the selection of pre-configured pipelines are :doc:`available here </user/pipelines/preconfig>`.

.. include:: pipelines/design_a_pipeline.rst

Acknowledgments
---------------

We currently have a publication in preparation, in the meantime please cite our poster from INCF:

.. code-block:: console

	Craddock C, Sikka S, Cheung B, Khanuja R, Ghosh SS, Yan C, Li Q, Lurie D, Vogelstein J, Burns R, Colcombe S,
	Mennes M, Kelly C, Di Martino A, Castellanos FX and Milham M (2013). Towards Automated Analysis of Connectomes:
	The Configurable Pipeline for the Analysis of Connectomes (C-PAC). Front. Neuroinform. Conference Abstract:
	Neuroinformatics 2013. doi:10.3389/conf.fninf.2013.09.00042

	@ARTICLE{cpac2013,
	    AUTHOR={Craddock, Cameron  and  Sikka, Sharad  and  Cheung, Brian  and  Khanuja, Ranjeet  and  Ghosh, Satrajit S
	        and Yan, Chaogan  and  Li, Qingyang  and  Lurie, Daniel  and  Vogelstein, Joshua  and  Burns, Randal  and
	        Colcombe, Stanley  and  Mennes, Maarten  and  Kelly, Clare  and  Di Martino, Adriana  and  Castellanos,
	        Francisco Xavier  and  Milham, Michael},
	    TITLE={Towards Automated Analysis of Connectomes: The {Configurable Pipeline for the Analysis of Connectomes (C-PAC)}},
	    JOURNAL={Frontiers in Neuroinformatics},
	    YEAR={2013},
	    NUMBER={42},
	    URL={http://www.frontiersin.org/neuroinformatics/10.3389/conf.fninf.2013.09.00042/full},
	    DOI={10.3389/conf.fninf.2013.09.00042},
	    ISSN={1662-5196}
	}
