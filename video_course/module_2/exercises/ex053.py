# check if a word is a palindrome

while True:
    p = input("Write a word ").upper().replace(" ", "")
    if p.isnumeric() or p.isdigit() or p.find(".") != -1 or p == "":
        print("enter a phrase")
    else:
        break
pi = p[::-1]
if p == pi:
    print("it is a palindrome")
else:
    print("it is not a palindrome")
