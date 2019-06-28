# imports
import requests
import json

# Variables
URL_API = "https://www.codewars.com/api/v1/users/{}"


class CWApi: 
    def __init__(self, user):
        self.user = user
        self.scores = dict()
        
    def set_scores(self): 
        url = URL_API.format(self.user)
        dictionary = requests.get(url).json()
        scores_lang = dictionary.get('ranks').get('languages')

        for lang, score in scores_lang.items(): 
            self.scores.update({lang: score.get('score', 0)})


if __name__ == '__main__': 
    user = 'albertogcmr'
    api = CWApi(user) 
    api.set_scores()
    print(api.scores)
