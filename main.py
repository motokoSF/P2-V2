from def_url_categorie import get_url_categorie
from def_url_book import get_url_book
from def_data_book import get_data_book
from tqdm import tqdm
import csv

# main = pacerelles entre les fonctions
# génère un dictionnaire (clé = nom de la catégorie // valeur = lien de la catégorie)
# boucle sur tous les liens de livre et la pagination des catégories 
# génère une liste de dictionnaires (scrap) pour tous les livres
# incrémente tous les dictionnaires dans un document CSV pour chaque catégorie   

url="https://books.toscrape.com/index.html"

categories_list_of_dicts = get_url_categorie(url)
 
for category_name,category_link in categories_list_of_dicts.items():
    books_links = get_url_book(category_link)

    info_books = []
    for book_link in tqdm(books_links,"{}".format(category_name)):
        info_books.append(get_data_book(book_link))

    with open("book_to_scrap/{}.csv".format(category_name),"w",newline="", encoding="utf-8") as file:     
        Dictwriter = csv.DictWriter(file, fieldnames =  info_books[0].keys())
        Dictwriter.writeheader()
        for book_dict in info_books:
            Dictwriter.writerow(book_dict)


