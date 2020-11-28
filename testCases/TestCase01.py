# Test case 01
from configparser import ConfigParser
import self as self
import os
from commonMethods.seleniumMethods import selMethods


class TestCase01(selMethods):

    def firsttestcase(self):
        print(os.path.realpath("TestCase01.py"))
        path1 = os.path.split(os.getcwd())
        print(path1[1])
        print(os.path.dirname(os.path.realpath("TestCase01.py")))
        # print(path.split("\\",3))
        # selMethods.browserStart(self)
        # selMethods.launchURL(self,"https://www.google.com")


tc = TestCase01()
tc.firsttestcase()
