from openpyxl import load_workbook

wb = load_workbook("jeya.xlsx")

point = wb.active

point.delete_rows(2)

wb.save("jeya.xlsx")

