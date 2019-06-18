from cw_api import CWApi
from cw_scrapin import CWScraper

class CWUser(CWApi, CWScraper): 
    def __init__(self, user): 
        self.user = user
        CWApi.__init__(self, self.user)
        CWScraper.__init__(self, self.user)

        self.all_data = {}

    def set_all_data(self): 
        self.set_scores()
        self.set_stats()
        self.all_data.update(self.scores)
        self.all_data.update(self.stats)
        
    


if __name__ == '__main__': 
    user = 'albertogcmr'
    cwuser = CWUser(user)
    cwuser.set_all_data()
    print(cwuser.all_data)
    for k, v in cwuser.all_data.items(): 
        print(k, v)



