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

# 判断是否安装了燃烧的蔬菜
if driver.is_app_installed("com.soco.veggies3.HUAWEI"):
    # 如果安装了就卸载
    driver.remove_app("com.soco.veggies3.HUAWEI")
else:
    # 如果没安装就安装
    driver.install_app(r"D:\appfile\wechatfile\WeChat Files\wxid_dbcu7if8725n22\FileStorage\File\2025-03\18_base.apk")

