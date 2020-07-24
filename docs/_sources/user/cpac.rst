cpac (Python package)
---------------------

`cpac <https://pypi.org/project/cpac/>`_ is available so that you can easily run analyses without needing interact with the container platform that allows you to run C-PAC without installing all of the underlying software.

Currently the cpac supports Singularity (version ≥ 2.5 ≤ 3.0) and Docker.

cpac requires Python 3.6 or greater. To get cpac, simply

.. code-block:: console

    pip install cpac

As a quick example, in order to run C-PAC in participant mode, for one participant, using a BIDS dataset stored on your machine or server, and using the container image's default pipeline configuration:

.. code-block:: console

    cpac run /Users/You/local_bids_data /Users/You/some_folder_for_outputs participant

By default, the cpac will try Docker first and fall back to Singularity if Docker fails. If both fail, an exception is raised.

You can specify a platform with the ``--platform docker`` or ``--platform singularity``. If you specify a platform without specifying an image, these are the defaults, using the first successfully found image:

Usage
`````
.. include:: /user/cpac/help.txt

``--platform docker``
*********************

* Look for ``fcpindi/c-pac:latest`` locally.
* Pull ``fcpindi/c-pac:latest`` from Docker Hub.

``--platform singularity``
**************************

* Look in the present working directory for any Singularity images. If more than one is found, use the most recently modified.
* Pull ``FCP-INDI/C-PAC`` from Singularity Hub.
* Pull ``fcpindi/c-pac:latest`` from Docker Hub and convert to a Singularity image.

You can also specify a container image with an ``--image`` argument, passing an image name (e.g., ``fcpindi/c-pac``) for a Docker image or a filepath (e.g. ``~/singularity_images/C-PAC.sif``) for a Singularity image. You can also specify a ``--tag`` (e.g., ``latest`` or ``nightly``).

You can also provide a link to an AWS S3 bucket containing a BIDS directory as the data source:

.. code-block:: console

    cpac run s3://fcp-indi/data/Projects/ADHD200/RawDataBIDS /Users/You/some_folder_for_outputs participant

In addition to the default pipeline, C-PAC comes packaged with a growing library of pre-configured pipelines that are ready to use. To run C-PAC with one of the pre-packaged pre-configured pipelines, simply invoke the ``--preconfig`` flag, shown below. See the full selection of pre-configured pipelines :doc:`here </preconfig>`.

.. code-block:: console

    cpac run /Users/You/local_bids_data /Users/You/some_folder_for_outputs --preconfig anat-only

To run C-PAC with a pipeline configuration file other than one of the pre-configured pipelines, assuming the configuration file is in the ``/Users/You/Documents`` directory:

.. code-block:: console

    cpac run /Users/You/local_bids_data /Users/You/some_folder_for_outputs participant --pipeline_file /Users/You/Documents/pipeline_config.yml

Finally, to run C-PAC with a specific data configuration file (instead of providing a BIDS data directory):

.. code-block:: console

    cpac run /Users/You/any_directory /Users/You/some_folder_for_outputs participant --data_config_file /Users/You/Documents/data_config.yml

Note: we are still providing the postionally-required ``bids_dir`` input parameter. However C-PAC will not look for data in this directory when you provide a data configuration YAML with the ``--data_config_file`` flag. Providing ``.`` or ``$PWD`` will simply pass the present working directory. In addition, if the dataset in your data configuration file is not in BIDS format, just make sure to add the ``--skip_bids_validator`` flag at the end of your command to bypass the BIDS validation process.

The full list of parameters and options that can be passed to C-PAC are shown below:

.. include:: /user/run/help.txt

.. include:: /user/utils/help.txt

Note that any of the optional arguments above will over-ride any pipeline settings in the default pipeline or in the pipeline configuration file you provide via the ``--pipeline_file`` parameter.

**Further usage notes:**

* You can run only anatomical preprocessing easily, without modifying your data or pipeline configuration files, by providing the ``--anat_only`` flag.

* As stated, the default behavior is to read data that is organized in the BIDS format. This includes data that is in Amazon AWS S3 by using the format ``s3://<bucket_name>/<bids_dir>`` for the ``bids_dir`` command line argument. Outputs can be written to S3 using the same format for the ``output_dir``. Credentials for accessing these buckets can be specified on the command line (using ``--aws_input_creds`` or ``--aws_output_creds``).

* When the app is run, a data configuration file is written to the working directory. This directory can be specified with ``--working_dir`` or the directory from which you run ``cpac`` will be used. This file can be passed into subsequent runs, which avoids the overhead of re-parsing the BIDS input directory on each run (i.e. for cluster or cloud runs). These files can be generated without executing the C-PAC pipeline using the ``test_run`` command line argument.

* The ``participant_label`` and ``participant_ndx`` arguments allow the user to specify which of the many datasets should be processed, which is useful when parallelizing the run of multiple participants.

* If you want to pass runtime options to your container plaform (Docker or Singularity), you can pass them with ``-o`` or ``--container_options``.