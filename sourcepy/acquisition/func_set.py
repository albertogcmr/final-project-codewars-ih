def string2set(st): 
    '''
    input: "{'betegelse', 'OlegRadchenko'}" <str>
    output: set('betegelse', 'OlegRadchenko') <set>
    '''
    return set(user.replace("'", "") for user in st[1:-1].split(', '))
