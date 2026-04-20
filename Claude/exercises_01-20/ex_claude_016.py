# started using files

from pathlib import Path

DATA_FILE = Path(__file__).parent / "data16.txt"


def to_float(items, start):
    for i in range(start, len(items)):
        items[i] = float(items[i])
    return items

with open(DATA_FILE, "r") as file:
    lines = file.readlines()
    first_line = lines[0].split()

    to_float(first_line, 1)

    print(first_line)
