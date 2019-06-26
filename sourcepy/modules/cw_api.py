# imports

import requests
import json
import pandas as pd

from languages import get_languages

# Variables

URL_API = "https://www.codewars.com/api/v1/users/{}"

# hacer global




class CWApi: 
    def __init__(self, user, valid_languages): 
        self.user = user
        self.scores = dict()
        self.valid_languages = valid_languages
        
    def set_scores(self): 
        url = URL_API.format(self.user)
        dictionary = requests.get(url).json()
        scores_lang = dictionary.get('ranks').get('languages')

        # for lang in self.valid_languages: 
        for lang, score in scores_lang.items(): 
            self.scores.update({lang: score.get('score', 0)})


if __name__ == '__main__': 
    user = 'albertogcmr'
    api = CWApi(user, get_languages())
    # df = api.get_df()
    # print(df)
    api.set_scores()
    print(api.scores)
