# Comparaison de deux modèles candidats pour l'analyse de sentiment

## 1. Modèle 1 : `nlptown/bert-base-multilingual-uncased-sentiment`

* **Nom sur le Hub :** `nlptown/bert-base-multilingual-uncased-sentiment`
* **Lien :** [https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment](https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment)
* **Architecture de base :** BERT Base Multilingual Uncased
* **Taille :** ~0.2B paramètres (~167M)
* **Classes :** 5 étoiles (de 1 à 5)
* **Langues supportées :** 6 langues principales (Anglais, Néerlandais, Allemand, Français, Espagnol, Italien)
* **Licence :** `CC-BY-NC-4.0` (Non-commercial)

---

## 2. Modèle 2 : `tabularisai/multilingual-sentiment-analysis`

* **Nom sur le Hub :** `tabularisai/multilingual-sentiment-analysis`
* **Lien :** [https://huggingface.co/tabularisai/multilingual-sentiment-analysis](https://huggingface.co/tabularisai/multilingual-sentiment-analysis)
* **Architecture de base :** DistilBERT Base Multilingual Cased
* **Taille :** ~0.135B paramètres (~135M)
* **Classes :** 5 classes (Très négatif, Négatif, Neutre, Positif, Très positif)
* **Langues supportées :** 23 langues
* **Licence :** Permissive (MIT / Apache 2.0 - Commercialisable)

---

## 3. Synthèse comparative

| Critère | Modèle 1 (`nlptown`) | Modèle 2 (`tabularisai`) |
| :--- | :--- | :--- |
| **Nom Hub** | `nlptown/bert-base-multilingual-uncased-sentiment` | `tabularisai/multilingual-sentiment-analysis` |
| **Taille (Paramètres)** | ~0.2B | ~0.135B |
| **Langues couvertes** | 6 langues | 23 langues |
| **Classes de sortie** | 1 à 5 étoiles | 5 niveaux de sentiment |
| **Licence d'utilisation** | `CC-BY-NC-4.0` (Non commercial) | Permissive (Utilisation commerciale autorisée) |

---

## 4. Choix Final et Justification


** Le modèle **`tabularisai/multilingual-sentiment-analysis`** est le choix requis en raison de sa licence libre/permissive et de sa couverture linguistique étendue mais pour un usage commercial je vais partir sur le modèle **`nlptown/bert-base-multilingual-uncased-sentiment`**.