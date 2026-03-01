# 🧬 Jeu de la Vie — Python / Tkinter

Implémentation du **Jeu de la Vie de Conway** en Python avec une interface graphique Tkinter.


## 📐 Règles de Conway

Une cellule **vivante** (`*`) survit si elle a **2 ou 3 voisines vivantes**, sinon elle meurt.  
Une cellule **morte** (`-`) naît si elle a **exactement 3 voisines vivantes**.

---

## ✨ Fonctionnalités

- 🖱️ **Dessin à la souris** : clic ou glisser pour activer/désactiver des cellules
- ▶️ **Démarrer / Arrêter** l'évolution automatique
- 👣 **Pas à pas** : avancer d'une génération manuellement
- 🎲 **Placement aléatoire** des cellules (densité ~25%)
- 🗑️ **Effacer** la grille
- ⚡ **Vitesse réglable** via un curseur (50ms à 2000ms)
- 📐 **Grille redimensionnable** (lignes, colonnes, taille des cellules)
- 🔍 **Détection automatique** des états finaux :
  - Toutes cellules mortes
  - Structure stable
  - Oscillateur de période 2

---

## 🚀 Lancement

### Prérequis

- Python 3.x
- `tkinter` (inclus avec Python sur la plupart des systèmes)

### Commande

```bash
python main.py
```

---

## 📁 Structure

```
game-of-life-python/
├── main.py            # Point d'entrée — lance la fenêtre Tkinter
├── ClassJeuDeLavie.py # Logique du jeu (grille, règles, étapes)
└── tkinterclass.py    # Interface graphique (VieIHM)
```

---

## 🏗️ Architecture

| Fichier              | Rôle |
|----------------------|------|
| `ClassJeuDeLavie.py` | Classe `JeuDeLaVie` : gestion de la grille et application des règles de Conway |
| `tkinterclass.py`    | Classe `VieIHM` : interface Tkinter, canvas, boutons, détection de fin |
| `main.py`            | Initialisation de la fenêtre et lancement de l'application |
