# 导包
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# 打开谷歌浏览器
chrome = webdriver.Chrome()
# 最大化
chrome.maximize_window()
# 隐式等待
# chrome.implicitly_wait(10)
# 进入主界面
chrome.get("https://ys.mihoyo.com/cloud/#/")

# 进入默认iframe
# chrome.switch_to.default_content()
# 进入登录iframe
chrome.switch_to.frame(WebDriverWait(chrome, 10, 0.5).until(lambda x: x.find_element(By.ID, "mihoyo-login-platform-iframe")))
# chrome.switch_to.frame(chrome.find_element(By.ID, "mihoyo-login-platform-iframe"))

# 点击密码登录
# 显式等待
# WebDriverWait(chrome, 10, 0.5).until(lambda x: x.find_element(By.ID, "tab-password")).click()
chrome.find_element(By.ID, "tab-password").click()

# 输入账号
chrome.find_element(By.ID, "username").send_keys("17876963323")
# 输入密码
chrome.find_element(By.ID, "password").send_keys("ZXCvbn13")
# 点击同意协议
chrome.find_element(By.CLASS_NAME, "el-checkbox__inner").click()
# 点击登录
chrome.find_element(By.CSS_SELECTOR, "#app > div > div > form > button > span").click()
# 进入默认iframe
chrome.switch_to.default_content()


# 退出浏览器
time.sleep(100)
chrome.quit()