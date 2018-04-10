stringvier = input('Geef een string van vier letters: ')



while len(stringvier) != 4:
    print(stringvier + ' heeft ' + str(len(stringvier)) + ' letters')
    stringvier = input('Geef een string van vier letters: ')
else:
    print('Inlezen van correcte string: '+ stringvier + ' is geslaagd')