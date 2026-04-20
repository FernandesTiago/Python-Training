# Create a dictionary representing a product with the keys:
# "name", "price", "available" (boolean)
#
# Then print a line formatted like this:
# Product: Keyboard | Price: $ 150.00 | Available: Yes

product = {"name": "Keyboard", "price": 150, "available": True}

available = product["available"]
availability = "Yes" if available else "No"

print(f"Product: {product['name']} | Price: $ {product['price']:.2f} | Available: {availability}")
