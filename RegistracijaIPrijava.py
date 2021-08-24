from Administrator import *
from Korisnik import *

def registracija():
    while(True):
        ime = input("Unesite ime: ")
        if(len(ime) == 0):
            continue
        else:
            break
    while(True):
        prezime = input("Unesite prezime: ")
        if(len(prezime) == 0):
            continue
        else:
            break
    fajl = open("Podaci.txt", "r")
    lista = []
    for linija in fajl:
        i, p, ki, l = linija[:-1].split("|")
        lista.append(ki)
    fajl.close()
    while(True):
        korisnickoIme = input("Unesite korisnicko ime: ")
        if(len(korisnickoIme) == 0):
            continue
        elif(korisnickoIme not in lista and korisnickoIme != "admin"):
            break
        else:
            print("Korisnicko ime " + korisnickoIme + " vec postoji.")
            print("Pokusajte ponovo.")
            continue
    while(True):
        lozinka = input("Unesite lozinku: ")
        if(len(lozinka) == 0):
            continue
        else:
            break
    fajl = open("Podaci.txt", "a")
    fajl.write(ime + "|" + prezime + "|" + korisnickoIme + "|" + lozinka + "\n")
    fajl.close()
    print("Uspesno ste se registrovali, " + korisnickoIme + ".")

def prijava():
    lista = {"admin":"admin"}
    fajl = open("Podaci.txt", "r")
    for linija in fajl:
        i, p, ki, l = linija[:-1].split("|")
        lista[ki] = l
    fajl.close()
    while(True):
        korisnickoIme = input("Unesite korisnicko ime: ")
        if(len(korisnickoIme) == 0):
            continue
        elif(korisnickoIme not in lista.keys()):
            print("Korisnicko ime " + korisnickoIme + " ne postoji u bazi podataka.")
            print("Pokusajte ponovo.")
            continue
        elif(korisnickoIme in lista.keys()):
            break
    while(True):
        lozinka = input("Unesite lozinku: ")
        if(len(lozinka) == 0):
            continue
        elif(lista[korisnickoIme] == lozinka):
            break
        else:
            print("Pokusajte ponovo.")
            continue
    print("Uspesno ste se prijavili, " + korisnickoIme + ".")
    if(korisnickoIme == "admin" and lozinka == "admin"):
        obavestenje()
        admin()
    else:
        korisnik(korisnickoIme)
