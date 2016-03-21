#!/usr/local/bin/python
# encoding: utf-8
"""
*Add crosshairs, logo, scale, orientation and fake transients to the PS1 images*

:Author:
    David Young

:Date Created:
    March  4, 2016

**Usage:**
        .. todo::

            - add usage info
            - create a sublime snippet for usage

        .. code-block:: python 

            usage code 

.. todo::
    
    @review: when complete pull all general functions and classes into dryxPython
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
        - ``crosshairs`` -- add crosshairs to the image?. Default *True*
        - ``transient`` -- add a small transient marker at the centre of the image. Default *False*
        - ``scale`` -- add scale bar and orientation indicator to the image. Default *True*
        - ``invert`` -- invert the colours of the image. Default *False*
        - ``greyscale`` -- convert the image to greyscale. Default *False*

    **Usage:**
        .. todo::

            - add usage info
            - create a sublime snippet for usage

        .. code-block:: python 

            usage code 

    .. todo::

        - @review: when complete, clean image class
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract class to another module
    """
    # Initialisation
    # 1. @flagged: what are the unique attrributes for each object? Add them
    # to __init__

    def __init__(
            self,
            log,
            imagePath,
            settings=False,
            crosshairs=True,
            transient=False,
            scale=True,
            invert=False,
            greyscale=False
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
        *get the image object*

        **Return:**
            - ``image``

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

        image = None

        self.log.info('completed the ``get`` method')
        return image

    # xt-class-method

    # 5. @flagged: what actions of the base class(es) need ammending? ammend them here
    # Override Method Attributes
    # method-override-tmpx
