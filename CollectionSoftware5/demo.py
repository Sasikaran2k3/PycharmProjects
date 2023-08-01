import csv


cs = open("Customer.txt","r")
custo = cs.read().split("\n")

for i in custo:
    print(i)
    c = open(i+".csv","r")
    read = csv.reader(c)
    data = [j for j in read]
    s = open(i + ".csv", "w")
    writer = csv.writer(s)
    for j in data:
        print(j)
        if j[1].isnumeric():
            print(j)
            writer.writerow([j[0],int(j[1])])

