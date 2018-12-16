from bs4 import BeautifulSoup
import requests


def get_languages(url='https://www.codewars.com/kata/latest/my-languages', ignore={'all', 'my languages'}): 
    html = requests.get(url).content
    soup = BeautifulSoup(html, "lxml")
    return {e.text.lower() for e in soup.select('#language_filter option')}.difference(ignore) 


def get_social(user): 
    res = set()
    for link in ['following', 'followers', 'allies']: 
        url = 'https://www.codewars.com/users/{}/{}'.format(user, link)
        html = requests.get(url).content

        soup = BeautifulSoup(html, "lxml")
        res = res.union({e.text for e in soup.select('table a')})
    return res