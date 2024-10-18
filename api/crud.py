'''
C=> Create  (INSERT INTO)
R=> Read    (SELECT)
U=> Update  (UPDATE)
D=> Delete  (DELETE)

UPDATE AND DELETE NEED WJERE CLAUSE*

'''

from database import con
import os

def main_menu():
    print("::: MAIN MENU :::")
    print("[1]. Create user")
    print("[2]. Liat users")
    print("[3]. Salir")
    opt = int(input('Press any option: '))
    return opt 

def create_user():
    new_user_query='''INSERT INTO users (username, email, password)
    VALUES('Cristian','crizh221@gmail.com','123456')
    '''
    
    con.execute(new_user_query)
    con.commit()
    
    print('user create succesfully.')
    os.system('pause')
    con.close()
    
create_user()
