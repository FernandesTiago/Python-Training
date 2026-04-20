# read, show message, ask if user wants to write more

from pathlib import Path

DATA_FILE = Path(__file__).parent / "data17.txt"


def write(mode):
    """Write to data17.txt — 'a' to append, 'w' to erase and rewrite."""
    while True:
        keep_going = input("Do you want to write something? (Y/N) (D) to delete: ").upper().strip()
        if keep_going == "N":
            print("No text added.")
            break
        elif keep_going == "Y":
            text = input("Enter your text: ")
            with open(DATA_FILE, mode) as file:
                file.write(text + "\n")
            with open(DATA_FILE, "r") as file:
                print("Text added!\n" + file.read())
            break
        elif keep_going == "D":
            with open(DATA_FILE, "w"):
                pass
            print("File emptied.")
            break
        else:
            print("Enter Y, N or D.")

try:
    with open(DATA_FILE, "r") as file:
        text = file.read()
    if text:
        print(text)
        write("a")
    else:
        print("File is empty.")
        write("w")
except FileNotFoundError:
    write("w")
