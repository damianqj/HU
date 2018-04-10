bedrag = 4356

try:
    straantal = input('Hoeveel personen gaan mee op reis? ')
    intaantal = int(straantal)
    bedragpp = bedrag / intaantal


    if bedragpp < 0:
        print('Alleen positieve getallen invoeren.')
    else:
        print(bedragpp)


except ZeroDivisionError:
    print('Delen door nul kan niet.')

except:
    print('Alleen getallen invoeren van 0 t/m 9')