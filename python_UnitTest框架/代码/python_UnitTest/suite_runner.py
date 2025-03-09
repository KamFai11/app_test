"""学习 TestSuite 和 TestRunner 的使用"""
# 导包
import unittest

from testcast1 import TestDemo1
from testcast2 import TestDemo2

# 实例化套件对象
suite = unittest.TestSuite()

# 使用套件对象添加用例方法
# 方法一：
# suite.addTest(TestDemo1('test_method1'))
# suite.addTest(TestDemo1('test_method2'))
# suite.addTest(TestDemo2('test_method1'))
# suite.addTest(TestDemo2('test_method2'))

# 方法二：
suite.addTest(unittest.makeSuite(TestDemo1))
suite.addTest(unittest.makeSuite(TestDemo2))

# 实例化运行对象
runner = unittest.TextTestRunner()
# 使用运行对象去执行套件对象
# 运行对象.run(套件对象)
runner.run(suite)
