# xlcsv

A Python micropackage for consuming Excel as CSV.

Build CSV `StringIO` from Excel files.

```py
import xlcsv


stringio = xlcsv.csv_stringio_from_excel("your-file.xslx", sheet_name="sheet_name")
```
