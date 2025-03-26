from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
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

# --------------轻敲手势
# 定位要点击的元素
element_WLAN = driver.find_element(By.XPATH, "//*[@text='WLAN']")
# 创建 TouchAction 对象并执行点击动作
# TouchAction(driver).tap(element_WLAN).perform()
# 根据鼠标位置点击
# TouchAction(driver).tap(x=144, y=799).perform()

# --------------按下和抬起
# TouchAction(driver).press(x=200, y=799).perform()  # 按下
# time.sleep(2)  # 等待两秒
# TouchAction(driver).press(x=200, y=799).release().perform()  # 再次按下并抬起

# --------------等待
# TouchAction(driver).tap(x=144, y=799).perform()  # 点击WLAN,进入
# time.sleep(2)
# TouchAction(driver).press(x=145, y=304).wait(2000).release().perform()  # 长安两秒并松开

# --------------长按
# TouchAction(driver).tap(x=144, y=799).perform()  # 点击WLAN,进入
# time.sleep(2)
# TouchAction(driver).long_press(x=145, y=304, duration=2000).perform()

# --------------移动
# 启动新的 Activity（界面），进入手势密码界面
activity_params = {
    "intent": "com.android.settings/.ChooseLockPattern",  # 目标 Activity 的完整路径
    "appPackage": "com.android.settings",  # 应用包名
    "appActivity": ".ChooseLockPattern",  # 要启动的 Activity
    "stopApp": False   # 是否先停止应用（默认 true）
}
# 执行脚本进入手势密码界面
driver.execute_script("mobile: startActivity", activity_params)
print(driver.current_package)
print(driver.current_activity)
# 获取屏幕尺寸
size = driver.get_window_size()
print("屏幕尺寸：", size)  # 输出示例：{'width': 1080, 'height': 1920}
# 画一个手势
(TouchAction(driver).press(x=208, y=899).move_to(x=540, y=906)
 .move_to(x=869, y=906).move_to(x=538, y=1232)
 .move_to(x=212, y=1563).move_to(x=540, y=1565)
 .move_to(x=869, y=1560).release().perform())




# 退出
time.sleep(5)
driver.quit()
