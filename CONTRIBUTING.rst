Contributing to this documentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This document is |CONTRIBUTING.rst|_ (in the root of `this repository <https://github.com/FCP-INDI/fcp-indi.github.io>`_). The other source files (outside of the code itself) are in `this repository`_ under |docs/_sources|_.

.. contents::
   :local:

Branches
********

Please, always base changes on the ``source`` branch. ``main`` branch will be overwritten by the CI deployment.

Versions
""""""""

``nightly``
```````````

Pushes to ``source`` will rebuild docs at https://fcp-indi.github.io/docs/nightly

C-PAC release tags
``````````````````

Tags in the format ``v.*-source`` will build docs for the given version.

If a matching version tag doesn't exist in https://github.com/FCP-INDI/C-PAC/tags, the build should fail.

Steps to build a release:

#. Checkout a commit from the ``source`` from a time appropriate for documentation for the branch being built/rebuilt.
#. If you need to make changes, create a branch (\ ``git switch -c`` or ``git checkout -b`` ).
#. Make any changes you need for the specific version.
#. Tag the commit that's ready to build (\ ``git tag v`` version\ ``-source`` )
#. (Force) push to the remote tag (\ ``git push origin v`` version\ ``-source`` ).
#. CircleCI should deploy the versioned documentation. If the version tag is the newest, it should also overwrite ``latest`` with these documents.

Guidelines
**********

* Only write a document once, and liberally use the |rst include|_ to include that document where appropriate.
* Use absolute paths for ``.. include::`` s. That way the path will resolve correctly regardless of differences in nesting levels.
* Include any source documents that you want built in at least one |toctree|_. Use the ``:hidden:`` option if you don't want it linked in an actual table of contents in the document with the ``toctree``.
* Use consistent section title indicators throughout a sourcetree. `fcp-indi.github.io/docs/user <https://fcp-indi.github.io/docs/user>`_ currently has the following hierarchy (top to bottom):

  .. code-block::

     =
     ^
     -
     *
     #
     `
     '
     "

Building
""""""""

Let CircleCI build your drafts / works-in-progress
``````````````````````````````````````````````````

* Build environment will match actual docs build environment
* CircleCI takes ~2 minutes to build

#. Fork https://github.com/FCP-INDI/fcp-indi.github.io
#. In your fork's settings, set the GitHub Pages ``source`` to ``main`` branch

   .. image:: ./images/github-pages-settings-example.png
      :target: ./images/github-pages-settings-example.png
      :alt: GitHub Pages settings example screenshot

#. Add your project on CircleCI
#. Merge your draft / work-in-progress into your fork's ``source`` branch. Make sure you push to your fork and not the main repository's ``source`` branch.
#. Your fork will publish at ``https://[your_GitHub_username].github.io/fcp-indi.github.io/``.

Build locally (C-PAC ≥ v1.8.0)
``````````````````````````````

This documentation aspires to rely on a `single source of truth <https://en.wikipedia.org/wiki/Single_source_of_truth>`_ where possible.  To this end, building this documentation requires an installation of the version of `C-PAC <https://github.com/FCP-INDI/C-PAC>`_ that is being documented.

Steps to build this documentation locally:

#. Clone `this repository`_.
#. *(optional)* Locally replicate the step "👊 Running cpac commands" from ``.circleci/config`` to generate `cpac <https://pypi.org/project/cpac/>`_ usage strings.
    Either perform this "👊 Running cpac commands" step in a separate Python environment or uninstall cpac after generating the usage string(s).

   #. *(optional)* Create an environment for cpac and activate this environment.
   #. ``pip install cpac``
   #. If you don't have a local container for the version of C-PAC you're documenting, ``cpac pull`` to download the latest or ``cpac pull --tag $TAG`` to pull a specific version.
   #. Generate ReStructuredText documents with cpac usage strings:

      .. code-block:: BASH

          mkdir -p docs/_sources/user/cpac
          printf ".. code-block:: console\n\n   $ cpac --help\n\n" > docs/_sources/user/cpac/help.rst
          cpac --help | sed -e "s/.*/   &/" >> docs/_sources/user/cpac/help.rst
          mkdir -p docs/_sources/user/run
          printf "Usage: cpac run\n\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\n.. code-block:: console\n\n   $ cpac run --help\n\n" > docs/_sources/user/run/help.rst
          cpac run --help | sed -e "s/.*/   &/" >> docs/_sources/user/run/help.rst
          mkdir -p docs/_sources/user/utils
          printf "Usage: cpac utils\n\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\`\n.. code-block:: console\n\n   $ cpac utils --help\n\n" > docs/_sources/user/utils/help.rst
          cpac utils --help | sed -e "s/.*/   &/" >> docs/_sources/user/utils/help.rst

   #. ``deactivate`` your cpac environment if you used a separate environment or ``pip uninstall cpac``.

#. Locally install `C-PAC`_ from source.
#. Run ``./bin/build $VERSION`` where ``$VERSION`` is the version to build (\ ``nightly`` , ``latest`` , or |semver| for production, but this string can be anything you want locally).

   .. image:: ./images/example_version.png
      :target: ./images/example_version.png
      :alt: example version

Flowcharts
**********

* SVGs exported from Lucidchart have scaling coded in in ``width`` and ``height`` XML attributes. Add the XML attributes ``preserveAspectRatio="xMinYMin meet"`` and ``viewBox`` to the SVG element in the actual SVG files:

.. code-block:: xml

   <svg preserveAspectRatio="xMinYMin meet" viewBox="0 0 {width} {height}"></svg>

where ``{width}`` and ``{height}`` are the values already present in the existing ``width`` and ``height`` XML attributes.


* Load SVGs in HTML ``object`` elements with the ``raw:: html`` directive to preserve hyperlinks and scaling:

.. code-block:: rst

   .. raw:: html

       <object data="../_static/path/to/chart.svg" type="image/svg+xml"></object>

Tutorials
*********

See `FCP-INDI/C-PAC_tutorials/CONTRIBUTING.md <https://github.com/FCP-INDI/C-PAC_tutorials/blob/main/CONTRIBUTING.md>`_ for how to contribute tutorials. Add them to the TOC tree in that repository or in any TOC tree in `this repository`_ with a relative path beginning ``/user/tutorials/`` (e.g., ``/user/tutorials/observed_usage`` for |observed_usage|_\ ).

References and citations
************************

`sphinxcontrib-bibtex <https://sphinxcontrib-bibtex.readthedocs.io/>`_ is installed and configured. This extension creates links between the citations and the reference in the reference list and formats citations in referenced BibTeX files using built-in or `custom styles <https://github.com/FCP-INDI/fcp-indi.github.io/blob/source/docs/_sources/references/style.py>`_. To use this Sphinx extension,


#. Include your references in a BibTeX file. Unless you have a speficic reason to use a separate file, that BibTeX file should be |references.bib|_.
#. If the entry type (e.g., ``book`` , ``article`` , ``misc`` ) of any of the entries in your BibTeX file(s) is not included in `docs/_sources/references/style.py <https://github.com/FCP-INDI/fcp-indi.github.io/blob/source/docs/_sources/references/style.py>`_\ , add a ``get_{entry_type}_template`` `Pybtex <https://pybtex.org>`_ method to ``CPAC_DocsStyle``.
#. If you want to include a header over a reference list, either follow the heirarchy under `the Guidelines section of this document <#guidelines>`_ or use the ``.. rubric::`` directive above its ``.. bibliography`` directive.

Local bibliography
""""""""""""""""""

For a bibliography of just the citations on the current page. This is the bibliography style you probably want, unless you have a specific reason for the central bibliography style.

#. Using the key (the text between the opening ``{`` and the first ``,`` in a BibTeX entry) use the ReStructuredText syntax |footcite example| to cite your reference in a ReStructuredText file.
#. Somewhere below your citations in the same page, place ``.. footbibliography::``. You can use this directive multiple times.

   .. epigraph::

      If specified multiple times in the same document, footnotes are only created for references that do not yet have a footnote earlier in the document.

      -- https://sphinxcontrib-bibtex.readthedocs.io/en/2.4.2/usage.html#directive-footbibliography

Central bibliography
""""""""""""""""""""

For a bibliography that includes references from multiple pages,

#. Include a ``.. bibliography::`` directive somewhere on any page that you want to use this extension to format references and create two-way links between the references and citations. You can list uncited references by listing their BibTeX keys explicilty.
#. If you will (or might) use more than one ``.. bibliography::`` directive (including via ``.. include::`` directives), choose a prefix for the keys and include that prefix in both the ``:cite:`` role (like |prefix-key example| ) and the bibliography directive (like ``:keyprefix: prefix-`` ).

For example, if you have a BibTeX file called ``cpac_citation.bib`` that contains

.. code-block:: BibTeX

   @ARTICLE{cpac2013,
       AUTHOR={Craddock, Cameron  and  Sikka, Sharad  and  Cheung, Brian  and  Khanuja, Ranjeet  and  Ghosh, Satrajit S
           and Yan, Chaogan  and  Li, Qingyang  and  Lurie, Daniel  and  Vogelstein, Joshua  and  Burns, Randal  and
           Colcombe, Stanley  and  Mennes, Maarten  and  Kelly, Clare  and  Di Martino, Adriana  and  Castellanos,
           Francisco Xavier  and  Milham, Michael},
       TITLE={Towards Automated Analysis of Connectomes: The {Configurable Pipeline for the Analysis of Connectomes (C-PAC)}},
       JOURNAL={Frontiers in Neuroinformatics},
       YEAR={2013},
       NUMBER={42},
       URL={http://www.frontiersin.org/neuroinformatics/10.3389/conf.fninf.2013.09.00042/full},
       DOI={10.3389/conf.fninf.2013.09.00042},
       ISSN={1662-5196}
   }

…and you include

.. code-block:: rst

   To cite C-PAC, use :cite:`cite-example-cpac2013`.

   .. rubric Cite C-PAC

   .. bibliography::
      :cited:
      :keyprefix: cite-example-

…the rendered file should look something like

.. highlights::

   .. raw:: html

      <p>To cite C-PAC, use <a name="backref1" href="#ref1">[1]</a>.</p>

      <div><p><b>Cite C-PAC</b></p>

      <p><a name="ref1" href="#backref1">[1]</a> Craddock, C., Sikka, S., Cheung, B., Khanuja, R., Ghosh, S. S., Yan, C., Li, Q., Lurie, D., Vogelstein, J., Burns, R., Colcombe, S., Mennes, M., Kelly, C., Di Martino, A., Castellanos, F. X., and Milham, M. 2013. <a href="http://www.frontiersin.org/neuroinformatics/10.3389/conf.fninf.2013.09.00042/full">Towards automated analysis of connectomes: the Configurable Pipeline for the Analysis of Connectomes (C-PAC)</a>. <i>Frontiers in neuroinformatics</i> 42. <a href="https://dx.doi.org/10.3389/conf.fninf.2013.09.00042">doi:10.3389/conf.fninf.2013.09.00042</a></p></div>

The local bibliography method to generate the same rendered output:

.. code-block:: rst

   To cite C-PAC, use :footcite:`cpac2013`.

   .. rubric Cite C-PAC

   .. footbibliography::

If you want to generate that bibliography entry without the citation:

.. code-block:: rst

   .. bibliography::
      :cited:

      cpac2013

Environment notes
*****************

* Because `C-PAC`_ and `cpac`_ have conflicting commandline commands, we first run any ``cpac`` commands in a virtual environment and spoof the ``command-output`` directive with ``code-block`` like

  .. code-block:: RST

      .. code-block:: console

          cpac run --help

      .. program-output:: cpac_py run --help
         :shell:
         :ellipsis: 0,9

* |:heavy_plus_sign:| Check |circleci config|_ of the branch you're working from for build dependencies.

* |:octocat:| Set an environment variable ``GITHUBTOKEN`` to a `personal access token <https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line>`_ to increase `your API rate limit <https://developer.github.com/v3/#rate-limiting>`_ from 60 to 5000 requests per hour (for getting `release notes from GitHub <https://github.com/FCP-INDI/C-PAC/releases>`_\ ).

.. |circleci config| replace:: ``.circleci/config.yml``
   
.. _circleci config: https://github.com/FCP-INDI/fcp-indi.github.io/blob/source/.circleci/config.yml

.. |CONTRIBUTING.rst| replace:: ``./CONTRIBUTING.rst``

.. _CONTRIBUTING.rst: ./CONTRIBUTING.rst

.. |docs/_sources| replace:: ``./docs/_sources``

.. _docs/_sources: ./docs/_sources

.. |footcite example| raw:: html

   <code>:footcite:`key`</code>

.. |nightly| replace:: ``nightly``

.. _nightly: #nightly

.. |observed_usage| replace:: ``observed_usage.ipynb``

.. _observed_usage: https://github.com/FCP-INDI/C-PAC_tutorials/blob/main/observed_usage.ipynb

.. |:octocat:| image:: https://github.githubassets.com/images/icons/emoji/octocat.png
      :alt: Octocat
      :width: 20

.. |prefix-key example| raw:: html

   <code>:cite:`prefix-key`</code>

.. |references.bib| replace:: ``docs/_sources/references/references.bib``

.. _references.bib: https://github.com/FCP-INDI/fcp-indi.github.io/blob/source/docs/_sources/references/references.bib

.. |rst include| replace:: reStructured Text ``.. include::`` directive

.. _rst include: https://docutils.sourceforge.io/docs/ref/rst/directives.html#include

.. |semver| raw:: html

   <span title='Semantic Versioning'><a href="https://semver.org/">semver</a></span>

.. |toctree| replace:: ``toctree``

.. _toctree: https://www.sphinx-doc.org/en/1.8/usage/restructuredtext/directives.html#directive-toctree


More information
****************

For full developer documentation about documentation, see `Documentation <https://fcp-indi.github.io/docs/developer/documentation>`_