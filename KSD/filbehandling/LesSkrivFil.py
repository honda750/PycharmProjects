"""
    LesSkrivFil
"""
filNavn = 'LesSkrivFil.txt'

# Oppretter ny fil, sletter gammel hvis finns og skriver inn tekst >>>>>>>>>>>
# tekst starter her med linjeskift.
tekst = '''
Programmering er morsomt
Når arbeidet er gjort
hvis du ønsker at arbeidet ditt også er kjekt:
   bruk Python!
'''
f = open(filNavn, 'w')              # Åpne fil for skriving
f.write(tekst)                      # Skriver tekst til fil
f.close()                           # Lukker fil

# Skriver tekst2 som tillegg til fil >>>>>>>>>>>>>>>>>>>>>>>>>>>>
tekst2 = '''Dette er tillegstekst
som er lagt til. 
'''
f = open(filNavn, 'a')              # Åpne fil for å legge til
f.write(tekst2)
f.close()



# Leser fil og tilorndner innhold til variabel >>>>>>>>>>>>>>>>>>>>>>>>>>>>
with open(filNavn) as txtFil:       # Åpner fil for lesing
    filInnhold = txtFil.read()      # Innhold i fil leses og tilordnes variabel

# Skriver innhold i fil som tillegg i fil >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
with open(filNavn,'a') as txtFil:   # Åpner fil for skriving (legge til)
    txtFil.write(filInnhold)        # Skriver filinnhold til (legger til) fil.

# Skriver ut allt innhold i fil >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
f = open(filNavn)                   # Åpne for lesing
while True:
    linje = f.readline()
    if len(linje) == 0:         # Tom linje indikerer EOF (uten linjeskift \n)
        break

    print(linje, end='')            # Skriver linje for linje
f.close()                           # Lukker fil
