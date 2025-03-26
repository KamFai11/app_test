import time

from appium import webdriver

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '7.1.2',  # 需与adb devices显示的设备系统版本一致[1,3](@ref)
    'deviceName': 'localhost:62001',  # 需通过adb devices验证设备连接[1,2](@ref)
    'automationName': 'UiAutomator2',  # 新版Appium必须添加的自动化引擎[1](@ref)
    'appPackage': 'com.android.launcher3',
    'appActivity': '.launcher3.Launcher',
    'noReset': True,  # 防止每次重置应用状态[2](@ref)
    'newCommandTimeout': 600  # 超时时间建议缩短为10分钟[1](@ref)
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

# 启动新的 Activity(界面)
activity_params = {
    "intent": "com.soco.veggies3.HUAWEI/com.soco.veggies3.MainActivity",  # 目标 Activity 的完整路径
    "appPackage": "com.soco.veggies3.HUAWEI",  # 应用包名
    "appActivity": "com.soco.veggies3.MainActivity",  # 要启动的 Activity
    "stopApp": False   # 是否先停止应用（默认 true）
}
# 启动
driver.execute_script("mobile: startActivity", activity_params)

# 进入后台5s，再回到前台
driver.background_app(5)
print("————————已回到前台")

driver.quit()