import config
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Scraper:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.chrome()
        
    def open_website(self):
        """Opens the target website."""
        self.driver.get(self.url)
        
    def select_date(self, date):
        """Selects the given date in the website."""
        try:
            date_input = self.driver.find_element(By.XPATH, config.DATE_INPUT_XPATH)
            date_input.clear()
            date_input.send_keys(date)
            time.sleep(1)
            
            submit_button = self.driver.find_element(By.XPATH, config.DATE_SUBMIT_XPATH)
            submit_button.click()
            time.sleep(2)
            
        except Exception as e:
            print(f"⚠️ Error selecting date: {e}")
        