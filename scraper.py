import config
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
     
    def scrape_data(self, date):
        """Scrapes data from the site after selecting the date."""
        self.select_date(date)
        
        try:
            # Modify this section based on the website's HTML structure
            table = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, config.DATA_XPATH))
            )

            rows = table.find_elements(By.TAG_NAME, "tr")[1:6]
            
            extracted_data = []
            for row in rows:
                columns = row.find_elements(By.TAG_NAME, "td")  # Extract columns
                row_data = [col.text.strip() for col in columns]  # Clean text
                extracted_data.append(row_data)

            return extracted_data

        except Exception as e:
            print(f"Error scraping data: {e}")
            return []
            
    def close_browser(self):
        """Closes the browser."""
        self.driver.quit()
        