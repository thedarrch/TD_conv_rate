# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 01:31:25 2020

@author: theda
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time

def get_rates():
    drv_path = "C:/Users/theda/Documents/Coding Projects/TDconv/chromedriver.exe"
    driver = webdriver.Chrome(drv_path)  # full path of browser driver
    url = 'https://tool.td.com/fxcal/#/fxcalculator'
    # opening the url
    driver.get(url)
    time.sleep(5)
    
    a=[]
    soup = BeautifulSoup(driver.page_source, "lxml")
    p_list = soup.find_all('p')
    for p in p_list:
        if "CAD" in p.get_text() or "USD" in p.get_text():
            a.append(p.get_text())
    return a