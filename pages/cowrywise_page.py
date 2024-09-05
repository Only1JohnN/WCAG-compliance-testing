from selenium.webdriver.common.by import By

class CowrywisePage:
    def __init__(self, driver):
        self.driver = driver

    # Example locators for text and background elements
    def get_text_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'p.text-element')  # Update selector as needed

    def get_background_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'div.background-element')  # Update selector as needed
