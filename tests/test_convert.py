import polars as pl

import xlcsv


def test_polars_read_csv() -> None:
    filepath = "./tests/test.xlsx"
    df = pl.read_csv(xlcsv.csv_stringio_from_excel(filepath))

    assert not df.is_empty()
