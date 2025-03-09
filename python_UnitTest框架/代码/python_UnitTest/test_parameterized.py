"""参数化代码"""
# 导包
from parameterized import parameterized
import unittest

from tools import add

# 组织测试数据 [(), (), ()]
data = [(1, 2, 3), (10, 20, 30), (2, 3, 5)]

# 定义测试类
class TestLogin(unittest.TestCase):
    # 书写测试方法
    @parameterized.expand(data)
    def test_Login(self, a, b, acount):
        self.assertEquals(acount, add(a, b))
# 组织测试数据并传参（装饰器 @）
