Unlike most lines in a C-PAC pipeline configuration file, the keys under ``*_roi_paths`` are user-definable.

If you exclude ``*_roi_paths`` from your pipeline configuration, the default atlases and analyses will be used.

If you include ``*_roi_paths``, **only the atlases and analyses provided** will be used, unless you add the optional key/value pair ``roi_paths_fully_specified: False`` in the relevant section, in which case the default atlases and analyses will be updated with the atlases and analyses specified in your pipeline config. For example,

.. code-block:: yaml

    timeseries_extraction:
        roi_paths_fully_specified: False

    seed_based_correlation_analysis:
        roi_paths_fully_specified: False

would keep any default atlases not respecified in your pipeline configuration.