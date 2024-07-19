import time

from selenium import webdriver
from selenium.webdriver.common.by import By

import random

from xpaths import *
import toExcel
import dataParse

# 不自动关闭浏览器
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

appID = "1544827472"
# appID = input()

# 注意此处添加了chrome_options参数
driver = webdriver.Chrome(options = option)
# 全屏显示
driver.maximize_window()
driver.get('https://www.baidu.com/')

time.sleep(2)
input = driver.find_element(by=By.XPATH, value='//*[@id="kw"]')
time.sleep(2)
input.send_keys("aaaaa")
time.sleep(2)
input.clear()