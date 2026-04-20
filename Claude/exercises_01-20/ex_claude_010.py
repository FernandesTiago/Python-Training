# discount def

def discounted_price(a, b=0):
    print(f"The product price is {a - a * b/100:.2f}")

# not using the input validations I usually use since I am just exploring def
price = int(input("what is the product price? "))
discount = int(input("what is the discount? (0%-100%) "))
discounted_price(price, discount)
