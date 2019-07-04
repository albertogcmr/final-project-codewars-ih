def string2set(st): 
    '''
    input: "{'betegelse', 'OlegRadchenko'}" <str>
    output: set('betegelse', 'OlegRadchenko') <set>
    '''
    return set(user.replace("'", "") for user in st[1:-1].split(', '))


if __name__ == '__main__': 
    s = "{'betegelse', 'OlegRadchenko', 'verma.amardeep@gmail.com', 'mro', 'PilgrimShadow', 'blinker345678', 'bwblock', 'jamad', 'spirit11', 'cnn', 'booox', 'mstrotta', 'Liova99'}"
    res = string2set(s)
    print(res)
    print(type(res))