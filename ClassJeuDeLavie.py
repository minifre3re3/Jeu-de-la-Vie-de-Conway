import random


class JeuDeLaVie:
    def __init__(self, nbr_lig, nbr_col):
        if (nbr_lig <= 0 or nbr_col <= 0):
            exit(0)
        self.lig = nbr_lig
        self.col = nbr_col
        self.grille = []
        for i in range(self.lig):
            ligne = []
            for j in range(self.col):
                ligne.append('-')
            self.grille.append(ligne)

    def afficher_grille(self):
        print("La grille :")
        for i in range(self.lig):
            lig_aff = ""
            for j in range(self.col):
                lig_aff += self.grille[i][j] + " "
            print(lig_aff)
    
    def grille_est_vide(self):
        for i in range(self.lig):
            for j in range(self.col):
                if self.grille[i][j] == '*':
                    return False 
        return True

    def placer_cellules_aleatoirement(self, nbr_cell):
        cpt = 0 
        while cpt < nbr_cell:
            i = random.randint(0, self.lig - 1)
            j = random.randint(0, self.col - 1)

            if self.grille[i][j] == '-': 
                self.grille[i][j] = '*'
                cpt += 1

    def get_adjacents(self, i, j):
        cpt = 0 
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                if x == i and y == j:
                    continue
                if 0 <= x < self.lig and 0 <= y < self.col:
                    if self.grille[x][y] == '*':
                        cpt += 1
        return cpt 

    def etape_suivante(self):
        nouv_grille = []
        for i in range(self.lig):
            ligne = []
            for j in range(self.col):
                vivantes = self.get_adjacents(i, j)

                if self.grille[i][j] == '*': 
                    if vivantes == 2 or vivantes == 3:
                        ligne.append('*') 
                    else:
                        ligne.append('-') 
                else: 
                    if vivantes == 3:
                        ligne.append('*') 
                    else:
                        ligne.append('-')
            nouv_grille.append(ligne)
        self.grille = nouv_grille