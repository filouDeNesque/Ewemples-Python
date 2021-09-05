from Db import Db

db = Db()
listUsers = db.listallusers()
print(listUsers[0].name)
