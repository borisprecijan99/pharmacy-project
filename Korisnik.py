from datetime import *
from random import randint


def kupiLek(kIme):
    racun = 0
    nazCene = {}
    nazNam = {}
    nazKol = {}
    lekovi = open("Lekovi.txt", "r")
    for linija in lekovi:
        naziv, cena, namena, kolicina = linija[:-1].split("|")
        nazCene[naziv] = cena
        nazNam[naziv] = namena
        nazKol[naziv] = kolicina
    lekovi.close()
    kraj = False
    while(not kraj):
        if(not nazKol):
            print("Baza lekova je prazna.")
            break
        else:
            naziv = input("Unesite naziv leka: ")
            if(len(naziv) == 0):
                continue
            naziv = naziv.upper()
            if(naziv in nazKol.keys()):
                if(int(nazKol[naziv]) == 0):
                    print("Leka " + naziv + " nema na stanju.")
                else:
                    while(True):
                        try:
                            br = int(input("Unesite broj kutija: "))
                            while(not (br > 0)):
                                br = int(input("Unesite broj kutija: "))
                            break
                        except ValueError:
                            print("Greska. Niste uneli ceo broj.")
                    if(br <= int(nazKol[naziv])):
                        for naz, kol in nazKol.items():
                            if(naz == naziv):
                                nazKol[naziv] = str(int(nazKol[naziv]) - br)
                        racun = racun + br * int(nazCene[naziv])
                        racuni = open("Racuni.txt", "a")
                        zaduzenje = int(nazCene[naziv]) * br
                        racuni.write(naziv + "|" + str(br) + "|" + str(zaduzenje) + "\n")
                        racuni.close()
                        lekovi = open("Lekovi.txt", "w")
                        lekovi.close()
                        lekovi = open("Lekovi.txt", "a")
                        for n, c in nazCene.items():
                            lekovi.write(n + "|" + c + "|" + nazNam[n] + "|" + nazKol[n] + "\n")
                        lekovi.close()
                    else:
                        print("Mozete uzeti samo " + nazKol[naziv] + " kutija.")
                        while(True):
                            try:
                                br = int(input("Koliko kutija zelite?: "))
                                while(not (br > 0 and br <= int(nazKol[naziv]))):
                                    br = int(input("Koliko kutija zelite?: "))
                                break
                            except ValueError:
                                print("Greska. Niste uneli ceo broj.")
                        for naz, kol in nazKol.items():
                            if(naz == naziv):
                                nazKol[naziv] = str(int(nazKol[naziv]) - br)
                        racun = racun + br * int(nazCene[naziv])
                        racuni = open("Racuni.txt", "a")
                        zaduzenje = int(nazCene[naziv]) * br
                        racuni.write(naziv + "|" + str(br) + "|" + str(zaduzenje) + "\n")
                        racuni.close()
                        lekovi = open("Lekovi.txt", "w")
                        lekovi.close()
                        lekovi = open("Lekovi.txt", "a")
                        for n, c in nazCene.items():
                            lekovi.write(n + "|" + c + "|" + nazNam[n] + "|" + nazKol[n] + "\n")
                        lekovi.close()
            else:
                print("Ovaj lek ne postoji u bazi lekova.")
        unos = str(input("Zelite li da nastavite? (DA/NE): "))
        unos = unos.lower()
        while(not(unos == "da" or unos == "ne")):
            unos = str(input("Zelite li da nastavite? (DA/NE): "))
            unos = unos.lower()
        if(unos == "da"):
            pass
        else:
            datum, vreme = str(datetime.now()).split(" ")
            datum = str(datum)
            god, mesec, dan = datum.split("-")
            vreme = str(vreme)
            h, m, s = vreme.split(":")
            racuni = open("Racuni.txt", "a")
            if(racun > 1500):
                racuni.write("||" + kIme + ", Vas racun sa popustom od 5% iznosi " + str(0.95 * racun) + " dinara.\n")
            else:
                racuni.write("||" + kIme + ", Vas racun iznosi " + str(racun) + " dinara.\n")
            racuni.write("||Datum i vreme:\t" + dan + "." + mesec + "." + god + ".\t" + h + ":" + m + "\n")
            racuni.write("||" + 60 * "_" + "\n")
            racuni.close()
            kraj = True
    if(racun == 0):
        print("Niste nista kupili.")
    elif(racun > 1500):
        print("Vas racun sa popustom od 5% iznosi " + str(0.95 * racun) + " dinara.")
    else:
        print("Vas racun iznosi " + str(racun) + " dinara.")

def infoOLeku():
    lekoviLista = {}
    lekovi = open("Lekovi.txt", "r")
    for linija in lekovi:
        lek, cena, namena, kol = linija[:-1].split("|")
        lekoviLista[lek] = namena
    lekovi.close()
    while(True):
        if(not lekoviLista):
            print("Baza lekova je prazna.")
            break
        unos = str(input("Unesite lek za koji zelite da dobijete informacije: "))
        unos = unos.upper()
        if(len(unos) == 0):
            continue
        for naziv in lekoviLista.keys():
            if(unos == naziv):
                print("Namena leka " + unos + ": " + lekoviLista[naziv])
        if(unos not in lekoviLista.keys()):
            print("Lek " + unos + " se ne nalazi u bazi lekova.")
        nastavi = input("Zelite li da nastavite? (DA/NE): ")
        nastavi = nastavi.lower()
        while(not(nastavi == "da" or nastavi == "ne")):
            nastavi = input("Zelite li da nastavite? (DA/NE): ")
            nastavi = nastavi.lower()
        if(nastavi == "da"):
            continue
        else:
            break

def izmeriPritisak():
    a = randint(70, 150)
    b = randint(50, 100)
    if(a < b):
        izmeriPritisak()
    else:
        print("Vas pritisak: " + str(a) + "/" + str(b))

def korisnik(korIme):
    odjava = False
    while(not odjava):
        print("\n1. Kupovina leka")
        print("2. Informacije o leku")
        print("3. Merenje pritiska")
        print("4. ODJAVA")
        while(True):
            try:
                x = int(input("Izaberite opciju: "))
                while(not (x >= 1 and x <= 4)):
                    x = int(input("Izaberite opciju: "))
                break
            except ValueError:
                print("Greska. Niste uneli ceo broj.")
        if(x == 1):
            kupiLek(korIme)
        elif(x == 2):
            infoOLeku()
        elif(x == 3):
            izmeriPritisak()
        else:
            odjava = True
