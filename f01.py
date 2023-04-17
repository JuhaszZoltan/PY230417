#                      0          1         2         3        4
nevek:list[str] = ['Richárd', 'ferenc', 'Borbála', 'Judit', 'Ákos']
magassagok:list[int] = []

for nev in nevek:
    m:int = int(input(f'{nev} magassága (cm): '))
    magassagok.append(m)

osszeg:int = sum(magassagok)
elemszam:int = len(magassagok)
atlag:float = osszeg / elemszam

print(f'magasságok átlaga: {atlag} cm')


legnagyobb:int = max(magassagok)
print(f'legnagyobb magasság: {legnagyobb}')

hol:int = magassagok.index(legnagyobb)
print(f'ezen az indexen van ez a legnagyobb érték: {hol}')

print(f'tehát a legmagasabb barátom: {nevek[hol]}')

# nevek.sort()
# print('a nevek ABCrendben:')
# for nev in nevek:
#     print(nev)

for i in range(0, len(nevek) - 1):
    for j in range(i + 1, len(nevek)):
        if magassagok[i] > magassagok[j]:
            csm:int = magassagok[i]
            magassagok[i] = magassagok[j]
            magassagok[j] = csm
            csn:str = nevek[i]
            nevek[i] = nevek[j]
            nevek[j] = csn
print('rendezve magasságok szerint:')
for i in range(len(nevek)):
    print(f'{nevek[i]}: {magassagok[i]} cm')