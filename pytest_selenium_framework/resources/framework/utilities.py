import inspect
import json
from .config import Config
import logging

class TestData:
    def __init__(self,file=Config.TEST_DATA_FILE):
        with open(file,'r') as f:
            self.test_data = json.load(f)

    def get_test_data(self,scenario):
        return self.test_data[scenario]

class Logger:
    def __init__(self):
        # create logger
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.DEBUG)
        # create handlers for console/ terminal and file
        terminal_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(Config.LOG_FILE,'w')
        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s', datefmt='%d-%b-%Y %H:%M:%S')
        # add formatter to handlers
        terminal_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)
        # add console and file handler to logger
        self.logger.addHandler(terminal_handler)
        self.logger.addHandler(file_handler)

    def get_logger(self):
        return self.logger

