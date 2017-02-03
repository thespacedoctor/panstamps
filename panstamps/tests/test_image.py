import os
import nose
import shutil
import yaml
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


class test_image(unittest.TestCase):

    def test_image_function(self):
        kwargs = {}
        kwargs["log"] = log
        kwargs["settings"] = settings
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
        kwargs["imagePath"] = "/tmp/something.png"
        kwargs["settings"] = False
        kwargs["crosshairs"] = True
        kwargs["transient"] = False
        kwargs["scale"] = True
        kwargs["invert"] = False
        kwargs["greyscale"] = False
        testObject = image(**kwargs)
        testObject.get()

        basePath = "/tmp/70.60271m21.72433"
        for d in os.listdir(basePath):
            if os.path.isfile(os.path.join(basePath, d)) and "jpeg" in d:
                print d

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
        kwargs["imagePath"] = "/tmp/something.png"
        kwargs["settings"] = False
        kwargs["crosshairs"] = True
        kwargs["transient"] = False
        kwargs["scale"] = True
        kwargs["invert"] = False
        kwargs["greyscale"] = False
        testObject = image(**kwargs)
        testObject.get()

        basePath = "/tmp/70.60271m21.72433"
        for d in os.listdir(basePath):
            if os.path.isfile(os.path.join(basePath, d)) and "jpeg" in d:
                print d

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
