# imports
from acquisition.cw_data_adquisition import CWDataExtractor
from acquisition.leaders import get_leaderboard_users
from acquisition.func_set import string2set
from acquisition.cw_user import CWUser
from acquisition.cw_api import CWApi
from acquisition.cw_scrapin import CWScraper


def test_CWDataExtractor(): 
    OUTPUT_TEST_FILE = './output/tests.csv'
    
    seed = get_leaderboard_users()
    data = CWDataExtractor(users_seed=seed, seed_path=OUTPUT_TEST_FILE, max_users=3)
    data.users_checked
    print(len(data.users_seed))
    print(len(data.users_checked))
    print(len(data.users_to_check))
    
    while not data.is_complete(): 
        data.scan_next()
        print(len(data.users_checked))
    data.save_dataframe()


def test_CWUser(): 
    user = 'albertogcmr'
    cwuser = CWUser(user) 
    cwuser.scan()
    print(cwuser.all_data.items())


def test_CWApi(): 
    user = 'potacho'
    api = CWApi(user) 
    api.set_scores()
    print(api.scores)


def test_CWScraper(): 
    user = 'albertogcmr'
    s = CWScraper(user)
    s.set_stats()
    print('stats:', s.stats, end='\n\n')
    s.set_social_15()
    print('social:', s.social, end='\n\n')
    print('stats:', s.stats, end='\n\n')


def test_string2set(): 
    s = "{'betegelse', 'OlegRadchenko', 'verma.amardeep@gmail.com', 'mro', 'PilgrimShadow', 'blinker345678', 'bwblock', 'jamad', 'spirit11', 'cnn', 'booox', 'mstrotta', 'Liova99'}"
    res = string2set(s)
    print(res)
    print(type(res))


if __name__ == '__main__': 
    test_string2set()
    test_CWScraper()
    test_CWApi()
    test_CWUser()
    test_CWDataExtractor()
    