# imports
from modules.leaders import get_leaderboard_users
from modules.cw_data_adquisition import CWData

# variables
MAX_USERS = 4 # modificar


def scan(users_seed=get_leaderboard_users(), 
          seed_path='./output/codewar_users.csv', 
          max_users=MAX_USERS): 

    data = CWData(users_seed=users_seed, seed_path=seed_path, max_users=max_users)
    while not data.is_complete(): 
        data.scan_next()
        print(len(data.users_checked))
    data.save_dataframe()
    


def main(): 
    scan(users_seed=get_leaderboard_users(), seed_path='./output/codewar_users.csv', max_users=MAX_USERS)


if __name__ == "__main__":
    main()