import pytest
from selenium import webdriver
from page_objects.accessibility_page import AccessibilityPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://cowrywise.com/")
    yield driver
    driver.quit()

def test_screen_reader(driver):
    page = AccessibilityPage(driver)
    
    # Check for elements with ARIA attributes
    aria_elements = page.get_aria_elements()
    
    # Assert that ARIA elements are found
    assert len(aria_elements) > 0, "No ARIA attributes found on the page."

