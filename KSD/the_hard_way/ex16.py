"""
    ex16
    Reading and writing files.
"""
#from sys import argv       #   tar filnavn som argument ved oppstart av prog (ex16 filnavn.txt)
#script, filename = argv    # script = path og filnavn (mac)

filNavn = 'ex16.txt'
print('\n>>>   TEKSTBEHANDLING   <<<\n')
print(f'Vi kommer til å slette filen {filNavn}.')
print('Hvis ikke trykk CTRL-C (^C).')
print('Ellers trykk RETURN')
input('?')

print('Åpner filen...')
target = open(filNavn, 'w')             # åpner for skriving (tømmer allt gammelt innhold ved skriving)

print('Truncating(fjerner innhold) i filen. Adjø data!')
target.truncate()

print('Nå vil jeg be deg skrive inn 3 linjer.')
linje1 = input('linje 1: ')
linje2 = input('linje 2: ')
linje3 = input('linje 3: ')

print('\nDisse blir nå skrevet til filen.\n')

target.write(linje1)
target.write('\n')
target.write(linje2)
target.write('\n')
target.write(linje3)
target.write('\n')

target = open(filNavn ,'r')                     # åpner for lesing
with target as txtFil :
    filInnhold = txtFil.readlines()
print(filInnhold)                               # skriver ut allt innhold i filen rått
print()
for data in filInnhold:                         # Tilordner innhold i fil til variabel
    print(data, end='')                         # Skriver ut innhold i filen

print('\nTil slutt lukker vi filen')
target.close()

print('adjø')