""" 学习 TestCase（测试用例）的书写方法 """
import unittest
class TestDemo2(unittest.TestCase):
    def test_method1(self):
        print("测试方法2-1")
    def test_method2(self):
        print("测试方法2-2")