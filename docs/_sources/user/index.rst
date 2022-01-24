.. C-PAC documentation main file, created by
   sphinx-quickstart on Fri Jul 20 16:32:55 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

User Documentation
==================

Welcome to C-PAC's user guide!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The C-PAC Mission
^^^^^^^^^^^^^^^^^

Once a distant goal, discovery science for the human connectome is now a reality. Researchers who previously struggled to obtain neuroimaging data from 20-30 participants are now exploring the functional connectome using data acquired from thousands of participants, made publicly available through the `1000 Functional Connectomes Project and the International Neuroimaging Data-sharing Initiative (INDI) <http://fcon_1000.projects.nitrc.org/>`_. However, in addition to access to data, scientists need access to tools that will facilitate data exploration. Such tools are particularly important for those who are inexperienced with the nuances of fMRI image analysis, or those who lack the programming support necessary for handling and analyzing large-scale datasets.

The Configurable Pipeline for the Analysis of Connectomes (C-PAC) is a configurable, open-source, Nipype-based, automated processing pipeline for resting state functional MRI (R-fMRI) data, for use by both novice and expert users. C-PAC was designed to bring the power, flexibility and elegance of the `Nipype platform <http://nipy.sourceforge.net/nipype/>`_ to users in a plug and play fashion—without requiring the ability to program. Using an easy to read, text-editable configuration file or a graphical user interface, C-PAC users can rapidly orchestrate automated R-fMRI processing procedures, including:

* standard quality assurance measurements
* standard image preprocessing based upon user specified preferences
* generation of functional connectivity maps (e.g., :doc:`seed-based correlation analyses </user/sca>`)
* customizable extraction of time-series data
* generation of graphical representations of the connectomes at various scales (e.g., voxel, parcellation unit)
* generation of local R-fMRI measures (e.g., :doc:`regional homogeneity </user/reho>`, :doc:`voxel-matched homotopic connectivity </user/vmhc>`, :doc:`frequency amplitude measures </user/alff>`)

Importantly, C-PAC makes it possible to use a single configuration file to launch a factorial number of pipelines differing with respect to specific processing steps (e.g., spatial/temporal filter settings, global correction strategies, motion correction strategies, group analysis models). Additional noteworthy features include the ability to easily:

* customize C-PAC to handle any systematic directory organization
* specify Nipype distributed processing settings

C-PAC maintains key Nipype strengths, including the ability to:

* interface with different software packages (e.g., FSL, AFNI, ANTS)
* protect against redundant computation and/or storage
* automatically carry out input checking, bug tracking and reporting

Future updates will include more configurability, advanced analytic features (e.g., support vector machines, cluster analysis) and diffusion tensor imaging (DTI) capabilities.

For more information and additional tutorials, check out our `YouTube channel <https://www.youtube.com/channel/UCMhbaa3bF7oQgnAWX6HmyMQ>`_, as well as slides from our previous presentations:

* `CPAC Connectome Analysis in the Cloud <http://www.slideshare.net/CameronCraddock/cpac-connectome-analysis-in-the-cloud>`_
* `Open science resources for 'Big Data' Analyses of the human connectome <http://www.slideshare.net/CameronCraddock/open-science-resources-for-big-data-analyses-of-the-human-connectome>`_
* `Computational approaches for mapping the human connectome <http://www.slideshare.net/CameronCraddock/computational-approaches-for-mapping-the-human-connectome>`_

.. _ndmg_atlases:

.. topic:: Neuroparc v1.0: Baseline

  .. include:: /user/ndmg_atlases.rst

.. include:: /user/release_notes/latest.rst

The C-PAC Team
^^^^^^^^^^^^^^
.. line-block::

   **Primary Development Team:**
   Michael Milham (Founder, Co-Principal Investigator)
   Cameron Craddock (Co-Principal Investigator)
   Steven Giavasis (Lead Developer)
   Jon Clucas (Developer)
   Hecheng Jin (Developer)
   Xinhui Li (Developer)

   **Project Alumni:**
   Anibal Solon Heinsfeld
   Nanditha Rajamani
   Alison Walensky
   David O'Connor
   Carol Froehlich
   John Pellman
   Amalia MacDonald
   Daniel Clark
   Rosalia Tungaraza
   Daniel Lurie
   Zarrar Shehzad
   Krishna Somandepali
   Aimi Watanabe
   Qingyang Li
   Ranjit Khanuja
   Sharad Sikka
   Brian Cheung

   **Other Contributors:**
   Ivan J. Roijals-Miras (Google Summer of Code)
   Florian Gesser (Google Summer of Code)
   Asier Erramuzpe (Google Summer of Code)
   Chao-Gan Yan
   Joshua Vogelstein
   Adriana Di Martino
   F. Xavier Castellanos
   Sebastian Urchs
   Bharat Biswal

Funding Acknowledgements
^^^^^^^^^^^^^^^^^^^^^^^^
Primary support for the work by Michael P. Milham, Cameron Craddock and the INDI team was provided by gifts from Joseph P. Healey and the `Stavros Niarchos Foundation <http://www.snf.org/>`_ to the `Child Mind Institute <http://www.childmind.org/>`_, as well as by `NIMH <http://www.nimh.nih.gov/index.shtml>`_ awards to Dr. Milham (R03MH096321) and F.X. Castellanos (R01MH083246).

User Guide Index
^^^^^^^^^^^^^^^^
.. toctree::
   :maxdepth: 2
   :includehidden:
   :titlesonly:

   1. C-PAC Quickstart <quick>
   2. Specify Your Data <subject_list_config>
   3. Select Your Pipeline <pipelines/pipeline_config>
   4. Pre-Process Your Data <preprocessing>
   5. Compute Derivatives <derivatives>
   6. All Run Options <running>
   7. Run Group Analysis <group_analysis>
   8. Check Your Outputs <output_dir>
   9. Troubleshoot <help>
   10. Release Notes <rnotes>
   11. Appendix <appendix>
