# imports 

import pandas as pd
import re


def get_numeric_one(x, deletes=''): 
    try: 
        num = str(x)
        for ch in deletes: 
            num = num.replace(ch, '').strip()
        return float(num)
    except: 
        return x


def get_numeric_groups(x, groups=1): 
    try: 
        numbers = [int(number) for number in re.findall(r'\d+', x)]
        # in case x=0 or x=='0'
        if str(x) == '0': 
            numbers = [0] * groups
    except: 
        numbers = [0] * groups
    else: 
        pass
    finally: 
        # return list if groups > 1 else return first element in list
        return numbers[:groups] if groups > 1 else numbers[0]
    
def get_highest_trained(x): 
    try: 
        res = x.split('(')[0].strip()
        return res
    except: 
        return x

def columns_to_datetime(df, columns=[]): 
    for col in columns: 
        df[col] = pd.to_datetime(df[col])
    return df

def single_columns_to_numeric(df, dictionary=dict()): 
    for column, erase in dictionary.items(): 
        df[column] = df[column].apply(lambda x: get_numeric_one(x, deletes=erase)).fillna(0)
    return df

def two_columns_from_one(df, dictionary=dict()): 
    for column_one, column_two in dictionary.items(): 
        df[column_one], df[column_two] = zip(*df[column_one].map(lambda x: get_numeric_groups(x, groups=2)))
    return df


class CWDataCleaner: 
    def __init__(self, input_file_path, output_file_path): 
        self.input = input_file_path
        self.output = output_file_path
        self.df = None

    def load_file(self): 
        try: 
            self.df = pd.read_csv(self.input, index_col=0)
        except FileNotFoundError: 
            print('Fallo en la carga del fichero {}'.format(self.input))

    def save_file(self): 
        self.df.to_csv(self.output)

    def clean(self): 
        # clean column names
        self.df.columns = self.df.columns.str.replace(' ', '_').str.replace('.', '').str.lower()

        # replace nan in numeric colmuns with 0
        self.df._get_numeric_data().fillna(0, inplace=True)

        dictionary_one_two = {
            "authored_translations": "approved_translations", 
            "comments": "replies", 
            "translations": "translations_aproved", 
            "created": "beta", 
            "kumite": "started_kumite"
        }
        self.df = two_columns_from_one(self.df, dictionary=dictionary_one_two)

        columns_deletes_dictionary = {
            'total_stars': ',', 
            'total_completions': ',', 
            'total_completed_kata': ',', 
            'total_collected': ',', 
            'rank': 'kyudan', 
            'leaderboard_position': '#,', 
            'honor_percentile': 'Top%', 
            'honor': ',', 
            'highest_trained': '', 
            'clever_solutions': ',', 
            'best_practice_solutions': ',', 
            'best_practice': ',', 
            'avg_rank': 'kyudan', 
            'avg_satisfaction_rating': '%'
        }
        self.df = single_columns_to_numeric(self.df, dictionary=columns_deletes_dictionary)

        # cleans dates column
        columns = ['date', 'ended_on', 'first_completed', 'last_completed', 'last_seen', 'member_since']
        self.df = columns_to_datetime(self.df, columns=columns)

        