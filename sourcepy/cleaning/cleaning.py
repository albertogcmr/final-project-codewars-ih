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


def cleaning(df): 
    # clean column names
    df.columns = df.columns.str.replace(' ', '_').str.replace('.', '').str.lower()

    # replace nan in numeric colmuns with 0
    df._get_numeric_data().fillna(0, inplace=True)


    # creates two new columns and delete the previous
    df["authored_translations"], df["approved_translations"] = zip(*df["authored_translations"].map(lambda x: get_numeric_groups(x, groups=2)))
    df["authored_translations"].value_counts()

    # creates new column and delete the previous
    df['avg_rank'] = df['avg_rank'].apply(lambda x: get_numeric_one(x, deletes='kyudan')).fillna(0)

    # creates new column and delete the previous
    df['avg_satisfaction_rating'] = df['avg_satisfaction_rating'].apply(lambda x: get_numeric_one(x, deletes='%')).fillna(0)

    # creates new column and delete the previous
    df['best_practice'] = df['best_practice'].apply(lambda x: get_numeric_one(x, deletes=',')).fillna(0)

    # creates new column and delete the previous
    df['best_practice_solutions'] = df['best_practice_solutions'].apply(lambda x: get_numeric_one(x, deletes=',')).fillna(0)

    # creates new column and delete the previous
    df['clever_solutions'] = df['clever_solutions'].apply(lambda x: get_numeric_one(x, deletes=',')).fillna(0)

    # creates two new columns and delete the previous
    df["comments"], df["replies"] = zip(*df["comments"].map(lambda x: get_numeric_groups(x, groups=2)))

    # creates two new columns and delete the previous
    df["created"], df["beta"] = zip(*df["created"].map(lambda x: get_numeric_groups(x, groups=2)))

    # cleans dates column
    df['date'] = pd.to_datetime(df['date'])
    df['ended_on'] = pd.to_datetime(df['ended_on'])
    df['first_completed'] = pd.to_datetime(df['first_completed'])
    df['last_completed'] = pd.to_datetime(df['last_completed'])
    df['last_seen'] = pd.to_datetime(df['last_seen'])
    df['member_since'] = pd.to_datetime(df['member_since'])

    # creates new column and delete the previous
    df['highest_trained'] = df['highest_trained'].apply(get_highest_trained)

    # creates new column and delete the previous
    df['honor'] = df['honor'].apply(lambda x: get_numeric_one(x, deletes=',')).fillna(0)

    # creates new column and delete the previous
    df['honor_percentile'] = df['honor_percentile'].apply(lambda x: get_numeric_one(x, deletes='Top%')).fillna(0)

    # creates two new columns and delete the previous
    df["kumite"], df["started_kumite"] = zip(*df["kumite"].map(lambda x: get_numeric_groups(x, groups=2)))

    # creates new column and delete the previous
    df['leaderboard_position'] = df['leaderboard_position'].apply(lambda x: get_numeric_one(x, deletes='#,')).fillna(0)

    # creates new column and delete the previous
    df['rank'] = df['rank'].apply(lambda x: get_numeric_one(x, deletes='kyudan')).fillna(0)

    # creates new column and delete the previous
    df['total_collected'] = df['total_collected'].apply(lambda x: get_numeric_one(x, deletes=',')).fillna(0)

    # creates new column and delete the previous
    df['total_completed_kata'] = df['total_completed_kata'].apply(lambda x: get_numeric_one(x, deletes=',')).fillna(0)

    # creates new column and delete the previous
    df['total_completions'] = df['total_completions'].apply(lambda x: get_numeric_one(x, deletes=',')).fillna(0)

    # creates new column and delete the previous
    df['total_stars'] = df['total_stars'].apply(lambda x: get_numeric_one(x, deletes=',')).fillna(0)

    # creates two new columns and delete the previous
    df["translations"], df["translations_aproved"] = zip(*df["translations"].map(lambda x: get_numeric_groups(x, groups=2)))
    
    return df