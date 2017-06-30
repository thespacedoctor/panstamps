Command-Line Tutorial
=====================

There are 2 ways to use **panstamps**, either via the command-line or import it into your own python code and use it from there.

Command-Line
--------------

Full usage options can be found by typing:

.. code-block:: bash 
    
     panstamps -h

Here I'll run through the basics. By default the command will only download the fits files for the location given. To download the stack fits cutouts for M82 run the command:

.. code-block:: bash 

    panstamps stack 09:55:52.2 +69:40:47

By default the *gri* filter, 1 arcmin fits cutouts are downloaded:

.. image:: https://i.imgur.com/DRvOiZ1.png
    
.. image:: https://i.imgur.com/3u9gVBW.png

To increase the image width and download all filters, run the command:

.. code-block:: bash

    panstamps --width=4 --filters=griyz stack 09:55:52.2 +69:40:47

As you can see we now have a larger cutout:

.. image:: https://i.imgur.com/ST9Y6Wv.png

JPEGS
~~~~~~~

To download the jpegs, and not the fits files rerun the command with the correct flags set. We'll also use the ``--downloadFolder`` option to assign the download directory.

.. code-block:: bash

    panstamps -Fj --width=4 --filters=gri --downloadFolder=/Users/Dave/Desktop/m81 stack 09:55:52.2 +69:40:47

This downloads the jpegs and adds some useful annotation, which can be switched off if required.

.. image:: https://i.imgur.com/yxPjt4U.png

Sometimes it maybe useful to add a transient marker at the centre of the image:

.. code-block:: bash

    panstamps -FjAt --width=4 --filters=gri --downloadFolder=/Users/Dave/Desktop/m81 stack 09:55:52.2 +69:40:47

.. image:: https://i.imgur.com/SDoYvR7.png

Or grab the color image as well as/instead of the single filter images:

.. code-block:: bash

    panstamps -FJc --width=4 --filters=gri --downloadFolder=/Users/Dave/Desktop/m81 stack 09:55:52.2 +69:40:47

.. image:: https://i.imgur.com/f5ixUts.png
    
Note the code will try its best to choose a colour for the annotation lines and text to make them contrast well against the background image.

Finally you can invert the image colors or convert the image to greyscale:

.. code-block:: bash

    panstamps -FJci --width=4 --filters=gri --downloadFolder=/Users/Dave/Desktop/m81 stack 09:55:52.2 +69:40:47

.. image:: https://i.imgur.com/rrcAsRN.png

.. code-block:: bash

    panstamps -FJcig --width=4 --filters=gri --downloadFolder=/Users/Dave/Desktop/m81 stack 09:55:52.2 +69:40:47

.. image:: https://i.imgur.com/g4w8Mv3.png

Temporal Constraints (Useful for Moving Objects)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For moving objects, alongside spatially filter the panstarrs images, we also require a temporal filter. We need to be able to request images at a given sky-position that were taken within a given time range. With panstamps we have the option of passing a time-window to filter the images by via the `mjdStart` and `mjdEnd` variables:

For example I can run:

```bash
panstamps -Fj --width=4 --filters=gri --downloadFolder=~/Desktop/movers warp 189.1960991 28.2374845 55246.63 55246.64
```

to return only the 2 images I want within the temporal window at the location in the sky.


Importing to Your Own Python Script
-----------------------------------

To use panstamps within your own scripts please read the full documentation. But for those of you that can't wait, this snippet should give you the basics:

.. code-block:: python 
    
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
        imageType="stack",  # warp | stack
        mjdStart=False,
        mjdEnd=False
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

    
