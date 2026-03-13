class Mot:
    def __init__(self,mot1,mot2,dict):
        self.mot1=mot1
        self.mot2=mot2
        self.dict=dict
    def getMot1(self):
        return self.mot1
    def getMot2(self):
        return self.mot2
    def getDict(self):
        return self.dict
    
class ajout(Mot):
    pass
    
    def MethodeAjout(self):
        def ajoute(a,b,c):
            a=self.mot1
            b-self.mot2
            c=self.dict
            if not a in c:
                c[a]=b
            else:
                print("le mot existe deja")

class supp(Mot):
    def MethodeSupp(self):
        def supp(a,c):
            a=self.mot1
            c=self.dict
            if a in c:
                del c[a]
            else:
                print("Le mot est deja supprime")

