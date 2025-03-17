# 导包
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 打开浏览器
chrome = webdriver.Chrome()
# 窗口最大化
chrome.maximize_window()
# 打开登录界面
chrome.get("https://hmshop-test.itheima.net/Home/User/login.html")
# 用户操作

# 定位账号输入框并输入账号
account_input = chrome.find_element(By.CSS_SELECTOR, "#username")
account_input.send_keys("13488888888")


# 定位密码输入框并输入密码
password_input = chrome.find_element(By.CSS_SELECTOR, "#password")
password_input.send_keys("123456")

# 定位验证码输入框并输入验证码
yzm_input = chrome.find_element(By.CSS_SELECTOR, "#verify_code")
yzm_input.send_keys("8888")

# 点击登录
login_button = chrome.find_element(By.CSS_SELECTOR, "#loginform > div > div.login_bnt > a")
login_button.click()

# 关闭浏览器
time.sleep(100)
chrome.quit()
