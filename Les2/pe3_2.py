leeftijd=eval(input('Geef je leeftijd:'))
paspoort=(input('Nederlands paspoort:'))
X = 'Ja'

if leeftijd > 18 and paspoort in X:
    print('Gefeliciteerd, je mag stemmen!')

else:
    print('Helaas, je mag niet stemmen!')