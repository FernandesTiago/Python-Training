# player list in a .txt file

from pathlib import Path

DATA_FILE = Path(__file__).parent / "data18.txt"


try:
    with open(DATA_FILE, "r") as file:
        content = file.read()
        if not content:
            print("Player list is empty")
        else:
            print(content)
except FileNotFoundError:
    with open(DATA_FILE, "a"):
        pass
    print("Player list is empty")

with open(DATA_FILE, "a") as file:
    name = input("What name do you want to add? ").title().strip()
    if name == "D":
        with open(DATA_FILE, "w"):
            pass
        exit()
    else:
        while True:
            try:
                score = int(input("What is their score: "))
                print(f"{name}, {score} was added!")
                file.write(f"{name}, {score}\n")
                break
            except ValueError:
                print("Enter an integer!")

with open(DATA_FILE, "r") as file:
    updated_list = file.readlines()
    sorted_list = []
    for i in range(0, len(updated_list)):
        player = updated_list[i].split()
        player[0] = player[0].replace(",", "")
        player[1] = int(player[1])
        sorted_list.append(player)
    sorted_list = sorted(sorted_list, key=lambda x: x[1], reverse=True)
    for entry in sorted_list:
        print(f"Player {entry[0]} scored: {entry[1]} points!!")
