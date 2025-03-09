import unittest

from test.testcase import TestAdd

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestAdd))
runner = unittest.TextTestRunner()
runner.run(suite)
