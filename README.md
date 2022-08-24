[![ci](https://github.com/cnpryer/xlcsv/workflows/ci/badge.svg)](https://github.com/cnpryer/xlcsv/actions)
[![PyPI Latest Release](https://img.shields.io/pypi/v/xlcsv.svg)](https://pypi.org/project/xlcsv/)

# xlcsv

A Python micropackage for consuming Excel as CSV.

Build CSV `StringIO` from Excel files.

```py
import xlcsv

buffer = xlcsv.to_csv_buffer("my-file.xlsx")
```

Read Excel files without Excel using a `DataFrame` library.

```py
# ...

import pandas as pd

df = pd.read_csv(buffer)

import polars as pl

df = pl.read_csv(buffer)
```

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md).
