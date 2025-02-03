# panstamps

[![](https://zenodo.org/badge/DOI/10.5281/zenodo.8037664.svg)](https://zenodo.org/doi/10.5281/zenodo.8037664)


<!-- INFO BADGES -->  

[![](https://img.shields.io/pypi/pyversions/panstamps)](https://pypi.org/project/panstamps/)
[![](https://img.shields.io/pypi/v/panstamps)](https://pypi.org/project/panstamps/)
[![](https://img.shields.io/github/license/thespacedoctor/panstamps)](https://github.com/thespacedoctor/panstamps)
[![](https://img.shields.io/pypi/dm/panstamps)](https://pypi.org/project/panstamps/)

<!-- STATUS BADGES -->  

[![](https://soxs-eso-data.org/ci/buildStatus/icon?job=panstamps%2Fmaster&subject=build%20master)](https://soxs-eso-data.org/ci/blue/organizations/jenkins/panstamps/activity?branch=master)
[![](https://soxs-eso-data.org/ci/buildStatus/icon?job=panstamps%2Fdevelop&subject=build%20dev)](https://soxs-eso-data.org/ci/blue/organizations/jenkins/panstamps/activity?branch=develop)
[![](https://cdn.jsdelivr.net/gh/thespacedoctor/panstamps@master/coverage.svg)](https://raw.githack.com/thespacedoctor/panstamps/master/htmlcov/index.html)
[![](https://readthedocs.org/projects/panstamps/badge/?version=master)](https://panstamps.readthedocs.io/en/master/)
[![](https://img.shields.io/github/issues/thespacedoctor/panstamps/type:%20bug?label=bug%20issues)](https://github.com/thespacedoctor/panstamps/issues?q=is%3Aissue+is%3Aopen+label%3A%22type%3A+bug%22+)

*Download stacked and/or warp image stamps from the STScI PanSTARRS image server via CL or Python API*.

Documentation for panstamps is hosted by [Read the Docs](https://panstamps.readthedocs.io/en/master/) ([development version](https://panstamps.readthedocs.io/en/develop/) and [master version](https://panstamps.readthedocs.io/en/master/)). The code lives on [github](https://github.com/thespacedoctor/panstamps). Please report any issues you find [here](https://github.com/thespacedoctor/panstamps/issues).

:::{note}
If working with warped PS1 images then you need to work off a machine that has an IP address whitelisted by the `Pan-STARRS1 data archive <https://panstarrs.stsci.edu/>`_, otherwise only stacked images will be available to you. Also *w*-band images are not (yet) accessible from the data archive.
:::

## Installation

The easiest way to install panstamps is to use `pip` (here we show the install inside of a conda environment):

``` bash
conda create -n panstamps python=3.9 pip
conda activate panstamps
pip install panstamps
```

To upgrade to the latest version of panstamps use the command:

``` bash
pip install panstamps --upgrade
```

To check installation was successful run `panstamps -v`. This should return the version number of the install.


## How to cite panstamps

If you use `panstamps` in your work, please cite using the following BibTeX entry: 

```bibtex
@software{Young_panstamps,
author = {Young, David R.},
doi = {10.5281/zenodo.8037664},
license = {GPL-3.0-only},
title = {{panstamps. PanSTARRS image downloader}},
url = {https://zenodo.org/doi/10.5281/zenodo.8037664}
}
```
 
