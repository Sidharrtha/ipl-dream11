''''
logger
'''
import os
import inspect
import configparser
import logging
from logging.handlers import RotatingFileHandler
PATH = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
def get_config(name='config.ini'):
    '''get configuration'''
    configuration = configparser.RawConfigParser()
    config_file = os.path.join(PATH, 'resources', name)
    r_r = configuration.read(config_file)
    if not r_r:
        print(f"could not find the config file '{name}'")
        raise Exception(f"could not find the config file '{name}'")
    else:
        return configuration
def get_logger(name, show_console=True):
    '''get logger'''
    log_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(funcName)s : %(lineno)d - %(message)s")
    logger = logging.getLogger(f"{name}_logger")
    logger.setLevel(logging.INFO)
    log_directory = os.path.join(PATH, 'log', name)
    os.makedirs(log_directory, exist_ok=True)
    log_file = os.path.join(log_directory, name+'_log.log')
    file_handler = RotatingFileHandler(log_file, 'a', maxBytes=10000000, backupCount=10)
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    if show_console:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(log_formatter)
        console_handler.setLevel(logging.INFO)
        logger.addHandler(console_handler)
    return logger
