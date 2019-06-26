from cw_api import CWApi
from cw_scrapin import CWScraper



class CWUser(CWApi, CWScraper): 
    def __init__(self, user, valid_languages): 
        self.user = user
        CWApi.__init__(self, self.user, valid_languages)
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


if __name__ == '__main__': 
    from languages import get_languages

    user = 'albertogcmr'
    cwuser = CWUser(user, get_languages())
    cwuser.scan()
    #print(cwuser.all_data)
    for k, v in cwuser.all_data.items(): 
        pass
        print(k, v)
    #print(cwuser.social)



