# Projet de NIM

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






g1 = Grille(value="0110100111010110", n=4)
for i in g1.getAllSymetries():
    print(i)
    print()
