# imports
from adquisition.leaders import get_leaderboard_users
from adquisition.cw_data_adquisition import CWData

# variables
MAX_USERS = 13005 # modificar
OUTPUT_FILE_PATH = './output/codewar_users.csv'


# TO DO: mover esta función CWData como método y llamarlo desde el main

    


def main(): 
    top500 = get_leaderboard_users()
    data = CWData(users_seed=top500, seed_path=OUTPUT_FILE_PATH, max_users=MAX_USERS)
    data.scan()


if __name__ == "__main__":
    main()