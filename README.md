# API d'Analyse de Sentiment et Traitement des Avis

Une API REST performante développée avec **FastAPI** et **Hugging Face Transformers** pour analyser la polarité des avis clients et déterminer leur niveau d'urgence.

---

## Fonctionnalités Principales

* **Chargement Optimisé (Design Pattern Singleton & Cache) :** Le modèle Hugging Face est instancié une seule fois via un pattern Singleton et `functools.lru_cache` pour économiser la mémoire et accélérer le temps de réponse.
* **Modèle NLP Multilingue :** Utilisation de `nlptown/bert-base-multilingual-uncased-sentiment` pour la classification d'avis en étoiles (1 à 5).
* **Validation stricte des données (Pydantic) :**
  * Le contenu doit être une chaîne de caractères non vide.
  * Longueur contrôlée : **entre 20 et 50 caractères**.
* **Post-traitement personnalisé :**
  * **Classification par polarité :**
    * `1 star` / `2 stars` ➔ **Négatif**
    * `3 stars` ➔ **Neutre**
    * `4 stars` / `5 stars` ➔ **Positif**
  * **Alerte d'urgence (`is_urgent`) :** Automatiquement positionné à `True` si l'avis est **Négatif**.

---

## Informations Modèle & Licence

* **Modèle utilisé :** [`nlptown/bert-base-multilingual-uncased-sentiment`](https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment)
* **Licence du modèle :** **`CC-BY-NC-4.0` (Creative Commons Attribution-NonCommercial 4.0 International)**
  * **Utilisation :** Libre pour la recherche, les projets académiques et l'usage personnel.
  * **Restriction :** L'utilisation à des fins commerciales directes est restreinte par les termes de la licence du modèle d'origine.

---

## Installation & Configuration

### 1. Prérequis
* Python 3.10+
* PIP

### 2. Cloner le projet et installer les dépendances
```bash
pip install fastapi uvicorn transformers torch pydantic