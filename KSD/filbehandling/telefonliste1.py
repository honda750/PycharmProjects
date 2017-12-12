"""
    Telefonliste 1
        Dict lagres til fil med json format
"""
import json
import os

def cls():                              # Sletter skjerme
    os.system('cls' if os.name == 'nt' else 'clear')
    #print('hei')

def skrivFil(data, fil):                # Skrive til en fil (fra start, sletter gammelt innhold)
    with open(fil, 'w') as jsonFil:
        json.dump(data, jsonFil)        # Skrver data til fil på json format

def lesFil(fil):                        # Lese en fil med sjekk om fil finns
    try:
        with open(fil) as jsonFil:
            data = json.load(jsonFil)   # Leser data på json format fra fil som tilordnes variabel
    except FileNotFoundError:
        print('Kan ikke finne ', format(fil))   #   Skriver navn på fil som ikke kan finnes
    return data

def printTelefonListe(fil):                             # Skriver ut innhold i fil
    print('\nTelefonliste:')
    for (navn, tlf) in sorted(telefonListe.items()):    # Sortert på navn med nummer
        print('\t\t',navn,'\t:\t', tlf)

def nyPerson(liste):                            # Ny person
    print('\nNytt navn i listen:')
    nyttNavn = input('\tNavn  : ')
    nyttNummer = input('\tNummer: ')
    telefonListe[nyttNavn] = nyttNummer         # Legger nytt navn og nummer inn i liste
    skrivFil(liste, filNavn)                    # Skriver endring til fil
    cls()

def slettPerson(liste):                                 # Slett person
    slettNavn = input('Skriv navn som skal fjernes: ')
    finnsNavn = sjekkNavn(slettNavn, liste)             # Sjekker om navn finns
    if finnsNavn == True:
        del telefonListe[slettNavn]                     # Sletter navn og nummer i liste
        skrivFil(telefonListe, filNavn)                 # Skriver endring til fil
    else:
        print('Navnet finnes ikke i listen!')


def endreNummer(liste):                                 # Endre nummer
    navn = input('Hvem har nytt nummer? ')
    finnsNavn = sjekkNavn(navn, liste)             # Sjekker om navn finns
    if finnsNavn == True:
        nyttNummer = input('Nytt nummer: ')
        telefonListe[navn] = nyttNummer  # Legger nytt nummer inn i liste
        skrivFil(telefonListe, filNavn)  # Skriver endring til fil
    else:
        print('Navnet finnes ikke i listen!')


def sjekkNavn(innNavn, liste):                          # Sjekker om navn er i liste
    for (navn, tlf) in (liste.items()):
        if (navn == innNavn):
            return True


filNavn = 'telefonliste1.txt'
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

    cls()                                           # Sletter skjermen
    printTelefonListe(telefonListe)                 # Skriver innhold i fil
    svar = input(meny)

