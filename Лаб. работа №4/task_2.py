import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(csv_file, delimiter=',', line_terminator='\n') -> None:
    with open(csv_file, 'r', newline='') as f:
        read = csv.DictReader(f, delimiter=delimiter)
        data = list(read)
    json_data = json.dumps(data, indent=4)

    with open(OUTPUT_FILENAME, 'w') as output_f:
        output_f.write(json_data)


if __name__ == '__main__':
    # Нужно для проверки
        task(INPUT_FILENAME)

        with open(OUTPUT_FILENAME) as output_f:
            for line in output_f:
                print(line, end="")
