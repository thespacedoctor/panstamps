#!/usr/local/bin/python
# encoding: utf-8
"""
*Tools to download the panstarrs image stamps from STScI PanSTARRS image server*

:Author:
    David Young

:Date Created:
    March  2, 2016

.. todo::
    
    @review: when complete pull all general functions and classes into dryxPython
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import re
os.environ['TERM'] = 'vt100'
from fundamentals import tools


class downloader():
    """
    *Tools to download the panstarrs image stamps from STScI PanSTARRS image server*

    **Key Arguments:**
        - ``log`` -- logger
        - ``settings`` -- the settings dictionary
        - ``downloadDirectory`` -- the path to where you want to download the images to. Default */tmp*
        - ``fits`` -- download the fits files? Default *True*
        - ``jpeg`` -- download the jpeg files? Default *False*
        - ``arcsecSize`` -- the size of the image stamps to download (1 arcsec == 4 pixels). Default *60*
        - ``filterSet`` -- the filter set used to create color and/or download as individual stamps. Default *gri*
        - ``color`` -- download the color jpeg? Default *True*
        - ``singleFilters`` -- download the single filter stmaps? Default *False*
        - ``ra`` -- ra in decimal degrees.
        - ``dec`` -- dec in decimal degrees.
        - ``imageType`` -- warp or stacked images? Default *stack*

    **Usage:**
        .. todo::

            - create a sublime snippet for usage

        The following will return 3 lists of paths to local fits, jpeg and color-jpeg files:

        .. code-block:: python 

            from panstamps.downloader import downloader
            fitsPaths, jpegPaths, colorPath = downloader(
                log=log,
                settings=False,
                fits=False,
                jpeg=True,
                arcsecSize=600,
                filterSet='gri',
                color=True,
                singleFilters=True,
                ra="70.60271",
                dec="-21.72433",
                imageType="stack"
            ).get() 


    .. todo::

        - @review: when complete, clean downloader class
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract class to another module
    """
    # Initialisation

    def __init__(
            self,
            log,
            downloadDirectory="/tmp",
            settings=False,
            fits=True,
            jpeg=False,
            arcsecSize=60,
            filterSet='gri',
            color=True,
            singleFilters=False,
            ra=False,
            dec=False,
            imageType="stack"
    ):
        self.log = log
        log.debug("instansiating a new 'downloader' object")
        self.settings = settings
        self.fits = fits
        self.jpeg = jpeg
        self.arcsecSize = arcsecSize
        self.filterSet = filterSet
        self.color = color
        self.singleFilters = singleFilters
        self.ra = ra
        self.dec = dec
        self.imageType = imageType
        self.downloadDirectory = downloadDirectory

        # xt-self-arg-tmpx

        # 2. @flagged: what are the default attrributes each object could have? Add them to variable attribute set here
        # Variable Data Atrributes

        # 3. @flagged: what variable attrributes need overriden in any baseclass(es) used
        # Override Variable Data Atrributes

        # Initial Actions

        return None

    # 4. @flagged: what actions does each object have to be able to perform? Add them here
    # Method Attributes
    def get(self):
        """
        *get the downloader object*

        **Return:**
            - ``downloader``

        **Usage:**
        .. todo::

            - add usage info
            - create a sublime snippet for usage

        .. code-block:: python 

            usage code 

        .. todo::

            - @review: when complete, clean get method
            - @review: when complete add logging
        """
        self.log.info('starting the ``get`` method')
        fitsPaths = []
        jpegPaths = []
        colorPath = []

        content, status_code = self.get_html_content()
        if int(status_code) != 200:
            message = 'cound not download the image stamps. The STScI PanSTARRS image server returned HTTP status code %(status_code)s' % locals(
            )
            self.log.error(message)
            raise IOError(message)

        allStacks, allWarps, colorImage = self.parse_html_for_image_urls_and_metadata(
            content=content
        )

        ra = self.ra
        dec = float(self.dec)
        if dec > 0:
            sign = "p"
        else:
            sign = "m"
        dec = abs(dec)

        directoryName = """%(ra)s%(sign)s%(dec)s""" % locals()
        downloadDirectory = self.downloadDirectory + "/" + directoryName
        # Recursively create missing directories
        if not os.path.exists(downloadDirectory):
            os.makedirs(downloadDirectory)

        # IF SINGLE FILTER STAMPS HAVE BEEN REQUESTED
        if self.singleFilters:
            for images in [allStacks, allWarps]:
                urls = []

                # DOWNLOAD THE FITS FILES?
                fitsFilenames = []
                if self.fits:
                    fitsFilenames[:] = [
                        t + ".fits" for t in images["filenames"]]
                    urls += images["fits"]

                fitsPaths += self.download_images(
                    urls=urls,
                    filenames=fitsFilenames,
                    downloadDirectory=downloadDirectory
                )

                # DOWNLOAD THE JPEGS FILES?
                urls = []
                jpegFilenames = []
                if self.jpeg:
                    jpegFilenames[:] = [
                        t + ".jpeg" for t in images["filenames"]]
                    urls += images["jpegs"]

                jpegPaths += self.download_images(
                    urls=urls,
                    filenames=jpegFilenames,
                    downloadDirectory=downloadDirectory
                )

        # IF COLOR STAMPS HAS BEEN REQUESTED
        if self.color:
            theseFilenames = []
            theseFilenames[:] = [t + ".jpeg" for t in colorImage["filename"]]

            colorPath += self.download_images(
                urls=colorImage["jpeg"],
                filenames=theseFilenames,
                downloadDirectory=self.downloadDirectory + "/" + directoryName
            )

        self.log.info('completed the ``get`` method')

        return fitsPaths, jpegPaths, colorPath

    def get_html_content(
            self):
        """
        *Build the URL for the stamp request and extract the HTML content*

        **Return:**
            - None

        **Usage:**
        .. todo::

            - add usage info
            - create a sublime snippet for usage

        .. code-block:: python 

            usage code 

        .. todo::

            - @review: when complete, clean get_html_content method
            - @review: when complete add logging
        """
        self.log.info('starting the ``get_html_content`` method')

        import requests

        pos = self.ra + " " + self.dec
        filterSet = self.filterSet.split()
        if self.color:
            filterSet.append("color")

        imageSize = int(self.arcsecSize * 4)

        try:
            response = requests.get(
                url="http://plpsipp1v.stsci.edu/cgi-bin/ps1cutouts",
                params={
                    "pos": pos,
                    "filter": filterSet,
                    "filetypes": self.imageType,
                    "size": imageSize,
                    "output_size": imageSize,
                    "verbose": "0",
                    "autoscale": "99.500000",
                    "catlist": "",
                },
            )
        except requests.exceptions.RequestException:
            print('HTTP Request failed')

        self.log.info('completed the ``get_html_content`` method')
        return response.content, response.status_code

    # use the tab-trigger below for new method
    def parse_html_for_image_urls_and_metadata(
            self,
            content):
        """
        *parse html for image urls and metadata*

        **Key Arguments:**
            - ``content`` -- the content of the stamp results HTML page

        **Usage:**
        .. todo::

            - add usage info
            - create a sublime snippet for usage

        .. code-block:: python 

            usage code 

        **Return:**
            - None

        .. todo::

            - @review: when complete, clean parse_html_for_image_urls_and_metadata method
            - @review: when complete add logging
        """
        self.log.info(
            'starting the ``parse_html_for_image_urls_and_metadata`` method')

        stackFitsUrls = []
        warpFitsUrls = []
        stackJpegUrls = []
        warpJpegUrls = []
        colorJpegUrl = []
        stackFitsFilename = []
        warpFitsFilename = []
        stackJpegFilename = []
        warpJpegFilename = []
        colorJpegFilename = []
        allStacks = {
            "jpegs": [],
            "fits": [],
            "filenames": [],
            "filters": []
        }
        allWarps = {
            "jpegs": [],
            "fits": [],
            "filenames": []
        }
        colorImage = {
            "jpeg": [],
            "filename": []
        }

        reFitscutouts = re.compile(
            r"""<th>(?P<imagetype>\w+)\s+(?P<skycellid>\d+.\d+)\s+(?P<ffilter>[\w\\]+)(\s+(?P<mjd>\d+\.\d+))?<br.*?href="http://plpsipp1v.*?Display</a>.*?Fits cutout" href="(?P<fiturl>http://plpsipp1v.*?\.fits)".*?</th>""", re.I)

        thisIter = reFitscutouts.finditer(content)
        for item in thisIter:
            imagetype = item.group("imagetype")
            skycellid = item.group("skycellid")
            ffilter = item.group("ffilter")
            fiturl = item.group("fiturl")
            mjd = item.group("mjd")
            if imagetype == "stack":
                stackFitsUrls.append(fiturl)
            elif imagetype == "warp":
                warpFitsUrls.append(fiturl)

        reJpegs = re.compile(
            r"""<img src="(?P<jpegUrl>http://plp.*?skycell.*?)\"""", re.I)

        thisIter = reJpegs.finditer(content)
        for item in thisIter:
            jpegUrl = item.group("jpegUrl")

            if "red" in jpegUrl and "blue" in jpegUrl:
                colorJpegUrl.append(jpegUrl)
            elif ".wrp." in jpegUrl:
                warpJpegUrls.append(jpegUrl)
            elif ".stk." in jpegUrl:
                stackJpegUrls.append(jpegUrl)

            else:
                self.log.warning(
                    "We are not downloading this jpeg: '%(jpegUrl)s'" % locals())

        reFitsMeta = re.compile(
            r'http.*?\?.*?skycell\.(?P<skycell>\d+\.\d+).*?x=(?P<ra>\d+\.\d+).*?y=(?P<dec>[+|-]?\d+\.\d+).*?size=(?P<pixels>\d+).*?stk\.(?P<ffilter>\w+).*?fits', re.S | re.I)

        for i in stackJpegUrls:
            fitsUrl = i.split("&")[0].replace("%3A", ":")
            for f in stackFitsUrls:
                if fitsUrl in f:
                    matchObject = re.search(reFitsMeta, f)
                    skycell = matchObject.group("skycell")
                    ra = matchObject.group("ra")
                    dec = matchObject.group("dec")
                    pixels = matchObject.group("pixels")
                    arcsec = str(int(int(pixels) / 4))
                    ffilter = matchObject.group("ffilter")
                    filename = """stack_%(ffilter)s_ra%(ra)s_dec%(dec)s_arcsec%(arcsec)s_skycell%(skycell)s""" % locals(
                    )
                    allStacks["jpegs"].append(i)
                    allStacks["fits"].append(f)
                    allStacks["filenames"].append(filename)
                    allStacks["filters"].append(ffilter)

        reFitsMeta = re.compile(
            r'http.*?\?.*?skycell\.(?P<skycell>\d+\.\d+).*?x=(?P<ra>\d+\.\d+).*?y=(?P<dec>[+|-]?\d+\.\d+).*?size=(?P<pixels>\d+).*?wrp\.(?P<ffilter>\w+)\.(?P<mjd>\d+\.\d+).*?fits', re.S | re.I)

        for i in warpJpegUrls:
            fitsUrl = i.split("&")[0].replace("%3A", ":")
            for f in warpFitsUrls:
                if fitsUrl in f:
                    matchObject = re.search(reFitsMeta, f)
                    skycell = matchObject.group("skycell")
                    ra = matchObject.group("ra")
                    dec = matchObject.group("dec")
                    pixels = matchObject.group("pixels")
                    arcsec = str(int(int(pixels) / 4))
                    ffilter = matchObject.group("ffilter")
                    mjd = matchObject.group("mjd")
                    filename = """warp_%(ffilter)s_ra%(ra)s_dec%(dec)s_mjd%(mjd)s_arcsec%(arcsec)s_skycell%(skycell)s""" % locals(
                    )
                    allWarps["jpegs"].append(i)
                    allWarps["fits"].append(f)
                    allWarps["filenames"].append(filename)

        if len(colorJpegUrl):
            reColorMeta = re.compile(
                r'(?P<color>\w+)=(?P<datapath>/data.*?)&', re.S | re.I)

            thisIter = reColorMeta.finditer(colorJpegUrl[0])
            ffilter = ""
            for item in thisIter:
                fits = item.group("datapath").replace(
                    "%3A", ":").split("/")[-1]
                for j, f, n, b in zip(allStacks["jpegs"], allStacks["fits"],  allStacks["filenames"], allStacks["filters"]):
                    if fits in f:
                        ffilter += b
                        filename = n
            filename = "color_" + ffilter + "_" + \
                ("_").join(filename.split("_")[2:])
            colorImage["jpeg"].append(colorJpegUrl[0])
            colorImage["filename"].append(filename)

        self.log.info(
            'completed the ``parse_html_for_image_urls_and_metadata`` method')
        return allStacks, allWarps, colorImage

    # use the tab-trigger below for new method
    def download_images(
        self,
        urls=[],
        filenames=[],
        downloadDirectory="/tmp"
    ):
        """
        *download images*

        **Key Arguments:**
            # -

        **Usage:**
        .. todo::

            - add usage info
            - create a sublime snippet for usage

        .. code-block:: python 

            usage code 

        **Return:**
            - None

        .. todo::

            - @review: when complete, clean download_images method
            - @review: when complete add logging
        """
        self.log.info('starting the ``download_images`` method')

        from fundamentals.download.multiobject_download import multiobject_download
        localUrls = multiobject_download(
            urlList=urls,
            # directory(ies) to download the documents to - can be one url or a
            # list of urls the same length as urlList
            downloadDirectory=downloadDirectory,
            log=self.log,
            timeStamp=0,
            timeout=180,
            concurrentDownloads=10,
            resetFilename=filenames,
            credentials=False,  # { 'username' : "...", "password", "..." }
            longTime=False,
            indexFilenames=False
        )

        self.log.info('completed the ``download_images`` method')
        return localUrls

    # use the tab-trigger below for new method
    # xt-class-method

    # 5. @flagged: what actions of the base class(es) need ammending? ammend them here
    # Override Method Attributes
    # method-override-tmpx
