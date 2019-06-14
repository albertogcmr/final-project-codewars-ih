# imports

import requests
from bs4 import BeautifulSoup

# # Variables

URL_WEB = 'https://www.codewars.com/users/{}'

class CWScraper: 
    def __init__(self, user): 
        self.user = user
        self.data = {}
        self.social = {
            'following': [], 
            'followers': [], 
            'allies': []
        }

    def set_data(self): 
        url = URL_WEB.format(self.user)
        html = requests.get(url).content
        soup = BeautifulSoup(html, "lxml")
        print(soup)

    def set_social_15(self):  # Le falta selenium
        for network in self.social.keys(): 
            url = 'https://www.codewars.com/users/{}/{}'.format(self.user, network)
            html = requests.get(url).content
            soup = BeautifulSoup(html, "html.parser")
            users = [e.text for e in soup.select('table a')]
            self.social[network].extend(users)

if __name__ == '__main__': 
    user = 'albertogcmr'
    s = CWScraper(user)
    s.set_data()
    s.set_social_15()
    print(s.social)