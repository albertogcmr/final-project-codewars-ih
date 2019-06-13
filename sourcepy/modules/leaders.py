# imports 

import requests
from bs4 import BeautifulSoup

# Variables

URL_LEADERBOARD = 'https://www.codewars.com/users/leaderboard'

def get_leaderboard_users(): 
    leaders = Leaderboard()
    leaders.get_top()
    return leaders.top

class Leaderboard: 
    def __init__(self, url=URL_LEADERBOARD): 
        self.url = url
        self.top = set()

    # @timeit
    def get_top(self): 
        """ Set self.top from leaderboard """
        html = requests.get(self.url).content
        soup = BeautifulSoup(html, "lxml")
        self.top = {e.text for e in soup.select('tr a')}