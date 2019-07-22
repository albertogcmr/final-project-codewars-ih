# imports
import pandas as pd
import os


from .leaders import get_leaderboard_users
from .func_set import string2set
from .cw_user import CWUser


class CWDataExtractor: 
    def __init__(self, users_seed=set(), seed_path='./default-output.csv', max_users=0): 
        self.cwuser_list = list() # list of dictionaries
        self.users_checked = set()
        self.users_to_check = set()

        self.users_seed = users_seed 
        self.seed_path = seed_path
        self.max_users = max_users # max users registered until break the scanning

        self.set_actual_state() # actualize: self.cwuser_list, self.users_checked, self.users_to_check


    def is_complete(self): 
        """ Is complete if users has exceded expectations or has no more users in queue """
        users_limit = len(self.users_checked) >= self.max_users
        social_limit = len(self.users_to_check) <= 0

        if users_limit: 
            print('users_limit: Max users scanned')
        elif social_limit: 
            print('social_limit: No more users to scan')
        return users_limit or social_limit

    def scan_next(self): 
        try: 
            user = self.users_to_check.pop()
            cwuser = CWUser(user)
            cwuser.scan()
            social_users = cwuser.get_all_social()

            self.users_checked.add(user)
            self.users_to_check = self.users_to_check.union(social_users) # - self.users_checked
            # self.users_to_check = self.users_to_check.union(social_users) - self.users_checked
            self.cwuser_list.append(cwuser.all_data)
        except: 
            print('Error al añadir el usuario: {}'.format(user))
    
    def save_dataframe(self): 
        pd.DataFrame(self.cwuser_list).to_csv(self.seed_path, header=True)
    

    def set_actual_state(self): 
        self.users_to_check = self.users_seed

        if os.path.isfile(self.seed_path): 
            df = pd.read_csv(self.seed_path, index_col=0)         # create DF
            self.cwuser_list.extend(df.to_dict(orient='records')) # get list of dict from DF
            self.users_checked.update(list(df.user))              # update users_checked from DF
            
            for elem in df.social: 
                self.users_to_check = self.users_to_check.union(string2set(elem))
            self.users_to_check = self.users_to_check - self.users_checked   # update users_to_check from previous data
        '''
        else: 
            self.users_to_check = self.users_seed
        '''


    def scan(self):         
        while not self.is_complete(): 
            try: 
                self.scan_next()
            except: 
                print('ha fallado')
            else: 
                print(len(self.users_checked), len(self.users_seed), len(self.users_to_check))
            finally: 
                if len(self.users_checked) % 100 == 0: 
                    self.save_dataframe()
                    print('salvado DF')
        self.save_dataframe()
