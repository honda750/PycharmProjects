#!/usr/bin/python
# Filename: minModul_Demo.py


"""
import minModul
ksd = minModul

ksd.siHei('Kurt')
print('Versjon', ksd.versjon)                           # Variabel fra modul
print('Dette er en variabel fra minModul: ',ksd.svar)   # Variabel fra modul
print('Dette er returdata: ', ksd.siHei('Karen'))
print()

print(dato())
print(ksd.tidS())
print(ksd.tid())
print(ksd.dag())
print(ksd.dag3())
print(ksd.dag(), ksd.dato(), ksd.tidS())
print(ksd.dag3(), ksd.dato(), ksd.tid())
"""
# ELLER henter bare de funsjoner og varable som trengs.
#"""
from minModul import siHei, dato, tidS, tid, dag, dag3, svar, versjon   # Funksjoner og Variable

siHei('Kurt')
print('Versjon', versjon)                              # Variabel fra modul
print('Dette er en variabel fra minModul: ', svar)     # Variabel fra modul
print('Dette er returdata: ', siHei('Karen'))
print()

print(dato())
print(tidS())
print(tid())
print(dag())
print(dag3())
print(dag(), dato(), tidS())
print(dag3(), dato(), tid())

#"""
emne = 'Test5!'
tekst = '-' #('Denne email er sendt fra fra ett python program.')
til = 'ksdraege@gmail.com'
send_email(emne,tekst,til)