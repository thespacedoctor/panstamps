#!/usr/local/bin/python
# encoding: utf-8
"""
downloader
===========

*Tools to download the PS1 3Pi image stamps from STScI PanSTARRS image server*

The stamp server can be found `here <http://plpsipp1v.stsci.edu/cgi-bin/ps1cutouts>`_

:Author:
    David Young

:Date Created:
    March  2, 2016
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
        - ``downloadDirectory`` -- the path to where you want to download the images to. Downlaods to path command is run from by default.
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
    """
    # Initialisation

    def __init__(
            self,
            log,
            downloadDirectory=False,
            settings=False,
            fits=True,
            jpeg=False,
            arcsecSize=60,
            filterSet='gri',
            color=True,
            singleFilters=True,
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

        return None

    # Method Attributes
    def get(self):
        """
        *download the requested jpegs and fits files*

        **Return:**
            - ``fitsPaths`` -- a list of local paths to downloaded fits files
            - ``jpegPaths`` -- a list of local paths to downloaded jpeg files
            - ``colorPath`` -- a list of local paths to downloaded color jpeg file (just one image)
        """
        self.log.info('starting the ``get`` method')
        fitsPaths = []
        jpegPaths = []
        colorPath = []

        # REQUEST THE URL FROM STAMP SERVER
        content, status_code, url = self.get_html_content()
        if int(status_code) != 200:
            message = 'cound not download the image stamps. The STScI PanSTARRS image server returned HTTP status code %(status_code)s' % locals(
            )
            self.log.error(message)
            raise IOError(message)

        # CHECK WE ARE IN THE PS1 FOOTPRINT
        if "No PS1 3PI images were found" in content:
            self.log.warning(
                "No images found. PS1 3Pi has not covered this area of the sky. Here's the requested URL:\n%(url)s" % locals())
            return [], [], []

        # PARSE IMAGE URLS FROM HTML CONTENT
        allStacks, allWarps, colorImage = self.parse_html_for_image_urls_and_metadata(
            content=content
        )

        # GENERATE A DIRECTORY NAME IF ON DOWNLOAD DIRECTORY SPECIFIED
        if not self.downloadDirectory:
            ra = self.ra
            dec = self.dec
            try:
                dec = float(dec)
                if dec > 0:
                    sign = "p"
                else:
                    sign = "m"
                dec = abs(dec)
                directoryName = """%(ra)s%(sign)s%(dec)s""" % locals()
            except:
                if dec[0] == "-":
                    dec = "m" + dec[1:]
                elif dec[0] == "+":
                    dec = "p" + dec[1:]
                else:
                    dec = "p" + dec

                directoryName = """%(ra)s%(dec)s""" % locals()
                directoryName = directoryName.replace(":", "")
            downloadDirectory = directoryName
        else:
            downloadDirectory = self.downloadDirectory

        # RECURSIVELY CREATE MISSING DIRECTORIES
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

                fitsPaths += self._download_images(
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

                jpegPaths += self._download_images(
                    urls=urls,
                    filenames=jpegFilenames,
                    downloadDirectory=downloadDirectory
                )

        # IF COLOR STAMPS HAS BEEN REQUESTED
        if self.color:
            theseFilenames = []
            theseFilenames[:] = [t + ".jpeg" for t in colorImage["filename"]]

            colorPath += self._download_images(
                urls=colorImage["jpeg"],
                filenames=theseFilenames,
                downloadDirectory=downloadDirectory
            )

        self.log.info('completed the ``get`` method')

        if len(fitsPaths + jpegPaths + colorPath) == 0:
            self.log.warning(
                "No images found. Your options may not be set correctly. Here's the requested URL:\n%(url)s" % locals())

        return fitsPaths, jpegPaths, colorPath

    def get_html_content(
            self):
        """
        *Build the URL for the stamp request and extract the HTML content*

        **Return:**
            - ``content`` -- the HTML content of the requested URL
            - ``status_code`` -- the HTTP status code of the request response
            - ``url`` -- the URL requested from the PS1 stamp server

        **Usage:**

        .. code-block:: python 

            from panstamps.downloader import downloader
            content, status_code, url = downloader(
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
            ).get_html_content() 

            print status_code
            # OUT: 200

            print url
            # OUT: http://plpsipp1v.stsci.edu/cgi-bin/ps1cutouts?filter=gri&filter=color&catlist=&autoscale=99.500000&verbose=0&output_size=2400&filetypes=stack&pos=70.60271+-21.72433&size=2400
        """
        self.log.info('starting the ``get_html_content`` method')

        import requests

        r = self.ra
        d = self.dec

        pos = """%(r)s %(d)s""" % locals()
        filterSet = self.filterSet.split()
        if self.color:
            filterSet.append("color")

        fitsSize = int(self.arcsecSize * 4)
        jpegSize = fitsSize
        if jpegSize < 1200:
            jpegSize = 1200

        try:
            response = requests.get(
                url="http://plpsipp1v.stsci.edu/cgi-bin/ps1cutouts",
                params={
                    "pos": pos,
                    "filter": filterSet,
                    "filetypes": self.imageType,
                    "size": fitsSize,
                    "output_size": jpegSize,
                    "verbose": "0",
                    "autoscale": "99.500000",
                    "catlist": "",
                },
            )
        except requests.exceptions.RequestException:
            print('HTTP Request failed')

        self.log.info('completed the ``get_html_content`` method')
        return response.content, response.status_code, response.url

    def parse_html_for_image_urls_and_metadata(
            self,
            content):
        """
        *parse html for image urls and metadata*

        **Key Arguments:**
            - ``content`` -- the content of the requested PS1 stamp HTML page

        **Usage:**

        .. code-block:: python 

            from panstamps.downloader import downloader
            mydownloader = downloader(
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
            )
            content, status_code, url = mydownloader.get_html_content() 

            allStacks, allWarps, colorImage = mydownloader.parse_html_for_image_urls_and_metadata(content=content)

            for k,v in allStacks.iteritems():
                print k, v

            # OUT:
            ## jpegs ['http://plpsipp1v.stsci.edu/cgi-bin/fitscut.cgi?red=/data/ps1/node15/stps15.1/nebulous/23/3a/7187453864.gpc1%3ALAP.PV3.20140730%3A2015%3A01%3A29%3ARINGS.V3%3Askycell.0812.050%3ARINGS.V3.skycell.0812.050.stk.4297354.unconv.fits&x=70.602710&y=-21.724330&size=2400&wcs=1&asinh=True&autoscale=99.500000&output_size=2400', 'http://plpsipp1v.stsci.edu/cgi-bin/fitscut.cgi?red=/data/ps1/node08/stps08.1/nebulous/de/fa/5761784572.gpc1%3ALAP.PV3.20140730%3A2014%3A12%3A25%3ARINGS.V3%3Askycell.0812.050%3ARINGS.V3.skycell.0812.050.stk.4106421.unconv.fits&x=70.602710&y=-21.724330&size=2400&wcs=1&asinh=True&autoscale=99.500000&output_size=2400', 'http://plpsipp1v.stsci.edu/cgi-bin/fitscut.cgi?red=/data/ps1/node08/stps08.1/nebulous/1b/d7/5756633973.gpc1%3ALAP.PV3.20140730%3A2014%3A12%3A25%3ARINGS.V3%3Askycell.0812.050%3ARINGS.V3.skycell.0812.050.stk.4097309.unconv.fits&x=70.602710&y=-21.724330&size=2400&wcs=1&asinh=True&autoscale=99.500000&output_size=2400']
            ## fits ['http://plpsipp1v.stsci.edu/cgi-bin/fitscut.cgi?red=/data/ps1/node15/stps15.1/nebulous/23/3a/7187453864.gpc1:LAP.PV3.20140730:2015:01:29:RINGS.V3:skycell.0812.050:RINGS.V3.skycell.0812.050.stk.4297354.unconv.fits&format=fits&x=70.602710&y=-21.724330&size=2400&wcs=1&imagename=cutout_rings.v3.skycell.0812.050.stk.g.unconv.fits', 'http://plpsipp1v.stsci.edu/cgi-bin/fitscut.cgi?red=/data/ps1/node08/stps08.1/nebulous/de/fa/5761784572.gpc1:LAP.PV3.20140730:2014:12:25:RINGS.V3:skycell.0812.050:RINGS.V3.skycell.0812.050.stk.4106421.unconv.fits&format=fits&x=70.602710&y=-21.724330&size=2400&wcs=1&imagename=cutout_rings.v3.skycell.0812.050.stk.r.unconv.fits', 'http://plpsipp1v.stsci.edu/cgi-bin/fitscut.cgi?red=/data/ps1/node08/stps08.1/nebulous/1b/d7/5756633973.gpc1:LAP.PV3.20140730:2014:12:25:RINGS.V3:skycell.0812.050:RINGS.V3.skycell.0812.050.stk.4097309.unconv.fits&format=fits&x=70.602710&y=-21.724330&size=2400&wcs=1&imagename=cutout_rings.v3.skycell.0812.050.stk.i.unconv.fits']
            ## filters ['g', 'r', 'i']
            ## filenames ['stack_g_ra70.602710_dec-21.724330_arcsec600_skycell0812.050', 'stack_r_ra70.602710_dec-21.724330_arcsec600_skycell0812.050', 'stack_i_ra70.602710_dec-21.724330_arcsec600_skycell0812.050']

        **Return:**
            - ``allStacks`` -- dictionary of 4 equal length lists. jpeg remote urls, fits remote urls, filters and filenames.
            - ``allWarps`` -- dictionary of 4 equal length lists. jpeg remote urls, fits remote urls, filters and filenames.
            - ``colorImage`` -- dictionary of 4 equal length lists. jpeg remote urls, fits remote urls, filters and filenames.
        """
        self.log.info(
            'starting the ``parse_html_for_image_urls_and_metadata`` method')

        # SETUP THE VARIABLES
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

        # USE REGEX TO FIND FITS URLS
        reFitscutouts = re.compile(
            r"""<th>(?P<imagetype>\w+)\s+(?P<skycellid>\d+.\d+)\s+(?P<ffilter>[\w\\]+)(\s+(?P<mjd>\d+\.\d+))?<br.*?href="(http:)?//plpsipp1v.*?Display</a>.*?Fits cutout" href="(?P<fiturl>(http:)?//plpsipp1v.*?\.fits)".*?</th>""", re.I)

        thisIter = reFitscutouts.finditer(content)
        for item in thisIter:
            imagetype = item.group("imagetype")
            skycellid = item.group("skycellid")
            ffilter = item.group("ffilter")
            fiturl = item.group("fiturl")
            if fiturl[0:5] != "http":
                fiturl = "http:" + fiturl
            mjd = item.group("mjd")
            if imagetype == "stack":
                stackFitsUrls.append(fiturl)
            elif imagetype == "warp":
                warpFitsUrls.append(fiturl)

        # USE REGEX TO FIND JPEG URLS
        reJpegs = re.compile(
            r"""<img src="(?P<jpegUrl>(http:)?//plp.*?skycell.*?)\"""", re.I)

        thisIter = reJpegs.finditer(content)
        for item in thisIter:
            jpegUrl = item.group("jpegUrl")
            if jpegUrl[0:5] != "http":
                jpegUrl = "http:" + jpegUrl

            if "red" in jpegUrl and "blue" in jpegUrl:
                colorJpegUrl.append(jpegUrl)
            elif ".wrp." in jpegUrl:
                warpJpegUrls.append(jpegUrl)
            elif ".stk." in jpegUrl:
                stackJpegUrls.append(jpegUrl)

            else:
                self.log.warning(
                    "We are not downloading this jpeg: '%(jpegUrl)s'" % locals())

        # USE REGEX TO FIND FITS METADATA (STACKS)
        reFitsMeta = re.compile(
            r'http?.*?\?.*?skycell\.(?P<skycell>\d+\.\d+).*?x=(?P<ra>\d+\.\d+).*?y=(?P<dec>[+|-]?\d+\.\d+).*?size=(?P<pixels>\d+).*?stk\.(?P<ffilter>\w+).*?fits', re.S | re.I)

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

        # USE REGEX TO FIND FITS METADATA (WARPS)
        reFitsMeta = re.compile(
            r'http?.*?\?.*?skycell\.(?P<skycell>\d+\.\d+).*?x=(?P<ra>\d+\.\d+).*?y=(?P<dec>[+|-]?\d+\.\d+).*?size=(?P<pixels>\d+).*?wrp\.(?P<ffilter>\w+)\.(?P<mjd>\d+\.\d+).*?fits', re.S | re.I)

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

        # USE REGEX TO FIND COLOR IMAGE METADATA
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

    def _download_images(
        self,
        urls=[],
        filenames=[],
        downloadDirectory=False
    ):
        """
        *download images*

        **Key Arguments:**
            - ``urls`` -- list of the remote URLs to download
            - ``filenames`` -- list filenames to rename the downloads as
            - ``downloadDirectory`` -- path to the download directory

        **Return:**
            - ``localUrls`` -- list of the paths to local image files
        """
        self.log.info('starting the ``_download_images`` method')

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

        self.log.info('completed the ``_download_images`` method')
        return localUrls
