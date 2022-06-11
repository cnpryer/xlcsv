[![ci](https://github.com/cnpryer/xlcsv/workflows/ci/badge.svg)](https://github.com/cnpryer/xlcsv/actions)
[![PyPI Latest Release](https://img.shields.io/pypi/v/xlcsv.svg)](https://pypi.org/project/xlcsv/)

# xlcsv

A Python micropackage for consuming Excel as CSV.

Build CSV `StringIO` from Excel files.

```py
import xlcsv


buffer = xlcsv.excel_to_csv_buffer("my-file.xlsx")
```

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md).
