# xlcsv

A Python micropackage for consuming Excel as CSV.

Build CSV `StringIO` from Excel files.

```py
import xlcsv


buffer = xlcsv.excel_to_csv_buffer("my-file.xlsx")
```
