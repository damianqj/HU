def ticker(filename):
    bestand = open('/Users/Damian/PycharmProjects/untitled2/Les7/tickersymbols.txt', 'r')
    inhoud = bestand.readlines()
    bestand.close()
    bedrijven = []

    for item in inhoud:
        item2 = item.split(':')
        bedrijven.append(item2)


    lijst = {
            bedrijven[0][0]:bedrijven[0][1],
            bedrijven[1][0]:bedrijven[1][1],
            bedrijven[2][0]:bedrijven[2][1],
            bedrijven[3][0]:bedrijven[3][1],
            bedrijven[4][0]:bedrijven[4][1],
            bedrijven[5][0]:bedrijven[5][1],
    }
   #print(lijst)
    return lijst






ticker('/Users/Damian/PycharmProjects/untitled2/Les7/tickersymbols.txt')

