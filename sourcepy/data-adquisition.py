# Proyecto Final IH: Recomendador de Codewars

# https://www.codewars.com/users/leaderboard

# imports 

from modules.leaders import get_leaderboard_users
from modules.languages import get_languages


# from funciones_tiempo import timeit

MAX_ITERATIONS = 2
MAX_USERS = 3000 # modificar
VALID_LANGUAGES = get_languages()

# pd.options.display.max_columns = None




def main(): 
    top500 = get_leaderboard_users()
    print((top500))
    print(VALID_LANGUAGES)


if __name__ == "__main__":
    main()