import os
import shutil
import yaml
import unittest
from panstamps import downloader, cl_utils
from panstamps.image import image
from panstamps.utKit import utKit

from fundamentals import tools

su = tools(
    arguments={"settingsFile": None},
    docString=__doc__,
    logLevel="DEBUG",
    options_first=True,
    projectName="panstamps"
)
arguments, settings, log, dbConn = su.setup()

# load settings
stream = file(
    "/Users/Dave/.config/panstamps/panstamps.yaml", 'r')
settings = yaml.load(stream)
stream.close()

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
utKit = utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()

import shutil
try:
    shutil.rmtree(pathToOutputDir)
except:
    pass
# COPY INPUT TO OUTPUT DIR
shutil.copytree(pathToInputDir, pathToOutputDir)


class test_image(unittest.TestCase):

    def test_image_function(self):
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

        kwargs["imageType"] = "warp"
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

        kwargs["imageType"] = "warp"
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
