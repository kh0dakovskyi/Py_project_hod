import requests
from bs4 import BeautifulSoup

resp = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(resp.text, "html.parser")

for book in soup.select("article.product_pod h3 a"):
    print(book["title"])
