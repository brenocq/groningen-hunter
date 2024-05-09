from hunters.hunter import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

class Kamernet(Hunter):
    def __init__(self):
        name = 'Kamernet'
        url = 'https://kamernet.nl/en/for-rent/rooms-groningen?radius=5&minSize=1&maxRent=17&listingTypes=4&listingTypes=2'
        super().__init__(name, url)

    def process(self):
        # Get list
        wait = WebDriverWait(browser, 10)
        item_list = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-result-page')))
        items = item_list.find_elements(By.XPATH, './div')

        # Process items
        preys = []
        for item in items:
            name = item.find_element(By.CLASS_NAME, 'tile-title').text
            price = item.find_element(By.CLASS_NAME, 'tile-rent').text
            price = re.search(r'\d+', price).group()
            link = item.find_element(By.CLASS_NAME, 'tile-wrapper').get_attribute('href')
            agency = 'No Agency'

            # Add if available for indefinite time
            availability = item.find_element(By.CLASS_NAME, 'tile-availability')
            if 'Indefinite period' in availability.find_element(By.CLASS_NAME, 'left').text:
                preys.append(Prey(name, price, link, agency, self.name))
        return preys
