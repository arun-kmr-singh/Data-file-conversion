import csv
from xml.etree import ElementTree

tree = ElementTree.parse('data.xml')
root = tree.getroot()

numb = len(root.find("row"))
#print(numb)

data1 = open('aks.csv', 'w')
list_head=[]

csvwriter = csv.writer(data1)
count1 = 0
count = 0
cnt=0
cjki=0
for child in root.iter():
	if cjki >= 2 and cjki <= numb+2:
		if count1 < numb:
			list_head.append(child.tag)
			count1 += 1
		else:
			csvwriter.writerow(list_head)
			count1=0
			list_head.clear()
	cjki +=1
	
for att in root.iter():
	if cnt >= 2:
		if count < numb:
			list_head.append(att.text)
			count += 1
		#if count > numb:
		else:
			csvwriter.writerow(list_head)
			count=0
			list_head.clear()
	cnt +=1	
	
data1.close()