import csv

with open('info.csv','r+') as file:
    reader = csv.reader(file)
    reader.next()
    info = reader.next()
    print(info[0])
    print(info[1])