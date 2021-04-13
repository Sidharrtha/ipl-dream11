'''
@author: Rajat.D
'''
import re
import time
import logging
import os
from logging.handlers import RotatingFileHandler
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
PATH = os.getcwd()
if not os.path.exists(PATH+"/log"):
    os.makedirs(PATH+"/log")
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
HANDLER = RotatingFileHandler(PATH+"/log/stfc_log.log", 'a', maxBytes=10000000, backupCount=10)
HANDLER.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
HANDLER.setFormatter(formatter)
logger.addHandler(HANDLER)
def check_error(driver):
    """check error"""
    print('checking error')
    error_box_xpath = "//div[@id='errorReportModal']"
    close_button_xpath = "//button[@name='confirm' and text()='Close'] "
    message_field_xpath = "//div[@class = 'modal-content errorReportModalContent']/p/span[text()='Message:']/.."
    load_xpath = "//span[@class='loading']"
    logout_buttton_xpath = "//button[text()='Logout']"
    while is_xpath_displayed(driver, load_xpath, 1):
        print('Loading')
    print('after loading')
    if is_xpath_displayed(driver, error_box_xpath, 2):
        error_message = read_text(driver, message_field_xpath)
        if error_message:
            mouse_click(driver, close_button_xpath)
            raise Exception(error_message)
    if wait_till_clickable(driver, logout_buttton_xpath, 1):
        mouse_click(driver, logout_buttton_xpath)
        time.sleep(2)
        raise Exception('Session timed out')
def press_down(driver):
    '''press_down'''
    actions = ActionChains(driver)
    actions.send_keys(Keys.DOWN).perform()
def get_attribute(driver, xpath, name):
    '''getting attribute'''
    try:
        control_click = driver.find_element_by_xpath(xpath)
        time.sleep(1)
        return control_click.get_attribute(name)
    except RuntimeError:
        logger.info('%s - %s - %s', "Unable to find the Xpath getAttributess ", xpath, RuntimeError)
def is_clickable(driver, xpath, timeout):
    '''check is_clickable'''
    try:
        WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        element = driver.find_element_by_xpath(xpath)
        element.click()
        return True
    except RuntimeError:
        logger.info('Exception   - %s - Xpath : %s',
                    "is_clickable".ljust(30), xpath)
        logger.exception(RuntimeError)
        return False
def switch_iframe(driver, xpath):
    '''do switch_iframe'''
    try:
        iframe = driver.find_element_by_xpath(xpath)
        driver.switch_to.frame(iframe)
    except RuntimeError:
        logger.info('%s - %s - %s', "Unable to find the Xpath in switch_iframe ",
                    xpath, RuntimeError)
def choose_drop_down_click(driver, controlxpath, drop_down_xpath, value, tries=30):
    '''chose one from drop down'''
    while tries > 0:
        tries -= 1
        print(tries)
        try:
            print('in drop down')
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                            controlxpath)))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, controlxpath)))
            control_click = driver.find_element_by_xpath(controlxpath)
            control_click.click()
            print('clicked')
            time.sleep(1)
            control_click.clear()
            control_click.send_keys(value)
            if not is_xpath_displayed(driver, drop_down_xpath, 3):
                print('not found')
                continue
            time.sleep(1)
            drop_down_element = driver.find_element_by_xpath(drop_down_xpath)
            drop_down_element_list = drop_down_element.find_elements_by_tag_name("div")
            for row in drop_down_element_list:
                print(row.text)
                if row.text.upper() == value.upper():
                    time.sleep(1)
                    row.click()
                    return
            print(' not clicked')
            control_click.send_keys(Keys.ARROW_DOWN)
            control_click.send_keys(Keys.ENTER)
            return
        except RuntimeError:
            print(RuntimeError)
            check_error(driver)
            if tries == 0:
                logger.info('%s - %s - %s',
                            "Unable to find the Xpath mouseClick",
                            controlxpath, RuntimeError)
                raise
def choose_drop_down_enter(driver, xpath, drop_down_xpath, value, tries=30):
    '''chise and enter'''
    while tries > 0:
        tries -= 1
        print("in loop", tries)
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            element = driver.find_element_by_xpath(xpath)
            print('in drop down')
            element.click()
            print('clicked')
            time.sleep(0.5)
            element.clear()
            element.send_keys(value)
            time.sleep(0.5)
            if not element.get_attribute('value').lower() == value.lower():
                continue
            if not is_xpath_displayed(driver, drop_down_xpath, 3):
                print('not found')
                continue
            time.sleep(1)
            element.send_keys(Keys.ARROW_DOWN)
            element.send_keys(Keys.ENTER)
            return
        except RuntimeError:
            print(RuntimeError)
            check_error(driver)
            if tries == 0:
                logger.info('%s - %s - %s',
                            "Unable to find the Xpath mouseClick",
                            xpath, RuntimeError)
                raise
def clear(driver, xpath):
    '''clearing'''
    try:
        control_click = driver.find_element_by_xpath(xpath)
        control_click.clear()
    except RuntimeError:
        logger.info('%s - %s - %s', "Unable to find the Xpath clear ", xpath, RuntimeError)
def send_key_no_check(driver, xpath, value):
    '''sending keys'''
    try:
        control_click = driver.find_element_by_xpath(xpath)
        control_click.send_keys(value)
    except RuntimeError:
        logger.info('%s - %s - %s', "Unable to find the Xpath Send Keys ", xpath, RuntimeError)
def send_key(driver, xpath, value, no_of_tries=30):
    '''send key'''
    while True:
        try:
            print('in try')
            no_of_tries -= 1
            element = driver.find_element_by_xpath(xpath)
            element.clear()
            element.send_keys(value)
            if value.lower() == element.get_attribute('value').lower():
                logger.info('Successfull - %s - Xpath : %s',
                            "send_key".ljust(30), xpath)
            if no_of_tries == 0:
                logger.info('Tries Exceeded - %s - Xpath : %s',
                            "send_key".ljust(30), xpath)
                raise Exception('Entering Value failed. Value : ' + value)
        except RuntimeError:
            print(RuntimeError)
            check_error(driver)
            if no_of_tries == 0:
                logger.info('Exception - %s - Xpath : %s',
                            "send_key".ljust(30), xpath)
                logger.exception(RuntimeError)
                raise
def send_key_with_special_check(driver, xpath, value, no_of_tries=30):
    '''send_key_with_special_check'''
    while True:
        try:
            print('in try')
            no_of_tries -= 1
            element = driver.find_element_by_xpath(xpath)
            element.clear()
            element.send_keys(value)
            if re.sub('[^a-zA-Z0-9]', "", value.lower()) == re.sub('[^a-zA-Z0-9]', "", element.get_attribute('value').lower()):
                logger.info('Successfull - %s - Xpath : %s',
                            "send_key".ljust(30), xpath)
                return
            if no_of_tries == 0:
                logger.info('Tries Exceeded - %s - Xpath : %s',
                            "send_key".ljust(30), xpath)
                raise Exception('Entering Value failed. Value : ' + value)
        except RuntimeError:
            print(RuntimeError)
            check_error(driver)
            if no_of_tries == 0:
                logger.info('Exception - %s - Xpath : %s',
                            "send_key".ljust(30), xpath)
                logger.exception(RuntimeError)
                raise
def send(driver, xpath, value, no_of_tries=30):
    '''send'''
    while True:
        try:
            print('in try')
            no_of_tries -= 1
            element = driver.find_element_by_xpath(xpath)
            element.send_keys(value)
            if no_of_tries == 0:
                logger.info('Tries Exceeded - %s - Xpath : %s',
                            "send_key".ljust(30), xpath)
                raise Exception('Entering Value failed. Value : ' + value)
        except RuntimeError:
            print(RuntimeError)
            check_error(driver)
            if no_of_tries == 0:
                logger.info('Exception - %s - Xpath : %s',
                            "send_key".ljust(30), xpath)
                logger.exception(RuntimeError)
                raise
def select_all_send_key(driver, xpath, value, no_of_tries=10):
    '''select all'''
    while True:
        try:
            print('in try')
            no_of_tries -= 1
            element = driver.find_element_by_xpath(xpath)
            element.click()
            element.send_keys(Keys.CONTROL + "A")
            element.send_keys(Keys.BACK_SPACE)
            element.send_keys(value)

            if value.lower() == element.get_attribute('value').lower():
                logger.info('Successfull - %s - Xpath : %s',
                            "send_key".ljust(30), xpath)
                return
            if no_of_tries == 0:
                logger.info('Tries Exceeded - %s - Xpath : %s',
                            "send_key".ljust(30), xpath)
                raise Exception('Entering Value failed. Value : ' + value)
        except RuntimeError:
            print(RuntimeError)
            check_error(driver)
            if no_of_tries == 0:
                logger.info('Exception - %s - Xpath : %s',
                            "send_key".ljust(30), xpath)
                logger.exception(RuntimeError)
                raise
def mouse_click(driver, xpath, tries=30):
    '''mouse click'''
    while tries > 0:
        tries -= 1
        try:
            WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            element = driver.find_element_by_xpath(xpath)
            element.click()
            logger.info('Successfull - %s - Xpath : %s',
                        "mouse_click".ljust(30), xpath)
            return
        except IndexError:
            check_error(driver)
            if tries == 0:
                logger.info('Exception - %s - Xpath : %s',
                            "mouse_click".ljust(30), xpath)
                raise
# =============================================================================
# Mouse click and send value to the field with given xpath
# checks whether the right value is entered in the field
# if not then the field is cleared and value is re entered
# =============================================================================
def mouse_click_send_keys(driver, xpath, value, no_of_tries=30):
    '''mouse click and send'''
    while True:
        try:
            no_of_tries -= 1
            WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            element = driver.find_element_by_xpath(xpath)
            element.click()
            element.clear()
            time.sleep(0.5)
            element.send_keys(value)
            if value.lower() == element.get_attribute('value').lower():
                logger.info('Successfull - %s - Xpath : %s',
                            "mouse_click_send_keys".ljust(30), xpath)
                return
            if no_of_tries == 0:
                logger.info('Tries Exceeded - %s - Xpath : %s',
                            "mouse_click_send_keys".ljust(30), xpath)
                raise Exception('Entering Value failed. Value : ' + value)
        except IndexError:
            check_error(driver)
            if no_of_tries == 0:
                logger.info('Exception - %s - Xpath : %s',
                            "mouse_click_send_keys", xpath)
                logger.exception(IndexError)
                raise
def mouse_click_send_keyand_tab(driver, controlxpath, value):
    '''mouse_click_send_keyand_tab'''
    try:
        time.sleep(0.5)
        control_click = driver.find_element_by_xpath(controlxpath)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, controlxpath)))
        control_click.click()
        control_click.clear()
        time.sleep(1)
        control_click.send_keys(value)
        control_click.send_keys(Keys.TAB)
    except IndexError:
        logger.info('%s - %s - %s', "Unable to find the Xpath mouse_click_send_keyand_tab",
                    controlxpath, IndexError)
def scroll(driver, offset):
    '''scroll'''
    driver.execute_script("window.scrollBy(0,"+ str(offset)+");")
def scroll_to_element(driver, xpath):
    '''scroll to element'''
    try:
        element = driver.find_element_by_xpath(xpath)
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
    except IndexError:
        logger.info('%s - %s - %s',
                    "Unable to find the Xpath in scroll to element ",
                    xpath, IndexError)
#def click(driver, xpath):
#    try:
#        element = driver.find_element_by_xpath(xpath)
#        actions = ActionChains(driver)
#        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
#        actions.click(element).perform()
#    except Exception as timout:
#        actions.click(element).perform()
#        logger.info('%s - %s - %s', "Unable to find the Xpath in Click ",xpath,timout)

#def sendKeyActionChain(driver, value):
#    try:
#        actions = ActionChains(driver)
#        actions.send_keys(value).perform()
#    except Exception as timout:
#        logger.info('%s - %s - %s', "Unable to sendkeys using action chains ",timout)
#def doubleClick(driver, xpath):
#    try:
#        element = driver.find_element_by_xpath(xpath)
#        actions = ActionChains(driver)
#        actions.double_click(element).perform()
#    except Exception as timout:
#        logger.info('%s - %s - %s', "Unable to find the Xpath in Click ",xpath,timout)
#def scrollToElementandClick(driver, xpath):
#    try:
#        element = driver.find_element_by_xpath(xpath)
#        actions = ActionChains(driver)
#        actions.move_to_element(element).perform()
#        waitTillClickable(driver, xpath)
#        actions.click(element).perform()
#    except Exception as timout:
#        logger.info('%s - %s - %s', "Unable to find the Xpath
#in scrollToElementandClick ",xpath,timout)
def read_text(driver, xpath):
    '''read_text'''
    try:
        element = driver.find_element_by_xpath(xpath)
        return element.text
    except IndexError:
        logger.info('%s - %s - %s', "Unable to find the Xpath in readText ", xpath, IndexError)
# =============================================================================
# Waits for timeout sec for the element with the xpath to be displayed
# =============================================================================
def processing_check_wait(driver, xpath, timeout):
    '''processing check'''
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        logger.info('Successfull - %s - Xpath : %s',
                    "processing_check_wait".ljust(30), xpath)
        return True
    except RuntimeError:
        logger.info('Exception   - %s - Xpath : %s',
                    "processing_check_wait".ljust(30), xpath)
        logger.exception(RuntimeError)
        return False
def wait_till_clickable(driver, xpath, timeout):
    '''wati till click'''
    try:
        WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath)))
#        WebDriverWait(driver, timeout).until(EC.stalenessOf((By.XPATH, xpath)))
        return True
    except RuntimeError:
        logger.info('%s - %s - %s', "Unable to find the Xpath in wait till clickable to element ",
                    xpath, RuntimeError)
        return False
def is_xpath_displayed(driver, element_xpath, timeout):
    '''a'''
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located(
            (By.XPATH, element_xpath)))
        logger.info('%s - %s', "Content Displayed  ", element_xpath)
        return True
    except ValueError:
        logger.info('%s - %s - %s', "Unable to find the Xpath in is xpath displayed ",
                    element_xpath, ValueError)
        return False
def check_elemen_present(driver, xpath):
    """checking checkElemenPresent"""
    try:
        element = driver.find_element_by_xpath(xpath)
        if element.is_displayed():
            print('Founded', element.text)
            return True
        else:
            print('Hidden')
            return False
    except:
        return 'Not Found'
        