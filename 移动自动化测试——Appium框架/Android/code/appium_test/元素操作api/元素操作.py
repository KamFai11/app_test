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

# 点击
# driver.find_element(By.ID, "com.android.settings:id/search").click()  # 点击放大镜

# # 输入和清空输入框
# input_label = driver.find_element(By.ID, "android:id/search_src_text")
# # 输入hello
# input_label.send_keys("hello")
# # 等待2s
# time.sleep(2)
# # 清空文本内容
# input_label.clear()
# # 等待5s
# time.sleep(5)
# # 输入你好
# input_label.send_keys("你好")

# 获取文本内容
# texts = driver.find_elements(By.ID, "android:id/title")
# for text in texts:
#     print(text.text)

# 获取元素的位置和大小
# search_button = driver.find_element(By.ID, "com.android.settings:id/search")
# print(search_button.location)
# print(search_button.size)

# 根据元素的属性名获取属性值
titles = driver.find_elements(By.ID, "android:id/title")
for title in titles:
    print(title.get_attribute("enabled"))
    print(title.get_attribute("clickable"))
    print(title.get_attribute("name"))
    print(title.get_attribute("resourceId"))  # 特殊的
    print(title.get_attribute("className"))  # 特殊的

# 退出driver
driver.quit()

