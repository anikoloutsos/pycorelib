"""
    Main module to handle logging configuration and setup
    Contains the following functions:
    1. initialize - initial setup of the logger
"""
import logging
import time
import inspect
import os

from system.utils import dir_mgr


def initialize(log_level=logging.INFO, path='', log_name=''):
    """
    initializes the logger to output to both the console and a file.
    The file is

    :param log_level: <Optional> Sets the level of logging. Default is INFO
    :param path: <Optional> Sets the path where the log should be created. If the path is missing it is created. If the
    path is not set, it is created under the cwd
    :param log_name: <Optional> Sets the name of the log to be created. If the log_name is not set, a log named
    <timestamp>.log is added under the path
    """

    initialization_file = inspect.stack()[-1].filename
    # Get the root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    # Setup file logging
    file_log_formatter = logging.Formatter('[%(asctime)s];[%(pathname)s];[%(funcName)s];[%(levelname)s]: %(message)s')
    if path == '':
        path = '{0}/{1}/'.format(os.path.split(initialization_file)[0], 'logs', )
    # Create the directory if it is missing
    dir_mgr.create_dir_if_missing(path)
    if log_name == '':
        log_name = time.strftime('%Y%m%d%H%M%S') + '.log'
    file_handler = logging.FileHandler(path + log_name)
    file_handler.setFormatter(file_log_formatter)
    root_logger.addHandler(file_handler)

    # Setup and add console logging to root handler
    console_log_formatter = file_log_formatter
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(console_log_formatter)
    root_logger.addHandler(console_handler)

    logging.info('Logger has been initialized\n'
                 'Log Level = {0}\n'
                 'Path = {1}\n'
                 'Filename = {2}'.format(logging.getLevelName(log_level), path, log_name))
