Run on Singularity
------------------

For those who wish to avoid the administrator rights requirements often associated with Docker usage (or the security hazards when used on a shared computing system), `Singularity <https://apptainer.org/docs-legacy>`_ is a good option. Singularity is a container solution just like Docker, except it is designed specifically to offer secure deployment on shared cluster environments.

You can pull a Singularity container much like how you would pull a Docker container:

.. code-block:: console

    singularity pull docker://fcpindi/c-pac:latest

This will produce a Singularity container image in your current directory, named something like ``c-pac_latest.sif``. You can instead specify the local filename you want before the ``docker://`` URI.

Running a Singularity image is similar to running a Docker image, except ``-B`` maps local directories to a location in the Singularity image instead of ``-v``:

.. code-block:: console

    singularity run \
            -B /Users/You/local_bids_data:/bids_dataset \
            -B /Users/You/some_folder:/outputs \
            -B /tmp:/tmp \
            FCP-INDI-C-PAC-master-latest.simg \
            /bids_dataset \
            /outputs \
            participant

Again, you can also provide an AWS S3 link for the data:

.. code-block:: console

    singularity run \
            -B /Users/You/some_folder:/outputs \
            -B /tmp:/tmp \
            FCP-INDI-C-PAC-master-latest.simg \
            s3://fcp-indi/data/Projects/ADHD200/RawDataBIDS \
            /outputs \
            participant

As mentioned above, in addition to the default pipeline, C-PAC comes packaged with a growing library of pre-configured pipelines that are ready to use. Once again, you can use the ``--preconfig`` flag with Singularity to run any of the pre-configured pipelines. See the full selection of pre-configured pipelines :doc:`here </user/pipelines/preconfig>`.

.. code-block:: console

    singularity run \
            -B /Users/You/some_folder:/outputs \
            -B /tmp:/tmp \
            FCP-INDI-C-PAC-master-latest.simg \ 
            s3://fcp-indi/data/Projects/ADHD200/RawDataBIDS \
            /outputs \
            participant \
            --preconfig anat-only
