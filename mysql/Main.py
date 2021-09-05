from Db import Db

name = input("Votre nom : ")
surname = input("Votre prenom : ")
password = input ("Créer un mot de passe : ")
login = input("Créer un login : ")

db = Db()
db.addUser(name, surname, password, login)

listUsers = db.getAllusers()
