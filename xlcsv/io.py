import csv
from io import BytesIO, StringIO
from pathlib import Path
from typing import BinaryIO, Optional, Union

from openpyxl import load_workbook  # type: ignore

from xlcsv import utils


def excel_to_csv_buffer(
    file_like: Union[str, BytesIO, Path, BinaryIO, bytes],
    sheet_name: Optional[str] = "Sheet1",
) -> StringIO:
    """Build a reset StringIO buffer of CSV data from Excel.

    Args:
        file_like (Union[str, BytesIO, Path, BinaryIO, bytes]):
            Path to a file or a file-like object. Objects with a
            ``read()`` method, such as a file handler
            (e.g. via builtin ``open`` function) or ``BytesIO``.
        sheet_name (Optional[str], optional): Name of sheet to read.
            Defaults to "Sheet1".

    Returns:
        StringIO: Reset String IO buffer.
    """
    if isinstance(file_like, (str, Path)):
        file_like = utils.format_path(file_like)

    # create book
    book = load_workbook(
        file_like,
        read_only=True,
        data_only=True,
    )
    sheet = book[sheet_name]

    # write book to csv string io
    buffer = StringIO()
    writer = csv.writer(buffer, quoting=csv.QUOTE_ALL)
    for row in sheet.iter_rows():
        data = []
        for cell in row:
            data.append(cell.value)
        writer.writerow(data)

    # reset buffer
    buffer.seek(0)

    return buffer
