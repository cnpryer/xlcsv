[![tests](https://github.com/cnpryer/xlcsv/actions/workflows/ci.yaml/badge.svg)](https://github.com/cnpryer/xlcsv/actions/workflows/ci.yaml)
[![pypi-release](https://img.shields.io/pypi/v/xlcsv.svg)](https://pypi.org/project/xlcsv/)

# xlcsv

A Python micropackage for consuming Excel as CSV.

Build CSV `StringIO` from Excel files.

```zsh
pip install xlcsv
```

Note: `xlcsv` was used prior to `polars`' excel reader for loading Excel files into DataFrames.

```py
import polars as pl

from xlcsv import to_csv_buffer

buffer = to_csv_buffer("my-file.xlsx")
df = pl.read_csv(buffer)
```
