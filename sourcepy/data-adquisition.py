# imports
from modules.leaders import get_leaderboard_users
from modules.cw_data_adquisition import CWData

# variables
MAX_USERS = 20 # modificar


def main(): 
    data = CWData(users_seed=get_leaderboard_users(), 
                  seed_path='./output/codewar_users.csv', 
                  max_users=MAX_USERS)
    while not data.is_complete(): 
        data.scan_next()
        print(len(data.users_checked))
    data.save_dataframe()


if __name__ == "__main__":
    main()