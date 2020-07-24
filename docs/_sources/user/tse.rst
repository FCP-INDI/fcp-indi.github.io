Timeseries Extraction
=====================
C-PAC lets you easily export BOLD timeseries in a number of different ways. This can be useful for those wishing to undertake advanced analysis not included in C-PAC, but still take advantage of its robust pre-processing features. For instructions on how to use these seeds within C-PAC
, please see :doc:`Seed-based Correlation Analysis </user/sca>`.

ROI Timeseries Extraction allows you to export the timeseries for one or more regions of interest (ROIs). This is done by calculating the average timeseries across all voxels within an ROI. As such, C-PAC will output one timeseries for each ROI specified by you.

.. figure:: /_images/roi_timeseries.png

When an ROI is placed within a functionally homogeneous area, averaging signals in this way can produce a timeseries which may more accurately reflect the overall activity pattern in the region than does the timeseries of any individual voxel. Voxel Timeseries Extraction will export the individual timeseries of all voxels within one or more masks.

.. figure:: /_images/voxel_timeseries.png

Configuring ROI Time Series Extraction
======================================

.. figure:: /_images/tse_gui.png

#. **Time Series Extraction- [On,Off]:**  Extract the average time series of one or more ROIs/seeds. Must be enabled if you wish to run seed-based correlation analysis.

#. **TSE ROI Image - [path]:** Clicking on the *+* icon to the bottom-right of the box here will bring up a dialog where you can define multiple paths to NifTIs containing ROI masks.  You may add multiple ROIs to the box.  Three columns within the box can be checked on and off to enable specific types of TSE:
    * Avg - For each ROI, output the average of the all the voxel time series within that ROI.
    * Voxel - For each ROI, output the individual voxel time series for all voxels within that ROI.
    * SpatialReg - Use a spatial map as a spatial regressor in a GLM to find the time series associated with the voxels in that map (see :doc:`dual regression </user/sca>`).

#. **Realignment - [ROI to func, func to ROI]:** Choose functional time-series and ROI realignment method. 'ROI to func' will realign the atlas/ROI to functional space (fast). 'func to ROI' will realign the functional time series to the atlas/ROI space. NOTE: in rare cases, realigning the ROI to the functional space may result in small misalignments for very small ROIs - please double check your data if you see issues.

#. **Outputs - [CSV, NUMPY]:** Choose to save voxelwise time series extraction outputs as a csv file or a Numpy array.  Voxelwise TSE outputs are saved as a text file and 1D file by default.  ROI Average TSE outputs are saved as a tab-delimited value file ('roi_stats.csv') only.

Configuration Without the GUI
""""""""""""""""""""""""""""""

The following key/value pairs must be defined in your :doc:`pipeline configuration YAML </user/pipeline_config>` for C-PAC to run time series extraction:

.. csv-table::
    :header: "Key","Description","Potential Values"
    :widths: 5,30,15
    :file: ../_static/params/tse_roi_config.csv

The box below contains an example of what these parameters might look like when defined in the YAML::

    runROITimeseries :  [1]
    realignment : ['ROI_to_func']
    tsa_roi_paths:
        - s3://fcp-indi/resources/cpac/resources/CC400.nii.gz: Avg
          s3://fcp-indi/resources/cpac/resources/PNAS_Smith09_rsn10.nii.gz: SpatialReg
    roiTSOutputs :  [True, True]
