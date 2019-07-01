# imports
import pandas as pd
import os
from .func_set import string2set
from .cw_user import CWUser


class CWData: 
    def __init__(self, users_seed=set(), seed_path='./output/codewar_users.csv', max_users=50): 
        self.cwuser_list = list() # list of dictionaries
        self.users_checked = set()
        self.users_to_check = set()

        self.users_seed = users_seed 
        self.seed_path = seed_path
        self.max_users = max_users # max users registered until break the scanning

        self.set_actual_state() # actualize: self.cwuser_list, self.users_checked, self.users_to_check
        '''
        self.set_cwuser_list()
        self.set_users_checked()
        self.set_users_to_check()
        '''


    def is_complete(self): 
        """ Is complete if iterations or users has exceded expectations """
        return len(self.users_checked) >= self.max_users

    def scan_next(self): 
        user = self.users_to_check.pop()
        cwuser = CWUser(user)
        cwuser.scan()
        social_users = cwuser.get_all_social()

        self.users_checked.add(user)
        self.users_to_check = self.users_to_check.union(social_users) - self.users_checked
        self.cwuser_list.append(cwuser.all_data)
    '''
    def get_dataframe(self): 
        return pd.DataFrame(self.cwuser_list) 
    '''
    def save_dataframe(self): 
        pd.DataFrame(self.cwuser_list).to_csv(self.seed_path, header=True)
    '''
    def set_users_checked(self): 
        if os.path.isfile(self.seed_path): 
            df = pd.read_csv(self.seed_path)
            self.users_checked.update(list(df.user))

    def set_cwuser_list(self): 
        if os.path.isfile(self.seed_path): 
            df = pd.read_csv(self.seed_path, index_col=0)
            self.cwuser_list.extend(df.to_dict(orient='records'))
        
    def set_users_to_check(self): 
        self.users_to_check = self.users_seed - self.users_checked
        if os.path.isfile(self.seed_path): 
            df = pd.read_csv(self.seed_path)
            for elem in df.social: 
                self.users_to_check = self.users_to_check - string2set(elem)
    '''

    def set_actual_state(self): 
        self.users_to_check = self.users_seed
        if os.path.isfile(self.seed_path): 
            df = pd.read_csv(self.seed_path, index_col=0)         # create DF
            self.cwuser_list.extend(df.to_dict(orient='records')) # get dict from DF
            self.users_checked.update(list(df.user))              # update users_checked from DF
            for elem in df.social: 
                self.users_to_check = self.users_to_check.union(string2set(elem))
            self.users_to_check = self.users_to_check - self.users_checked   # update users_to_check from previous data

        else: 
            self.users_to_check = self.users_seed

if __name__ == '__main__': 

    from leaders import get_leaderboard_users
    
    seed = get_leaderboard_users()
    data = CWData(users_seed=seed, max_users=3)
    data.users_checked
    print(len(data.users_seed))
    print(len(data.users_checked))
    print(len(data.users_to_check))
    
    while not data.is_complete(): 
        data.scan_next()
        print(len(data.users_checked))
    data.save_dataframe()

