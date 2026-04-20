# stock using def

def register_product(name, quantity, price):
    product = {"name": name, "quantity": quantity, "price": price}
    return product

def product_total_value(product):
    total_value = product["quantity"] * product["price"]
    return total_value

def stock_total_value(product_list):
    total_stock_value = 0
    for product in product_list:
        total_stock_value += product_total_value(product)
    return total_stock_value
def out_of_stock_products(product_list):
    missing_products = []
    for product in product_list:
        if product["quantity"] == 0:
            missing_products.append(product["name"])
    return missing_products
def display(product_list):
    missing = out_of_stock_products(product_list)
    for product in product_list:
        print(f"Product: {product['name']:<10} Quantity: {product['quantity']:>3} Price: {product['price']:>6.2f}")
    print(f"Total stock value: {stock_total_value(product_list):.2f}")
    if len(missing) == 0:
        print("No missing items")
    else:
        print(f"The missing items are: {', '.join(missing)}")

product1 = register_product("Pen", 50, 1.5)
product2 = register_product("Notebook", 0, 12.90)
product3 = register_product("Eraser", 30, 0.75)
product4 = register_product("Ruler", 0, 3.20)
product5 = register_product("pencil", 100, 0.5)

products = [product1, product2, product3, product4, product5]

display(products)
