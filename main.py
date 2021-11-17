from def_url_categorie import get_url_categorie
from def_url_book import get_url_book
from def_data_book import get_data_book
from tqdm import tqdm
import csv

# pacerelles entre les fonctions
# génère une liste de catégories
# génère une liste de livres pour tous les liens de catégories
# génère une liste de dictionnaires pour tous les livres
# incrémente tous les dictionnaires dans un document CSV   

url="https://books.toscrape.com/index.html"

categories_links = get_url_categorie(url) 

books_links = []
for link in tqdm(categories_links, "books_links"):
    books_links.extend(get_url_book(link))

info_books = []
for book_link in tqdm(books_links, "info_books"):
    info_books.append(get_data_book(book_link))

with open(r"C:\Users\Albin\Desktop\P2-V2\book_to_scrap.csv","w",newline="", encoding="utf-8") as file:
    Dictwriter = csv.DictWriter(file, fieldnames =  info_books[0].keys())
    Dictwriter.writeheader()
    for book_dict in info_books:
        Dictwriter.writerow(book_dict)

    
