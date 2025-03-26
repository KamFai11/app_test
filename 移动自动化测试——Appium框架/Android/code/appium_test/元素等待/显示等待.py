from appium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '7.1.2',  # 需与adb devices显示的设备系统版本一致[1,3](@ref)
    'deviceName': 'localhost:62001',  # 需通过adb devices验证设备连接[1,2](@ref)
    'automationName': 'UiAutomator2',  # 新版Appium必须添加的自动化引擎[1](@ref)
    'appPackage': 'com.android.settings',
    'appActivity': '.Settings',
    'noReset': True,  # 防止每次重置应用状态[2](@ref)
    'newCommandTimeout': 600  # 超时时间建议缩短为10分钟[1](@ref)
}

# 注意确认Appium Server端口是否为4723（默认值）
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 点击返回
# 显示等待10s（等待返回按钮的出现）
back_button = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.XPATH, "//*[@content-desc='收起']"))
back_button.click()  # 点击


driver.quit()