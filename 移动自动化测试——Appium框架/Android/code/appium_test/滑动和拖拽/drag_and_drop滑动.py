from appium import webdriver
from selenium.webdriver.common.by import By
import time
desired_caps = {
    'platformName': 'Android',
    'platformVersion': '7.1.2',  # 需与adb devices显示的设备系统版本一致[1,3](@ref)
    'deviceName': 'localhost:62026',  # 需通过adb devices验证设备连接[1,2](@ref)
    'automationName': 'UiAutomator2',  # 新版Appium必须添加的自动化引擎[1](@ref)
    'appPackage': 'com.android.settings',
    'appActivity': '.Settings',
    'noReset': True,  # 防止每次重置应用状态[2](@ref)
    'newCommandTimeout': 600,  # 超时时间建议缩短为10分钟[1](@ref)
    # "unicodeKeyboard": True,  # 启用 Unicode 输入法
    # "resetKeyboard": True  # 测试结束后恢复系统输入法
}
# 注意确认Appium Server端口是否为4723（默认值）
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)  # 隐式等待10s

# drag_and_drop滑动，有惯性
# 需要传进一个开始元素和一个结束元素
e_WLAN = driver.find_element(By.XPATH, "//*[@text='WLAN']")
e_tongzhi = driver.find_element(By.XPATH, "//*[@text='通知']")
driver.drag_and_drop(e_tongzhi, e_WLAN)


# 退出
time.sleep(5)
driver.quit()