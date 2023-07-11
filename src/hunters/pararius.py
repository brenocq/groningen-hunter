from hunters.hunter import Hunter

class Pararius(Hunter):
    def __init__(self):
        name = 'Pararius'
        url = 'https://www.pararius.nl/huurwoningen/groningen/0-1200'
        super().__init__(name, url)

    def check(self):
        print(f'[{self.name}] Checking website {self.url}')
        self.browser.refresh()
