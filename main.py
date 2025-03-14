from scraper import Scraper
from storage import save_to_csv
import config
import time
from persiantools.jdatetime import JalaliDate
import jdatetime
from datetime import timedelta

def main():

    scraper = Scraper(config.WEBSITE_URL)
    scraper.open_website()
    
    start_date_str = input("Enter start date (YYYY/MM/DD): ")
    
    start_date = jdatetime.date.fromisoformat(start_date_str.replace("/","-"))  
    end_date = jdatetime.date.today()  

    print(f"Start Date: {start_date.strftime('%Y/%m/%d')}")
    print(f"End Date: {end_date.strftime('%Y/%m/%d')}")

    all_data = []
    
    while start_date <= end_date:
        print(f"Scraping data for {start_date.strftime('%Y/%m/%d')}") 
        data = scraper.scrape_data(start_date.strftime("%Y/%m/%d"))

        if data:
            all_data.extend(data)
        else:
            print(f"⚠️ No data found for {start_date.strftime('%Y/%m/%d')}.")
            
        start_date = start_date.togregorian() + timedelta(days=1)
        start_date = jdatetime.date.fromgregorian(date=start_date)
        
    save_to_csv(all_data)
        
        
if __name__ == "__main__":
    main()