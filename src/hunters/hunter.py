from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.binary_location = "/usr/bin/google-chrome-stable"
browser = webdriver.Chrome(options=options)

class Prey:
    def __init__(self, name, price, link, agency, website):
        self.name = name
        self.price = price
        self.link = link
        self.agency = agency
        self.website = website
    def __str__(self):
        return f'{self.website}:{self.name}:{self.price}'

class Hunter:
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def start(self):
        pass

    def stop(self):
        browser.close()

    def hunt(self):
        browser.get(self.url)
        return self.process()

    def process(self):
        # This method should be overloaded by derived classes
        pass
