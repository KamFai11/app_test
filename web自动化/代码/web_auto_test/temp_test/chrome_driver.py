# 导包
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 打开浏览器
chrome = webdriver.Chrome()  # 打开浏览器
chrome.maximize_window()  # 最大化窗口

# 访问登录页
chrome.get("https://www.baidu.com/")
time.sleep(100)

# 关闭浏览器
chrome.quit()
