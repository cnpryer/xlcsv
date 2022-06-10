import os
import timeit
from typing import Callable

import pandas as pd  # type ignore
import polars as pl

from xlcsv import excel_to_csv_buffer

DF_N = 1_000_000
N_TESTS = 1_000
INSTANCE_DIRPATH = os.path.normpath("./instance")
EXCEL_FILEPATH = os.path.join(INSTANCE_DIRPATH, "df.xlsx")


if not os.path.exists(INSTANCE_DIRPATH):
    os.mkdir(INSTANCE_DIRPATH)


def create_df(size: int = DF_N) -> pl.DataFrame:
    df = pd.DataFrame({_: list(map(str, range(size))) for _ in "abcdefg"})

    return df


def bench_excel_file(fn: Callable, n_tests: int = N_TESTS) -> float:
    return timeit.timeit(lambda: fn(EXCEL_FILEPATH), number=n_tests)


if __name__ == "__main__":
    df, n = create_df(100), 1

    # test: (fn name, fn)
    tests = (
        # save large .xslx (pandas)
        ("pd.to_excel", df.to_excel),
        # read .xslx (pandas)
        ("pd.read_excel", pd.read_excel),
        # read .xlsx (polars native)
        ("pl.read_excel", pl.read_excel),
        # read .xslx (xlcsv)
        ("xlcsv.excel_to_csv_buffer", excel_to_csv_buffer),
    )

    for test in tests:
        res = bench_excel_file(fn=test[1], n_tests=n)
        print(test[0], res)
