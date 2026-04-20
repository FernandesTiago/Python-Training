import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data19.json"


def load_data():
    """RETURNS DATA FROM JSON"""
    with open(DATA_FILE, "r") as file:
        data = json.load(file)
        return data

def save_data(data):
    """SAVES DATA () TO FILE"""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file)

def delete_data():
    """DELETES THE WHOLE LIST"""
    with open(DATA_FILE, "w"):
        pass

def display(txt):
    """PRINTS THE LIST IN AN ORGANIZED WAY"""
    text = sorted(txt, key=lambda x: x["score"], reverse=True)
    for i in range(0, len(text)):
        print(f"Name: {text[i]['name']:<10} Score: {text[i]['score']}")

leaderboard = [
    {"name": "Mocotó", "score": 2000},
    {"name": "Tiago", "score": 2500},
    {"name": "Mari", "score": 1750},
    {"name": "Juliana", "score": 3000}
]

while True:
    try:
        text = load_data()
        print("\nTournament table\n")
        display(text)
        break
    except (FileNotFoundError, json.JSONDecodeError):
        save_data(leaderboard)

while True:
    add = input("Do you want to add a new player? (Y/N/D) ").strip().title()
    if add == "Y":
        player = input("What is the player name? ").title().strip()
        while True:
            try:
                score = int(input("What is the score? "))
                break
            except ValueError:
                print("Enter an integer!")
        player_dict = {"name": player, "score": score}
        text.append(player_dict)
        print("\nTournament table\n")
        display(text)
        save_data(text)
        break
    elif add == "D":
        delete_data()
        break
    elif add == "N":
        print("Nothing added!")
        break
    else:
        print("Enter Y, N or D!!")
