#login
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup


options = webdriver.ChromeOptions()

target = 'https://school.pths.ptc.edu.tw/auth/Auth/Login'

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("prefs", {"profile.password_manager_enabled": False, "credentials_enable_service": False})

driver=webdriver.Chrome(chrome_options=options)
driver.get(target)
print("seccess to get the web")


#acc = input("input account:")
#pwd = input("input password:")
acc = "810217"
pwd = "T125930711"

account = driver.find_element_by_name("studentLId")
account.send_keys(acc)
password = driver.find_element_by_name("studentPwd")
password.send_keys(pwd)
#password.send_keys('\ue006')
driver.find_element_by_xpath("//button[@class='btn.btn-primary.loginBtnAdjust' and @data-bind='click:login,visible:isCanPressLogin']").click()
driver.find_element_by_xpath("//button[@class='btn.btn-primary.loginBtnAdjust' and @data-bind='click:login,visible:isCanPressLogin']").click()
driver.find_element_by_xpath("//button[@class='btn.btn-primary.loginBtnAdjust' and @data-bind='click:login,visible:isCanPressLogin']").click()
login = find_element_by_xpath("//button[@class='btn.btn-primary.loginBtnAdjust' and @data-bind='click:login,visible:isCanPressLogin']")
login.click()
