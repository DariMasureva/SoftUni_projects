class Catalogue:

    def __init__(self, name:str):
        self.name = name
        self.products = []

    def add_product(self, product_name:str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter:str):
        products_by_letter = [product for product in self.products if product.startswith(first_letter)]
        return products_by_letter

    def __repr__(self):
        sorted_products = sorted(self.products)
        return f"Items in the {self.name} catalogue:\n" + '\n'.join(sorted_products)

