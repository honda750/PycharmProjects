"""
    MODULER
"""
#!/usr/bin/python
#filnavn: minModul
""" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    GLOBALE VARIABLE   
"""
minKone = 'Karen'
pi = 3.14

# Test
def siHei(navn):
    print('Hei',navn,'dette er minModul som snakker')
    returData = 'Hei på deg!'
    return(returData)

""" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    Tid og Dato 
"""
from datetime import datetime as time

def dato():                                         # Dato, måned, år
    date = time.strftime(time.now(), '%d.%m.%Y')
    return date

def tidS():                                         # Time, minutt, sekund
    clock = time.strftime(time.now(), '%H:%M:%S')
    return clock

def tid():                                          # Time, minutt
    clock = time.strftime(time.now(), '%H:%M')
    return clock

def dag():                                          # Dag
    day = time.strftime(time.now(), '%A')
    if (day == 'Monday'):
        day = 'Mandag'
    elif (day == 'Tuesday'):
        day = 'Tirsdag'
    elif (day == 'Wednesday'):
        day = 'Onsdag'
    elif (day == 'Thursday'):
        day = 'Torsdag'
    elif (day == 'Friday'):
        day = 'Fredag'
    elif (day == 'Saturday'):
        day = 'Lørdag'
    elif (day == 'Sunday'):
        day = 'Søndag'
    return day

def dag3():                                         # Dag 3 bokstaver
    day = time.strftime(time.now(), '%A')
    if (day == 'Monday'):
        day = 'Man'
    elif (day == 'Tuesday'):
        day = 'Tir'
    elif (day == 'Wednesday'):
        day = 'Ons'
    elif (day == 'Thursday'):
        day = 'Tor'
    elif (day == 'Friday'):
        day = 'Fre'
    elif (day == 'Saturday'):
        day = 'Lør'
    elif (day == 'Sunday'):
        day = 'Søn'
    return day

""" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    SEND EMAIL
    Med emne og innhold
"""
def send_email(emne, innhold, til_addr):            # Sender en email.
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    fra_addr = 'ksdraege@gmail.com'
    passord = 'passord'  # mcxx
    msg = MIMEMultipart()
    msg['From'] = fra_addr
    msg['To'] = til_addr
    msg['Subject'] = emne
    msg.attach(MIMEText(innhold, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    text = msg.as_string()
    server.login(fra_addr,passord)
    text = msg.as_string()
    server.sendmail(fra_addr,til_addr,text)
    server.quit()

#st5!'
#tekst = '-' #('Denne email er sendt fra fra ett python program.')
#til = 'ksdraege@gmail.com'
#send_email(emne,tekst,til)

""" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    FILBEHANDLING
"""
# Lese ,skrive og legge til innhold i fil >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def skrivFil(data, fil):        # Skrive til en fil (fra start, sletter gammelt innhold)
    sjekkFil(fil)               # Sjekker om fil finns?
    with open(fil, 'w') as txtFil:
        txtFil.write(data)

def leggTilFil(data, fil):      # Legge til innhold i en fil
    sjekkFil(fil)               # Sjekker om fil finns?
    with open(fil, 'a') as txtFil:
        txtFil.write(data)

def lesFil(fil):                # Leser fil, returnerer innhold
    sjekkFil(fil)               # Sjekker om fil finns?
    with open(fil) as txtFil:
        data = txtFil.readlines()
    return (data)

def sjekkFil(fil):              # Sjekker om fil finns? (alle typer fil)
    try:
        open(fil)
    except:
        FileNotFoundError
        print('\n>>>   Kan ikke finne filen', format(fil), '   <<<')  # Skriver feilmelding med filnavn
        quit()

# Behandler innhold i fil >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def printFil(fil):              # Skriver ut innhold i fil
    for filInnhold in lesFil(fil):
        print(filInnhold)

def leggTilData(fil):
    leggTil = input('Skriv inn tillegg i fil: ')
    # print(leggTil)
    leggTilFil(leggTil, fil)

def overskrivData(fil):
    nyttInnhold = input('Skriv inn nye data (sletter gamle): ')
    skrivFil(nyttInnhold, fil)

# Skriv og les (dump og load) json fil) >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

import json

def skrivFilJson(filInnhold, fil):          # Skrive til en fil (fra start, sletter gammelt innhold)
    sjekkFil(fil)                           # Sjekker om fil finns?
    with open(fil, 'w') as jsonFil:
        json.dump(filInnhold, jsonFil)      # Skriver data til fil på json format

def lesFilJson(fil):                        # Lese en fil
    sjekkFil(fil)                           # Sjekker om fil finns?
    with open(fil) as jsonFil:
        filInnhold = json.load(jsonFil)     # Leser data på json format fra fil som tilordnes variabel
    return filInnhold

# Navn og data behandles som 'dictionares' i *.json fil >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def printListe(fil):                                    # Skriver ut innhold i fil
    filInnhold = lesFilJson(fil)
    for (navn, data) in sorted(filInnhold.items()):     # Sortert på navn med nummer
        tabLengde = 13 - (len(navn))                    # Variabel tabulator lengde
        print('\t',navn,' ' * tabLengde,':\t', data)

def nyPerson(fil):                                      # Ny person
    filInnhold = lesFilJson(fil)
    print('\nNytt navn i listen:')
    nyttNavn = input('\tNavn  : ')
    nyttNummer = input('\tData: ')
    filInnhold[nyttNavn] = nyttNummer                   # Legger nytt navn og nummer inn i liste
    skrivFilJson(filInnhold, fil)                           # Skriver endring til fil

def slettPerson(fil):                                   # Slett person
    filInnhold = lesFilJson(fil)
    finnsNavn = False
    while finnsNavn != True:
        slettNavn = input('Skriv navn som skal fjernes: ')
        finnsNavn = sjekkNavn(slettNavn, filInnhold)    # Sjekker om navn finns
        if finnsNavn == True:
            del filInnhold[slettNavn]                   # Sletter navn og nummer i liste
            skrivFilJson(filInnhold, fil)                   # Skriver endring til fil

def endreData(fil):                                     # Endre nummer
    filInnhold = lesFilJson(fil)
    finnsNavn = False
    while finnsNavn != True:
        navn = input('Person med nye data? ')
        finnsNavn = sjekkNavn(navn, filInnhold)         # Sjekker om navn finns
        if finnsNavn == True:
            nyeInndata = input('Data: ')
            filInnhold[navn] = nyeInndata               # Legger nytt nummer inn i liste
            skrivFilJson(filInnhold, fil)                   # Skriver endring til fil

def sjekkNavn(innNavn, filInnhold):                     # Sjekker om navn er i liste
    for (navn, data) in (filInnhold.items()):
        if (navn == innNavn):
            return True
    print('>>>   Navnet finnes ikke i listen!   <<<')
    return False