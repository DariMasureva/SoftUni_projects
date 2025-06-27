class Catalogue:

    def __init__(self, name:str):
        self.name = name
        self.products = []

    def add_product(self, product:str):
        self.products.append(product)

    def get_by_letter(self, letter:str):
        products_by_letter = [product for product in self.products if product[0].lower() == letter.lower()]
        return products_by_letter

    def __repr__(self):
        sorted_products = sorted(self.products)
        return f"Items in the {self.name} catalogue: \n" + '\n'.join(sorted_products)


