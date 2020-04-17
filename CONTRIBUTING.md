## Branches

Please, always change `source` branch. `master` branch will be overriden by the CI.

## Guidelines

- Only write a document once, and liberally use the [reStructured Text `.. include::` directive](https://docutils.sourceforge.io/docs/ref/rst/directives.html#include) to include that document where appropriate.
- Use absolute paths for `.. include::`s. That way the path will resolve correctly regardless of differences in nesting levels.
- Include any source documents that you want built in at least one [`toctree`](https://www.sphinx-doc.org/en/1.8/usage/restructuredtext/directives.html#directive-toctree). Use the `:hidden:` option if you don't want it linked in an actual table of contents in the document with the `toctree`.
- Use consistent section title indicators throughout a sourcetree. [fcp-indi.github.com/docs/user](https://fcp-indi.github.com/docs/user) currently has the following hierarchy (top to bottom):
  ```
  =
  ^
  -
  *
  #
  `
  '
  "
  ```
- Let CircleCI build your drafts / works-in-progress
    * Build environment will match actual docs build environment
    * CircleCI takes ~2 minutes to build
    1. Fork https://github.com/FCP-INDI/fcp-indi.github.com
    1. In your fork's settings, set the GitHub Pages `source` to `master` branch
        ![GitHub Pages settings example screenshot](./images/github-pages-settings-example.png)
    1. Add your project on CircleCI
    1. Merge your draft / work-in-progress into your fork's `source` branch. Make sure you push to your fork and not the main repository's `source` branch.
    1. Your fork will publish at `https://[your_GitHub_username].github.io/fcp-indi.github.com/docs/user` and `https://[your_GitHub_username].github.io/fcp-indi.github.com/docs/developer`.

## Flowcharts

- SVGs exported from Lucidchart have scaling coded in in `width` and `height` XML attributes. Add the XML attributes `preserveAspectRatio="xMinYMin meet"` and `viewBox` to the SVG element in the actual SVG files:

```xml
<svg preserveAspectRatio="xMinYMin meet" viewBox="0 0 {width} {height}"></svg>
```

where `{width}` and `{height}` are the values already present in the existing `width` and `height` XML attributes.
- Load SVGs in HTML `object` elements with the `raw:: html` directive to preserve hyperlinks and scaling:

```rst
.. raw:: html

    <object data="_static/path/to/chart.svg" type="image/svg+xml"></object>
```

## Environment notes
* :snake: Until [C-PAC Python 2 → 3 conversion](https://github.com/FCP-INDI/C-PAC/issues/1114) is complete, these docs require Python 2.7 to build.
* :heavy_plus_sign: Check [`.circleci/config.yml`](https://github.com/FCP-INDI/fcp-indi.github.com/blob/source/.circleci/config.yml) of the branch you're working from for build dependencies.
* :octocat: Set an environment variable `GITHUBTOKEN` to a [personal access token](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line) to increase [your API rate limit](https://developer.github.com/v3/#rate-limiting) from 60 to 5000 requests per hour (for getting [release notes from GitHub](https://github.com/FCP-INDI/C-PAC/releases)).
