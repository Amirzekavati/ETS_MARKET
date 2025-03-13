import config


class Scraper:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.chrome()
        
    def open_website(self):
        self.driver.get(self.url)
        