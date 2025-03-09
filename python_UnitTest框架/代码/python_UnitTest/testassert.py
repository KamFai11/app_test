""" assert """
# 导包
import unittest

from tools import add


# 自定义测试类
class TestAdd(unittest.TestCase):
    def test_add1(self):
        # 断言
        # （预期结果，实际结果）
        self.assertEquals(3, add(1, 2))
    def test_add2(self):
        self.assertEquals(30, add(10, 20))
    def test_add3(self):
        self.assertEquals(5, add(2, 3))