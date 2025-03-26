from appium import webdriver
from selenium.webdriver.common.by import By
import time
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
driver.implicitly_wait(10)  # 建议添加隐式等待提升稳定性[2](@ref)
time.sleep(3)


# ---------------定位一个元素
# # 通过id定位放大镜，点击
# driver.find_element(By.ID, "com.android.settings:id/search").click()
# # 通过class定位输入框，输入hello
# driver.find_element(By.CLASS_NAME, "android.widget.EditText").send_keys("hello")
# time.sleep(2)
# # 通过xpath定位返回按钮，点击
# driver.find_element(By.XPATH, "//*[@content-desc='收起']").click()


# ---------------定位一组元素
titles = driver.find_elements(By.ID, "android:id/title")
print(titles)
print(len(titles))
for title in titles:
    print(title.text)

text_view = driver.find_elements(By.CLASS_NAME, "android.widget.TextView")
for text_view in text_view:
    print(text_view.text)
elements = driver.find_elements(By.XPATH, "//*[contains(@text,'设')]")
for element in elements:
    print(element.text)
time.sleep(5)
driver.quit()