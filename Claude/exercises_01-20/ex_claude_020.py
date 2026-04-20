# try except else

from pathlib import Path

DATA_FILE = Path(__file__).parent / "data20.txt"


def read_number_from_file(path):
    try:
        file = open(path, "r")
        try:
            number = float(file.readline())
        except ValueError:
            print("Content is not a number")
        else:
            return number
        finally:
            file.close()
    except FileNotFoundError:
        print("File not found")

result = read_number_from_file(DATA_FILE)
if result:
    print(result)
