# Proyecto Final IH: Recomendador de Codewars

# https://www.codewars.com/users/leaderboard

# imports 

# from modules import adquire, cleaning, create_df_checking, outputs # example 
from modules.leaders import get_leaderboard_users
from modules.cw_data_adquisition import CWData


# from funciones_tiempo import timeit

# MAX_ITERATIONS = 2
# VALID_LANGUAGES = get_languages()
MAX_USERS = 10 # modificar

# pd.options.display.max_columns = None




def main(): 
    top500 = get_leaderboard_users()
    print(top500)
    cwd = CWData()
    cwd = CWData(users_seed=top500, seed_path='./output/codewar_users.csv', max_users=MAX_USERS)
    # cw.save_dataframe()
    # print((top500))
    # print(VALID_LANGUAGES)


if __name__ == "__main__":
    main()