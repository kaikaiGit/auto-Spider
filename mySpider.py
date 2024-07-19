import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By

from xpaths import *
import toExcel
import dataParse

# 不自动关闭浏览器
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

default_appID = "1544827472"

# 注意此处添加了chrome_options参数
driver = webdriver.Chrome(options = option)
# 全屏显示
driver.maximize_window()
driver.get('https://app.diandian.com/login')

# todo 给20秒钟的时间来手动扫码登录
time.sleep(12)

# 输入appID
input1 = driver.find_element(by=By.XPATH, value=input1Xpath)
input1.send_keys(default_appID)

time.sleep(4)

# 点击搜索
btn1 = driver.find_element(by=By.XPATH, value=btn1Xpath)
btn1.click()

time.sleep(2)

# 获取打开的多个窗口句柄
windows = driver.window_handles
# 切换到当前最新打开的窗口
driver.switch_to.window(windows[-1])

time.sleep(6)

# todo 从此处开始 数据获取
for appID in dataParse.appIDList:
    input2 = driver.find_element(by=By.XPATH, value=input2Xpath)
    input2.clear()
    time.sleep(1)
    input2.send_keys(appID)

    btn2 = driver.find_element(by=By.XPATH, value=btn2Xpath)
    btn2.click()

    time.sleep(random.randint(3, 5))

    for country in dataParse.countryList:
        selectList = driver.find_element(by=By.XPATH, value=selectListXpath)

        selectList.click()

        time.sleep(1)

        selectInput = driver.find_element(by=By.XPATH, value=selectInputXpath)
        selectInput.clear()
        time.sleep(0.5)
        selectInput.send_keys(country)

        time.sleep(1)

        countryChoice = driver.find_element(by=By.XPATH, value=countryXpath)
        countryChoice.click()

        sleep_time = random.randint(3, 5)
        time.sleep(sleep_time)

        title = driver.find_element(by=By.XPATH, value=titleXpath).text.strip()
        subTitile = driver.find_element(by=By.XPATH, value=subTitileXpath).text.strip()
        commentNum = driver.find_element(by=By.XPATH, value=commentNumXpath).text.strip()
        commentRate = driver.find_element(by=By.XPATH, value=commentRateXpath).text.strip()
        rank = driver.find_element(by=By.XPATH, value=rankXpath).text.strip()

        # todo 数据处理

        if(subTitile == ""):
            subTitile = "-"
        commentNum = commentNum[:-3] # 去除后3个字符
        if rank != '-':
            rank = rank[1:] # 去除第一个字符

        dataParse.data.append([country, title, subTitile, commentNum, commentRate, rank])

    # todo 保存到excel中
    toExcel.createExcell(dataParse.data, appID)

driver.close() # todo 关闭
windows.clear()
