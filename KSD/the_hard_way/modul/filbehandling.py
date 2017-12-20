"""
    FILBEHANDLING
    Lese ,skrive og legge til innhold i fil
"""
from minModul import printFil, leggTilData, overskrivData, dag, dato, tid

filNavn= 'filbehandling.txt'
print(f'Filen det leses og skrives mot er {filNavn}')
promt = dag()+' '+dato()+' '+tid()+' >>>'
print(promt)
meny = 's = skriv ut innhold   l = legge til data   o = overskriv innhold   x = avslutt program   t = Liste '
print('\n>>>   FILBEHANDLING   <<<\n')
svar = 1


while (svar != 'x'):

    if (svar == 's'):                               # Skriver ut innhold i fil
        printFil(filNavn)
    elif (svar == 'l'):                             # Legger til data i fil
        leggTilData(filNavn)
    elif (svar == 'o'):                             # Overskriver innhold i fil med nye data
        overskrivData(filNavn)

    print(meny)
    svar = input(promt)
print('>>>   Takk for nå   <<<')
quit()
