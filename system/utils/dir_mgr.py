import os
import logging


def create_dir_if_missing(path):
    """
    Function checks if a directory exists. If not creates the whole path to the directory even if intermediate
    directories are missing.

    :param path: The path to the directory preferably absolute. If relative path is used it is compared against cwd
    :return: None
    """
    path = os.path.abspath(path)
    if os.path.exists(path):
        # If directory exists nothing to do
        logging.info('Directory already exists: ' + path)
    else:
        # If directory is missing then create the whole path to the directory
        # even if intermediate directories are missing
        logging.info('Creating directory: ' + path)
        os.makedirs(path)
