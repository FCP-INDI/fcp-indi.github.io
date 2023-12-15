Regression Testing
^^^^^^^^^^^^^^^^^^

Regression testing for C-PAC involves several repositories.

.. container:: svg-flowchart

    .. raw:: html
        :file: ../../../_static/flowcharts/regression_suite.svg

    `Open image <../../../_static/flowcharts/regression_suite.svg>`_

GitHub repository environment
-----------------------------

The GitHub repository `FCP-INDI/C-PAC`_ has an environment called ``ACCESS`` that contains the necessary secrets and variables for running the regression test continuous integration:

secrets
*******
.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Name
     - Description
   * - ``$GH_CLI_BIN_PATH``
     - Path to GitHub CLI executable.
   * - ``$SSH_HOST``
     - ``host`` parameter for the GitHub Action `SSH Remote Commands`_. The host on which to run the automated regression tests.
   * - ``$SSH_PRIVATE_KEY``
     - ``key`` parameter for the GitHub Action `SSH Remote Commands`_. Must be a valid SSH private key for ``${SSH_USER}@${SSH_HOST}``.
   * - ``$SSH_USER``
     - ``username`` parameter for the GitHub Action `SSH Remote Commands`_. The user to sign into ``${SSH_HOST}`` as.
   * - ``$SSH_WORK_DIR``
     - Working directory on ``${SSH_HOST}`` in which to run automated regression tests.

variables
*********
.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Name
     - Description
   * - ``$DASHBOARD_REPO``
     - Owner/repo-name of `amygutierrez/regression_dashboard`_ or the relevant fork or drop-in replacement for calculating and reporting correlations from a remote server.
   * - ``$SLURM_TESTING_REPO``
     - Owner/repo-name of `cmi-dair/slurm_testing`_ or the relevant fork or drop-in replacement for running test runs on a remote server.

If you want to run automated regression tests on a fork of `FCP-INDI/C-PAC`_, you'll need to configure an environment called ``ACCESS`` in your fork with all of these secrets and variables defined correctly for your testing environment.

.. include::
   :glob:
   :maxdepth: 2

   /developer/continuous_integration/regression/*
   !/developer/continuous_integration/regression/index.rst

.. _amygutierrez/regression_dashboard: https://www.github.com/amygutierrez/regression_dashboard
.. _cmi-dair/slurm_testing: https://www.github.com/cmi-dair/slurm_testing
.. _FCP-INDI/C-PAC: https://www.github.com/FCP-INDI/C-PAC
.. _SSH Remote Commands: https://github.com/marketplace/actions/ssh-remote-commands?version=v1.0.0
