Appendix
========

Installing C-PAC
^^^^^^^^^^^^^^^^

Before You Start
----------------

**WAIT! Installing C-PAC is not required, and is an option for those who want to maintain their own installation, often on a server or cluster. For a faster way to get started:**

C-PAC can be run without installing through any of these three options:

.. include:: /user/run/without_installing.rst

For more details, skip ahead to the :doc:`C-PAC Quickstart </user/quick>` or :doc:`Run C-PAC </user/running>` pages.

Requirements
------------

System Requirements
"""""""""""""""""""
C-PAC is **designed to run in a \*nix-like environment** and thus does not support Windows.  The C-PAC team actively tests C-PAC in Ubuntu Linux, although older versions of that distribution and other \*nixes (such as Mac OS X) should work as well.   As a general rule, C-PAC can operate on any machine capable of reliably running `AFNI <http://afni.nimh.nih.gov/afni>`__ and `FSL <http://fsl.fmrib.ox.ac.uk/fsl/fslwiki/>`__.

Hardware Requirements
"""""""""""""""""""""
* A multiprocessor/multicore system (highly recommended)
* 8 GB of RAM (for computationally-intensive processes such as anatomical registration using ANTS)
* 5.7 GB of free hard disk space (8.3 GB with ANTs)

A Note About the \*nix Command Line
"""""""""""""""""""""""""""""""""""
**This user guide assumes a basic level of experience using the command line.** If you are new to the command line (also known as the terminal), the resources below will help you get started:

* `Getting to Know the Command Line <http://www.davidbaumgold.com/tutorials/command-line/>`__
* Terminals for Absolute Beginners (`Part 1 <http://glennstovall.com/blog/2012/02/15/terminals-for-absolute-beginners/>`__) (`Part 2 <http://glennstovall.com/blog/2012/03/07/terminals-for-absolute-beginners-part-2/>`__)
* `Learning the Shell <http://linuxcommand.org/lc3_learning_the_shell.php>`__
* `Unix Tutorial for Beginners <http://www.ee.surrey.ac.uk/Teaching/Unix/index.html>`__
* `Unix for the Beginning Mage <http://unixmages.com/>`__

Overview
--------
If you are using Ubuntu (version 12/14) you can download and run `cpac_install.sh <https://github.com/FCP-INDI/C-PAC/blob/master/cpac_install.sh?raw=true>`__ with the following terminal commands as root:

.. code-block:: console

    wget https://github.com/FCP-INDI/C-PAC/blob/master/cpac_install.sh?raw=true
    mv cpac_install.sh?raw=true cpac_install.sh
    chmod +x cpac_install.sh
    sudo ./cpac_install.sh -r

This will install all of the prerequisites and resources listed below. If you have previously installed versions of these, they will not be reinstalled, and the script will not check the release version to match the requirements of C-PAC.

.. note::

   This script is intended for Ubuntu Linux 12/14,  but it may work for older releases of Ubuntu.

**For other operating systems**, this page will guide you through the following C-PAC installation steps:

* Installing the required system-level dependencies
* Installing the required Python dependencies
* Installing AFNI and FSL
* Installing C3D and ANTS (optional, but recommended)
* Installing the required C-PAC image resources
* Installing C-PAC itself

It will also provide information on how to:

* Test your installation.
* Upgrade C-PAC to a new version.
* Run C-PAC without installing.

Instructions
------------

Installing System-Level Dependencies
""""""""""""""""""""""""""""""""""""

A complete installation of C-PAC requires that the following dependencies be installed on your OS (and possibly other packages depending on your configuration):

* cmake
* make
* build
* git
* unzip
* libxp
* netpbm
* gcc (with Fortran and C++ compilers and libgfortran)
* The Python developer libraries
* lapack and its developer libraries
* libcanberra (under Linux)
* The Mesa OpenGL utility library
* gsl
* zlib and its developer libraries
* `Graphviz <http://www.graphviz.org/>`__ (optional; required for workflow graphs)
* Xvfb
* libxml
* libxslt
* Python developer libraries

The command to install all of these on Ubuntu 12/14 is:

.. code-block:: console

    sudo apt-get install -y cmake git make unzip libcanberra-gtk-module libxp6 netpbm libglu1-mesa gsl-bin zlib1g-dev graphviz graphviz-dev pkg-config build-essential libxml2-dev libxslt-dev python-dev xvfb

OS-Specific Instructions
''''''''''''''''''''''''

**Mac OS X:**

* Installing system-level and Python dependencies will be made much easier if you download the `Xcode Command Line Tools from Apple <https://developer.apple.com/downloads/index.action>`__ (requires a free Apple account), which includes (among other things) Git and gcc.
* You may want to consider using a package manager such as `Homebrew <http://brew.sh/>`__, `Macports <https://www.macports.org/>`__, or `Fink <http://www.finkproject.org/>`__.

**Ubuntu 16.04:**

* The apt-get command used for Ubuntu 12/14 works with *libxp6* omitted. Unfortunately, libxp is no longer included in the Ubuntu repositories and will need to be compiled from source.  The commands to accomplish this are as follows (note that these commands must be executed as the root user).

.. code-block:: console

    apt-get install autoconf autogen xutils-dev x11proto-print-dev
    cd /tmp
    git clone https://anongit.freedesktop.org/git/xorg/lib/libXp.git
    cd libXp
    ./autogen.sh
    configure
    make
    make install

Installing Python Dependencies
""""""""""""""""""""""""""""""
Please ensure that you are using Python 3.6 and above. Though many computers come with Python pre-installed, C-PAC relies on a number of special-purpose packages, which are listed below. Packages with an asterisk can be installed through `easy_install <https://pythonhosted.org/setuptools/easy_install.html>`__ or pip.  Installing `Anaconda <https://store.continuum.io/cshop/anaconda/>`__ (**64-bit version only**), `Miniconda <http://conda.pydata.org/miniconda.html>`__ or  `Enthought Canopy <https://www.enthought.com/products/canopy/>`__ and using a package manager can simplify installation greatly.  Instructions for Miniconda are given below.

.. note::

   :doc:`cpac (the simple Python commandline interface) <cpac>` and a local installation of C-PAC will conflict if installed in the same environment because both use the same commandline command (``cpac``).

.. note::

   Specific maximum versions are required for the following dependencies. C-PAC is currently (temporarily) not compatible with versions past the following:

* `Nipype <http://nipype.readthedocs.io/en/latest/>`__ - version 1.1.2
* `NetworkX <http://networkx.lanl.gov/>`__ - version 1.11
* `Jinja2 <http://jinja.pocoo.org/docs/intro/#installation>`__ - version 2.7.2

These specific versions can be installed via pip:

.. exec::
    import CPAC

    print('pip install \\')
    for req in CPAC.info.REQUIREMENTS:
        print('    ' + req + ' \\')

The rest of the dependencies are as follows:

* `SciPy <http://www.scipy.org/install.html>`__
* `Nibabel <http://nipy.org/nibabel/>`__
* `Traits <https://github.com/enthought/traits>`__
* `Matplotlib <http://matplotlib.sourceforge.net/>`__
* `PyYAML <http://pyyaml.org/wiki/PyYAML>`__
* `PyLockfile <https://code.google.com/p/pylockfile/>`__
* `Patsy <https://patsy.readthedocs.org/en/latest/>`__
* `Boto 3 <https://boto3.readthedocs.org/en/latest/>`__
* `psutil <https://github.com/giampaolo/psutil>`__
* `INDI-Tools <https://github.com/FCP-INDI/INDI-Tools>`__
* `prov <http://prov.readthedocs.io/en/latest/>`__
* `simplejson <https://simplejson.readthedocs.io/en/latest/>`__
* `pandas <http://pandas.pydata.org/>`__
* `Cython <http://www.cython.org/>`__ (version 12.1 or greater)
* `iPython <http://ipython.org/>`__ (optional)
* `PyGraphviz <http://www.graphviz.org/>`__ (optional; required for workflow graphs)

Miniconda
'''''''''

The following commands will install all the Python dependencies within a Miniconda environment:

.. code-block:: console

   wget http://repo.continuum.io/miniconda/Miniconda-3.8.3-Linux-x86_64.sh
   chmod +x Miniconda-3.8.3-Linux-x86_64.sh
   ./Miniconda-3.8.3-Linux-x86_64.sh -b
   export PATH=~/miniconda/bin:${PATH}
   echo 'export PATH=~/miniconda/bin:${PATH}' >> ~/.bashrc
   conda create -y -n cpac python
   source activate cpac
   conda install -y cython numpy scipy matplotlib networkx==1.11 traits pyyaml jinja2==2.7.2 nose ipython pip wxpython pandas
   pip install lockfile pygraphviz nibabel nipype==1.1.2 patsy psutil boto3 INDI-Tools future==0.15.2 prov simplejson fs==0.5.4
   source deactivate

OS-Specific Instructions
''''''''''''''''''''''''

**Mac OS X:**

* It is recommended that you use either Canopy or Anaconda/Miniconda to install Python packages such as wxPython, SciPy and NumPy.  Manually installing these packages on OS X can be difficult and error-prone.  If you use Anaconda/Conda, the commands above should install all packages seamlessly (assuming you download the Mac OS X Miniconda install script instead of the Linux script when using `wget`).


Installing AFNI and FSL
"""""""""""""""""""""""
C-PAC harnesses the power of two leading neuroimaging software packages (`AFNI <http://afni.nimh.nih.gov/>`__ and `FSL <http://fsl.fmrib.ox.ac.uk/fsl/fslwiki/>`__) to perform key analyses. These packages must be installed before running C-PAC.

To install AFNI on a non-Fedora 21 64-bit Linux machine you may run the follow commands as the super user:

.. code-block:: console

    cd /tmp
    wget http://afni.nimh.nih.gov/pub/dist/tgz/linux_openmp_64.tgz
    tar xfz linux_openmp_64.tgz
    mv linux_openmp_64 /opt/afni

For AFNI to be available globally on your machine, you should then add the following lines to the file located at `/etc/bash.bashrc`:

.. code-block:: console

    export PATH=/opt/afni:$PATH
    export DYLD_FALLBACK_LIBRARY_PATH=/opt/afni

If you open a new shell and type `afni` the AFNI console should now appear.  If not, double-check the lines added to `/etc/bash.bashrc` for typos and make sure that `/opt/afni` contains the AFNI commands.

.. note::

   Regarding the Neurodebian repository: We have encountered compatibility issues in the past with the Neurodebian binary for AFNI.  For this reason, it is suggested that you follow the installation instructions above or the instructions from the AFNI homepage.

.. note::

   On some Ubuntu systems, AFNI can have trouble locating the libgsl.so.0 software library required for some of their tools (3dSkullStrip, and 3dHist). If you experience an error trying to run any of these tools, first attempt to re-install AFNI via the instructions on the AFNI homepage. If this does not resolve the issue, another solution involves locating your system's GSL library and re-configuring:

.. code-block:: console

    locate libgsl
    ldconfig -n /path/to/libgsl

For more details about installing AFNI (including instructions for other architectures) please refer to the AFNI manual `here <https://afni.nimh.nih.gov/pub/dist/doc/htmldoc/background_install/install_instructs/index.html>`__.

To install FSL on a Debian or Ubuntu-based Linux machine you may run the follow commands as the super user to install the `Neurodebian <http://neuro.debian.net/>`__ repository, which contains a pre-packaged version of FSL that integrates seamlessly with the Debian ecosystem:

.. code-block:: console

    wget -O- http://neuro.debian.net/lists/$(lsb_release -cs).us-nh.full | tee /etc/apt/sources.list.d/neurodebian.sources.list
    apt-key adv --recv-keys --keyserver pgp.mit.edu 2649A5A9
    apt-get update

Now install FSL using:

.. code-block:: console

    apt-get install -y fsl-5.0-complete

For FSL to be available globally on your machine, you should then add the following lines to the file located at `/etc/bash.bashrc`:

.. code-block:: console

    FSLDIR=/usr/share/fsl/5.0
    . ${FSLDIR}/etc/fslconf/fsl.sh
    PATH=${FSLDIR}/bin:${PATH}
    export FSLDIR PATH

For more details about installing FSL (including instructions for other architectures) please refer to the FSL documentation `here <http://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FslInstallation>`__.

OS-Specific Instructions
''''''''''''''''''''''''

**Mac OS X:**

* In Mac OS X, you can make it so that a local user account can find AFNI by adding the lines in the instructions above to the :file:`.bashrc` file in your home directory and then adding the following code to the :file:`.bash_profile` file in your home directory.

    .. code-block:: console

        if [ -f ~/.bashrc ]; then
            source ~/.bashrc
        fi

Installing C3D and ANTS (optional, but recommended)
"""""""""""""""""""""""""""""""""""""""""""""""""""
ANTS is an optional, but recommended package for performing image registration / normalization.  ANTS depends upon C3D, which can be installed by following the steps below.  If you do not want to install ANTS, you may skip this step.  You can always install ANTS later.

Installing C3D
''''''''''''''

#. Download C3D from `here <http://sourceforge.net/projects/c3d/>`__ or `here <http://www.nitrc.org/frs/downloadlink.php/1327>`__ (for Mac users).
#. Unzip the downloaded archive, and place the extracted folder in the location of your choosing.

#. Add the following text to your :file:`.bashrc` file:

.. code-block:: console

    export PATH=/path_to/C3D/bin:$PATH

Where :file:`/path_to/C3D` is the location of the extracted folder.

#. Open a new terminal window. Test your installation by running :file:`c3d_affine_tool`. If this fails, see the `Troubleshooting` section below.

**Troubleshooting:**

* If you are given a permissions error, run :file:`chmod -R /path_to/X`, where X is the folder of the package giving you the error.

* If you have added the paths to your :file:`.bashrc` (and :file:`.bash_profile` if necessary) but you are still unable to run the commands above, try adding or removing a trailing / from the paths (e.g. :file:`../bin` vs. :file:`../bin/`). We are working to compile a list of which platforms require the slash and which do not.


Installing ANTS
'''''''''''''''

To install ANTS, follow the instructions below.

For Debian-based platforms, install the Neurodebian keys (see the FSL installation instructions above) and run the following command as the super user:

.. code-block:: console

    apt-get install ants

For other platforms, download ANTS from Github and compile from source:

.. code-block:: console

    cd /tmp
    git clone https://github.com/stnava/ANTs.git

This will create a folder named "ANTS" in the directory where you ran the command from.

Next, create a new directory in a location of your choosing and navigate to it:

.. code-block:: console

    mkdir /opt/ants
    cd /opt/ants

Next, run these commands from this directory to build your ANTS install:

.. code-block:: console

    cmake -c -g /tmp/ANTS
    make -j <number>

Where <number> is how many cores you wish to dedicate to building your install - the more you use, the sooner it will complete. For example, if you want to use four cores, you would run 'make -j 4'.

Once this is complete, you will need to modify your environment. Add the following text to your :file:`.bashrc` file:

.. code-block:: console

    export ANTSPATH=/opt/ants/bin
    export PATH=/opt/ants/bin:$PATH

You can test the installation by opening a new terminal window and running this command:

.. code-block:: console

    antsApplyTransforms

If this returns a help page with a list of parameters, your ANTS installation was a success.

OS-Specific Instructions
''''''''''''''''''''''''

**Mac OS X:**

* Similar to the AFNI and FSL path setup, you must also add the C3D and ANTS paths to your :file:`.bash_profile` file.

Installing ICA-AROMA
""""""""""""""""""""
If you wish to run ICA-AROMA motion artifact de-noising (implemented by Maarten Mennes: `https://github.com/maartenmennes/ICA-AROMA <https://github.com/maartenmennes/ICA-AROMA>`__), you need to install the script first:

.. code-block:: console

    mkdir -p /opt/ICA-AROMA
    curl -sSL "https://github.com/rhr-pruim/ICA-AROMA/archive/v0.4.3-beta.tar.gz" \
        | tar -xzC /opt/ICA-AROMA --strip-components 1
    chmod +x /opt/ICA-AROMA/ICA_AROMA.py

Once this is complete, you will need to modify your environment. Add the following text to your :file:`.bashrc` or :file:`.bash_profile` (if on Mac OS) file:

.. code-block:: console

    export PATH=/opt/ICA-AROMA/ICA_AROMA.py:$PATH

Installing C-PAC Image Resources
""""""""""""""""""""""""""""""""
During preprocessing and analysis, C-PAC utilizes many of the standard brain atlases and tissue maps provided by FSL. Additionally, C-PAC requires the following non-standard files in order to run properly:

* Binarized tissue prior probability maps (used during :doc:`tissue segmentation </user/anat>`)
* Symmetric versions of the MNI152 brain template and masks (used when calculating :doc:`VMHC </user/vmhc>`)

These files are included in the C-PAC Image Resources package, available `here <http://fcon_1000.projects.nitrc.org/indi/cpac_resources.tar.gz>`__. You may install these files using the following commands or use the included script (install_resources.sh):

.. code-block:: console

    cd /tmp
    wget http://fcon_1000.projects.nitrc.org/indi/cpac_resources.tar.gz
    tar xfz cpac_resources.tar.gz
    cd cpac_image_resources
    cp -n MNI_3mm/* $FSLDIR/data/standard
    cp -n MNI_4mm/* $FSLDIR/data/standard
    cp -n symmetric/* $FSLDIR/data/standard
    cp -nr tissuepriors/2mm $FSLDIR/data/standard/tissuepriors
    cp -nr tissuepriors/3mm $FSLDIR/data/standard/tissuepriors
    cp -nr tissuepriors/4mm $FSLDIR/data/standard/tissuepriors
    cp -n HarvardOxford-lateral-ventricles-thr25-2mm.nii.gz $FSLDIR/data/atlases/HarvardOxford

These commands perform the following steps:

* The image resources are downloaded.

* 3mm and 4mm MNI tempaltes are copied to the :file:`/data/standard` directory of your FSL installation.

* Files located in the :file:`/symmetric` folder of the C-PAC Image Resources directory are copied to the :file:`/data/standard` directory of your FSL installation.

* The :file:`/2mm` and :file:`/3mm` folders located in C-PAC Image Resources directory are copied to :file:`/data/standard/tissuepriors` directory of your FSL installation.

Installing C-PAC
""""""""""""""""
Congratulations, you are now ready to install C-PAC itself!

C-PAC is available for download from the `C-PAC Homepage <http://fcp-indi.github.com/>`__. Click the button labeled "Download as tar.gz". Unpack the downloaded archive and navigate to the new directory. To install C-PAC, run the command ``sudo python setup.py install``. C-PAC will be installed alongside your other python packages. If this fails, check to make sure that you have all the dependencies installed.  You may also install C-PAC using the commands below:

 .. code-block:: console

   cd /tmp
   git clone https://github.com/FCP-INDI/C-PAC.git
   cd C-PAC
   python setup.py install

Testing Your C-PAC Installation
'''''''''''''''''''''''''''''''
In a new terminal window, open iPython (or Python) and enter the command ``import CPAC``. If installation was successful, this will execute without an error and present you with a blank new line. If you encounter an error (e.g. ``no module named C-PAC``), try re-running the C-PAC install command above. If this does not work, see the :doc:`Troubleshooting and Help Page </user/help>`.  Note that if you do not open a new terminal window and are still within the C-PAC installation directory ('C-PAC'), you may encounter errors that can be alleviated by leaving the 'C-PAC' directory.

Once you are able to successfully ``import CPAC`` it is safe to delete any setup files downloaded during the install process (e.g. Nipype and C-PAC downloads, FSL install scripts, etc.), as they are no longer needed.

.. note::

   The test process described here only acts to confirm that the C-PAC python package (the core package, not :doc:`the simple Python commandline interface with the same name <cpac>`) has been correctly installed. To fully test C-PAC on your system, please see the :doc:`Benchmark Page </user/benchmark>`.

Updating C-PAC
""""""""""""""
C-PAC is being actively developed, and new versions (containing bug fixes and new features) are often released. To update to the latest version, simply download it from the `C-PAC Homepage <http://fcp-indi.github.com/>`__ and repeat the instructions in the `Installing C-PAC` section above. A list of previous versions and the changes they contain is available on the :doc:`Release Notes Page </user/rnotes>`.

.. note::

   If you are using Anaconda/Miniconda you may also use the following command (replacing 'cpac' with your environment name) to remove an old environment before creating a new environment to replace it.**

 .. code-block:: console

    conda remove --all -n cpac

Running C-PAC Without Installing
""""""""""""""""""""""""""""""""

Users wishing to run C-PAC without installing it can do so by copying the downloaded C-PAC directory to the location of their choice. C-PAC can then be run by opening iPython (or Python) from within this directory. This is useful in cases where a user does not have sufficient privileges to install Python packages, but is running on a machine that already contains all C-PAC dependencies.

Some network centrality features will not be available without compiling the C-based elements. In order to do this without installing the rest of C-PAC, simply use the following command

.. code-block:: console

    python setup.py build_ext --inplace

.. note::

   Unfortunately, it is not possible at this time to use the C-PAC GUI without installing C-PAC.

.. include:: benchmark.rst