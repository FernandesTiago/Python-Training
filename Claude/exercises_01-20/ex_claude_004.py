# Register 3 products and display on screen (using lists and dictionaries)

product1 = {"item": "Computer", "price": 3500, "stock": 4}
product2 = {"item": "Speaker", "price": 300, "stock": 2}
product3 = {"item": "Television", "price": 5500, "stock": 10}

products = [product1, product2, product3]

for product in products:
    print(f"Item: {product['item']}", end=" ")
    print(f"Price: {product['price']}", end=" ")
    print(f"Stock: {product['stock']}")
