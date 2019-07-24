import re

def get_numeric_groups(x, groups=1): 
    try: 
        numbers = [int(number) for number in re.findall(r'\d+', x)]
    except: 
        numbers = [0] * groups
    else: 
        pass
    finally: 
        # return list if groups > 1 else return first element in list
        return numbers[:groups] if groups > 1 else numbers[0]
# df["authored_translations"], df["approved_translations"] = zip(*df["authored translations"].map(lambda x: get_numeric_groups(x, groups=2)))


def cleaning(df): 

    columns = ["authored_translations", "approved_translations", "avg_satisfaction_rating", 'best_practice', 
                'best_practice_solutions']
    for col in columns: 
        print(df[col].unique())



    return df

