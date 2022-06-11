from io import StringIO

import polars as pl

from xlcsv.io import excel_to_csv_buffer


def create_df(buffer: StringIO) -> None:
    df = pl.read_csv(buffer)
    assert not df.is_empty()


def test_polars_read_csv() -> None:
    filepath = "./tests/test.xlsx"

    buffers = (
        excel_to_csv_buffer(filepath),
        excel_to_csv_buffer(filepath, sheet_index=0),
    )

    for buffer in buffers:
        create_df(buffer)
