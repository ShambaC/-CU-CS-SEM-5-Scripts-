import csv

with open('a.csv', 'w', newline='') as wf :
    writer = csv.writer(wf)
    writer.writerow(["Name", "ID", "Age"])
    writer.writerow(["ABC", 24, 12])
    writer.writerow(["DEF", 42, 21])

with open('a.csv', 'r') as rf :
    reader = csv.reader(rf)
    for row in reader :
        print(row)