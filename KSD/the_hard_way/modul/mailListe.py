from minModul import skrivFilJson, lesFilJson, printListe, nyPerson, slettPerson, endreData  # Funksjoner

filNavn = 'mailListe.json'
#mailListe = lesFil(filNavn)                      # Leser fil og tilordner innhold til variabel
meny = '\nn = ny person   e = endre mailaddresse   s = slett person   x = avslutt program '
svar = 1

while (svar != 'x'):

    if (svar == 'n'):                               # Nytt navn og nummer
        nyPerson(filNavn)
    elif (svar == 's'):                             # Slette post
        slettPerson(filNavn)
    elif (svar == 'e'):                             # Endre post
        endreData(filNavn)

    print('\t Navn\t\t\t\t Email\n')
    printListe(filNavn)                             # Skriver innhold i fil
    print(meny)
    svar = input('>>> ')

print('>>>   Takk for nå   <<< ')
quit()


