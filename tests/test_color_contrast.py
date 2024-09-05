import pytest
from selenium import webdriver
from page_objects.accessibility_page import CowrywisePage
from selenium.common.exceptions import NoSuchElementException
from utils.contrast_calculator import calculate_color_contrast
import wcag_contrast_ratio

# List all attributes of the module to find available functions
print(dir(wcag_contrast_ratio))


# Constants for color codes (update as needed)
TEXT_COLOR = '#082552'  # Black
BACKGROUND_COLOR = '#FFFFFF'  # White
MIN_CONTRAST_RATIO = 4.5  # Minimum WCAG AA contrast ratio

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://cowrywise.com/")  # Replace with the actual URL
    yield driver
    driver.quit()

def test_color_contrast(driver):
    page = CowrywisePage(driver)
    
    # Debugging step to take a screenshot
    driver.save_screenshot('screenshots/screenshot.png')
    
    try:
        text_element = page.get_text_element()
        background_element = page.get_background_element()
        
        text_color = text_element.value_of_css_property('color')
        background_color = background_element.value_of_css_property('background-color')
        
        print(f'Text Color: {text_color}')
        print(f'Background Color: {background_color}')
        
        # Calculate the contrast ratio
        contrast_ratio = calculate_color_contrast(text_color, background_color)
        
        print(f'Contrast Ratio: {contrast_ratio}')
        
        # Assert that the contrast ratio meets the minimum requirement
        assert contrast_ratio >= MIN_CONTRAST_RATIO, f"Contrast ratio {contrast_ratio} is below the minimum required {MIN_CONTRAST_RATIO}"
    except NoSuchElementException:
        print("Element not found with the selector.")
