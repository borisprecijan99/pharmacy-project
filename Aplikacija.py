from RegistracijaIPrijava import *

fajl = open("Podaci.txt", "a")
fajl.close()
lekovi = open("Lekovi.txt", "a")
lekovi.close()

def sortiranjePodataka():
    lista = []
    fajl = open("Podaci.txt", "r")
    for linija in fajl:
        ime, prezime, korIme, lozinka = linija[:-1].split("|")
        lista.append(linija)
    fajl.close()
    if(not lista):
        pass
    else:
        lista.sort()
        fajl = open("Podaci.txt", "w")
        fajl.close()
        fajl = open("Podaci.txt", "a")
        for linija in lista:
            fajl.write(linija)
        fajl.close()

def sortiranjeLekova():
    lista = []
    fajl = open("Lekovi.txt", "r")
    for linija in fajl:
        naziv, cena, namena, kolicina = linija[:-1].split("|")
        lista.append(linija)
    fajl.close()
    if(not lista):
        pass
    else:
        lista.sort()
        fajl = open("Lekovi.txt", "w")
        fajl.close()
        fajl = open("Lekovi.txt", "a")
        for linija in lista:
            fajl.write(linija)
        fajl.close()

def app():
    print("Dobrodosli\n")
    while(True):
        sortiranjePodataka()
        sortiranjeLekova()
        izbor = input("REGISTRACIJA / PRIJAVA / KRAJ: ")
        izbor = izbor.lower()
        while(not(izbor == "registracija" or izbor == "prijava" or izbor == "kraj")):
            izbor = input("REGISTRACIJA / PRIJAVA / KRAJ: ")
            izbor = izbor.lower()
        if(izbor == "registracija"):
            registracija()
        elif(izbor == "prijava"):
            prijava()
        else:
            exit()

app()
