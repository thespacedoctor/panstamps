#!/usr/local/bin/python
# encoding: utf-8
"""
getpackagepath.py
====================
:Summary:
    Get common file and folder paths for the host package

:Author:
    David Young

:Date Created:
    March  2, 2016

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: davidrobertyoung@gmail.com
"""
import os


def getpackagepath():
    """getpackagepath
    """
    moduleDirectory = os.path.dirname(__file__)
    packagePath = os.path.dirname(__file__) + "/../"

    return packagePath
