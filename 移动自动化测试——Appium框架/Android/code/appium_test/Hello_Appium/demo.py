import time

from appium import webdriver
desired_caps = dict()
# 手机参数
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.2'
desired_caps['deviceName'] = 'localhost:62001'
# 应用参数
desired_caps['appPackage'] = 'com.android.gallery3d'
desired_caps['appActivity'] = '.app.GalleryActivity'

# 获取driver
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(5)

# 启动短信
driver.start_activity("com.amaze.filemanager", ".activities.MainActivity")
driver.quit()