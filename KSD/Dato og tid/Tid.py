"""
    Tid og Dato
"""
from datetime import datetime as time

def dato():                                         # Dato, måned, år
    date = time.strftime(time.now(), '%d.%m.%Y')
    return date

def tidS():                                          # Time, minutt, sekund
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

def dag3():                                          # Dag 3 bokstaver
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


print(dato())
print(tidS())
print(tid())
print(dag())
print(dag3())
print(dag(), dato(), tidS())
print(dag3(), dato(), tid())