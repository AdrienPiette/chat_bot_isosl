---
id: "apoweb_commande_magasin_v1"
title: "Commande Magasin via APOWEB"
description: "Procédure complète pour commander du matériel médical via l'application APOWEB, remplaçant LIFT."
application: "Portail Applicatif ISoSL"
module: "APOWEB"
document_type: "user-guide"
target_audience: "staff-hospitalier"
language: "fr"

date_created: "2025-01-01"
last_updated: "2025-01-01"

sections:
  - "Connexion à APOWEB"
  - "Page Produits"
  - "Filtres et recherche"
  - "Encoder les quantités"
  - "Sauvegarder les changements"
  - "Consultation des commandes"
  - "Menu Demandes"
  - "Bon de commande"
  - "Envoi du bon de commande"
  - "Urgence et commentaires"

tags:
  - "commande-magasin"
  - "apoweb"
  - "portail-applicatif"
  - "matériel-médical"
  - "commande"
  - "formation"
  - "procédure"

screenshots_count: 14
document_type_detail: "Procédure détaillée d'utilisation d'APOWEB pour les commandes internes"
---



# Commande Magasin optimisée RAG

## Guide de commande du matériel médical via APOWEB

(Remplace l’application LIFT)

---

## Introduction

Depuis le **Portail Applicatif**, double-cliquez sur l’icône **ApoWeb** (orange avec pansements croisés).

Une page web s’ouvre et affiche l’écran de connexion.  
Saisissez votre **NOM D’UTILISATEUR** (ex. en majuscules : `LIERNEUX.MASALLE`) et le mot de passe identique à celui utilisé pour vos sessions de salle.

Une fois connecté, l’application APOWEB s’affiche.

---

# Capture d’écran – Page de Connexion (APO)

## Contexte

Page permettant l’authentification des utilisateurs de l’application APO.

---

## Structure de la page

**Titre :** Connexion

**Champs :**

- Nom d’utilisateur (texte)
    
- Mot de passe (champ masqué)
    

**Icônes :** utilisateur / cadenas

**Bouton :** Se connecter (bleu)

**Pied de page :** logo Medsoc

**Barre du navigateur :**

- URL `sapoadpp1/apo/webapp/Login`
    
- Icônes de navigation
    
- Onglet « Login »
    

---

## Résumé fonctionnel

Page simple d’accès — aucune autre option visible.

---

# Capture d’écran – Page « Produits » (APO)

## Contexte

Page principale de sélection des articles.  
Permet d’encoder les quantités et de sauvegarder les modifications.

---

## Zones principales

### En-tête

- Menus : Demandes / Consulter
    
- Site actif (ex. LIE_Tilleul Étage — varie selon l’unité)
    
- Bouton : Changer de site/service
    

### Filtres

- Code facturation
    
- Code post-fact
    
- Imputation
    

---

## Tableau des produits

### Colonnes visibles

- Article
    
- Qté à comm. (éditable)
    
- Cond.
    
- Prix cond.
    
- Coût
    
- Qté max
    
- Qté commandé
    
- Stock
    

### Éléments mis en évidence

1. **Article** : nom des produits
    
2. **Qté à comm.** : champ éditable
    
3. **Sauvegarder les changements**
    
4. **Qté commandé** : quantités déjà envoyées
    

### Action supplémentaire

- **Imprimer**
    

---

# Procédure – Étape 1

## Encoder la quantité des produits

### 1) Zone « ABC » – Filtre sur les articles

Permet de rechercher un produit par mot-clé.

**Astuce :**  
Pour afficher tous les articles contenant un mot, sélectionner **abc → Contient**.

---

# Capture d’écran – Menu de filtre « Article » (APO)

## Structure

- Champ de recherche
    
- Opérateurs : Contient, Ne contient pas, Débute par, Termine par, Est égal à, N'est pas égal à
    
- Réinitialiser
    

## Fonction

Affiner l’affichage des articles selon un critère textuel.

---

### 2) Tri alphabétique

Un clic sur **l’en-tête Article** trie la liste de A→Z ou Z→A.

---

### 3) Qté à comm.

Encoder les quantités souhaitées.

**Attention :**  
La quantité correspond **au nombre de conditionnements**, pas au nombre d’unités.  
Exemple :

- Vacutainer 22G → encoder « 45 » = 45 unités
    
- Compresses 5x5 → livrées par 100 (affiché dans Cond.)
    

Après encodage → cliquer **Sauvegarder les changements**.

---

# Capture d’écran – Bouton « Sauvegarder les changements » (APO)

## Structure

- Icône : disquette
    
- Texte : Sauvegarder les changements
    

## Fonction

Enregistre les quantités modifiées.

---

### 4) Qté commandé

Affiche les quantités déjà transmises et en attente à la pharmacie.

**Astuce :**  
Pour voir toutes les commandes en attente → menu **Demandes > En attente**

---

# Capture d’écran – Menu « Demandes » (APO)

## Structure

Options :

- Produits
    
- Bon de commande
    
- Historique
    
- En attente
    
- Partielles / annulées
    

Icône : chariot / commande

## Fonction

Accès centralisé à toutes les étapes des commandes internes.

---

# Procédure – Étape 2

## Envoyer le bon de commande

Cliquer sur **Demandes → Bon de commande**.

---

# Capture d’écran – Menu « Demandes » : Option « Bon de commande »

## Contexte

Accès à l’écran final de vérification et envoi de la commande.

## Note

La surbrillance rose n’existe pas dans APO — elle a été ajoutée pour la capture.

---

# Capture d’écran – Écran « Bon de commande » (APO)

## Structure générale

- Tableau des articles
    
- Qté en stock
    
- Qté à comm.
    
- Cond.
    
- Qté max / Qté commandé
    
- Panel inférieur : Urgent / Commentaire
    

## Fonctions

5. Contrôler la commande et ajuster les quantités
    
6. Cocher **Urgent** si nécessaire
    
7. Ajouter un **Commentaire**
    

---

# Capture d’écran – Bouton « Envoyer le bon de commande » (APO)

## Structure

- Bouton vert
    
- Icône : ✓
    
- Texte : Envoyer le bon de commande
    

## Fonction

Transmission définitive du bon de commande à la pharmacie.