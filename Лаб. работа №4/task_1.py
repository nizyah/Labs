import json

json_file = 'input.json'
def task(json_file) -> float:
    with open(json_file, 'r') as file:
        data = json.load(file)

    sum_ = sum(item['score'] * item['weight'] for item in data)

    return round(sum_, 3)

print(task(json_file))
