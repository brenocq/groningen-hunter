from selenium import webdriver

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
        self.browser = webdriver.Firefox(executable_path="../drivers/geckodriver")

    def start(self):
        self.browser.get(self.url)

    def stop(self):
        self.browser.close()
