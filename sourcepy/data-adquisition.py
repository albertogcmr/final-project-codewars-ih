# Proyecto Final IH: Recomendador de Codewars

# https://www.codewars.com/users/leaderboard

# imports 

from modules.leaders import get_leaderboard_users

# from funciones_tiempo import timeit

MAX_ITERATIONS = 2

# pd.options.display.max_columns = None




def main(): 
    top500 = get_leaderboard_users()
    print((top500))


if __name__ == "__main__":
    main()