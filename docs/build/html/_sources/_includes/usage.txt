Command-Line Usage
==================

.. code-block:: bash 
   
    
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
    
