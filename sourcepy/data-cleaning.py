# imports 

import pandas as pd
from cleaning.cleaning import cleaning

INPUT_FILE_PATH = './output/codewar_users.csv' 
OUTPUT_FILE_PATH = './output/codewar_users_clean.csv' 


def main(): 
    df = pd.read_csv(INPUT_FILE_PATH, index_col=0)
    df = cleaning(df)
    df.to_csv(OUTPUT_FILE_PATH)


if __name__ == "__main__":
    main()