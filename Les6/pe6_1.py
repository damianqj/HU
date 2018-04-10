def seizoen(maand):
    if maand < 0:
        print('Vul een juiste maand in')
    elif maand < 4:
        print('Winter')
    elif maand < 7:
        print('Lente')
    elif maand < 10:
        print('Zomer')
    elif maand < 13:
        print('Herfst')
    else:
        print('Vul een juiste maand in')

seizoen(8)