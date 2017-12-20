"""
    SKRIV OG LES FRA FIL
    Kun string eller binærfiler
"""

# Skriver til fil

file = open('filbehandling.txt','w')

file.write('hello World Linje 0\n')
file.write('hello World Linje 1\n')
file.write('hello World linje 2\n')
file.write('hello World linje 3\n')
file.write('hello World linje 4\n')

file.close()

print(file.name)    # Skriver filnavn

# Leser fra fil

file = open('filbehandling.txt','r')    # Skiver ut hele innholdet
print(file.read())

file = open('filbehandling.txt','r')    # Skriver ut 5 første tegn
print(file.read(5))

#file = open('filbehandling.txt','r')    # skriver ut første linje
print(file.readline())

#file = open('filbehandling.txt','r')    # skriver ut 3 første tegn
print(file.readline(3))

#file = open('filbehandling.txt','r')    # skriver ut alle linjer på liste format.
print(file.readlines())

#file = open('filbehandling.txt','r')    # skriver ut linje for linje
for line in file:
    print(line, end='')


# Skriv til fil
file.close()
file = open('filbehandling.txt','a')    # Legger til nye data
file.write('Dette er en ny linje.\n')
file.write('Dette er enda en ny linje.\n')

file = open('filbehandling.txt','r')    # Skiver ut hele innholdet
print(file.read())

file.close()