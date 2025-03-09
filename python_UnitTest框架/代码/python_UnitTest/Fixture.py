import unittest
class Login(unittest.TestCase):
    def setUp(self):
        """在执行每个方法之前，都会执行一次该方法"""
        print("输入网址...")
    def tearDown(self):
        """在执行每个方法之后，都会执行一次该方法"""
        print("关闭当前页面...")
    @classmethod
    def setUpClass(cls):
        print("打开浏览器")
    @classmethod
    def tearDownClass(cls):
        print("关闭浏览器")
    def test_1(self):
        print("输入正确的用户名和密码")
    def test_2(self):
        print("输入错误的用户名和密码")