# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 19:10:29 2019

@author: Rajat.Dhawale
"""
import os
import inspect
from logging.handlers import RotatingFileHandler
import logging
import Inputhandler



PATH = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
handler = RotatingFileHandler(PATH + "/log/stfc_log.log", 'a', maxBytes=10000000, backupCount=10)
handler.setLevel(logging.INFO)
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)
LOGGER.addHandler(handler)

def challan_date(driver, config, i):
    '''challan_date'''
    try:
        Inputhandler.processing_check_wait(driver,
                                           config.get('echallnXPath',
                                                      'paid.table.details')+'['+str(i)+']/td[3]', 5)
        Challan_Date = Inputhandler.read_text(driver,
                                               (config.get('echallnXPath',
                                                           'paid.table.details')+'['+str(i)+']/td[3]'))
        LOGGER.info("Successfully get the notice_number")
        return Challan_Date
    except RuntimeError:
        print("record not found")
        print(RuntimeError)
        
def notice_number(driver, config, i):
    '''notice_number'''
    try:
        Inputhandler.processing_check_wait(driver,
                                           config.get('echallnXPath',
                                                      'paid.table.details')+'['+str(i)+']/td[4]', 5)
        notice_Number = Inputhandler.read_text(driver,
                                               (config.get('echallnXPath',
                                                           'paid.table.details')+'['+str(i)+']/td[4]'))
        LOGGER.info("Successfully get the notice_number")
        return notice_Number
    except RuntimeError:
        print("record not found")
        print(RuntimeError)
        
def challan_ammount(driver, config, i):
    '''notice_ammount'''
    try:
        Inputhandler.processing_check_wait(driver,
                                           config.get('echallnXPath',
                                                      'paid.table.details')+'['+str(i)+']/td[4]', 5)
        notice_Number = Inputhandler.read_text(driver,
                                               (config.get('echallnXPath',
                                                           'paid.table.details')+'['+str(i)+']/td[4]'))
        LOGGER.info("Successfully get the notice_number")
        return notice_Number
    except RuntimeError:
        print("record not found")
        print(RuntimeError)
        
def voilation_reason(driver, config, i):
    '''voilation_reason'''
    try:
        Inputhandler.processing_check_wait(driver,
                                           config.get('echallnXPath',
                                                      'paid.table.details')+'['+str(i)+']/td[1]', 5)
        voilation_Reason = Inputhandler.read_text(driver,
                                               (config.get('echallnXPath',
                                                           'paid.table.details')+'['+str(i)+']/td[1]'))
        voilation_Reason = voilation_Reason.split(':')
        LOGGER.info("Successfully get the voilation_reason")
        return voilation_Reason[1]
    except RuntimeError:
        print("record not found")
        print(RuntimeError)
        
def offence_place(driver, config, i):
    '''offence_place'''
    try:
        Inputhandler.processing_check_wait(driver,
                                           config.get('echallnXPath',
                                                      'paid.table.details')+'['+str(i)+']/td[2]', 5)
        offence_Place = Inputhandler.read_text(driver,
                                               (config.get('echallnXPath',
                                                           'paid.table.details')+'['+str(i)+']/td[2]'))
        offence_Place = offence_Place.split(':')
        LOGGER.info("Successfully get the offence_place")
        return offence_Place[1]
    except RuntimeError:
        print("record not found")
        print(RuntimeError)
    