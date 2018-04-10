bestand = open('/Users/Damian/Desktop/pe5_2.txt')
regels = bestand.readlines()
for regel in regels:
    regel = regel.strip()
    splitsing = regel.split(',')
print('Deze file telt ' + str(len(regels)) + ' regels.')
print('Het grootste kaartnummer is ' + str(max(splitsing)) + '.')