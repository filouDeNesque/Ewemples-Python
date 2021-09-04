class User:
    def __init__(self, login, password, name, surname):
        self.login = login
        self.password = password
        self.name = name
        self.surname = surname

    def toString(self):
        print('login: '+self.login+', name: '+self.surname+', name: '+self.name+', password'+ self.password)
