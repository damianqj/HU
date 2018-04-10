bestand = open('hardlopers.txt', 'w')
import datetime
vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %Y")
import time
vandaag2 = time.strftime("%H:%M:%S", time.localtime())
naam = input('Voer naam in:')

print(s + ', ' + vandaag2 +', ' + naam)