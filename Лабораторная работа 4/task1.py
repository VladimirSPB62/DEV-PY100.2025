import json


def task() -> float:
    filename = "input.json"
    with open(filename, encoding="utf-8") as f:
        python_obj = json.load(f)

    sum_values = sum([item["score"] * item["weight"] for item in python_obj])
    return round(sum_values, 3)


print(task())
