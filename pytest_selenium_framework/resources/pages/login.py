from .base import BasePage
from .home import HomePage
from selenium.webdriver.common.by import By

"""conatins all locators and methods corresponding to the login page"""

class LoginPage(BasePage):
    """locators"""
    username_field = (By.ID, 'txtUsername')
    password_field = (By.ID, 'txtPassword')
    login_button = (By.ID, 'btnLogin')
    creditals_text = (By.XPATH,'//span[contains(text(),"Username") and contains(text(),"Password")]')
    error_text = (By.ID,'spanMessage')

    def __init__(self, driver):
        super().__init__(driver)

    """Logs into the application with the given username and password and returns the home page handle"""
    def login_to_application(self, username, password):
        self.log.info(f"Logging into the application with {username} and {password}")
        self.input_text(self.username_field,username)
        self.input_text(self.password_field,password)
        self.click_element(self.login_button)
        home = HomePage(self.driver)
        return home
        # self.wait_visibility_element(*self._employee_distribution_graphic)

    """extracts and returns the user name and password from the login page"""
    def extract_credentials_from_login_page(self):
        self.log.info(f"Extracting credentials from login page")
        text = self.get_text(self.creditals_text)
        split_text = text.split(":")
        username = split_text[1].replace(' ','').split("|")[0]
        password = split_text[2].replace(' ','').replace(')','')
        self.log.info(f"extraced username :{username} and password : {password}")
        return username,password

    """returns the error message text if visible"""
    def get_login_error_message(self):
        self.wait_until_element_is_visible(self.error_text)
        if self.is_element_visible(self.error_text):
            return  self.get_text(self.error_text)
        