import csv

header: int = 0
line_number_to_print: int = 1

with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for i, row in enumerate(reader, start=header):
        if i == line_number_to_print - 1:
            print(row)
            break
