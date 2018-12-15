

# Librería de funciones sobre archivos

def save_set_users(users, filename='../output/codewars-users.txt'): 
    ''' Save set/list of users to file '''
    with open(filename, 'w') as f: 
        f.write('\n'.join(users)) 
# save_set_users({'hola', 'adios'})

def save_string_users(users, filename='../output/codewars-users.txt'): 
    ''' Save string of users to file '''
    with open(filename, 'w') as f: 
        f.write(users) 
# save_set_users(users)

def add_set_users(users, filename='../output/codewars-users.txt'): 
    ''' Append to file '''
    with open(filename, 'a') as f: 
        f.write(users) 
# add_set_users(users)

def load_set_users(filename='../output/codewars-users.txt'): 
    ''' Read from file '''
    with open(filename, 'r') as f: 
        users = f.readlines()
    return {user.strip() for user in users}
# len(load_set_users())