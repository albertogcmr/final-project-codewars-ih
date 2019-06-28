# imports
import requests
from bs4 import BeautifulSoup

# # Variables
URL_WEB = 'https://www.codewars.com/users/{}'


class CWScraper: 
    def __init__(self, user): 
        self.user = user
        self.stats = {}
        self.social = {
            'following': [], 
            'followers': [], 
            'allies': []
        }

    def set_stats(self): 
        url = URL_WEB.format(self.user)
        html = requests.get(url).content
        soup = BeautifulSoup(html, "html.parser")
        x = dict()
        for s in soup.select('.stat-box div'): 

            if s.text.split(':')[0] != 'Profiles': 
                x[s.text.split(':')[0].lower()] = s.text.split(':')[1]
            else: 
                try: 
                    for e in s.find_all('a', href=True): 
                        if 'github' in e['href']: 
                            x['github'] = e['href']
                        if 'linkedin' in e['href']: 
                            x['linkedin'] = e['href']
                except: 
                    x['github'] = ''
                    x['linkedin'] = ''
        self.stats = x

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
    s.set_stats()
    print('stats:', s.stats, end='\n\n')
    s.set_social_15()
    print('social:', s.social, end='\n\n')
    print('stats:', s.stats, end='\n\n')

