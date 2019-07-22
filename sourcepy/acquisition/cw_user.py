# imports

from .cw_api import CWApi
from .cw_scrapin import CWScraper

class CWUser(CWApi, CWScraper): 
    def __init__(self, user): 
        self.user = user
        CWApi.__init__(self, self.user) 
        CWScraper.__init__(self, self.user)

        self.all_data = {'user': self.user}

    def scan(self): 
        self.set_scores()
        self.set_stats()
        self.set_social_15()
        self.all_data.update(self.scores)
        self.all_data.update(self.stats) 
        self.all_data.update({'social': self.get_all_social()})

    def get_all_social(self): 
        res = set()
        for users in self.social.values(): 
            res.update(users)
        return res

    def __repr__(self): 
        return str(self.all_data)    