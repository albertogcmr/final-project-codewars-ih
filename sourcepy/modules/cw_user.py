from cw_api import CWApi
from cw_scrapin import CWScraper

from languages import get_languages


class CWUser(CWApi, CWScraper): 
    def __init__(self, user, valid_languages): 
        self.user = user
        CWApi.__init__(self, self.user, valid_languages)
        CWScraper.__init__(self, self.user)

        self.all_data = {'user': self.user}

    def set_user_data(self): 
        self.set_scores()
        self.set_stats()
        self.set_social_15()
        self.all_data.update(self.scores)
        self.all_data.update(self.stats) 

    def get_all_social(self): 
        res = set()
        for users in self.social.values(): 
            res.update(users)
        return res

    def __repr__(self): 
        return str(self.all_data)

    


if __name__ == '__main__': 
    user = 'albertogcmr'
    cwuser = CWUser(user, get_languages())
    cwuser.set_user_data()
    print(cwuser.all_data)
    for k, v in cwuser.all_data.items(): 
        print(k, v)
    print(cwuser.social)



