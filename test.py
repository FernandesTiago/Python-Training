while True:
    try:
        number = input("What is the phone number? (13 digits): ").strip()
        if number.isdigit and len(number) == 13:
            number = list(number)
            number.insert(0, "+")
            number.insert(3, " ")
            number.insert(4, "(")
            number.insert(7, ")")
            number.insert(8, " ")
            number.insert(14, "-")
            number = "".join(number)
            print(number)
            break
        else:
            print("\nEnter the country code, area code and number all together!\n")
    except ValueError:
        print("\nEnter a valid value\n")
