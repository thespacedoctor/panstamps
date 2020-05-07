# Installation

The easiest way to install panstamps is to use `pip` (here we show the install inside of a conda environment):

``` bash
conda create -n panstamps python=3.7 pip
conda activate panstamps
pip install panstamps
```

Or you can clone the [github repo](https://github.com/thespacedoctor/panstamps) and install from a local version of the code:

``` bash
git clone git@github.com:thespacedoctor/panstamps.git
cd panstamps
python setup.py install
```

To upgrade to the latest version of panstamps use the command:

``` bash
pip install panstamps --upgrade
```

To check installation was successful run `panstamps -v`. This should return the version number of the install.

### Troubleshooting on Mac OSX

panstamps uses pillow (a fork of the Python Imaging Library) which requires some [external libraries](https://pillow.readthedocs.org/en/3.1.x/installation.html#external-libraries).

If you have issues running panstamps on OSX, try installing [Homebrew](http://brew.sh/) and running:

``` bash
brew install libtiff libjpeg webp little-cms2
```

## Development

If you want to tinker with the code, then install in development mode. This means you can modify the code from your cloned repo:

``` bash
git clone git@github.com:thespacedoctor/panstamps.git
cd panstamps
python setup.py develop
```

[Pull requests](https://github.com/thespacedoctor/panstamps/pulls) are welcomed! 

<!-- ### Sublime Snippets

If you use [Sublime Text](https://www.sublimetext.com/) as your code editor, and you're planning to develop your own python code with soxspipe, you might find [my Sublime Snippets](https://github.com/thespacedoctor/panstamps-Sublime-Snippets) useful. -->


