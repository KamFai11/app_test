# 导包
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 进入谷歌浏览器
chrome = webdriver.Chrome()
# 最大化
chrome.maximize_window()
# 进入bilibili主页
chrome.get("https://www.bilibili.com/")
time.sleep(2)

# 点击登录按钮
chrome.find_element(By.CLASS_NAME, "header-login-entry").click()
time.sleep(2)

# 进入登录工作的iframe

# 输入账号
chrome.find_element(By.CSS_SELECTOR, "body > div.bili-mini-mask > div > div.bili-mini-login-right-wp > div.login-pwd-wp > form > div:nth-child(1) > input[type=text]").send_keys("17876963324")
# 输入密码
chrome.find_element(By.CSS_SELECTOR, "body > div.bili-mini-mask > div > div.bili-mini-login-right-wp > div.login-pwd-wp > form > div:nth-child(3) > input[type=password]").send_keys("ZXCvbn13")
time.sleep(2)
# 点击登录
chrome.find_element(By.CLASS_NAME, "btn_primary").click()
# chrome.find_element(By.CSS_SELECTOR, ".btn_primary.disabled").click() # 典型错误
# chrome.find_element(By.CSS_SELECTOR, "").click()





# 退出浏览器
time.sleep(3)
chrome.quit()
