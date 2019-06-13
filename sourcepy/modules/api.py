# imports

import requests
import json
import pandas as pd

# Variables

URL_API = "https://www.codewars.com/api/v1/users/"

class Codewars_Api: 
    def __init__(self, user): 
        self.user = user
        self.url = URL_API + self.user
        self.json = requests.get(self.url).json()
        print(type(self.json))
    def get_df(self): 
        return pd.DataFrame.from_dict(self.json)


user = 'albertogcmr'
api = Codewars_Api(user)
df = api.get_df()
print(df)