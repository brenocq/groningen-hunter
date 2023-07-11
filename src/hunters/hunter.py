from selenium import webdriver

class Hunter:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.browser = webdriver.Firefox(executable_path="../drivers/geckodriver")

    def start(self):
        self.browser.get(self.url)

    def stop(self):
        self.browser.close()
