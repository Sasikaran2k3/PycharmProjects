import openpyxl
from openpyxl import load_workbook, Workbook

l = ['sasi','karan','jeya','sivakumar']

wb = Workbook()
for i in l:
    wb.save("%s.xlsx" % i)

