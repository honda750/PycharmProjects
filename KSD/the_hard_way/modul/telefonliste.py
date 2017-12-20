"""
    TELEFONLISTE bruker mondulen minModul.py
    Navn og nummer lagres som 'dictionares' i *.json fil
    Menystyrt med feil sjekk.
"""
from minModul import skrivFil, lesFil, printListe, nyPerson, slettPerson, endreData, dag, dato, tid
filNavn = 'telefonListe.json'
meny = '\nn = ny person   e = endre nummer   s = slett person   x = avslutt program '
svar = 1
print(dag(), dato(), tid())

while (svar != 'x'):

    if (svar == 'n'):                               # Nytt navn og nummer
        nyPerson(filNavn)
    elif (svar == 's'):                             # Slette post
        slettPerson(filNavn)
    elif (svar == 'e'):                             # Endre post
        endreData(filNavn)
    elif (svar == 'x'):                             # Avslutte
        print('\n*** Takk for nå ***')

    print('\t Navn\t\t\t\t Telefon\n')
    printListe(filNavn)                             # Skriver innhold i fil
    print(meny)
    svar = input('>>> ')

print('>>>   Takk for nå   <<<')
quit()

