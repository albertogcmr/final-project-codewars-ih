# imports

import pandas as pd

from cw_user import CWUser
from leaders import get_leaderboard_users
from languages import get_languages


VALID_LANGUAGES = get_languages()

class CWData: 
    def __init__(self, users_seed, max_users=50): 
        self.max_users = max_users
        # self.max_iterations = max_iterations # add parameter: self.max_iterations=2
        self.cwuser_list = list()
        self.iterations = 0
        self.users_to_check = set(users_seed)
        self.users_checked = set()

    def is_complete(self): 
        """ Is complete if iterations or users has exceded expectations """
        # iters = self.iterations >= self.max_iterations
        # return iters or users
        return len( self.cwuser_list) >= self.max_users

    def iterate(self): 
        user = self.users_to_check.pop()
        cwuser = CWUser(user, VALID_LANGUAGES)
        cwuser.set_user_data()
        self.users_checked.add(user)
        social_users = cwuser.get_all_social()
        self.users_to_check.union(social_users)
        self.cwuser_list.append(cwuser.all_data)

    def get_dataframe(self): 
        # data = [elem.all_data for elem in self.cwuser_list]
        return pd.DataFrame(self.cwuser_list)

    def save_dataframe(self, path='./output/codewar_users.csv'): 
        self.get_dataframe().to_csv(path)


if __name__ == '__main__': 
    seed = get_leaderboard_users()
    data = CWData(seed, max_users=5)
    while not data.is_complete(): 
        data.iterate()
        print(len(data.users_checked))
    data.save_dataframe()