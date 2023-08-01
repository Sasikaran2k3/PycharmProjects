import csv
import openpyxl

cs = open("Customer.txt","r")
custo = cs.read().split("\n")
for i in custo:
    print(i)
    #s = openpyxl.load_workbook(r"C:\Users\HP\PycharmProjects\CollectionSoftware3\%s.xlsx"%i)
    #p = s.active
    f = open("%s.csv"%i,'w')
    #writer = csv.writer(f)
    """for j in range(1,p.max_row+1):
        print(p["A%d"%j].value,type(p["A%d"%j].value))
        if p["A%d"%j].value is not None:
            print([str(p["A%d"%j].value).strip(),str(p["B%d"%j].value).strip()])
            writer.writerow([str(p["A%d"%j].value).strip(),str(p["B%d"%j].value).strip()])"""
    f.close()
    #s.close()
