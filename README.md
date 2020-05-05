panstamps
=========

[![Documentation Status](https://readthedocs.org/projects/panstamps/badge/)](http://panstamps.readthedocs.io/en/latest/?badge)

[![Coverage Status](https://cdn.jsdelivr.net/gh/thespacedoctor/panstamps@master/coverage.svg)](https://cdn.jsdelivr.net/gh/thespacedoctor/panstamps@master/htmlcov/index.html)

*A python package and command-line tools to download stacked and/or warp
image stamps from the STScI PanSTARRS image server*.

> **note**
>
> If working with warped PS1 images then you need to work off a machine
> that has an IP address whitelisted by the [Pan-STARRS1 data
> archive](https://panstarrs.stsci.edu/), otherwise only stacked images
> will be available to you. Also *w*-band images are not (yet)
> accessible from the data archive.

Command-Line Usage
==================

    Documentation for panstamps can be found here: http://panstamps.readthedocs.org/en/stable

    Usage:
        panstamps [options] [--width=<arcminWidth>] [--filters=<filterSet>] [--settings=<pathToSettingsFile>] [--downloadFolder=<path>] (warp|stack) <ra> <dec> [<mjdStart> <mjdEnd>]
        panstamps [options] --closest=<beforeAfter> [--width=<arcminWidth>] [--filters=<filterSet>] [--settings=<pathToSettingsFile>] [--downloadFolder=<path>] <ra> <dec> <mjd>

        -h, --help                              show this help message
        -f, --fits                              download fits (default on)
        -F, --nofits                            don't download fits (default off)
        -j, --jpeg                              download jepg (default off)
        -J, --nojpeg                            don't download jepg (default on)
        -c, --color                             download color jepg (default off)
        -C, --nocolor                           don't download color jepg (default on)
        -a, --annotate                          annotate jpeg (default true)
        -A, --noannotate                        don't annotate jpeg (default false)
        -t, --transient                         add a small red circle at transient location (default false)
        -T, --notransient                       don't add a small red circle at transient location (default true)
        -g, --greyscale                         convert jpeg to greyscale (default false)
        -G, --nogreyscale                       don't convert jpeg to greyscale (default true)
        -i, --invert                            invert jpeg colors (default false)
        -I, --noinvert                          don't invert jpeg colors (default true)
        --width=<arcminWidth>                   width of image in arcsec (default 1)
        --filters=<filterSet>                   filter set to download and use for color image (default gri)
        --downloadFolder=<path>                 path to the download folder, relative or absolute (folder created where command is run if not set)
        --settings=<pathToSettingsFile>         the settings file    
        --closest=<beforeAfter>                 return the warp closest in time to the given mjd. If you want to set a strict time window then pass in a positive or negative time in sec (before | after | secs)

        ra                                      right-ascension in sexagesimal or decimal degrees
        dec                                     declination in sexagesimal or decimal degrees
        mjdStart                                the start of the time-window within which to select images
        mjdEnd                                  the end of the time-window within which to select images
        mjd                                     report the warp closest in time to this mjd

Documentation
=============

Documentation for panstamps is hosted by [Read the
Docs](http://panstamps.readthedocs.org/en/stable/) (last [stable
version](http://panstamps.readthedocs.org/en/stable/) and [latest
version](http://panstamps.readthedocs.org/en/latest/)).

Installation
============

The easiest way to install panstamps is to use `pip`:

    pip install panstamps

Or you can clone the [github
repo](https://github.com/thespacedoctor/panstamps) and install from a
local version of the code:

    git clone git@github.com:thespacedoctor/panstamps.git
    cd panstamps
    python setup.py install

To upgrade to the latest version of panstamps use the command:

    pip install panstamps --upgrade

Troubleshooting on Mac OSX
--------------------------

panstamps uses pillow (a fork of the Python Imaging Library) which
requires some [external
libraries](https://pillow.readthedocs.org/en/3.1.x/installation.html#external-libraries).

If you have issues running panstamps on OSX, try installing
[Homebrew](http://brew.sh/) and running:

    brew install libtiff libjpeg webp little-cms2

Development
-----------

If you want to tinker with the code, then install in development mode.
This means you can modify the code from your cloned repo:

    git clone git@github.com:thespacedoctor/panstamps.git
    cd panstamps
    python setup.py develop

[Pull requests](https://github.com/thespacedoctor/panstamps/pulls) are
welcomed!

### Sublime Snippets

If you use [Sublime Text](https://www.sublimetext.com/) as your code
editor, and you're planning to develop your own python code with
panstamps, you might find [my Sublime
Snippets](https://github.com/thespacedoctor/panstamps-Sublime-Snippets)
useful.

Issues
------

Please report any issues
[here](https://github.com/thespacedoctor/panstamps/issues).

License
=======

Copyright (c) 2018 David Young

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
