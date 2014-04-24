Installing CPAC
----------------

Installation Overview
^^^^^^^^^^^^^^^^^^^^^
If you are using Ubuntu (version 12.04 or newer) you can download, unzip, and run `cpac_install_ubuntu.tar.gz <https://github.com/FCP-INDI/C-PAC/blob/master/scripts/cpac_install_ubuntu.tar.gz?raw=true>`_ with the following terminal commands

.. code-block:: bash

    wget https://github.com/FCP-INDI/C-PAC/blob/master/scripts/cpac_install_ubuntu.tar.gz?raw=true
    tar -xzvf cpac_install_ubuntu.tar.gz
    sudo ./cpac_install.sh
    
This will install all of the prerequisites and resources listed below. If you have previously installed versions of these, they will not be reinstalled, and the script will not check the release version to match the requirements of CPAC.

**Note**: this is only rigorously tested on Ubuntu 12.04 and newer, but it may work for older releases of Ubuntu if the prerequisite packages are up to date.

**For other operating systems**, this page will guide you through the following CPAC installation steps:

* Installing the required Python dependencies (either manually or through Canopy).
* Installing Nibabel and Nipype.
* Installing AFNI and FSL.
* Installing required CPAC Image Resources.
* Installing CPAC itself.

It will also provide information on how to:

* Test your installation.
* Upgrade CPAC to a new version.
* Run CPAC without installing.


System Requirements
^^^^^^^^^^^^^^^^^^^
CPAC is **designed to run in a Unix-like environment** such as Linux or Mac OS X, and thus does not support Windows.

Although CPAC should run on most computers made in the past few years, **we highly recommend using a system with multiple cores or multiple processors**, as many of the analyses carried out by CPAC are computationally intensive. As a general rule, CPAC will run on any machine capable of reliably running `AFNI <http://afni.nimh.nih.gov/afni>`_ or `FSL <http://fsl.fmrib.ox.ac.uk/fsl/fslwiki/>`_.

A Note About the Command Line
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**This User Guide assumes a basic level of experience using the command line.** If you are new to the command line (also known as the terminal), the resources below can help you get started.

* `Getting to Know the Command Line <http://www.davidbaumgold.com/tutorials/command-line/>`_
* Terminals for Aboslute Beginners (`Part 1 <http://glennstovall.com/blog/2012/02/15/terminals-for-absolute-beginners/>`_) (`Part 2 <http://glennstovall.com/blog/2012/03/07/terminals-for-absolute-beginners-part-2/>`_)
* `Learning the Shell <http://linuxcommand.org/lc3_learning_the_shell.php>`_
* `Unix Tutorial for Beginners <http://www.ee.surrey.ac.uk/Teaching/Unix/index.html>`_
* `Unix for the Beginning Mage <http://unixmages.com/>`_


Platform Specific Instructions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The following instructions provide additional information about the peculiarities of installing CPAC and it's dependencies on various operating systems.

**Mac OS X:** 

* Before installing python dependencies, please download and install the `Xcode Command Line Tools from Apple <https://developer.apple.com/downloads/index.action>`_ (requires a free Apple account).
* Manually installing wxPython, SciPy and NumPy on OS X can be difficult. We therefore strongly recommend you use Canopy or Anaconda, which have user-friendly install-managers for these packages. (see tip_ below)


**Ubuntu, Debian-based systems:**

* wxPython should also be installed through ``apt`` unless you are using Enthought Canopy or Anaconda (see tip_ below).

Install Python Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Python is the glue (Bloom, 2012) that ties all the pieces of CPAC together. Though many computers come with Python pre-installed, CPAC relies on a number of special-purpose packages, which are listed below. Packages with an asterisk (*) can be installed through `setuptools <https://pythonhosted.org/setuptools/easy_install.html>`_ by running the command ``easy_install package`` (for example, ``easy_install networkx``).

* `SciPy and NumPy <http://www.scipy.org/install.html>`_ 
* `NetworkX <http://networkx.lanl.gov/>`_ * (``easy_install networkx``)
* `Traits <https://github.com/enthought/traits>`_ * (``easy_install traits``)
* `Matplotlib <http://matplotlib.sourceforge.net/>`_ * (``easy_install matplotlib``)
* `wxPython <http://www.wxpython.org/>`_
* `PyYAML <http://pyyaml.org/wiki/PyYAML>`_ * (``easy_install pyyaml``)
* `Jinja2 <http://jinja.pocoo.org/docs/intro/#installation>`_ * (``easy_install jinja2``)
* `PyLockfile <https://code.google.com/p/pylockfile/>`_ * (``easy_install lockfile``)
* `Cython <http://www.cython.org/">`_ (version 12.1 or greater)  * (``easy_install Cython``)
* `iPython <http://ipython.org/>`_ (optional)
* `Graphviz <http://www.graphviz.org/>`_ (optional; required for workflow graphs)

.. _tip: 

**TIP**: It is possible to install many of these packages (all but PyLockfile) automatically by using `Enthought Canopy <https://www.enthought.com/products/canopy/>`_. If you chose to use Canopy, you must download the **64-bit version**

It is possible to install many of these packages (all but PyLockfile) automatically by using `Enthought Canopy <https://www.enthought.com/products/canopy/>`_. If you chose to use Canopy, you must download the **64-bit version**. Likewise, `Anaconda <https://store.continuum.io/cshop/anaconda/>`_ is an alternative Python distribution which allows you to install the above packages with the `conda command <http://docs.continuum.io/anaconda/faq.html#install-packages>`_.
    ex: ``conda install -c https://conda.binstar.org/travis wxpython``

Install Nibabel and Nipype
^^^^^^^^^^^^^^^^^^^^^^^^^^
CPAC relies heavily on tools developed as part of the `Neuroimaging in Python project <http://nipy.sourceforge.net/nipy/stable/index.html>`_. Specifically, `Nipype <http://nipy.sourceforge.net/nipype/>`_ and `Nibabel <http://nipy.sourceforge.net/nibabel/>`_ must be installed for CPAC to run.

To install Nibabel, run the command ``easy_install nibabel``.

To install Nipype, first download, `click here <https://github.com/nipy/nipype/releases/tag/0.9.1>`_ the package from Github. CPAC requires Nipype 0.9.1, will not work with other versions.

Open a terminal window and unpack the file using the following command

.. code-block:: bash

    tar -xzvf filename.tar.gz

Where :file:`filename.tar.gz` is the name of the file you just downloaded.

This will result in a new directory containing Nipype files. Navigate to this directory and run the following command to install Nipype

.. code-block:: bash

    python setup.py install


Install AFNI and FSL
^^^^^^^^^^^^^^^^^^^^
CPAC harnesses the power of two leading neuroimaging software packages (`AFNI <http://afni.nimh.nih.gov/>`_ and `FSL <http://fsl.fmrib.ox.ac.uk/fsl/fslwiki/>`_) to perform key analyses. These packages must be installed before running CPAC. 

For instructions on how to install AFNI, `click here <http://afni.nimh.nih.gov/pub/dist/HOWTO/howto/ht00_inst/html/>`_. Downloading AFNI should take approximately 5 minutes on a standard broadband connection. **Mac Users:** If you are using OS X 10.7 or greater, we recommend doing a 

For instructions on how to install FSL, `click here <http://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FslInstallation>`_. Users should ensure they download and install FSL -5.0. Downloading FSL should take approximately 15 minutes on a standard broadband connection. 

**Mac OS X:**

* FSL - Follow the instructions on the `FSL Download Page <http://fsl.fmrib.ox.ac.uk/fsldownloads/fsldownloadmain.html>`_.
* AFNI - Follow the instructions to do a `Basic Install <http://afni.nimh.nih.gov/pub/dist/HOWTO/howto/ht00_inst/html/mac_10.78.html>`_.

**Ubuntu and NeuroDebian:**

* FSL - ``apt-get install fsl-5.0``
* AFNI - ``apt-get install afni``


Check AFNI and FSL Paths
""""""""""""""""""""""""
Application paths for AFNI and FSL should have been added to your user profile when they were installed, but it is useful to double-check this before continuing (as the absence of these paths is a common cause of CPAC errors). If the application paths have been set properly, you should be able to open AFNI and FSL by running the commands ``afni`` and ``fsl`` in a new terminal window.

If either of these commands fail, you will have to add the AFNI and FSL application paths manually. To do this, run the command ``nano ~/.bashrc``. This will open your :file:`.bashrc` file in the `nano text editor <http://mintaka.sdsu.edu/reu/nano.html>`_. Scroll to the bottom of the file (navigate using the arrow keys on your keyboard) and paste the following text

.. code-block:: bash

    # Path to FSL
    FSLDIR=/path/to/fsl
    . ${FSLDIR}/etc/fslconf/fsl.sh
    PATH=${FSLDIR}/bin:${PATH}
    export FSLDIR PATH

    # Path to AFNI
    export PATH=$PATH:/path/to/afni
    export DYLD_FALLBACK_LIBRARY_PATH=/path/to/afni

Where :file:`/path/to/fsl` and :file:`/path/to/afni` are the locations where FSL and AFNI are installed (by default, these are :file:`/usr/local/fsl` for FSL and :file:`~/abin` for AFNI). When you have added the paths, save your changes (control + O) and exit nano (control + X).

**Mac Users:** You must also add these paths to your :file:`.bash_profile` file. Simply follow the same instructions above but replace ``nano ~/.bashrc`` with ``nano ~/.bash_profile``.

**tcsh Users:** Add these paths to your ``.cshrc`` file.

To confirm that the changes have worked, open a new terminal window and try again to open AFNI and FSL.

Install ANTS (Optional)
^^^^^^^^^^^^^^^^^^^^^^^
If you wish to use ANTS for anatomical registration, follow the instructions below. It is also possible to skip this step now and choose to install ANTS later.

**ANTS:**

Download the latest version of ANTS (`found here <http://sourceforge.net/projects/advants/>`_). Unzip the downloaded archive, and place the extracted folder in a location of your choosing. Add the following text to your :file:`.bashrc` file (Mac Users: You must also add this text to your :file:`.bash_profile`.)

.. code-block:: bash

    export PATH=/path_to/ANTS/bin:$PATH
    export ANTSPATH=/path_to/ANTS/bin

Where :file:`/path_to/ANTS` is the location of the extracted folder.

Open a new terminal window. Test your installation by running :file:`antsIntroduction.sh`. If this fails, see the Troubleshooting section below.

Because of differences between the compiled binaries (which you have just downloaded and installed) and the version of ANTS which has been implemented in CPAC, you will need to manually replace your existing copy of :file:`antsIntroduction.sh` with the version available on Github. To do this, delete the copy of this file on your local machine, and replace it with the version available for `download here <https://raw.github.com/stnava/ANTs/master/Scripts/antsIntroduction.sh>`_.

When this is done, confirm that this has worked by re-running the :file:`antsIntroduction.sh` command in terminal.

**C3D:**

In order to use ANTS, you must also install C3D (found `here <http://sourceforge.net/projects/c3d/>`_ or `here for macs <http://www.nitrc.org/frs/downloadlink.php/1327>`_). Unzip the downloaded archive, and place the extracted folder in the location of your choosing. Add the following text to your :file:`.bashrc` file (Mac Users: You must also add this text to your :file:`.bash_profile`.)

.. code-block:: bash

    export PATH=/path_to/C3D/bin:$PATH

Where :file:`/path_to/C3D` is the location of the extracted folder.

Open a new terminal window. Test your installation by running :file:`c3d_affine_tool`. If this fails, see the Troubleshooting section below.

**Troubleshooting:**

* If you are given a permissions error, run :file:`chmod -R /path_to/X`, where X is the folder of the package giving you the error.

* If you have added the paths to your :file:`.bashrc` (and :file:`.bash_profile` if necessary) but you are still unable to run the commands above, try adding or removing a trailing / from the paths (e.g. :file:`../bin` vs. :file:`../bin/`). We are working to compile a list of which platforms require the slash and which do not.

Install CPAC Image Resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
During preprocessing and analysis, CPAC utilizes many of the standard brain atlases and tissue maps provided by FSL. Additionally, CPAC requires the following non-standard files in order to run properly.

* Binarized tissue prior probability maps (used during :doc:`tissue segmentation </anat>`)
* Symmetric versions of the MNI152 brain template and masks (used when calculating :doc:`VMHC </vmhc>`)

These files are included in the CPAC Image Resources package, available `for download here <http://fcon_1000.projects.nitrc.org/indi/cpac_resources.zip>`_. As above, this file can be unpacked by running the ``tar -xzvf`` command. 

Included in the package is a ``install_resources.sh`` script that when run will copy the resource files to your FSL directory (which is where CPAC looks for them by default). To run this script, navigate to the CPAC Image Resources directory and run the command ``sudo bash install_resources.sh``.

Users wishing to manually install these files can do so by following the directions below.

* Files located in the :file:`/symmetric` folder of the CPAC Image Resources directory should be copied to the :file:`/data/standard` directory of your FSL installation.

* The :file:`/2mm` and :file:`/3mm` folders located in CPAC Image Resources directory should be copied to :file:`/data/standard/tissuepriors` directory of your FSL installation.


Install CPAC
^^^^^^^^^^^^
Congratulations, you are now ready to install CPAC itself!

CPAC is available for download from the `CPAC Homepage <http://fcp-indi.github.com/>`_. Click the button labeled "Download as tar.gz". As above, unpack the downloaded archive and navigate to the new directory. To install CPAC, run the command ``sudo python setup.py install``. CPAC will be installed alongside your other python packages. If this fails, make sure you have all the dependencies installed.


Test CPAC Installation
""""""""""""""""""""""
In a new terminal window, open iPython (or Python) and enter the command ``import CPAC``. If installation was successful, this will execute without an error and present you with a blank new line. If you encounter an error (e.g. ``no module named CPAC``), try re-running the CPAC install command above. If this does not work, see the :doc:`Troubleshooting and Help Page </help>`.

Once you are able to successfully ``import CPAC`` it is safe to delete any setup files downloaded during the install process (e.g. Nipype and CPAC downloads, FSL install scripts, etc.), as they are no longer needed.

**Note:** The test process described here only acts to confirm that the CPAC python package has been correctly installed. To fully test CPAC on your system, please see the :doc:`Benchmark Page </benchmark>`.

Updating CPAC
^^^^^^^^^^^^^
CPAC is being actively developed, and new versions (containing bug fixes and new features) are released approximately once a month. To update to the latest version, simply download it from the `CPAC Homepage <http://fcp-indi.github.com/>`_ and repeat the instructions in the "Install CPAC" section above. A list of previous versions and the changes they contain is available on the :doc:`Release Notes Page </rnotes>`.

Running CPAC Without Installing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Users wishing to run CPAC without installing it can do so by copying the downloaded CPAC directory to the location of their choice. CPAC can then be run by opening iPython (or Python) from within this directory. This is useful in cases where a user does not have sufficient privledges to install Python packages, but is running on a machine that already contains all CPAC dependencies.

Some network centrality features will not be available without compiling the C-based elements. In order to do this without installing the rest of CPAC, simply use the following command

.. code-block:: bash

    python setup.py build_ext --inplace

**Note:** Unfortunately, it is not possible at this time to use the CPAC GUI without installing CPAC.

References
^^^^^^^^^^
Bloom, J. `Python as Super Glue for the Modern Scientific Workflow <http://www.youtube.com/watch?v=mLuIB8aW2KA>`_, video of a talk given at the SciPy2012 conference.
