import mysql.connector as MC
from User import User

class Db:

    def init(self):
        self.host = "localhost"
        self.database= "cat_db"
        self.user='root'
        slef.password='root'


#Recupere tout les utilisateurs
    def getAllusers(self):
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

            print('Select all users')
            for users in userArray:
                print('--------------')
                print('User name:{}, {}'.format(users.name, users.surname))

            return userArray


        except MC.error as err:
            print(err)

        finally:
            if(conn.is_connected()):
                cursor.close()
                conn.close

#Ajout d'un utilisateur

    def addUser(self):
        try:
            conn = MC.connect(host='localhost', database='cat_db', user='root', password='root')
            cursor = conn.cursor()
            req = 'insert into user(id, name , surname, password, login ) values(%s, %s, %s, %s, %s)'
            infos = (cursor.lastrowid, 'Lacoste','together', 'Belzebut', 'herisson59')

            cursor.execute(req, infos)
            conn.commit()


        except MC.error as err:
            print(err)

        finally:
            if(conn.is_connected()):
                cursor.close()
                conn.close
