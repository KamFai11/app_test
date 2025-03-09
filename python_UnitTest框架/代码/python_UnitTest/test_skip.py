import unittest

# version = 30
version = 29
class TestDemo(unittest.TestCase):
    @unittest.skip('没有什么原因，就是想跳过')
    def test_1(self):
        print("测试方法1")
    @unittest.skipIf(version >= 30, '版本大于等于30，不用跳过')
    def test_2(self):
        print("测试方法2")
    def test_3(self):
        print("测试方法3")