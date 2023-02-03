# Projet de NIM
from rich import print

class Grille():

    def __init__(self, value=None, n=3):
        self.n = n
        if value is None :
            self.value = "0" * n**2
        else :
            self.value = value

    def __repr__(self):
        return "\n".join([self.value[i:i+self.n] for i in range(0, self.n**2, self.n)])

    def __eq__(self, other): # pratique pour comparer deux grilles en utilisant un opérateur ==
        return self.value == other.value

    def rotate90(self):

        newValue = [0]*self.n**2

        for i in range(len(self.value)): # pour chaque bit
            if self.value[i] == "1":
                ligne = (i // self.n)+1
                colonne = (i % self.n)+1
                nouvelleLigne = colonne
                nouvelleColonne = (self.n)-ligne+1

                newValue[(nouvelleLigne-1)*self.n + (nouvelleColonne-1)] = 1

        return Grille("".join([str(i) for i in newValue]), self.n)


    def flipHorizontal(self):
        newValue = [0]*self.n**2

        for i in range(len(self.value)): # pour chaque bit
            if self.value[i] == "1":
                ligne = (i // self.n)+1
                colonne = (i % self.n)+1
                nouvelleLigne = ligne
                nouvelleColonne = (self.n+1)-colonne

                newValue[(nouvelleLigne-1)*self.n + (nouvelleColonne-1)] = 1

        return Grille("".join([str(i) for i in newValue]), self.n)

    def getAllSymetries(self):
        # symétries possibles :
        # - rotation de 90° (rotate90 x1)
        # - rotation de 180° (rotate90 x2)
        # - rotation de 270° (rotate90 x3)
        # - symétrie horizontale (flipHorizontal)
        # - symétrie verticale (flipHorizontal + rotate90 x2)
        # retourne toutes les grilles possibles sous forme de liste

        symetries = [self.value]

        symetries.append(self.rotate90().value)
        symetries.append(self.rotate90().rotate90().value)
        symetries.append(self.rotate90().rotate90().rotate90().value)
        symetries.append(self.flipHorizontal().value)
        symetries.append(self.flipHorizontal().rotate90().rotate90().value)

        # on retire les doublons
        symetries = list(set(symetries))
        # on retourne les grilles
        return [Grille(i, self.n) for i in symetries]

    def isLegal(self, grille2):
        # retourne True si la grille2 est une grille possible
        # retourne False sinon

        # première condition pour un coup légal : la grille2 doit être plus grande que la grille1 (car on rajoute au moins une croix)
        if int(grille2.value, 2) <= int(self.value, 2):
            return False

        # seconde contition pour un coup légal : tous les 1 présents sur la grille 1 doivent encore être présents sur la nouvelle grille
        for i in range(len(self.value)):
            if self.value[i] == "1" and grille2.value[i] == "0":
                return False

        # troisième condition pour un coup légal : les nouvelles croix (donc les nouveaux 1) doivent être alignées (sur la même ligne ou sur la même colonne)
        # on récupère les coordonnées des nouvelles croix
        nouvellesCroix = []
        for i in range(len(self.value)):
            if grille2.value[i] == "1" and self.value[i] == "0":
                nouvellesCroix.append((i // self.n, i % self.n))

        # on vérifie que les nouvelles croix sont alignées
        if len(nouvellesCroix) == 1:
            return True
        else:
            # on vérifie si les nouvelles croix sont sur la même ligne
            ligne = nouvellesCroix[0][0]
            for i in nouvellesCroix:
                if i[0] != ligne:
                    break
            else:
                return True

            # on vérifie si les nouvelles croix sont sur la même colonne
            colonne = nouvellesCroix[0][1]
            for i in nouvellesCroix:
                if i[1] != colonne:
                    break
            else:
                return True

            # si on est arrivé ici, c'est que les nouvelles croix ne sont pas alignées
            return False


    def toutesGrilles(self):
        # on retourne toutes les grilles possibles
        bitCount = self.n**2
        grilles = []
        for i in range(2**bitCount):
            binaryRepr = str(bin(i))[2:]
            # add 0 to the left if needed
            binaryRepr = "0"*(bitCount-len(binaryRepr)) + binaryRepr

            grille = Grille(value = binaryRepr, n = self.n)
            if self.isLegal(grille):
                grilles.append(grille)
            # passFlag = False
            # for j in grilles :
            #     if nouvelleGrille in j.getAllSymetries():
            #         passFlag = True
            # if not passFlag :
            #     grilles.append(Grille(value = str(bin(i))[2:], n = self.n))
        return grilles



class Graphe(object):

    def __init__(self, n):
        self.n = n
        grilleVide = Grille(value="0"*n**2, n=n)
        self.sommets = [[i, None] for i in range(2**(n**2))]
        for i in range(len(self.sommets)) :
            binaryRepr = str(bin(i))[2:]
            binaryRepr = binaryRepr = "0"*(n**2-len(binaryRepr)) + binaryRepr
            grille = Grille(value = binaryRepr, n = n)
            coupsLegaux = grille.toutesGrilles()
            self.sommets[i][1] = coupsLegaux if len(coupsLegaux) > 0 else None


        # maintenant qu'on a tous les sommets, c'est l'heure de la purge
        marques = [] # liste des sommets marqués
        while True :
            # première étape : on marque tous les sommets qui n'ont pas de successeurs
            for i in range(len(self.sommets)) :
                if self.sommets[i][1] == None :
                    marques.append(i)

            # seconde étape : on supprime tous les sommets qui ont pour succésseur un sommet marqué
            for i in range(len(self.sommets)) :
                if self.sommets[i][1] != None :
                    for j in self.sommets[i][1] :
                        if j.value in marques :
                            self.sommets[i][1] = None
                            break

            if 1 in marques :
                break

        print(self.sommets)

        # print(self.sommets)




# g1 = Grille(value="011010111", n=3)
# for i in g1.getAllSymetries():
#     print(i)
#     print()

# g1 = Grille(value="0"*9, n=3)
# coupsLegaux = g1.toutesGrilles()
# print(len(coupsLegaux))

graphe = Graphe(4)

#g1 = Grille(value="1"*9, n=3)
#print(g1.toutesGrilles())
