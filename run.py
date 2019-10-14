#!/usr/bin/python

import sys,getopt
import time
import uuid

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from lxml import html
from selenium.webdriver.common.proxy import Proxy, ProxyType

chrome_options = Options()
#chrome_options.add_argument("--headless")

#browser = webdriver.Chrome(executable_path="./chromedriver", options=chrome_options)
browser = webdriver.Firefox(executable_path="./geckodriver")
browser.get('https://www.google.com.vn')

# Search
time.sleep(5)
search = browser.find_element_by_name("q")
search.send_keys(sys.argv[1])
search.send_keys(Keys.RETURN)

# Get number ads
tree = html.fromstring(browser.page_source)
# number_ads = len(tree.xpath("//div[@class='ad_cclk']"))
number_ads = len(tree.xpath("//div[@class='ads-visurl']"))
print(number_ads)

# Click ads
for i in range(1, number_ads + 1):
    time.sleep(1)
    xpath = "//div[@id='tads']//ol/li[{}]//a[2]".format(i)
    browser.find_element_by_xpath(xpath).click()
    time.sleep(5)
    browser.save_screenshot("./screenshot/{}.png".format(str(uuid.uuid4())))
    # back to next ads
    browser.execute_script("window.history.go(-1)")

# browser.quit()
