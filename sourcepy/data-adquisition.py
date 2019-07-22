# imports
from adquisition.leaders import get_leaderboard_users
from adquisition.cw_data_adquisition import CWDataExtractor

# variables
MAX_USERS = 13715 # modificar
OUTPUT_FILE_PATH = './output/codewar_users.csv' 
OUTPUT_TEST_FILE = './output/tests.csv'


def main(): 
    top500 = get_leaderboard_users()
    # data = CWData(users_seed=top500, seed_path=OUTPUT_FILE_PATH, max_users=MAX_USERS)
    data = CWDataExtractor(users_seed=top500, seed_path=OUTPUT_FILE_PATH, max_users=MAX_USERS)
    data.scan()


if __name__ == "__main__":
    main()