""" 案例练习 """
# 导包
import unittest

from tools import add


# 自定义测试类
class TestAdd(unittest.TestCase):
    def test_add1(self):
        if add(1, 2) == 3:
            print("测试通过")
        else:
            print("测试不通过")
    def test_add2(self):
        if add(10, 20) == 30:
            print("测试通过")
        else:
            print("测试不通过")
    def test_add3(self):
        if add(2, 3) == 5:
            print("测试通过")
        else:
            print("测试不通过")