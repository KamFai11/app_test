""" 学习 TestCase（测试用例）的书写方法 """
# 导包
import unittest
# 创建一个类继承TestCase
class TestDemo(unittest.TestCase):
    # 方法名要以test开头
    def test_method1(self):
        print("测试方法1")
    def test_method2(self):
        print("测试方法2")

# 光标放在类名后面运行，运行整个类中的测试方法
# 光标放在方法名后面运行，运行该方法
