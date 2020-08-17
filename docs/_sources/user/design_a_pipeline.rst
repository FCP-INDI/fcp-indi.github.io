Design A Pipeline
-----------------

.. topic:: Neuroparc v1.0: Baseline

  .. include:: /user/ndmg_atlases.rst

C-PAC offers a graphical interface you can use to quickly and easily modify the default pipeline or create your own from scratch:

`https://fcp-indi.github.io/C-PAC_GUI/versions/latest/browser/#/ <https://fcp-indi.github.io/C-PAC_GUI/versions/latest/browser/#/>`_

.. figure:: /_images/gui_home1.png

Once you save the pipeline configuration YAML file, you can provide it to the C-PAC Docker container like so:

.. code-block:: console

    docker run -i --rm \
            -v /Users/You/local_bids_data:/bids_dataset \
            -v /Users/You/some_folder:/outputs \
            -v /tmp:/tmp \
            -v /Users/You/Documents:/configs \
            -v /Users/You/resources:/resources \
            fcpindi/c-pac:latest /bids_dataset /outputs participant --pipeline_file /configs/pipeline_config.yml

Or you can provide it to the C-PAC Singularity container like so:

.. code-block:: console

    singularity run \
            -B /Users/You/some_folder:/outputs \
            -B /tmp:/tmp \
            -B /Users/You/Documents:/configs \
            fcpindi_c-pac_latest-{date}-{hash value}.img s3://fcp-indi/data/Projects/ADHD200/RawDataBIDS /outputs participant --pipeline_file /configs/pipeline_config.yml
**Reporting errors and getting help**

Please report errors on the `C-PAC github page issue tracker <https://github.com/FCP-INDI/C-PAC/issues>`_. Please use the `C-PAC google group <https://groups.google.com/forum/#!forum/cpax_forum>`_ for help using C-PAC and this application.