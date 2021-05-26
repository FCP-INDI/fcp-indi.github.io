:orphan:

Output Settings
----------------

.. figure:: /_images/output_gui.png

#. **Working Directory - [path]:** Directory where CPAC should store temporary and intermediate files.  *Path should not contain spaces.*

#. **Output Directory - [path]:** Directory where CPAC should place processed data.  This can also be an S3 bucket path prepended with 's3://'.  *Path should not contain spaces.*

#. **Log Directory - [path]:** Directory where CPAC should place run logs.  *Path should not contain spaces.*

#. **Crash Log Directory - [path]:** Directory where CPAC should write crash logs.  *Path should not contain spaces.*

#. **AWS Output Bucket Credentials (optional) - [path]:**  If setting the *Output Directory* to an S3  bucket, insert the path to your AWS credentials file here.,

#. **S3 Encryption - [On, Off]:** Enable server-side 256-AES encryption on data to the S3 bucket,

#. **Write Extra Functional Outputs - [On, Off]:** Include extra versions and intermediate steps of functional preprocessing in the output directory.

#. **Write Debugging Outputs - [On, Off]:** Include extra outputs in the output directory that may be of interest when more information about intermediate steps is needed.

#. **Enable logging - [On, Off]:** Whether to write log details of the pipeline. run to the logging files..

#. **Remove Working Directory [On, Off]:** Deletes the contents of the Working Directory after running.  This saves disk space, but any additional preprocessing or analysis will have to be completely re-run.)

#. **Create organized output directory - [On, Off]:** Create a simplified version of the output directory.

#. **Regenerate Outputs - [On, Off]:**  Uses the contents of the working directory to regenerate all outputs and their symbolic links.  Requires an intact working directory from a previous C-PAC run.

#. **Enable Quality Control Interface - [On, Off]:** Generate quality control pages containing preprocessing and derivative outputs.

.. include:: /user/pipelines/without_gui.rst

.. literalinclude:: /references/default_pipeline.yml
   :language: YAML
   :lines: 10-80,138-149
