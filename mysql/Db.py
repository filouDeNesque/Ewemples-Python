import mysql.connector as MC
from User import User

class Db:

    def init(self):
        self.host = "localhost"
        self.database= "cat_db"
        self.user='root'
        slef.password='root'


    def listallusers(self):
        try:
            conn = MC.connect(host='localhost', database='cat_db', user='root', password='root')
            cursor = conn.cursor()
            req= 'select * from user'
            cursor.execute(req)
            userlist=cursor.fetchall()
            
            userArray= []

            for user in userlist:
                newuser = User(user[1],user[2],user[3],user[4])
                userArray.append(newuser)
                print ('nom:{}'.format(user[1]))
                print ('login:{}'.format(user[2]))
                print ('password:{}'.format(user[3]))
                print ('surname:{}'.format(user[4]))

            for users in userArray:
                print('--------------')
                print('User array:{}'.format(users.name) )



        except MC.error as err:
            print(err)

        finally:
            if(conn.is_connected()):
                cursor.close()
                conn.close
