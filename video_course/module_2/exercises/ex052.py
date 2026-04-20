# Prime number check

while True:
    try:
        n = int(input("what is the number you want to check if it is prime? "))
        break
    except ValueError:
        print("must be an integer")

prime_count = 0
if n == 0 or n == 1:
    print("it is not a prime number")
else:
    for c in range(1, n+1):
        if n % c == 0:
            print(f"\033[1;32m{c}\033[m", end=" ")
            prime_count += 1
        else:
            print(c, end=" ")
    print()
    if prime_count > 2:
        print(f"it is not a prime number, it is divisible {prime_count} times")
    else:
        print(f"it is a prime number")
