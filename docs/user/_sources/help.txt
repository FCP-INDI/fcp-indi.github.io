Troubleshooting and Help
------------------------

C-PAC is beta software, which means that it is still under active development and has not yet undergone large-scale testing. As such, although we have done our best to ensure a stable pipeline, there may still be a few bugs that we did not catch.
 

If you find a bug, would like to request a new feature, or have a question that is not answered in the User Guide, please visit `GitHub Issues page for CPAC <https://github.com/FCP-INDI/C-PAC/issues>`_.

Viewing Crash Files
^^^^^^^^^^^^^^^^^^^
Crash files are written as compressed numpy arrays, and can be viewed by executing the following command in iPython::

    from nipype.utils.filemanip import loadflat
    crashinfo = loadflat('crashfile.npz')
    %pdb
    crashinfo['node'].run()  # re-creates the crash
    pdb> up  #typically, but not necessarily the crash is one stack frame up
    pdb> inspect variables
    pdb>quit

Where :file:`crashfile.npz` is the name of the crash file you wish to view.

