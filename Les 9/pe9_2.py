import datetime
import csv

vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %Y")
import time
vandaag2 = time.strftime("%H:%M:%S", time.localtime())

bestand = 'inloggers.csv'

with open('inloggers.csv', 'w', newline='') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')
    writer.writerow(('datum', 'tijd', 'achternaam', 'voorletters', 'geboortedatum', 'email'))

    while True:
        naam = input("Wat is je achternaam? ")

        if naam == 'einde':
            break

        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")

        writer.writerow((s, vandaag2, naam, voorl, gbdatum, email))