import tkinter as tk
from tkinter import messagebox
from ClassJeuDeLavie import JeuDeLaVie
import copy
import random

class VieIHM:
    def __init__(self, fen_princ):
        self.fen_princ = fen_princ
        fen_princ.title("Jeu de la Vie — Interface Tkinter")

        self.nb_lig = 25
        self.nb_col = 25
        self.taille_c = 20

        self.jeu = JeuDeLaVie(self.nb_lig, self.nb_col)
        self.est_lance = False
        self.id_apres = None
        self.gen_actu = 0
        self.precedente = None
        self.precedente2 = None
        
        self._creer_widgets()
        self._config_canevas()
        self._dessiner_grille()

    def _creer_widgets(self):
        frm_canevas = tk.Frame(self.fen_princ)
        frm_canevas.grid(row=0, column=0)

        self.canevas = tk.Canvas(frm_canevas, bg="gray")
        self.canevas.grid(row=0, column=0)
        self.canevas.bind("<Button-1>", self._clic_souris)
        self.canevas.bind("<B1-Motion>", self._glisser_souris)

        frm_boutons = tk.Frame(self.fen_princ)
        frm_boutons.grid(row=1, column=0, pady=5)
        
        tk.Button(frm_boutons, text="Démarrer", command=self._demarrer).grid(row=0, column=0, padx=4)
        tk.Button(frm_boutons, text="Arrêter", command=self._arreter).grid(row=0, column=1, padx=4)
        tk.Button(frm_boutons, text="Pas", command=self._pas_suivant).grid(row=0, column=2, padx=4)
        tk.Button(frm_boutons, text="Effacer", command=self._effacer).grid(row=0, column=3, padx=4)
        tk.Button(frm_boutons, text="Aléatoire", command=self._alea).grid(row=0, column=4, padx=4)

        self.cur_vitesse = tk.Scale(frm_boutons, from_=50, to=2000, orient=tk.HORIZONTAL)
        self.cur_vitesse.set(300)
        self.cur_vitesse.grid(row=0, column=5, padx=10)

        frm_param = tk.Frame(self.fen_princ)
        frm_param.grid(row=2, column=0, pady=5)

        tk.Label(frm_param, text="Lignes:").grid(row=0, column=0)
        self.entree_lig = tk.Entry(frm_param, width=5)
        self.entree_lig.insert(0, str(self.nb_lig))
        self.entree_lig.grid(row=0, column=1)

        tk.Label(frm_param, text="Cols:").grid(row=0, column=2)
        self.entree_col = tk.Entry(frm_param, width=5)
        self.entree_col.insert(0, str(self.nb_col))
        self.entree_col.grid(row=0, column=3)

        tk.Label(frm_param, text="Taille:").grid(row=0, column=4)
        self.entree_taille = tk.Entry(frm_param, width=5)
        self.entree_taille.insert(0, str(self.taille_c))
        self.entree_taille.grid(row=0, column=5)

        tk.Button(frm_param, text="Appliquer", command=self._appliquer_grille).grid(row=0, column=6, padx=5)

        self.lbl_statut = tk.Label(self.fen_princ, text=f"Génération: 0 — Vivantes: 0")
        self.lbl_statut.grid(row=3, column=0)

    def _config_canevas(self):
        self.canevas.delete("all")
        self.canevas.config(width=self.nb_col * self.taille_c,
                            height=self.nb_lig * self.taille_c)

        self.rectangles = []
        for i in range(self.nb_lig):
            ligne = []
            for j in range(self.nb_col):
                x1 = j * self.taille_c
                y1 = i * self.taille_c
                x2 = x1 + self.taille_c
                y2 = y1 + self.taille_c
                r = self.canevas.create_rectangle(x1, y1, x2, y2, outline="#999", fill="gray")
                ligne.append(r)
            self.rectangles.append(ligne)

    def _dessiner_grille(self):
        nbr_vivantes = 0
        for i in range(self.nb_lig):
            for j in range(self.nb_col):
                id_rect = self.rectangles[i][j]
                if self.jeu.grille[i][j] == "*":
                    self.canevas.itemconfig(id_rect, fill="blue")
                    nbr_vivantes += 1
                else:
                    self.canevas.itemconfig(id_rect, fill="gray")

        self.lbl_statut.config(text=f"Génération: {self.gen_actu} — Vivantes: {nbr_vivantes}")

    def _clic_souris(self, event):
        i = event.y // self.taille_c
        j = event.x // self.taille_c
        if 0 <= i < self.nb_lig and 0 <= j < self.nb_col:
            self.jeu.grille[i][j] = "*" if self.jeu.grille[i][j] == "-" else "-"
            self._dessiner_grille()

    def _glisser_souris(self, event):
        i = event.y // self.taille_c
        j = event.x // self.taille_c
        if 0 <= i < self.nb_lig and 0 <= j < self.nb_col:
            self.jeu.grille[i][j] = "*"
            self._dessiner_grille()
            
    def _appliquer_grille(self):
        self._arreter()
        try:
            self.nb_lig = int(self.entree_lig.get())
            self.nb_col = int(self.entree_col.get())
            self.taille_c = int(self.entree_taille.get())
        except:
            return

        self.jeu = JeuDeLaVie(self.nb_lig, self.nb_col)
        self._config_canevas()
        self._dessiner_grille()
        self.gen_actu = 0
        self.precedente = None
        self.precedente2 = None

    def _demarrer(self):
        if not self.est_lance:
            self.est_lance = True
            self._lancer_pas()

    def _arreter(self):
        self.est_lance = False
        if self.id_apres:
            self.fen_princ.after_cancel(self.id_apres)

    def _pas_suivant(self):
        self.precedente2 = copy.deepcopy(self.precedente) if self.precedente else None
        self.precedente = copy.deepcopy(self.jeu.grille)
        self.jeu.etape_suivante()
        self.gen_actu += 1
        self._dessiner_grille()
        if self._verifier_fin():
            self._arreter()

    def _lancer_pas(self):
        if not self.est_lance:
            return
        self._pas_suivant()
        delai = int(self.cur_vitesse.get())
        self.id_apres = self.fen_princ.after(delai, self._lancer_pas)

    def _effacer(self):
        self._arreter()
        for i in range(self.nb_lig):
            for j in range(self.nb_col):
                self.jeu.grille[i][j] = "-"
        self.gen_actu = 0
        self.precedente = None
        self.precedente2 = None
        self._dessiner_grille()

    def _alea(self):
        self._effacer()
        for i in range(self.nb_lig):
            for j in range(self.nb_col):
                if random.random() < 0.25:
                    self.jeu.grille[i][j] = "*"
        self._dessiner_grille()

    def _verifier_fin(self):
        if self.jeu.grille_est_vide():
            messagebox.showinfo("Fin", "Toutes les cellules sont mortes.")
            return True

        if self.precedente and self.precedente == self.jeu.grille:
            messagebox.showinfo("Stable", "Structure stable détectée.")
            return True

        if self.precedente2 and self.precedente2 == self.jeu.grille:
            messagebox.showinfo("Oscillateur", "Oscillateur de période 2 détecté.")
            return True

        return False