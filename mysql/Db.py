import mysql.connector as MC

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

            for user in userlist:
                print ('nom:{}'.format(user[1]))

        except MC.error as err:
            print(err)

        finally:
            if(conn.is_connected()):
                cursor.close()
                conn.close
