# imports

import pandas as pd
import os

from cw_user import CWUser
from leaders import get_leaderboard_users
from languages import get_languages


VALID_LANGUAGES = get_languages()

class CWData: 
    def __init__(self, users_seed=set(), seed_path='./output/codewar_users.csv', max_users=50): 
        # self.max_iterations = max_iterations # add parameter: self.max_iterations=2
        self.cwuser_list = list() # list of dictionaries
        self.users_checked = set()
        self.users_to_check = set()

        self.users_seed = users_seed 
        self.seed_path = seed_path
        self.max_users = max_users # max users registered until break the scanning

        self.set_users_checked(self.seed_path)
        self.set_cwuser_list(self.seed_path)
        self.set_users_to_check(self.seed_path)


    def is_complete(self): 
        """ Is complete if iterations or users has exceded expectations """
        # iters = self.iterations >= self.max_iterations
        # return iters or users
        return len( self.cwuser_list) >= self.max_users

    def scan_all(self): 
        user = self.users_to_check.pop()
        cwuser = CWUser(user, VALID_LANGUAGES)
        cwuser.scan()

        self.users_checked.add(user)
        social_users = cwuser.get_all_social()
        self.users_to_check.union(social_users)
        self.cwuser_list.append(cwuser.all_data)

    def get_dataframe(self): 
        # data = [elem.all_data for elem in self.cwuser_list]
        return pd.DataFrame(self.cwuser_list)

    def save_dataframe(self, path='./output/codewar_users.csv'): 
        self.get_dataframe().to_csv(path)

    def set_users_checked(self, seed_path='./output/codewar_users.csv'): 
        if os.path.isfile(seed_path): 
            df = pd.read_csv(seed_path)
            self.users_checked.update(list(df.user))

    def set_cwuser_list(self, seed_path='./output/codewar_users.csv'): 
        if os.path.isfile(seed_path): 
            df = pd.read_csv(seed_path)
            self.cwuser_list.extend(df.to_dict(orient='records'))
        
    def set_users_to_check(self, seed_path='./output/codewar_users.csv'): 
        self.users_to_check = self.users_seed - self.users_checked
        if os.path.isfile(seed_path): 
            df = pd.read_csv(seed_path)
            x = df.social
            print(type(x[0])) # modificar
            print(x[0]) # modificar



if __name__ == '__main__': 
    seed = get_leaderboard_users()
    data = CWData(users_seed=seed, max_users=20)
    print(len(data.users_seed))
    print(len(data.users_checked))
    print(len(data.users_to_check))
    
    # data.set_seed()
    '''
    while not data.is_complete(): 
        data.scan_all()
        print(len(data.users_checked))
    data.save_dataframe()'''

