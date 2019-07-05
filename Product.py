import csv


class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def print_product_details(self):
        print(self.name)
        print(self.price)
        print(self.description)


class ProductList:
    def __init__(self):
        self.products = []

    def create_product(self, name, price, description):
        new_product = Product(name, price, description)
        self.products.append(new_product)

    def find_item_by_name(self, name):
        for product in self.products:
            if product.name == name:
                product.print_product_details()
                return
        print("Not found!")

    def print_products(self):
        for pr in self.products:
            print(pr.name,pr.price,pr.description)

    def save_products_to_csv(self,filename):
        with open(filename, 'w', newline='') as f:
            csv_writer = csv.writer(f, delimiter="|")
            for pr in self.products:
                csv_writer.writerow([pr.name,  pr.price,  pr.description])

    def load_products_from_csv(self,filename):
        with open(filename, 'r') as f:
            csv_reader = csv.reader(f, delimiter="|")
            self.products.clear()
            for row in csv_reader:
                self.create_product(row[0], row[1] ,row[2])

