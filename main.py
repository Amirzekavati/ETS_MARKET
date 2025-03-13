from scraper import Scraper
from storage import save_to_csv
import config
import time

def main():
    start_date = input("Enter start date (YYYY-MM-DD): ")
    
    scraper = scraper(config.WEBSITE_URL)
    scraper.open_website()
    
    