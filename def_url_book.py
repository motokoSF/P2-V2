from bs4 import BeautifulSoup
import requests

# Récupérer les liens de tous les livres à partir des ceux des catégories 
# Et traiter la pagination du site complet 

def get_url_book(link):

    books = []
    request_categories = requests.get(link)
    soup_book = BeautifulSoup(request_categories.text, 'html.parser')
   
    book_html = soup_book.find("section").find("ol", class_="row")

    for book in book_html.find_all("li"):
        partial_link = book.article.h3.a
        full_link = "https://books.toscrape.com/catalogue/" + partial_link.attrs["href"].replace("../../../", "")
        books.append(full_link)
    

    next_page = soup_book.find("li", class_ ="next")
    if next_page:
        next_partial_links = next_page.find("a")["href"]
        next_full_link = link.rsplit("/", 1)[0] + "/" + next_partial_links.replace("../../../", "")
        books.extend(get_url_book(next_full_link))

    return books








