panstamps
=========

*A python package and command-line tools to download stacked and/or warp image stamps from the STScI PanSTARRS image server*.

Here's a summary of what's included in the python package:

.. include:: /classes_and_functions.rst

Command-Line Usage
==================

.. code-block:: bash 
   
    
    Documentation for panstamps can be found here: http://panstamps.readthedocs.org/en/stable
    
    Usage:
        panstamps [options] [--width=<arcminWidth>] [--filters=<filterSet>] [--settings=<pathToSettingsFile>] [--downloadFolder=<path>] (warp|stack) <ra> <dec>
    
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
    

Documentation
=============

Documentation for panstamps is hosted by `Read the Docs <http://panstamps.readthedocs.org/en/stable/>`__ (last `stable version <http://panstamps.readthedocs.org/en/stable/>`__ and `latest version <http://panstamps.readthedocs.org/en/latest/>`__).

Installation
============

The easiest way to install panstamps is to use ``pip``:

.. code:: bash

    pip install panstamps

Or you can clone the `github repo <https://github.com/thespacedoctor/panstamps>`__ and install from a local version of the code:

.. code:: bash

    git clone git@github.com:thespacedoctor/panstamps.git
    cd panstamps
    python setup.py install

To upgrade to the latest version of panstamps use the command:

.. code:: bash

    pip install panstamps --upgrade

Troubleshooting on Mac OSX
---------------------------

panstamps uses pillow (a fork of the Python Imaging Library) which requires some `external libraries <https://pillow.readthedocs.org/en/3.1.x/installation.html#external-libraries>`_. 

If you have issues running panstamps on OSX, try installing `Homebrew <http://brew.sh/>`_ and running:

.. code:: bash

    brew install libtiff libjpeg webp little-cms2


Development
-----------

If you want to tinker with the code, then install in development mode.
This means you can modify the code from your cloned repo:

.. code:: bash

    git clone git@github.com:thespacedoctor/panstamps.git
    cd panstamps
    python setup.py develop

`Pull requests <https://github.com/thespacedoctor/panstamps/pulls>`__
are welcomed!

Sublime Snippets
~~~~~~~~~~~~~~~~

If you use `Sublime Text <https://www.sublimetext.com/>`_ as your code editor, and you're planning to develop your own python code with panstamps, you might find `my Sublime Snippets <https://github.com/thespacedoctor/panstamps-Sublime-Snippets>`_ useful. 

Issues
------

Please report any issues
`here <https://github.com/thespacedoctor/panstamps/issues>`__.

License
=======

Copyright (c) 2016 David Young

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

