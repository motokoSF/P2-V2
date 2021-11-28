# OpenClassrooms DA Python P2:

Ce projet scrap le site <https://books.toscrape.com/>

Pour chaque categorie le scraper genere des csv et un dossier image contenant  
toutes les informations de chaque livre.

* product_page_url
* universal_ product_code (upc)
* title
* price_including_tax
* price_excluding_tax
* number_available
* product_description
* category
* review_rating
* image_url

## Pour commencer:

1. Création d'un environnement virtuel
```bash
python3 -m venv <nom_env_virtuel>
source <nom_env_virtuel>/Scripts/activate
```

2. Installation des dependences
```bash
pip3 install -r requirements.txt

```
3. Execution du script
```bash 
python3 main.py
```



