from io import StringIO

import polars as pl

from xlcsv.io import excel_to_csv_buffer


def create_df(buffer: StringIO) -> None:
    df = pl.read_csv(buffer)
    assert not df.is_empty()


def test_polars_read_csv() -> None:
    filepath = "./tests/test.xlsx"

    buffer = excel_to_csv_buffer(filepath)
    create_df(buffer)

    buffer = excel_to_csv_buffer(filepath, sheet_name="Sheet1")
    create_df(buffer)

    buffer = excel_to_csv_buffer(filepath, sheet_index=0)
    create_df(buffer)
