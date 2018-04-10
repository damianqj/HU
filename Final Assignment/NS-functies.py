def standaardprijs(afstandKM):
    korting = 0.6
    b = 15
    if afstandKM < 0:
        prijs = 0
    elif afstandKM > 50:
        prijs = b + (afstandKM * korting)
    else:
        prijs = 0.8 * afstandKM
    return prijs

def ritprijs(leeftijd, weekendrit, afstandKM):
    prijs = standaardprijs(afstandKM)
    if weekendrit == False:
        if leeftijd < 12 or leeftijd > 65:
            kortingsprijs = prijs * 0.7
        else:
            kortingsprijs = prijs
    else:
        if leeftijd < 12 or leeftijd > 65:
            kortingsprijs = prijs * 0.65
        else:
            kortingsprijs = prijs * 0.6
    return kortingsprijs

print(ritprijs(18, True, 110))