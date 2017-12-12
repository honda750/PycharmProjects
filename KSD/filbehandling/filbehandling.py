"""
    Filbehandling
"""

filNavn = 'fil1.txt'
#with open(filNavn, 'w') as filinnhold:      # Skrive til en fil (fra start, sletter gammelt innhold)
#    filinnhold.write('\nDette var gøy')

with open(filNavn, 'a') as filInnhold:      # Legge til innhold i en fil
    filInnhold.write('\nDette var også gøy')

with open(filNavn) as filInnhold:           # Skrive til en fil
    linjer = filInnhold.readlines()

for linje in linjer:                         # Skriver ut innhold i fil
    print(linje)