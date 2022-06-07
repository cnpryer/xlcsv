import polars as pl

import xlcsv


def test_polars_read_csv() -> None:
    filepath = "./tests/test.xlsx"
    buffer = xlcsv.csv_stringio_from_excel(filepath)
    df = pl.read_csv(buffer)

    assert not df.is_empty()
