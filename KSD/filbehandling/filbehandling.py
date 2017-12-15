"""
    FILBEHANDLING
    Lese ,skrive og legge til innhold i fil
"""
def skrivFil(data, fil):                    # Skrive til en fil (fra start, sletter gammelt innhold)
    sjekkFil(fil)                           # Sjekker om fil finns?
    with open(fil, 'w') as txtFil:
        txtFil.write(data)

def leggTilFil(data, fil):                  # Legge til innhold i en fil
    sjekkFil(fil)                           # Sjekker om fil finns?
    with open(fil, 'a') as txtFil:
        txtFil.write(data)

def lesFil(fil):                            # Leser fil, returnerer innhold
    sjekkFil(fil)                           # Sjekker om fil finns?
    with open(fil) as txtFil:
        data = txtFil.readlines()
    return(data)

def sjekkFil(fil):                          # Sjekker om fil finns?
    try:
        open(fil)
    except:
        FileNotFoundError
        print('\n>>>   Kan ikke finne filen:', format(fil),'   <<<') # Feilmelding med filnavn
        quit()
        
def printFil(fil):                                # Skriver ut innhold i fil
    for filInnhold in lesFil(fil):
        print(filInnhold)

def leggTilData(fil):
    leggTil = input('Skriv inn tillegg i fil: ')
    print(leggTil)
    leggTilFil(leggTil, fil)

def overskrivData(fil):
    nyttInnhold = input('Skriv inn nye data (sletter gamle): ')
    skrivFil(nyttInnhold, fil)

filNavn= 'filbehandling.txt'
meny = 's = skriv ut innhold   l = legge til data   o = overskriv innhold   x = avslutt program   t = Liste '
print('\n>>>   FILBEHANDLING   <<<\n')
print(meny)
svar = 1

while (svar != 'x'):

    if (svar == 's'):                               # Skriver ut innhold i fil
        printFil(filNavn)
    elif (svar == 'l'):                             # Legger til data i fil
        leggTilData(filNavn)
    elif (svar == 'o'):                             # Overskriver innhold i fil med nye data
        overskrivData(filNavn)
    elif (svar == 'x'):                             # Avslutter program
        print('\n>>>   Takk for nå   <<<')
        quit()
    svar = input('>>> ')

