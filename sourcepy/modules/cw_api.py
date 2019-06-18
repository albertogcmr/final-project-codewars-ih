# imports

import requests
import json
import pandas as pd

from languages import get_languages

# Variables

URL_API = "https://www.codewars.com/api/v1/users/{}"

# hacer global
VALID_LANGUAGES = get_languages() 




class CWApi: 
    def __init__(self, user): 
        self.user = user
        self.scores = {}
        
    def set_scores(self): 
        res = {}
        url = URL_API.format(self.user)
        dictionary = requests.get(url).json()

        for lang in VALID_LANGUAGES: 
            try: 
                score = dictionary['ranks']['languages'][lang]['score']
            except: 
                score = 0
            else: 
                pass
            finally: 
                res[lang] = score
        self.scores.update(res)


if __name__ == '__main__': 
    user = 'albertogcmr'
    api = CWApi(user)
    # df = api.get_df()
    # print(df)
    api.set_scores()
    print(api.scores)
