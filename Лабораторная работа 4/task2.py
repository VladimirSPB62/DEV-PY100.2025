import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r', encoding="utf-8") as file:
        reader = [line for line in csv.DictReader(file)]

    with open(OUTPUT_FILENAME, 'w', encoding="utf-8") as output_file:
        json.dump(reader, output_file, indent=4)



if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME, encoding="utf-8") as output_f:
        for line in output_f:
            print(line, end="")
