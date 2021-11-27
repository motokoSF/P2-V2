
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests

# Récupérer les liens de toutes les catégories du site à partir de l'url de base
# retourne un dictionnaire 

def get_url_categorie(url):

    categories = {}
    réponse = requests.get(url)
    soup = BeautifulSoup(réponse.text, 'html.parser')
    
    categories_html = soup.find("div", class_ = "side_categories").ul.li.ul
    
    for category in categories_html.find_all("a"):
        category_link = urljoin(url, category.attrs["href"])
        
        categories[category.string.strip()] = category_link

    return categories








