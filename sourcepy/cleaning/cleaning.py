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

'''
self.df['date'] = pd.to_datetime(self.df['date'])
self.df['ended_on'] = pd.to_datetime(self.df['ended_on'])
self.df['first_completed'] = pd.to_datetime(self.df['first_completed'])
self.df['last_completed'] = pd.to_datetime(self.df['last_completed'])
self.df['last_seen'] = pd.to_datetime(self.df['last_seen'])
self.df['member_since'] = pd.to_datetime(self.df['member_since'])

['date', 'ended_on', 'first_completed', 'last_completed', 'last_seen', 'member_since']
'''
def columns_to_datetime(df, columns=[]): 
    columns = ['date', 'ended_on', 'first_completed', 'last_completed', 'last_seen', 'member_since']
    for col in columns: 
        df[col] = pd.to_datetime(df[col])
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

        # creates two new columns and delete the previous
        self.df["authored_translations"], self.df["approved_translations"] = zip(*self.df["authored_translations"].map(lambda x: get_numeric_groups(x, groups=2)))

        # creates new column and delete the previous
        self.df['avg_satisfaction_rating'] = self.df['avg_satisfaction_rating'].apply(lambda x: get_numeric_one(x, deletes='%')).fillna(0)

        # creates two new columns and delete the previous
        self.df["comments"], self.df["replies"] = zip(*self.df["comments"].map(lambda x: get_numeric_groups(x, groups=2)))

        # creates two new columns and delete the previous
        self.df["translations"], self.df["translations_aproved"] = zip(*self.df["translations"].map(lambda x: get_numeric_groups(x, groups=2)))

        # creates two new columns and delete the previous
        self.df["created"], self.df["beta"] = zip(*self.df["created"].map(lambda x: get_numeric_groups(x, groups=2)))

        # creates two new columns and delete the previous
        self.df["kumite"], self.df["started_kumite"] = zip(*self.df["kumite"].map(lambda x: get_numeric_groups(x, groups=2)))

        ####################### simples ########################
        # creates new column and delete the previous
        self.df['avg_rank'] = self.df['avg_rank'].apply(lambda x: get_numeric_one(x, deletes='kyudan')).fillna(0)


        # creates new column and delete the previous
        self.df['best_practice'] = self.df['best_practice'].apply(lambda x: get_numeric_one(x, deletes=',')).fillna(0)

        # creates new column and delete the previous
        self.df['best_practice_solutions'] = self.df['best_practice_solutions'].apply(lambda x: get_numeric_one(x, deletes=',')).fillna(0)

        # creates new column and delete the previous
        self.df['clever_solutions'] = self.df['clever_solutions'].apply(lambda x: get_numeric_one(x, deletes=',')).fillna(0)


        # creates new column and delete the previous
        self.df['highest_trained'] = self.df['highest_trained'].apply(get_highest_trained)

        # creates new column and delete the previous
        self.df['honor'] = self.df['honor'].apply(lambda x: get_numeric_one(x, deletes=',')).fillna(0)

        # creates new column and delete the previous
        self.df['honor_percentile'] = self.df['honor_percentile'].apply(lambda x: get_numeric_one(x, deletes='Top%')).fillna(0)


        # creates new column and delete the previous
        self.df['leaderboard_position'] = self.df['leaderboard_position'].apply(lambda x: get_numeric_one(x, deletes='#,')).fillna(0)

        # creates new column and delete the previous
        self.df['rank'] = self.df['rank'].apply(lambda x: get_numeric_one(x, deletes='kyudan')).fillna(0)

        # creates new column and delete the previous
        self.df['total_collected'] = self.df['total_collected'].apply(lambda x: get_numeric_one(x, deletes=',')).fillna(0)

        # creates new column and delete the previous
        self.df['total_completed_kata'] = self.df['total_completed_kata'].apply(lambda x: get_numeric_one(x, deletes=',')).fillna(0)

        # creates new column and delete the previous
        self.df['total_completions'] = self.df['total_completions'].apply(lambda x: get_numeric_one(x, deletes=',')).fillna(0)

        # creates new column and delete the previous
        self.df['total_stars'] = self.df['total_stars'].apply(lambda x: get_numeric_one(x, deletes=',')).fillna(0)

        # cleans dates column
        columns = ['date', 'ended_on', 'first_completed', 'last_completed', 'last_seen', 'member_since']
        self.df = columns_to_datetime(self.df, columns=columns)

        columns_deletes_dictionary = {
            'total_stars': ',', 
            'total_completions': ',', 
            'total_completed_kata': ',', 
            'total_collected': ',', 
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
            'highest_trained': '', 
            'highest_trained': '', 

        }