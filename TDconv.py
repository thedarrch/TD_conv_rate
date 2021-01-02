# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 01:31:25 2020

@author: theda
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import os

GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.binary_location = GOOGLE_CHROME_PATH

def get_rates():
	drv_path = os.getcwd() + "chromedriver.exe"
	print(drv_path + "aersf")
	driver = webdriver.Chrome(chrome_options=chrome_options)
	url = 'https://tool.td.com/fxcal/#/fxcalculator'
	driver.get(url)
	time.sleep(5)
	a=[]
	soup = BeautifulSoup(driver.page_source, "lxml")
	p_list = soup.find_all('p')
	for p in p_list:
		if "CAD" in p.get_text() or "USD" in p.get_text():
			a.append(p.get_text())
	driver.quit()
	return a