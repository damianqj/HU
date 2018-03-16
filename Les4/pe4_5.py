def kwadraten_som(grondgetallen):
    'deze functie verwacht een list'
    som = 0
    for getal in grondgetallen:
        if getal > 0:
            som = som + getal**2

    return som

print(kwadraten_som([1,4,7,-45,-6,22]))