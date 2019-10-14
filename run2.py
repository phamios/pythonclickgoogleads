#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import uuid
import sys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.proxy import Proxy, ProxyType


def ChangeProxy(ProxyHost, ProxyPort):
    "Define Firefox Profile with you ProxyHost and ProxyPort"
    profile = webdriver.FirefoxProfile()
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.http", ProxyHost)
    profile.set_preference("network.proxy.http_port", int(ProxyPort))
    profile.update_preferences()
    return webdriver.Firefox(firefox_profile=profile)

ProxyHost = sys.argv[2]
ProxyPort = sys.argv[3]
driver = ChangeProxy(ProxyHost, ProxyPort)
driver = webdriver.Firefox(executable_path="./geckodriver")
driver.implicitly_wait(15) # seconds
driver.get('https://www.google.com.vn')

a = driver.find_element_by_name('q')
a.send_keys(sys.argv[1]) 
a.send_keys(Keys.RETURN)
time.sleep(5)
post_box=driver.find_element_by_xpath("//div[contains(@class,'ads-visurl')]")
post_box.click()
driver.close();

 
