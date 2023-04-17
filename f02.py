from random import randint

szamok:list[int] = []

for x in range(20):
    rsz = randint(50, 150)
    szamok.append(rsz)

szamok.sort()
print(szamok)

osszeg:int = sum(szamok)
print(f'számok összege: {osszeg}')

atlag:int = osszeg / len(szamok)
print(f'számok átlaga: {atlag}')

szamlalo:int = 0
for szam in szamok:
    if szam % 10 == 0:
        szamlalo += 1
print(f'nullára végződő számok száma: {szamlalo} db')
