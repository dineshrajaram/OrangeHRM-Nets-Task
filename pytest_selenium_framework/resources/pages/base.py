from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import NoSuchElementException
from resources.framework.utilities import Logger
""" Contains actions that are common across all pages"""
class BasePage:
    log = Logger().get_logger()
    def __init__(self, driver):
        """intitalize the webdriver variable"""
        
        self.driver = driver
        

    def go_to(self, base_url):
        """navigate to the given url"""
        self.log.info(f"Navigating to {base_url}")
        return self.driver.get(base_url)

    def get_webelement(self, by_locator):
        """finds and returns the element located using the locator"""
        self.log.info(f"Finding element with locator {by_locator[0]}:{by_locator[1]}")
        return self.driver.find_element(*by_locator)

    def input_text(self,by_locator,text):
        self.log.info(f"Entering text {text} into the field with locator {by_locator[0]}:{by_locator[1]}")
        self.get_webelement(by_locator).send_keys(text)
    
    def click_element(self,by_locator):
        self.log.info(f"Clicking element with locator {by_locator[0]}:{by_locator[1]}")
        self.get_webelement(by_locator).click()

    def get_text(self, by_locator):
        """returns the text from a specific element"""
        text = self.get_webelement(by_locator).text
        self.log.info(f"Element with locator {by_locator[0]}:{by_locator[1]} has text: {text}")
        return text

    def is_element_visible(self, by_locator):
        """returns if the element located using the given locator is visbile or not"""
        try:
            return self.get_webelement(by_locator).is_displayed()
        except NoSuchElementException:
            return False
    
    def wait_until_element_is_visible(self, by_locator):
        """waits until the element located using the given locator is visible on the page"""
        self.log.info(f"Waiting until element with locator {by_locator[0]}:{by_locator[1]} is visible")
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by_locator)))

    def get_page_url(self):
        return self.driver.current_url