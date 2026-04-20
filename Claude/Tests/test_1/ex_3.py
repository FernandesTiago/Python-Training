# You have this list of dictionaries:
stock = [
    {"name": "Pen", "qty": 5},
    {"name": "Notebook", "qty": 12},
    {"name": "Eraser", "qty": 3}
]
# Sort the list by quantity (smallest to largest) and print
# each item like this:
# Pen - 5 units



stock = sorted(stock, key=lambda x: x["qty"], reverse=False)
# Honestly I got confused with lambda here, the x[1] I used in another exercise didn't work
# I had to look it up without a new fundamental I saw in the last exercise and only used once, and I saw that in this case
# I can use the name of the dict key


for i in range(0, len(stock)):
    print(f"{stock[i]['name']} - {stock[i]['qty']} Units")
