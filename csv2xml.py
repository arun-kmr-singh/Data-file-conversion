import csv

csvFile = 'abcd.csv'
xmlFile = 'data.xml'

csvData = csv.reader(open(csvFile))
xmlData = open(xmlFile, 'w')

rowNum = 0
xmlData.write('<table>' + "\n")
for row in csvData:
    if rowNum == 0:
        tags = row
        # replace spaces w/ underscores in tag names
        for i in range(len(tags)):
            tags[i] = tags[i].replace(' ', '_')
    else: 
        xmlData.write('    <row>' + "\n")
        for i in range(len(tags)):
            xmlData.write('          ' + '<' + tags[i] + '>' \
                          + row[i] + '</' + tags[i] + '>' + "\n")
        xmlData.write('    </row>' + "\n")
            
    rowNum +=1

xmlData.write('</table>')
xmlData.close()
