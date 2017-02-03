import os
import nose
import shutil
import yaml
from panstamps import downloader, cl_utils
from panstamps.utKit import utKit

from fundamentals import tools

su = tools(
    arguments={"settingsFile": None},
    docString=__doc__,
    logLevel="WARNING",
    options_first=False,
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


class test_downloader(unittest.TestCase):

    def test_downloader_function(self):
        kwargs = {}
        kwargs["log"] = log
        kwargs["settings"] = settings
        kwargs["fits"] = True
        kwargs["jpeg"] = False
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

    # def test_downloader_function02(self):
    #     kwargs = {}
    #     kwargs["log"] = log
    #     kwargs["settings"] = settings
    #     kwargs["fits"] = True
    #     kwargs["jpeg"] = True
    #     kwargs["arcsecSize"] = 60
    #     kwargs["filterSet"] = 'grizy'
    #     kwargs["color"] = True
    #     kwargs["singleFilters"] = False
    #     kwargs["ra"] = "70.60271"
    #     kwargs["dec"] = "-21.72433"
    #     kwargs["imageType"] = "warp"
    #     # xt-kwarg_key_and_value

    #     testObject = downloader(**kwargs)
    #     testObject.get()

    # def test_downloader_function03(self):
    #     kwargs = {}
    #     kwargs["log"] = log
    #     kwargs["settings"] = settings
    #     kwargs["fits"] = True
    #     kwargs["jpeg"] = False
    #     kwargs["arcsecSize"] = 60
    #     kwargs["filterSet"] = 'grizy'
    #     kwargs["color"] = False
    #     kwargs["singleFilters"] = True
    #     kwargs["ra"] = "70.60271"
    #     kwargs["dec"] = "-21.72433"
    #     kwargs["imageType"] = "stack"
    #     # xt-kwarg_key_and_value

    #     testObject = downloader(**kwargs)
    #     testObject.get()

    # def test_downloader_function04(self):
    #     kwargs = {}
    #     kwargs["log"] = log
    #     kwargs["settings"] = settings
    #     kwargs["fits"] = False
    #     kwargs["jpeg"] = True
    #     kwargs["arcsecSize"] = 60
    #     kwargs["filterSet"] = 'grizy'
    #     kwargs["color"] = False
    #     kwargs["singleFilters"] = True
    #     kwargs["ra"] = "70.60271"
    #     kwargs["dec"] = "-21.72433"
    #     kwargs["imageType"] = "warp"
    #     # xt-kwarg_key_and_value

    #     testObject = downloader(**kwargs)
    #     testObject.get()

    # def test_downloader_function05(self):
    #     kwargs = {}
    #     kwargs["log"] = log
    #     kwargs["settings"] = settings
    #     kwargs["fits"] = True
    #     kwargs["jpeg"] = False
    #     kwargs["arcsecSize"] = 600
    #     kwargs["filterSet"] = 'grizy'
    #     kwargs["color"] = False
    #     kwargs["singleFilters"] = True
    #     kwargs["ra"] = "70.60271"
    #     kwargs["dec"] = "-21.72433"
    #     kwargs["imageType"] = "stack"
    #     # xt-kwarg_key_and_value

    #     testObject = downloader(**kwargs)
    #     testObject.get()

    def test_downloader_function05(self):
        kwargs = {}
        kwargs["log"] = log
        kwargs["settings"] = settings
        kwargs["fits"] = False
        kwargs["jpeg"] = True
        kwargs["arcsecSize"] = 600
        kwargs["filterSet"] = 'gri'
        kwargs["color"] = True
        kwargs["singleFilters"] = True
        kwargs["ra"] = "70.60271"
        kwargs["dec"] = "-21.72433"
        kwargs["imageType"] = "stack"
        # xt-kwarg_key_and_value

        testObject = downloader(**kwargs)
        testObject.get()
