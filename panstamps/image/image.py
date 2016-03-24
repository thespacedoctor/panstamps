#!/usr/local/bin/python
# encoding: utf-8
"""
*Add crosshairs, logo, scale, orientation and fake transients to pre-downloaded PS1 images*

:Author:
    David Young

:Date Created:
    March  4, 2016
"""
################# GLOBAL IMPORTS ####################
import sys
import os
os.environ['TERM'] = 'vt100'
from fundamentals import tools


class image():
    """
    *The worker class for the image module*

    **Key Arguments:**
        - ``log`` -- logger
        - ``settings`` -- the settings dictionary
        - ``imagePath`` -- path to the image to manipulate
        - ``arcsecSize`` -- the size of the image stamps to download (1 arcsec == 4 pixels).
        - ``crosshairs`` -- add crosshairs to the image?. Default *True*
        - ``transient`` -- add a small transient marker at the centre of the image. Default *False*
        - ``scale`` -- add scale bar and orientation indicator to the image. Default *True*
        - ``invert`` -- invert the colours of the image. Default *False*
        - ``greyscale`` -- convert the image to greyscale. Default *False*
        - ``colorImage`` -- is the input image a color image, Default **False*. Note, also assumes a color image if 'color' in filename

    **Usage:**

        .. code-block:: python 

            from panstamps.image import image
            myimage = image(
                log=log,
                settings=False,
                imagePath="70.60271m21.72433/color_igr_ra70.602710_dec-21.724330_arcsec120_skycell0812.050.jpeg",
                arcsecSize=120,
                crosshairs=True,
                transient=False,
                scale=True,
                invert=False,
                greyscale=False,
                colorImage=True
            ).get()

        Here's the resulting image from this code:

        .. image:: https://i.imgur.com/TXX2BS0.png
    """
    # Initialisation

    def __init__(
            self,
            log,
            imagePath,
            arcsecSize,
            settings=False,
            crosshairs=True,
            transient=False,
            scale=True,
            invert=False,
            greyscale=False,
            colorImage=False
    ):
        self.log = log
        log.debug("instansiating a new 'image' object")
        self.settings = settings
        self.imagePath = imagePath
        self.crosshairs = crosshairs
        self.transient = transient
        self.scale = scale
        self.invert = invert
        self.greyscale = greyscale
        self.arcsecSize = arcsecSize
        self.colorImage = colorImage
        # xt-self-arg-tmpx

        return None

    # Method Attributes
    def get(self):
        """
        *annotate the PS1 image*

        **Return:**
            - ``image`` -- a PIL image object
        """
        self.log.info('starting the ``get`` method')

        from PIL import Image, ImageDraw, ImageChops, ImageFont

        im = Image.open(self.imagePath)
        im = im.convert("RGB")

        # DETERMINE THE SIZE OF THE IMAGE
        imWidth, imHeight = im.size

        # THE CROSS HAIRS SHOULD BE 1/6 THE LENGTH OF THE SMALLEST DIMENSON
        chLen = int(min(imWidth, imHeight) / 6)

        # THE GAP IN THE CENTRE SHOULD BE 1/60 OF THE LENGTH OF THE SMALLEST
        # DIMENSON
        gapLen = int(min(imWidth, imHeight) / 60)

        # LINE WIDTH SHOULD BE EASILY VIEWABLE AT ALL SIZES - 0.2% OF THE WIDTH SEEMS GOOD
        # SEEMS FINE
        lineWidth = int(max(imWidth, imHeight) / 350)

        lines = []
        l = (imWidth / 2 - gapLen - chLen, imHeight /
             2, imWidth / 2 - gapLen, imHeight / 2)
        lines.append(l)
        l = (imWidth / 2 + gapLen, imHeight /
             2, imWidth / 2 + gapLen + chLen, imHeight / 2)
        lines.append(l)
        l = (imWidth / 2, imHeight /
             2 - gapLen - chLen, imWidth / 2, imHeight / 2 - gapLen)
        lines.append(l)
        l = (imWidth / 2, imHeight /
             2 + gapLen, imWidth / 2, imHeight / 2 + gapLen + chLen)
        lines.append(l)

        if self.invert:
            im = ImageChops.invert(im)

        if self.greyscale:
            im = im.convert("L")
            im = im.convert("RGBA")

        # DETERMINE THE BEST COLOR FOR LINES
        # tmp = im.resize((1, 1), resample=3)
        # tmp = ImageChops.invert(tmp)
        # bestColor = tmp.getcolors()[0][1]

        if self.invert:
            bestColor = "#dc322f"
        elif not self.colorImage and 'color' not in self.imagePath.split("/")[-1]:
            bestColor = "#3c96ed"
        elif self.greyscale:
            bestColor = "#3c96ed"
        elif self.colorImage or 'color' in self.imagePath.split("/")[-1] and not self.invert:
            bestColor = "#7eb70a"
        else:
            bestColor = "#dc322f"

        # GENERATE THE DRAW OBJECT AND DRAW THE CROSSHAIRS
        draw = ImageDraw.Draw(im)
        if self.crosshairs:
            for l in lines:
                draw.line(l, fill=bestColor, width=lineWidth)

        from PIL import Image, ImageDraw, ImageChops, ImageFont

        # DRAW A SCALEBAR ON THE IMAGE
        physicalWidth = int(self.arcsecSize)
        startRatio = 0.3
        sbPhysicalWidth = physicalWidth * startRatio
        sbPixelWidth = imWidth * startRatio

        # IF ON THE DEGREE SCALE
        if sbPhysicalWidth > 3600:
            divider = 3600
            unit = "degree"
        # IF ON THE ARCMIN SCALE
        elif sbPhysicalWidth > 60:
            divider = 60.
            unit = "arcmin"
        # IF ON THE ARCSEC SCALE
        else:
            divider = 1.
            unit = "arcsec"

        # FIND THE WIDTH OF THE BAR TO THE NEAREST WHOLE NUMBER ON GIVEN SCALE
        tmpWidth = sbPhysicalWidth / divider
        self.log.debug("physicalWidth = %(physicalWidth)s" % locals())
        self.log.debug("sbPhysicalWidth = %(sbPhysicalWidth)s" % locals())
        displayPhysicalWidth = sbPhysicalWidth / divider
        self.log.debug(
            "displayPhysicalWidth = %(displayPhysicalWidth)s" % locals())
        displayPhysicalWidth = int(sbPhysicalWidth / divider)
        self.log.debug(
            "displayPhysicalWidth = %(displayPhysicalWidth)s" % locals())
        ratio = displayPhysicalWidth / tmpWidth
        sbPhysicalWidth = int(sbPhysicalWidth * ratio)
        sbPixelWidth = int(sbPixelWidth * ratio)

        # DRAW THE SCALEBAR
        l = (imWidth / 20, imHeight - imHeight / 20,
             imWidth / 20 + sbPixelWidth, imHeight - imHeight / 20)
        if self.scale:
            draw.line(l, fill=bestColor, width=lineWidth)

        # ADD SCALE TEXT
        text = """%(displayPhysicalWidth)s %(unit)s""" % locals()
        fontsize = int(imWidth / 30)
        moduleDirectory = os.path.dirname(__file__)
        font = ImageFont.truetype(
            moduleDirectory + "/../resources/fonts/source-sans-pro-regular.ttf", fontsize)
        if self.scale:
            draw.text((imWidth / 20, imHeight - imHeight / 20 - fontsize * 1.3), text, fill=bestColor,
                      font=font, anchor=None)

        # ADD ORIENTATION INDICATOR
        lines = []
        lineLength = int(min(imWidth, imHeight) / 20)
        l = (imWidth - imWidth / 20 - lineLength, imHeight - imHeight / 20,
             imWidth - imWidth / 20, imHeight - imHeight / 20)
        lines.append(l)
        l = (imWidth - imWidth / 20, imHeight - imHeight / 20,
             imWidth - imWidth / 20, imHeight - imHeight / 20 - lineLength)
        lines.append(l)
        if self.scale:
            for l in lines:
                draw.line(l, fill=bestColor, width=lineWidth)
            # ADD SCALE TEXT
            draw.text((imWidth - imWidth / 20 - fontsize * 0.3, imHeight - imHeight / 20 - lineLength - fontsize * 1.3), "N", fill=bestColor,
                      font=font, anchor=None)
            draw.text((imWidth - imWidth / 20 - lineLength - fontsize * 0.8, imHeight - imHeight / 20 - fontsize * 0.6), "E", fill=bestColor,
                      font=font, anchor=None)
        del draw

        # ADD THE PS1 LOGO
        wmHeight = int(max(imWidth, imHeight) / 20)
        moduleDirectory = os.path.dirname(__file__)
        imagePath = moduleDirectory + "/../resources/ps1.png"
        logo = Image.open(imagePath)
        (logoWidth, logoHeight) = logo.size
        wmWidth = int((wmHeight / float(logoHeight)) * logoWidth)
        logo = logo.resize((wmWidth, wmHeight), resample=3)

        # CREATE A TRANSPARENT IMAGE THE SIZE OF THE ORIGINAL IMAGE - PASTE THE
        # LOGO WHERE REQUIRED
        logoPH = Image.new("RGBA", (imWidth, imHeight), color=(0, 0, 0, 0))
        logoPH.paste(logo, box=(imHeight / 25, imHeight / 25))

        # NOW TONE DOWN THE OPACITY
        trans = Image.new("RGBA", (imWidth, imHeight), color=(0, 0, 0, 0))
        logo = Image.blend(trans, logoPH, alpha=0.75)

        # ADD THE WATERMARK STAMP TO THE ORIGINAL IMAGE
        im = Image.alpha_composite(im.convert("RGBA"), logo)

        # ADD A TRANSIENT MARKER
        outercircle = 60
        if self.transient:
            draw = ImageDraw.Draw(im)
            xy1 = (imWidth / 2 - imWidth / 100, imWidth / 2 - imWidth / 100,
                   imWidth / 2 + imWidth / 100, imWidth / 2 + imWidth / 100)
            xy2 = (imWidth / 2 - imWidth / outercircle, imWidth / 2 - imWidth / outercircle,
                   imWidth / 2 + imWidth / outercircle, imWidth / 2 + imWidth / outercircle)
            xy3 = (imWidth / 2 - imWidth / (outercircle) - 1, imWidth / 2 - imWidth / (outercircle) - 1,
                   imWidth / 2 + imWidth / (outercircle) + 1, imWidth / 2 + imWidth / (outercircle) + 1)
            xy4 = (imWidth / 2 - imWidth / (outercircle) - 2, imWidth / 2 - imWidth / (outercircle) - 2,
                   imWidth / 2 + imWidth / (outercircle) + 2, imWidth / 2 + imWidth / (outercircle) + 2)
            draw.arc(xy2, 0, 360, fill="#b2141c")
            draw.arc(xy3, 0, 360, fill="#b2141c")
            draw.arc(xy4, 0, 360, fill="#b2141c")
            draw.pieslice(xy1, 0, 361, fill="#b2141c")

        im.save(self.imagePath)

        self.log.info('completed the ``get`` method')
        return image

    # xt-class-method
