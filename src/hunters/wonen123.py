from hunters.hunter import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import re

class Wonen123(Hunter):
    def __init__(self):
        name = '123Wonen'
        url = 'https://www.expatrentalsholland.com/offer/in/groningen'
        super().__init__(name, url)

    def process(self):
        # Get list
        wait = WebDriverWait(browser, 10)
        items_wrap = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'pandlist')))
        items = items_wrap.find_elements(By.CSS_SELECTOR, '.pandlist-container')

        # Process items
        preys = []
        for item in items:
            name = item.find_element(By.CLASS_NAME, 'pand-address').text
            price = item.find_element(By.CLASS_NAME, 'pand-price').text
            price = re.search(r'\d+(?:\.\d+)?', price).group().replace(".", "")
            link = item.find_element(By.CLASS_NAME, 'textlink-design').get_attribute('href')
            agency = self.name
            preys.append(Prey(name, price, link, agency, self.name))
        return preys
