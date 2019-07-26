# imports 

from cleaning.cleaning import CWDataCleaner

INPUT_FILE_PATH = './output/codewar_users.csv' 
OUTPUT_FILE_PATH = './output/codewar_users_clean.csv' 


def main(): 
    cleaner = CWDataCleaner(input_file_path=INPUT_FILE_PATH, output_file_path=OUTPUT_FILE_PATH)
    cleaner.load_file()
    cleaner.clean()
    cleaner.save_file() 


if __name__ == "__main__":
    main()
