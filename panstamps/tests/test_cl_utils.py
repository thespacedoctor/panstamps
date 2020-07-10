from __future__ import print_function
from builtins import str
import os
import unittest
import shutil
import yaml
from panstamps.utKit import utKit
from fundamentals import tools
from os.path import expanduser
from docopt import docopt
from panstamps import cl_utils
doc = cl_utils.__doc__
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


class test_cl_utils(unittest.TestCase):

    def test_stack_fits_ra_dec(self):
        # TEST CL-OPTIONS

        command = "panstamps --downloadFolder=%(pathToOutputDir)s stack 09:55:52.2 +69:40:47" % globals()
        args = docopt(doc, command.split(" ")[1:])
        cl_utils.main(args)

        command = "panstamps --downloadFolder=%(pathToOutputDir)s --width=4 --filters=griyz stack 09:55:52.2 +69:40:47" % globals()
        args = docopt(doc, command.split(" ")[1:])
        cl_utils.main(args)

        return

    def test_stack_jpeg_ra_dec(self):
        # TEST CL-OPTIONS
        command = "panstamps -Fj --width=4 --filters=gri --downloadFolder=%(pathToOutputDir)s stack 09:55:52.2 +69:40:47" % globals(
        )
        args = docopt(doc, command.split(" ")[1:])
        cl_utils.main(args)

        command = "panstamps -FjAt --width=4 --filters=gri --downloadFolder=%(pathToOutputDir)s stack 09:55:52.2 +69:40:47" % globals(
        )
        args = docopt(doc, command.split(" ")[1:])
        cl_utils.main(args)

        command = "panstamps -FJc --width=4 --filters=gri --downloadFolder=%(pathToOutputDir)s stack 09:55:52.2 +69:40:47" % globals(
        )
        args = docopt(doc, command.split(" ")[1:])
        cl_utils.main(args)

        command = "panstamps -FJci --width=4 --filters=gri --downloadFolder=%(pathToOutputDir)s stack 09:55:52.2 +69:40:47" % globals(
        )
        args = docopt(doc, command.split(" ")[1:])
        cl_utils.main(args)

        command = "panstamps -FJcig --width=4 --filters=gri --downloadFolder=%(pathToOutputDir)s stack 09:55:52.2 +69:40:47" % globals(
        )
        args = docopt(doc, command.split(" ")[1:])
        cl_utils.main(args)

        return

    def test_temporal_constraints_ra_dec(self):
        # TEST CL-OPTIONS
        command = "panstamps -Fj --width=4 --filters=gri --downloadFolder=%(pathToOutputDir)s warp 189.1960991 28.2374845 55246.63 55246.64" % globals(
        )
        args = docopt(doc, command.split(" ")[1:])
        cl_utils.main(args)

        command = "panstamps -Fj --closest=before --width=4 --filters=gri --downloadFolder=%(pathToOutputDir)s 189.1960991 28.2374845 55246.64" % globals(
        )
        args = docopt(doc, command.split(" ")[1:])
        cl_utils.main(args)

        command = "panstamps -Fj --closest=-120 --width=4 --filters=gri --downloadFolder=%(pathToOutputDir)s 189.1960991 28.2374845 55246.64" % globals(
        )
        args = docopt(doc, command.split(" ")[1:])
        cl_utils.main(args)

        return

    # x-class-to-test-named-worker-function
