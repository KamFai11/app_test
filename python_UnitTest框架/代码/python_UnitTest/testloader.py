# 导包
import unittest
# 实例化加载对象并添加用例
# 方法一
# suite = unittest.TestLoader().discover('./case', 'test*.py')
# 方法二
suite = unittest.defaultTestLoader.discover('./case', 'test*.py')
# 实例化运行对象
runner = unittest.TextTestRunner()
# 执行
runner.run(suite)
