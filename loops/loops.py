ciudades = ['Lima', 'Iquique', 'Santiago', 'Los Ángeles', 'Guayaquil']
for ciudad in ciudades:
    if ciudad[0] == 'L':
        continue
    print(ciudad)

for ciudad in ciudades:
    if ciudad == 'Santiago':
        break
    print(ciudad)
