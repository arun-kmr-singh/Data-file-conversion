import json
import csv

with open("try.json") as file:
    data = json.load(file)
	

data1 = open('data.csv', 'w')

csvwriter = csv.writer(data1)
count = 0
for emp in data:
      if count == 0:
             header = emp.keys()
             csvwriter.writerow(header)
             count += 1
      csvwriter.writerow(emp.values())

data1.close()