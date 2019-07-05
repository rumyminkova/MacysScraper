import requests
from bs4 import BeautifulSoup
import Product

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
products = Product.ProductList()


class Scraper:
    def __init__(self, site):
        self.site = site
        self.links = set()

    def get_product_pages(self):
        try:
            res = requests.get(self.site, headers=headers)
            soup = BeautifulSoup(res.text, "html.parser")
            for a in soup.find_all('a', href=True):
                link = a['href']
                if 'shop/product/' in link:
                    self.links.add(link)
        except Exception as e:
            print(str(e))

    def scrape_products(self):
        self.get_product_pages()
        for link in self.links:
            url='https://www.macys.com/'+link
            r = requests.get(url, headers=headers)
            soup = BeautifulSoup(r.text, "html.parser")

            try:
                name = soup.find_all("h1", {"class": "p-name h3"})[0].text
                description = soup.find_all("p", {"class": "c-m-v-1"})[0].text
                price = soup.find_all("div", {"class": "price"})[0].text
            except IndexError:
                pass

            products.create_product(name.strip(), price.strip(), description.strip())


scraper = Scraper('https://www.macys.com/shop/womens-clothing/all-womens-clothing?id=188851')
scraper.scrape_products()
products.save_products_to_csv("womens_clothing_products")
products.load_products_from_csv("womens_clothing_products")
products.find_item_by_name('Side-Tie Top')
products.find_item_by_name('Scuba Crepe Sheath Dress')