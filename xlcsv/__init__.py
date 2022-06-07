import csv
from io import StringIO

import openpyxl

__version__ = "0.1.0"


def csv_stringio_from_excel(
    filepath: str, sheet_name: str = "Sheet1"
) -> StringIO:
    book = openpyxl.load_workbook(filepath)
    sheet = book[sheet_name]

    output = StringIO()
    wr = csv.writer(output, quoting=csv.QUOTE_ALL)
    for row in sheet.iter_rows():
        lrow = []
        for cell in row:
            lrow.append(cell.value)
        wr.writerow(lrow)

    output.seek(0)

    return output
