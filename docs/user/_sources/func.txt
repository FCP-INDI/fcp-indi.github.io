Functional Preprocessing
------------------------


Timeseries Options
^^^^^^^^^^^^^^^^^^
startIdx and stopIdx
""""""""""""""""""""
Users wishing to discard the first few volumes of a scan (to facilitate stable magnetization) can specify a starting volume here::

    # Ignore volumes before this timepoint
    # Options are an integer or None (defaults to beginning of timeseries)
    startIdx = 0

Users can also chose to ignore volumes after a specific timepoint::

    # Ignore volumes after this timepoint
    # Options are an integer or None (defaults to end of timeseries)
    stopIdx = None

TR
"""
If the actual TR used during scanning is different than what is specified in the image header, you can specify that value here::

    # Specify a TR (in seconds) other than what is listen in image headers
    # Options are a number or None (defaults to header information)
    TR = None

