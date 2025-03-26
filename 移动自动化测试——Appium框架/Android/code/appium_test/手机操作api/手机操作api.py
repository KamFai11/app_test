from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
desired_caps = {
    'platformName': 'Android',
    'platformVersion': '7.1.2',  # 需与adb devices显示的设备系统版本一致[1,3](@ref)
    'deviceName': 'localhost:62026',  # 需通过adb devices验证设备连接[1,2](@ref)
    'automationName': 'UiAutomator2',  # 新版Appium必须添加的自动化引擎[1](@ref)
    'appPackage': 'com.android.launcher3',
    'appActivity': '.launcher3.Launcher',
    'noReset': True,  # 防止每次重置应用状态[2](@ref)
    'newCommandTimeout': 600,  # 超时时间建议缩短为10分钟[1](@ref)
    # "unicodeKeyboard": True,  # 启用 Unicode 输入法
    # "resetKeyboard": True  # 测试结束后恢复系统输入法
}
# 注意确认Appium Server端口是否为4723（默认值）
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)  # 隐式等待10s

# 获取手机分辨率
print(driver.get_window_size())

# 截图
driver.get_screenshot_as_file("screenshot.png")

# 获取当前网络
print(driver.network_connection)

# 设置当前网络
driver.set_network_connection(6)
print(driver.network_connection)

# 发送键到设备
# 需求：三次音量+，一次返回，两次音量-
driver.press_keycode(24)
time.sleep(1)
driver.press_keycode(24)
time.sleep(1)
driver.press_keycode(24)
time.sleep(1)
driver.press_keycode(4)
time.sleep(1)
driver.press_keycode(25)
time.sleep(1)
driver.press_keycode(25)
time.sleep(1)

# 打开通知栏
driver.open_notifications()
# 关闭通知栏
driver.press_keycode(4)
# 退出
time.sleep(5)
driver.quit()