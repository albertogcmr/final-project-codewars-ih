# imports

import requests
from bs4 import BeautifulSoup

# definitions

def get_languages(url='https://www.codewars.com/kata/latest/my-languages', ignore={'all', 'my languages'}): 
    html = requests.get(url).content
    soup = BeautifulSoup(html, "html.parser")
    return {e.text.lower() for e in soup.select('#language_filter option')}.difference(ignore) 
