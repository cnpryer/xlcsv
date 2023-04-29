from io import StringIO
from pathlib import Path

import polars as pl
from xlcsv.io import to_csv_buffer


def test_polars_read_csv() -> None:
    filepath = Path(__file__).parent / "test.xlsx"

    buffers = (
        to_csv_buffer(filepath),
        to_csv_buffer(filepath, sheet_index=0),
    )

    for buffer in buffers:
        create_df(buffer)


def create_df(buffer: StringIO) -> None:
    df = pl.read_csv(buffer)
    assert not df.is_empty()
