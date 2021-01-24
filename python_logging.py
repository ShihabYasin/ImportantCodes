# -*- coding: utf-8 -*-
from logging.handlers import RotatingFileHandler
import logging


def get_logger(log_file_name, log_level='INFO'):
    '''

    :param log_file_name: file name for logging
    :param log_level: default INFO, could be set DEBUG
    :return: logger that could used for logging
    '''
    log_formatter = logging.Formatter ('%(asctime)s [%(levelname)-5.5s]  %(message)s')
    logger = logging.getLogger (__name__)
    file_handler = logging.FileHandler (log_file_name, mode='a')
    file_handler.setFormatter (log_formatter)
    rotation_handler = RotatingFileHandler (log_file_name, maxBytes=50 * 1024 * 1024, backupCount=100)
    logger.addHandler (file_handler)
    logger.addHandler (rotation_handler)
    if log_level == 'DEBUG':
        logger.setLevel (logging.DEBUG)
    else:
        logger.setLevel (logging.INFO)
    return logger


logger = get_logger (log_file_name='log_' + datetime.today ().strftime ('%Y-%m-%d'),
                     log_level='INFO')
logger.info ('info: Hello %s', 'bugs :) ')
