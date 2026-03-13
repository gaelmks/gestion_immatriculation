import string
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
            if not self.mot1 in self.mot2:
                self.dict[self.mot1]=self.mot2
                return self.dict
            else:
                print("le mot existe deja")

class supp(Mot):
    def MethodeSupp(self):
            if self.mot1 in self.dict:
                del self.dict[self.mot1]
                return self.dict
            else:
                print("Le mot est deja supprime")


demande=input("Entrer ajout ou supprimer: ")
if demande.lower()=='ajout':
    apt=input("entrer la matricule:")
    bpt=input("entrer le nom:")
    cpt={}
    ad=ajout(apt,bpt,cpt)
    print(ad.MethodeAjout())
    
elif demande.lower()=='supprimer':
     apt=input("Entrer la matricule:")
     cpt={}
     sp=supp(apt,cpt)
     print(sp.MethodeSupp())