bestand = open('/Users/Damian/Desktop/pe5_2.txt')
regels = bestand.readlines()
for regel in regels:
    regel = regel.strip()
    splitsing = regel.split(',')
    print(splitsing[1] + ' heeft kaartnummer:' + splitsing[0])