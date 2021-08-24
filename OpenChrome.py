# coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# open browser
driver = webdriver.Chrome()

# open Google top
driver.get("https://www.google.co.jp/")

# find me
search = driver.find_element_by_name('q')
search.send_keys("@worst_se_chan")
search.send_keys(Keys.ENTER)
element = driver.find_element_by_partial_link_text("Twitter")
element.click()
sleep(5)

# love me
driver.get("https://twitter.com/worst_se_chan/status/1422905167180025869")
sleep(10)

# I love you so much thank you
driver.close()
