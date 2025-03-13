import config



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
            date_input = self.driver.find
        