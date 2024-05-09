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

        # Locate the container holding listings (adjust if necessary)
        listings_container = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'GridGenerator_root__gJhqx')))
        listings = listings_container.find_elements(By.CLASS_NAME, 'ListingCard_root__e9Z81')

        preys = []
        for listing in listings:
            try:
                name = listing.find_element(By.CLASS_NAME, 'MuiTypography-subtitle1').text[:-1]
                price = listing.find_element(By.CLASS_NAME, 'MuiTypography-h5').text.replace("€", "").replace(",", "")
                link = listing.get_attribute('href')
                agency = 'No Agency'
                preys.append(Prey(name, price, link, agency, self.name))
            except (NoSuchElementException, TimeoutException):
                continue
        return preys
