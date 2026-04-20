# dictionaries and def

product1 = {"product": "Notebook", "price": 4000, "stock": 50}
product2 = {"product": "smartphone", "price": 10500, "stock": 100}
product3 = {"product": "Television", "price": 3000, "stock": 10}

def show_product(x):
    print(f"""\nProduct: {x['product']}
Price: {x['price']}
Stock: {x['stock']}
""")

show_product(product1)
show_product(product2)
show_product(product3)
