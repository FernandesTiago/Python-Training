# sales control

def register_sale(seller, product, value):
    sale = {"seller": seller, "product": product, "value": value}
    return sale
def total_by_seller(sale_list, name):
    total = 0
    for sale in sale_list:
        if sale["seller"] == name:
            total += sale["value"]
    return total
def biggest_sale(sale_list):
    max_value = 0
    max_sale = {}
    for sale in sale_list:
        if sale["value"] > max_value:
            max_value = sale["value"]
            max_sale = sale
    return max_sale

def summary(sale_list):
    printed_names = []
    print()
    for sale in sale_list:
        print(f"Seller: {sale['seller']:<10} Product: {sale['product']:<10} Value: $ {sale['value']:>8.2f}")
    print()
    for sale in sale_list:
        seller = sale["seller"]
        if seller not in printed_names:
            print(f"Total sales by {sale['seller']}: $ {total_by_seller(sale_list, seller):.2f}")
            printed_names.append(seller)
    sale_of_the_day = biggest_sale(sale_list)
    print()
    print(f"The biggest sale of the day was $ {sale_of_the_day['value']:.2f} made by {sale_of_the_day['seller']}")

sale1 = register_sale("Ana", "Notebook", 3200.00)
sale2 = register_sale("Carlos", "Mouse", 150.00)
sale3 = register_sale("Ana", "Keyboard", 280.00)
sale4 = register_sale("Maria", "Monitor", 1100.00)
sale5 = register_sale("Carlos", "Notebook", 3200.00)
sale6 = register_sale("Maria", "Headset", 420.00)

sales = [sale1, sale2, sale3, sale4, sale5, sale6]

summary(sales)
