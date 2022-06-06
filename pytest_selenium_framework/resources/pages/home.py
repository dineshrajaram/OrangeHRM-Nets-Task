from time import sleep, time
from .base import BasePage
from selenium.webdriver.common.by import By

"""conatins all locators and methods corresponding to the home page"""

class HomePage(BasePage):
    """locators"""
    tab_myinfo = (By.XPATH, '//ul[@id="mainMenuFirstLevelUnorderedList"]/li[a/b[text()="My Info"]]')
    tab_dashboard = (By.XPATH, '//ul[@id="mainMenuFirstLevelUnorderedList"]/li[a/b[text()="Dashboard"]]')
    span_welcome = (By.ID,'welcome')
    btn_logout = (By.XPATH,'//div[@id="welcome-menu" and contains(@style,"block")]//li/a[text()="Logout"]')
    
    def __init__(self, driver):
        super().__init__(driver)

    """clicks and navigates to the My Info Tab"""
    def navigate_to_myinfo_tab(self):
        self.click_element(self.tab_myinfo)

    """returns the logged in user's name"""
    def get_logged_in_user_name(self):
        return self.get_text(self.span_welcome).replace('Welcome ','')

    """logouts of the current session"""
    def logout(self):
        self.wait_until_element_is_visible(self.span_welcome)
        self.click_element(self.span_welcome)
        self.wait_until_element_is_visible(self.btn_logout)
        self.click_element(self.btn_logout)