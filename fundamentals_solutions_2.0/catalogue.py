class Catalogue:
    products = []

    def __init__(self, name:str):
        self.name = name

    def add_product(self, product:str):
        self.products.append(product)

    def get_by_letter(self, letter:str):
        products_by_letter = [product for product in self.products if product[0] == letter]
        return products_by_letter

    def __repr__(self):
        self.products.sort()
        return f"Items in tne {self.name} catalogue: \n" + '\n'.join(self.products)

