# Projet de NIM

from rich import print

class Grille():

    def __init__(self, value=0, n=3):
        self.n = n
        self.value = value

    def toBin(self):
        return bin(self.value)[2:].zfill(self.n**2)

    def __repr__(self):
        return "\n".join([self.toBin()[i:i+self.n] for i in range(0, self.n**2, self.n)])

    def isLegal(self, grille2):
        # retourne True si la grille2 est une grille possible
        # retourne False sinon

        # première condition pour un coup légal : la grille2 doit être plus grande que la grille1 (car on rajoute au moins une croix)
        if grille2.value <= self.value:
            return False

        # seconde condition pour un coup légal : tous les 1 présents sur la grille 1 doivent encore être présents sur la nouvelle grille
        for i in range(len(self.toBin())):
            if self.toBin()[i] == "1" and grille2.toBin()[i] == "0":
                return False

        # troisième condition pour un coup légal : les nouvelles croix (donc les nouveaux 1) doivent être alignées (sur la même ligne ou sur la même colonne)
        # on récupère les coordonnées des nouvelles croix
        nouvellesCroix = []
        for i in range(len(self.toBin())):
            if grille2.toBin()[i] == "1" and self.toBin()[i] == "0":
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
        # on retourne toutes les grilles possibles à partir de la grille actuelle
        bitCount = self.n**2
        grilles = []
        for i in range(2**bitCount):
            grille = Grille(i, self.n)
            if self.isLegal(grille):
                grilles.append(grille)
        return grilles

class Graphe(object):

    def __init__(self,n):
        self.n = n
        self.sommets = [[i, None] for i in range(2**(n**2))]
        for i in range(len(self.sommets)):
            candidates = [v.value for v in Grille(i, n).toutesGrilles()]
            self.sommets[i][1] = candidates if len(candidates) > 0 else None


        self.noyau = self._noyau()


    def _noyau(self):

        # maintenant qu'on a tous les sommets, c'est l'heure de la purge
        marques = []
        kl = 0
        while True :
            # première étape : on marque tous les sommets sans successeurs
            for i in range(len(self.sommets)):
                if self.sommets[i] != None and self.sommets[i][1] == None and self.sommets[i][0] not in marques:
                    marques.append(self.sommets[i][0])

            # seconde étape : on supprime tous les sommets qui ont pour succésseur un sommet marqué
            for i in range(len(self.sommets)):

                if self.sommets[i] != None and self.sommets[i][1] != None  :
                    for j in self.sommets[i][1]:

                        if j in marques:

                            self.sommets[i] = None

                            break


            mapSommets = [i[0] for i in self.sommets if i != None]
            # troisième étape : on supprime tous les successeurs qui n'ont pas d'équivalent dans le graphe
            for i in range(len(self.sommets)):
                if self.sommets[i] != None and self.sommets[i][1] != None :
                    toRemove = []
                    for j in self.sommets[i][1]:
                        if j not in mapSommets:
                            toRemove.append(j)
                    for r in toRemove:
                        self.sommets[i][1].remove(r)
                    if len(self.sommets[i][1]) == 0:
                        self.sommets[i][1] = None

            if 0 in marques:
                return marques

            kl += 1


gr = Graphe(3)
for i in gr.sommets:
    print(i)
    print("")
print(len(gr.noyau))

print(Grille(0, 3).toutesGrilles())
