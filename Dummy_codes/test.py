products = [
    {"product_id": 1, "category": "Electronics", "price": 799.99, "quantity": 10},
    {"product_id": 2, "category": "Clothing", "price": 49.99, "quantity": 25},
    {"product_id": 3, "category": "", "price": 199.99, "quantity": 5},
    {"product_id": 4, "price": 9.99, "quantity": 0, "category": "Home"},
    {"product_id": 5, "category": "Accessories", "price": -19.99, "quantity": 2},
    {"category": "Furniture", "product_id": 6, "price": 399.99, "quantity": 8},
    {"product_id": 7, "category": "Electronics", "price": 999.99},
    {"product_id": 8, "category": "Toys", "quantity": 20, "price": 29.99},
]

# if products is missing, remove
# category is missing, remove
# proce & quantity is missing or -ve, remove
# normalized_value = (value - min_value) / (max_value - min_value)

class Datacleaner:
    def __init__(self, products) -> None:
        self.products = products

    
    def clean_data(self):
        product = self.products
        output = []

        for row in product:
            temp_d = {}
            if ("product_id" in row.keys() and "category" in row.keys() and
                "price" in row.keys() and row["price"] > 0 and
                "quantity" in row.keys() and row["quantity"] > 0):
                output.append(row)
            
        print(output)

        


d = Datacleaner(products)
d.clean_data()
