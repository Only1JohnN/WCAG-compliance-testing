from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CowrywisePage:
    def __init__(self, driver):
        self.driver = driver

    def get_text_element(self):
        return WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".header-text.is-header-caption.is-header-size"))
    )  # Update selector as needed for the website

    def get_background_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#bulkit-landing")  # Update selector as needed for the website



class AccessibilityPage:
    def __init__(self, driver):
        self.driver = driver

    # ARIA (Accessible Rich Internet Applications)
    def get_aria_elements(self):
        """Return elements with ARIA attributes."""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[starts-with(@aria-, "")]'))
        )
        # Locate elements with ARIA attributes
        return self.driver.find_elements(By.XPATH, '//*[starts-with(@aria-, "")]')
    
    
    def get_alt_text_elements(self):
        """Get all image elements with alt text."""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//img[@alt]"))
        )
        return self.driver.find_elements(By.XPATH, "//img[@alt]")

