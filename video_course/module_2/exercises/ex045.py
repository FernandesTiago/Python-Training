# Rock Paper Scissors

from random import randint
from time import sleep

print("-=-" * 20)
print("                  WELCOME TO ROCK PAPER SCISSORS!!!!")
print("-=-" * 20)

# 1 Rock, 2 Paper, 3 Scissors

while True:
    cpu = randint(1, 3)
    while True:
        try:
            move = input("What is your move? (Rock, Paper, Scissors) ").strip().upper()
            if move == "ROCK" or move == "PAPER" or move == "SCISSORS":
                break
            else:
                print("Rock, paper or scissors? ")
        except ValueError:
            print("Rock, paper or scissors? ")

    print("CALCULATING...")
    sleep(3)

    if move == "ROCK" and cpu == 1 or move == "PAPER" and cpu == 2 or move == "SCISSORS" and cpu == 3:
        print("TIE!")
    elif move == "ROCK" and cpu == 2 or move == "PAPER" and cpu == 3 or move == "SCISSORS" and cpu == 1:
        print("you lost...")
    else:
        print("YOU WON!!!!!")
        break


# ADVANCED VERSION - study later

# 1. Use dictionary to map moves and results:
# options = {1: "ROCK", 2: "PAPER", 3: "SCISSORS"}
# cpu_move = options[randint(1, 3)]

# 2. Use dictionary to define who beats whom:
# beats = {"ROCK": "SCISSORS", "PAPER": "ROCK", "SCISSORS": "PAPER"}
# if beats[move] == cpu_move: print("YOU WON!")

# 3. Use function to validate input:
# def ask_move():
#     while True:
#         move = input("...").strip().upper()
#         if move in ["ROCK", "PAPER", "SCISSORS"]:
#             return move

# 4. Score counter:
# wins, losses, ties = 0, 0, 0

# 5. Ask if user wants to play again instead of stopping only on victory
