import os
import timeit
from io import BytesIO, StringIO
from pathlib import Path
from typing import BinaryIO, Callable, Union

import pandas as pd  # type ignore
import polars as pl

from xlcsv import excel_to_csv_buffer

DF_N = 10_000
N_TESTS = 1_000
INSTANCE_DIRPATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "instance"
)
EXCEL_FILEPATH = os.path.join(INSTANCE_DIRPATH, "df.xlsx")


if not os.path.exists(INSTANCE_DIRPATH):
    os.mkdir(INSTANCE_DIRPATH)


def create_df(size: int = DF_N) -> pd.DataFrame:
    df = pd.DataFrame({_: list(map(str, range(size))) for _ in "abcdefg"})

    return df


def preproc(
    file_like: Union[BytesIO, BinaryIO, StringIO, str, Path]
) -> Union[BytesIO, BinaryIO, StringIO, str, Path]:
    if isinstance(file_like, (str, Path)):
        return file_like

    buffer = file_like
    buffer.seek(0)

    return buffer


def bench_excel_file(
    fn: Callable,
    file_like: Union[str, BytesIO, Path, BinaryIO, StringIO] = EXCEL_FILEPATH,
    n_tests: int = N_TESTS,
) -> float:
    return timeit.timeit(lambda: fn(preproc(file_like)), number=n_tests)


if __name__ == "__main__":
    # pandas DataFrame, number of tests to run
    df, n = create_df(), 10

    # test: (fn name, fn)
    excel_io_tests = (
        # save .xslx (pandas)
        ("pd.to_excel", df.to_excel),
        # read .xslx (pandas)
        ("pd.read_excel", pd.read_excel),
        # read .xlsx (polars native)
        ("pl.read_excel", pl.read_excel),
        # read .xslx (xlcsv)
        ("xlcsv.excel_to_csv_buffer", excel_to_csv_buffer),
    )

    # test: (fn name, fn, buffer fn)
    with_buffer_tests = (
        # read .xlsx as .csv from buffer (polars)
        ("pl.read_csv", pl.read_csv, excel_to_csv_buffer),
    )

    for name, fn in excel_io_tests:
        res = bench_excel_file(fn, n_tests=n)
        print(name, res)

    for name, fn, buff in with_buffer_tests:
        buffer = buff(EXCEL_FILEPATH)
        res = bench_excel_file(fn, file_like=buffer, n_tests=n)
        print(name, res)
