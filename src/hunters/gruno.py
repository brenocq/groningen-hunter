from hunters.hunter import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import re

class Gruno(Hunter):
    def __init__(self):
        name = 'Gruno Verhuur'
        url = 'https://www.grunoverhuur.nl/huuraanbod/?search_property&lang=nl&property_type&property_area&property_bedrooms&property_city=Groningen&price_min=300%2C00&price_max=2.500%2C00'
        super().__init__(name, url)

    def process(self):
        # Get list
        wait = WebDriverWait(browser, 10)
        items_wrap = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="ich-settings-main-wrap"]//div[@class="row"]')))
        items = items_wrap.find_elements(By.XPATH, './div')

        # Process items
        preys = []
        for item in items:
            try:
                name = item.find_element(By.CLASS_NAME, 'post-title').text
                price = item.find_element(By.CLASS_NAME, 'rem-price-amount').text
                price = re.search(r'\d+(?:\.\d+)?', price).group().replace(".", "")
                link = item.find_element(By.CLASS_NAME, 'propery-style-6').find_element(By.XPATH, './a').get_attribute('href')
                agency = self.name
                preys.append(Prey(name, price, link, agency, self.name))
            except NoSuchElementException:
                 # Ignore the item is incomplete
                continue
        return preys
