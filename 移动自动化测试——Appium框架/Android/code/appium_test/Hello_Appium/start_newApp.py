from appium import webdriver

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

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

print(driver.current_package)
print(driver.current_activity)

# 启动新的 Activity（界面）
activity_params = {
    "intent": "com.android.documentsui/.FilesActivity",  # 目标 Activity 的完整路径
    "appPackage": "com.android.documentsui",  # 应用包名
    "appActivity": ".FilesActivity",  # 要启动的 Activity
    "stopApp": False   # 是否先停止应用（默认 true）
}
# 启动
driver.execute_script("mobile: startActivity", activity_params)
print(driver.current_package)
print(driver.current_activity)