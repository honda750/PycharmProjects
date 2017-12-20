"""
    TELEFONLISTE 1
    Navn og nummer lagres som 'dictionares' i *.json fil
    Menystyrt med feil sjekk.
"""
import json
import os

def skrivFil(data, fil):                    # Skrive til en fil (fra start, sletter gammelt innhold)
    sjekkFil(fil)                           # Sjekker om fil finns?
    with open(fil, 'w') as jsonFil:
        json.dump(data, jsonFil)            # Skriver data til fil på json format

def lesFil(fil):                            # Lese en fil
    sjekkFil(fil)                           # Sjekker om fil finns?
    with open(fil) as jsonFil:
        data = json.load(jsonFil)   # Leser data på json format fra fil som tilordnes variabel
    return data

def sjekkFil(fil):                                      # Sjekker om fil finns?
        try:
            open(fil)
        except:
            FileNotFoundError
            print('\n>>>   Kan ikke finne filen', format(fil),'   <<<') # Skriver feilmelding med filnavn
            quit()

def printTelefonListe(fil):                             # Skriver ut innhold i fil
    print('\nTelefonliste:\n')
    for (navn, tlf) in sorted(telefonListe.items()):    # Sortert på navn med nummer
        tabLengde = 13 - (len(navn))                    # Variabel tabulator lengde
        print('\t',navn,' ' * tabLengde,':\t', tlf)

def nyPerson(liste):                                    # Ny person
    print('\nNytt navn i listen:')
    nyttNavn = input('\tNavn  : ')
    nyttNummer = input('\tNummer: ')
    telefonListe[nyttNavn] = nyttNummer                 # Legger nytt navn og nummer inn i liste
    skrivFil(liste, filNavn)                            # Skriver endring til fil

def slettPerson(liste):                                     # Slett person
    finnsNavn = False
    while finnsNavn != True:
        slettNavn = input('Skriv navn som skal fjernes: ')
        finnsNavn = sjekkNavn(slettNavn, liste)             # Sjekker om navn finns
        if finnsNavn == True:
            del telefonListe[slettNavn]                     # Sletter navn og nummer i liste
            skrivFil(telefonListe, filNavn)                 # Skriver endring til fil
        print('>>>   Navnet finnes ikke i listen!   <<<')

def endreNummer(liste):                                     # Endre nummer
    finnsNavn = False
    while finnsNavn != True:
        navn = input('Hvem har nytt nummer? ')
        finnsNavn = sjekkNavn(navn, liste)                  # Sjekker om navn finns
        if finnsNavn == True:
            nyttNummer = input('Nytt nummer: ')
            telefonListe[navn] = nyttNummer                 # Legger nytt nummer inn i liste
            skrivFil(telefonListe, filNavn)                 # Skriver endring til fil
        print('>>>   Navnet finnes ikke i listen!   <<<')

def sjekkNavn(innNavn, liste):                              # Sjekker om navn er i liste
    for (navn, tlf) in (liste.items()):
        if (navn == innNavn):
            return True

filNavn = 'telefonListe.json'
telefonListe = lesFil(filNavn)                      # Leser fil og tilordner innhold til variabel
meny = '\nn = ny person   e = endre nummer   s = slett person   x = avslutt program '
svar = 1

while (svar != 'x'):

    if (svar == 'n'):                               # Nytt navn og nummer
        nyPerson(telefonListe)
    elif (svar == 's'):                             # Slette post
        slettPerson(telefonListe)
    elif (svar == 'e'):                             # Endre post
        endreNummer(telefonListe)
    elif (svar == 'x'):                             # Avslutte
        print('\n*** Takk for nå ***')
        quit()

    printTelefonListe(telefonListe)                 # Skriver innhold i fil
    print(meny)
    svar = input('>>> ')

