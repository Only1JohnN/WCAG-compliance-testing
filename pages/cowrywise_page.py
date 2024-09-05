from selenium.webdriver.common.by import By

class CowrywisePage:
    def __init__(self, driver):
        self.driver = driver

    # Example locators for text and background elements
    def get_text_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, "h2[class='xl']")  # Update selector as needed

    def get_background_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".bars-section")  # Update selector as needed
