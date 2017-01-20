panstamps
=========

*A python package and command-line tools to download stacked and/or warp image stamps from the STScI PanSTARRS image server*.

Here’s a summary of what’s included in the python package:

Command-Line Usage
==================

``` sourceCode
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
```

Installation
============

The easiest way to install panstamps us to use `pip`:

``` sourceCode
pip install panstamps
```

Or you can clone the [github repo](https://github.com/thespacedoctor/panstamps) and install from a local version of the code:

``` sourceCode
git clone git@github.com:thespacedoctor/panstamps.git
cd panstamps
python setup.py install
```

To upgrade to the latest version of panstamps use the command:

``` sourceCode
pip install panstamps --upgrade
```

Troubleshooting on Mac OSX
--------------------------

panstamps uses pillow (a fork of the Python Imaging Library) which requires some [external libraries](https://pillow.readthedocs.org/en/3.1.x/installation.html#external-libraries).

If you have issues running panstamps on OSX, try installing [Homebrew](http://brew.sh/) and running:

``` sourceCode
brew install libtiff libjpeg webp little-cms2
```

Documentation
=============

Documentation for panstamps is hosted by [Read the Docs](http://panstamps.readthedocs.org/en/stable/) (last [stable version](http://panstamps.readthedocs.org/en/stable/) and [latest version](http://panstamps.readthedocs.org/en/latest/)).

Command-Line Tutorial
=====================

There are 2 ways to use **panstamps**, either via the command-line or import it into your own python code and use it from there.

Command-Line
------------

Full usage options can be found by typing:

``` sourceCode
panstamps -h
```

Here I’ll run through the basics. By default the command will only download the fits files for the location given. To download the stack fits cutouts for M82 run the command:

``` sourceCode
panstamps stack 09:55:52.2 +69:40:47
```

By default the *gri* filter, 1 arcmin fits cutouts are downloaded:

![image](https://i.imgur.com/DRvOiZ1.png)

![image](https://i.imgur.com/3u9gVBW.png)

To increase the image width and download all filters, run the command:

``` sourceCode
panstamps --width=4 --filters=griyz stack 09:55:52.2 +69:40:47
```

As you can see we now have a larger cutout:

![image](https://i.imgur.com/ST9Y6Wv.png)

### JPEGS

To download the jpegs, and not the fits files rerun the command with the correct flags set. We’ll also use the `--downloadFolder` option to assign the download directory.

``` sourceCode
panstamps -Fj --width=4 --filters=gri --downloadFolder=/Users/Dave/Desktop/m81 stack 09:55:52.2 +69:40:47
```

This downloads the jpegs and adds some useful annotation, which can be switched off if required.

![image](https://i.imgur.com/yxPjt4U.png)

Sometimes it maybe useful to add a transient marker at the centre of the image:

``` sourceCode
panstamps -FjAt --width=4 --filters=gri --downloadFolder=/Users/Dave/Desktop/m81 stack 09:55:52.2 +69:40:47
```

![image](https://i.imgur.com/SDoYvR7.png)

Or grab the color image as well as/instead of the single filter images:

``` sourceCode
panstamps -FJc --width=4 --filters=gri --downloadFolder=/Users/Dave/Desktop/m81 stack 09:55:52.2 +69:40:47
```

![image](https://i.imgur.com/f5ixUts.png)

Note the code will try its best to choose a colour for the annotation lines and text to make them contrast well against the background image.

Finally you can invert the image colors or convert the image to greyscale:

``` sourceCode
panstamps -FJci --width=4 --filters=gri --downloadFolder=/Users/Dave/Desktop/m81 stack 09:55:52.2 +69:40:47
```

![image](https://i.imgur.com/rrcAsRN.png)

``` sourceCode
panstamps -FJcig --width=4 --filters=gri --downloadFolder=/Users/Dave/Desktop/m81 stack 09:55:52.2 +69:40:47
```

![image](https://i.imgur.com/g4w8Mv3.png)

Importing to Your Own Python Script
-----------------------------------

To use panstamps within your own scripts please read the full documentation. But for those of you that can’t wait, this snippet should give you the basics:

``` sourceCode
from panstamps.downloader import downloader
from panstamps.image import image
fitsPaths, jpegPaths, colorPath = downloader(
    log=log,
    settings=False,
    downloadDirectory=False,
    fits=False,
    jpeg=True,
    arcsecSize=600,
    filterSet='gri',
    color=True,
    singleFilters=True,
    ra="70.60271",
    dec="-21.72433",
    imageType="stack"  # warp | stack
).get()

for j in jpegPaths:

    myimage = image(
        log=log,
        settings=False,
        imagePath=j
        arcsecSize=120,
        crosshairs=True,
        transient=False,
        scale=True,
        invert=False,
        greyscale=False
    ).get() 
```
