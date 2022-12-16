Versions and Variants
=====================

While still in beta, C-PAC versions are currently released through a :doc:`feature-based schedule </glossary/release-schedule-feature-based>` :cite:`cite-variants-Khom12`.

For each version, in addition to the standard image, we release 3 variants:

2 intended for nearer like-for-like comparisons and harmonization when mixing or comparing software pipelines: 

* ``ABCD-HCP``, software dependencies are matched to `DCAN Labs ABCD-HCP BIDS fMRI Pipeline v0.0.3 <https://github.com/DCAN-Labs/abcd-hcp-pipeline/releases/tag/v0.0.3>`_ :cite:`cite-variants-Stur20`,
* ``fMRIPrep-LTS``, software dependencies are matched to those of `fMRIPrep v20.1 <https://fmriprep.org/en/20.1.3/>`_ :cite:`cite-variants-Este19,cite-variants-fMRI20`,

and 1 intended to conserve disk space:

* ``lite``, a slimmer image than the standard image; this variant does not include FreeSurfer.

This flowchart is intended to help guide selection of a version (and potentially variant) C-PAC image to use in :doc:`Docker </user/docker>` or `Apptainer / Singularity </user/singularity>`:

.. raw:: html

    <div class="flowchart-container"><object data="../_static/flowcharts/choose-an-image.svg" type="image/svg+xml"></object></div>

.. rubric:: References

.. bibliography::
   :cited:
   :keyprefix: cite-variants-
