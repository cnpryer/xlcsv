import csv
import os
from io import BytesIO, StringIO
from pathlib import Path
from typing import BinaryIO, Optional, Union

from pylamine import get_sheet_data  # type: ignore

from xlcsv import utils
from xlcsv.error import FileExtensionException

# default .xlsx
DEFAULT_EXCEL_SHEET_NAME = "Sheet1"
DEFAULT_SHEET_INDEX = 0

# supported file extensions
EXCEL_FILE_EXTENSIONS = {".xlsx"}


def excel_to_csv_buffer(
    file_like: Union[str, BytesIO, Path, BinaryIO, bytes],
    sheet_index: Optional[int] = DEFAULT_SHEET_INDEX,
) -> StringIO:
    """Build a reset StringIO buffer of CSV data from Excel.

    Args:
        file_like (Union[str, BytesIO, Path, BinaryIO, bytes]):
            Path to a file or a file-like object. Objects with a
            ``read()`` method, such as a file handler
            (e.g. via builtin ``open`` function) or ``BytesIO``.
        sheet_index (Optional[int], optional): Position of sheet in book.
            Defaults to None.

    Returns:
        StringIO: Reset String IO buffer.
    """

    if isinstance(file_like, (str, Path)):
        file_like = utils.format_path(file_like)
        file_ext = os.path.splitext(file_like)[1]

        if file_ext not in EXCEL_FILE_EXTENSIONS:
            raise FileExtensionException("File extension not allowed.")

    # create book
    sheet_data = get_sheet_data(file_like, sheet_index)

    # write book to csv string io
    buffer = StringIO()
    writer = csv.writer(buffer, quoting=csv.QUOTE_ALL)
    for row in sheet_data:
        data = [val for val in row]
        writer.writerow(data)

    # reset buffer
    buffer.seek(0)

    return buffer
