# bank loan to buy a house

house = float(input("What is the house price? R$"))
salary = float(input("what is your salary? R$"))
years = int(input("in how many years do you want to pay for the house? "))

installment = house / (years * 12)
max_balance = salary * 30 / 100

if installment < max_balance:
    print(f"you \033[32mcan \033[mfinance the house and must pay \033[30;42mR${installment:.2f}\033[m per installment.")
else:
    print(f"You \033[31mcannot \033[mfinance the house.")
    print(f"The installment value is \033[32mR${installment:.2f}\033[m and the maximum value you can pay is \033[32mR${max_balance:.2f}\033[m")
