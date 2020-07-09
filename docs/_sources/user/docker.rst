Run on Docker
-------------

A C-PAC `Docker image <https://www.docker.com/>`_ is available so that you can easily get an analysis running without needing to install C-PAC.

The Docker image is designed following the specification established by the `BIDS-Apps project <https://github.com/BIDS-Apps>`_, an initiative to create a collection of reproducible neuroimaging workflows that can be executed as self-contained environments using `Docker <https://www.docker.com/>`_ containers.  These workflows take as input any dataset that is organized according to the `Brain Imaging Data Structure (BIDS) standard <http://http://bids.neuroimaging.io>`_ and generating first-level outputs for this dataset. However, you can provide the C-PAC Docker image with a custom non-BIDS dataset by entering your own data configuration file. More details below.

In addition, we have created a Docker default pipeline configuration as part of this initiative that allows you to run the C-PAC pipeline on your data in an environment that is fully provisioned with all of C-PAC's dependencies - more details about the default pipeline are available further below. If you wish to run your own pipeline configuration, you can also provide this to the Docker image at run-time.

To start, first pull the image from Docker Hub:

.. code-block:: console

    docker pull fcpindi/c-pac:latest

Once this is complete, you can use the ``fcpindi/c-pac:latest`` image tag to invoke runs. The full C-PAC Docker image usage options are shown here, with some specific use cases.

As a quick example, in order to run the C-PAC Docker container in participant mode, for one participant, using a BIDS dataset stored on your machine or server, and using the Docker image's default pipeline configuration (broken into multiple lines for visual clarity):

.. code-block:: console

    docker run -i --rm \
            -v /Users/You/local_bids_data:/bids_dataset \
            -v /Users/You/some_folder:/outputs \
            -v /tmp:/tmp \
            fcpindi/c-pac:latest /bids_dataset /outputs participant

Note, the ``-v`` flags map your local filesystem locations to a "location" within the Docker image. (For example, the ``/bids_dataset`` and ``/outputs`` directories in the command above are arbitrary names). If you provided ``/Users/You/local_bids_data`` to the ``bids_dir`` input parameter, Docker would not be able to access or see that directory, so it needs to be mapped first. In this example, the local machine's ``/tmp`` directory has been mapped to the ``/tmp`` name because the C-PAC Docker image's default pipeline sets the working directory to ``/tmp``. If you wish to keep your working directory somewhere more permanent, you can simply map this like so: ``-v /Users/You/working_dir:/tmp``.

You can also provide a link to an AWS S3 bucket containing a BIDS directory as the data source:

.. code-block:: console

    docker run -i --rm \
            -v /Users/You/some_folder:/outputs \
            -v /tmp:/tmp \
            fcpindi/c-pac:latest s3://fcp-indi/data/Projects/ADHD200/RawDataBIDS /outputs participant

In addition to the default pipeline, C-PAC comes packaged with a growing library of pre-configured pipelines that are ready to use. To run the C-PAC Docker container with one of the pre-packaged pre-configured pipelines, simply invoke the ``--preconfig`` flag, shown below. See the full selection of pre-configured pipelines :doc:`here </user/preconfig>`.

.. code-block:: console

    docker run -i --rm \
            -v /Users/You/local_bids_data:/bids_dataset \
            -v /Users/You/some_folder:/outputs \
            -v /tmp:/tmp \
            fcpindi/c-pac:latest /bids_dataset /outputs --preconfig anat-only

To run the C-PAC Docker container with a pipeline configuration file other than one of the pre-configured pipelines, assuming the configuration file is in the ``/Users/You/Documents`` directory:

.. code-block:: console

    docker run -i --rm \
            -v /Users/You/local_bids_data:/bids_dataset \
            -v /Users/You/some_folder:/outputs \
            -v /tmp:/tmp \
            -v /Users/You/Documents:/configs \
            -v /Users/You/resources:/resources \
            fcpindi/c-pac:latest /bids_dataset /outputs participant --pipeline_file /configs/pipeline_config.yml

In this case, we need to map the directory containing the pipeline configuration file ``/Users/You/Documents`` to a Docker image virtual directory ``/configs``. Note we are using this ``/configs`` directory in the ``--pipeline_file`` input flag. In addition, if there are any ROIs, masks, or input files listed in your pipeline configuration file, the directory these are in must be mapped as well- assuming ``/Users/You/resources`` is your directory of ROI and/or mask files, we map it with ``-v /Users/You/resources:/resources``. In the pipeline configuration file you are providing, these ROI and mask files must be listed as ``/resources/ROI.nii.gz`` (etc.) because we have mapped ``/Users/You/resources`` to ``/resources``.

Finally, to run the Docker container with a specific data configuration file (instead of providing a BIDS data directory):

.. code-block:: console

    docker run -i --rm \
            -v /Users/You/any_directory:/bids_dataset \
            -v /Users/You/some_folder:/outputs \
            -v /tmp:/tmp \
            -v /Users/You/Documents:/configs \
            fcpindi/c-pac:latest /bids_dataset /outputs participant --data_config_file /configs/data_config.yml

Note: we are still providing ``/bids_dataset`` to the ``bids_dir`` input parameter. However, we have mapped this to any directory on your machine, as C-PAC will not look for data in this directory when you provide a data configuration YAML with the ``--data_config_file`` flag. In addition, if the dataset in your data configuration file is not in BIDS format, just make sure to add the ``--skip_bids_validator`` flag at the end of your command to bypass the BIDS validation process.

The full list of parameters and options that can be passed to the Docker container are shown below:

.. include:: /user/run/help.rst

Note that any of the optional arguments above will over-ride any pipeline settings in the default pipeline or in the pipeline configuration file you provide via the ``--pipeline_file`` parameter.

**Further usage notes:**

* You can run only anatomical preprocessing easily, without modifying your data or pipeline configuration files, by providing the ``--anat_only`` flag.

* A GUI can be invoked to assist in pipeline customization by specifying the ``GUI`` command line argument, as opposed to ``participant`` (this currently only works for Singularity containers).

* As stated, the default behavior is to read data that is organized in the BIDS format. This includes data that is in Amazon AWS S3 by using the format ``s3://<bucket_name>/<bids_dir>`` for the ``bids_dir`` command line argument. Outputs can be written to S3 using the same format for the ``output_dir``. Credentials for accessing these buckets can be specified on the command line (using ``--aws_input_creds`` or ``--aws_output_creds``).

* When the app is run, a data configuration file is written to the working directory. This file can be passed into subsequent runs, which avoids the overhead of re-parsing the BIDS input directory on each run (i.e. for cluster or cloud runs). These files can be generated without executing the C-PAC pipeline using the test_run command line argument.

* The ``participant_label`` and ``participant_ndx`` arguments allow the user to specify which of the many datasets should be processed, which is useful when parallelizing the run of multiple participants.
