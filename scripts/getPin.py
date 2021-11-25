#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 09:13:46 2021

@author: ess_admin
"""

import pandas
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from tqdm import tqdm 
import time


# text_list=[]

driver = webdriver.Firefox()
for i in tqdm(range(110460,124290)):
    url="https://sgp.postcodebase.com/node/"+str(i)
    driver.get(url)
    time.sleep(0.15)
    text_list.append(driver.title)


# https://developers.onemap.sg/commonapi/search?searchVal=128417&returnGeom=Y&getAddrDetails=Y&pageNum=1

