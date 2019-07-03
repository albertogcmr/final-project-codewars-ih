# imports
from modules.leaders import get_leaderboard_users
from modules.cw_data_adquisition import CWData

# variables
MAX_USERS = 12000 # modificar
OUTPUT_FILE_PATH = './output/codewar_users.csv'


def scan(users_seed=get_leaderboard_users(), 
          seed_path=OUTPUT_FILE_PATH, 
          max_users=MAX_USERS): 

    data = CWData(users_seed=users_seed, seed_path=seed_path, max_users=max_users)
    while not data.is_complete(): 
        try: 
            data.scan_next()
        except: 
            print('ha fallado')
        else: 
            print(len(data.users_checked), len(data.users_seed), len(data.users_to_check))
        finally: 
            if len(data.users_checked) % 100 == 0: 
                data.save_dataframe()
                print('salvado DF')
    data.save_dataframe()
    


def main(): 
    top500 = get_leaderboard_users()
    scan(users_seed=top500, seed_path=OUTPUT_FILE_PATH, max_users=MAX_USERS)


if __name__ == "__main__":
    main()