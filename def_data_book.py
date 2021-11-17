from bs4 import BeautifulSoup
import requests

# opérér le scraping des données à partir des liens de livres 

def get_data_book(book_link):

    request_book = requests.get(book_link)
    soup_book = BeautifulSoup(request_book.content, 'html.parser')
    
    data = {}

    # link 
    data["book_link"] = book_link
    # Universal product code        
    data["universal_product_code"] = soup_book.select("td")[0].text      
    # price_including_tax 
    data["price_including_tax"] = soup_book.select("td")[2].text
    # price_excluding_tax
    data["price_excluding_tax"] = soup_book.select("td")[3].text
    # number_available
    data["number_available"] = soup_book.select("td")[5].text  
    # titres
    data["title"] = soup_book.select("h1")[0].text
    # product_description
    data["product_description"] = soup_book.select("p")[3].text
    # category
    data["category"] = soup_book.select("a")[3].text
    # review_rating
    data["review_rating"] = soup_book.find_all("p", class_="star-rating")[0].get("class")[1]
    # image_url
    image = soup_book.find("div", class_="item active").img["src"]
    data["image_url"] = "http://books.toscrape.com/" + image.replace('../', '')

    return data
    

    
  