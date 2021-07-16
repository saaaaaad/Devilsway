#!/usr/bin/env python3 

from selenium import webdriver
driver = webdriver.Firefox()

cookies = driver.get_cookie("sid")
print (cookies)