from datetime import datetime
from struct import unpack
import pytest
import softest
from resources.pages.login import LoginPage
from ddt import ddt , data , unpack, file_data
from resources.framework.config import Config

@ddt
class TestOrangeHRM(softest.TestCase):
    @file_data(Config.TEST_DATA_FILE)
    def test_scenario_1_invalid_credentials_using_datadriven(self,username,password):
        self.loginpage.login_to_application(username,password)
        error_message_text =  self.loginpage.get_login_error_message() 
        self.soft_assert(self.assertEqual,error_message_text,"Invalid credentials")

    def test_scenario_1_invalid_credentials_using_custom_testdata_handler(self):
        data = self.test_data_handle.get_test_data('Scenario 1')
        self.loginpage.login_to_application(data['username'],data['password'])
        error_message_text =  self.loginpage.get_login_error_message() 
        self.loginpage.log.info(error_message_text)
        self.soft_assert(self.assertEqual,error_message_text,"Invalid credentials")

    def test_scenario_1_invalid_credentials_capture_screenshot_on_failure(self):
        data = self.test_data_handle.get_test_data('Scenario 1')
        self.loginpage.login_to_application(data['username'],data['password'])
        error_message_text =  self.loginpage.get_login_error_message() 
        self.soft_assert(self.assertEqual(error_message_text,"Invalids credentials XXX"))

    def test_Scenario_2_Extract_Credentials_and_Login(self):
            username,password = self.loginpage.extract_credentials_from_login_page()
            assert username is not None and password is not None
            homepage = self.loginpage.login_to_application(username,password)
            assert 'dashboard' in homepage.get_page_url().lower()
            print(homepage.get_logged_in_user_name())
            homepage.logout()

