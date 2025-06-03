import csv
from typing import Dict, List

header: int = 0
line_number_to_print: int = 1

EXPECTED_COLUMNS: List[str] = ['word', 'pos', 'definitions']

def get_column_indices(header: List[str], expected: List[str]) -> Dict[str, int]:
    missing = [col for col in expected if col not in header]
    if missing:
        raise ValueError(f"Missing expected columns: {', '.join(missing)}")
    return {col: header.index(col) for col in expected}

with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    header_names: List[str] = next(reader)
    print(header_names)
    col_indices: Dict[str, int] = get_column_indices(header_names, EXPECTED_COLUMNS)
    print(col_indices)
    for i, row in enumerate(reader, start=header):
        print(row[col_indices['definitions']])
