class Produit:
    def __init__(self, nom, prix, url):
        self.nom = nom
        self.prix = prix
        self.url = url

    def toString(self):
        return (self.nom+' '+self.prix+ ' '+ self.url)



