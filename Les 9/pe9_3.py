import csv
lijst = []

with open('gamers.csv', 'r') as myCSVFile:

    reader = csv.reader(myCSVFile, delimiter=';')

    for row in reader:
        #maximaal = int(max(row[1]))
        lijst.append(row[2])

if row[2] == max(lijst):
    print('De hoogste score is: ' + max(lijst) + ' op ' + row[1] + ' behaald door ' + row[0])