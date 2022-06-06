import os
class Config:
    URL="https://opensource-demo.orangehrmlive.com/"
    TEST_DATA_FILE = os.path.dirname(os.path.dirname(__file__))+'/test_data/test_data.json'
    RESULTS_FOLDER = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))+'/results/'
    LOG_FILE = RESULTS_FOLDER + 'logfile.txt'

