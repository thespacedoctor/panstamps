from __future__ import print_function
from builtins import str
import os
import unittest
import shutil
import yaml
from panstamps.utKit import utKit
from fundamentals import tools
from os.path import expanduser
home = expanduser("~")

packageDirectory = utKit("").get_project_root()
settingsFile = packageDirectory + "/test_settings.yaml"

su = tools(
    arguments={"settingsFile": settingsFile},
    docString=__doc__,
    logLevel="DEBUG",
    options_first=False,
    projectName=None,
    defaultSettingsFile=False
)
arguments, settings, log, dbConn = su.setup()

# SETUP PATHS TO COMMON DIRECTORIES FOR TEST DATA
moduleDirectory = os.path.dirname(__file__)
pathToInputDir = moduleDirectory + "/input/"
pathToOutputDir = moduleDirectory + "/output/"

try:
    shutil.rmtree(pathToOutputDir)
except:
    pass
# COPY INPUT TO OUTPUT DIR
shutil.copytree(pathToInputDir, pathToOutputDir)

# Recursively create missing directories
if not os.path.exists(pathToOutputDir):
    os.makedirs(pathToOutputDir)

class test_image(unittest.TestCase):

    def test_image_function(self):
        from panstamps import downloader
        from panstamps.image import image
        kwargs = {}
        kwargs["log"] = log
        kwargs["settings"] = settings
        kwargs["arcsecSize"] = 4
        kwargs["fits"] = False
        kwargs["jpeg"] = True
        kwargs["arcsecSize"] = 60
        kwargs["filterSet"] = 'grizy'
        kwargs["color"] = True
        kwargs["singleFilters"] = True
        kwargs["ra"] = "70.60271"
        kwargs["dec"] = "-21.72433"
        kwargs["imageType"] = "stack"
        # xt-kwarg_key_and_value

        testObject = downloader(**kwargs)
        testObject.get()

        # kwargs["imageType"] = "warp"
        kwargs["imageType"] = "stack"
        testObject = downloader(**kwargs)
        testObject.get()

        kwargs["arcsecSize"] = 600
        testObject = downloader(**kwargs)
        testObject.get()

        kwargs = {}
        kwargs["log"] = log
        kwargs["settings"] = settings
        # xt-kwarg_key_and_value
        kwargs["arcsecSize"] = 4
        kwargs["imagePath"] = pathToOutputDir + "/something.png"
        kwargs["settings"] = False
        kwargs["crosshairs"] = True
        kwargs["transient"] = False
        kwargs["scale"] = True
        kwargs["invert"] = False
        kwargs["greyscale"] = False
        testObject = image(**kwargs)
        testObject.get()

    def test_image_function02(self):
        from panstamps import downloader
        from panstamps.image import image
        kwargs = {}
        kwargs["log"] = log
        kwargs["settings"] = settings
        kwargs["fits"] = False
        kwargs["jpeg"] = True
        kwargs["arcsecSize"] = 60
        kwargs["filterSet"] = 'grizy'
        kwargs["color"] = True
        kwargs["singleFilters"] = True
        kwargs["ra"] = "208.49364"
        kwargs["dec"] = "-27.22365"
        kwargs["imageType"] = "stack"
        # xt-kwarg_key_and_value

        testObject = downloader(**kwargs)
        testObject.get()

        # kwargs["imageType"] = "warp"
        kwargs["imageType"] = "stack"
        testObject = downloader(**kwargs)
        testObject.get()

        kwargs["arcsecSize"] = 600
        testObject = downloader(**kwargs)
        testObject.get()

        kwargs = {}
        kwargs["log"] = log
        kwargs["settings"] = settings
        # xt-kwarg_key_and_value
        kwargs["arcsecSize"] = 4
        kwargs["imagePath"] = pathToOutputDir + "/something.png"
        kwargs["settings"] = False
        kwargs["crosshairs"] = True
        kwargs["transient"] = False
        kwargs["scale"] = True
        kwargs["invert"] = False
        kwargs["greyscale"] = False
        testObject = image(**kwargs)
        testObject.get()

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
