def convert(celsius):
    fahrenheit = ((celsius * 1.8) + 32)
    return fahrenheit

for i in range(-30, 50, 10):
    print('{:3}{:10}'.format(i, ((i * 1.8) + 32)))