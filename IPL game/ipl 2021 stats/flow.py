# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 12:45:55 2019

@author: Rajat.Dhawale
"""
import logging
import os
import inspect
import time
import datetime
from logging.handlers import RotatingFileHandler
import configparser
#import schedule
#from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import Inputhandler as ip
from bs4 import BeautifulSoup

#import DBConnectivity
#import process
#import pandas as pd

PATH = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
handler = RotatingFileHandler(PATH + "/log/stfc_log.log", 'a', maxBytes=10000000, backupCount=10)
handler.setLevel(logging.INFO)
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)
LOGGER.addHandler(handler)

global index
index = 0

config = configparser.RawConfigParser()
config.read('configFile.properties')

def load_browser():
    
    options = Options()
    options.add_argument('--disable-infobars')
    options.add_argument("--start-fullscreen")
    options.add_argument("--start-maximized")
    url = config.get('LoginCredentials', 'url')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    return driver
    
        


        

def main_flow():
    '''main flow of this vahana'''
    driver = load_browser() 
    ip.scroll_to_element(driver, config.get('LoginCredentials', 'inning_1'))
    ip.mouse_click(driver,config.get('LoginCredentials', 'inning_1'))
    element = driver.page_source
    soup = BeautifulSoup(element,'html.parser') 
    table = soup.find('div', attrs = {"class":"imspo_tps__pss"}) 
    for row in table.findAll('div',
                         attrs = {'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
        print(row)
    driver.close()



    


                
                

        