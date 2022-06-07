import polars as pl

import xlcsv


def test_polars_read_csv() -> None:
    filepath = "./tests/test.xlsx"
    buffer = xlcsv.excel_to_csv_buffer(filepath)
    df = pl.read_csv(buffer)

    assert not df.is_empty()
