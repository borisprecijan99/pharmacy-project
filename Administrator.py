def obavestenje():
    lek = {}
    sviLekovi = {}
    lekovi = open("lekovi.txt", "r")
    for linija in lekovi:
        naziv, cena, namena, kolicina = linija[:-1].split("|")
        if(int(kolicina) < 10):
            lek[naziv] = kolicina
        sviLekovi[naziv] = kolicina
    lekovi.close()
    if(lek):
        print("VAZNO OBAVESTENJE")
        print("Morate nabaviti sledece lekove!")
        for naziv, kolicina in lek.items():
            print("Naziv leka: " + naziv + "\t" + "Kolicina: " + kolicina)
    elif(not sviLekovi):
        print("VAZNO OBAVESTENJE")
        print("Baza lekova je prazna.")
    else:
        pass

def dodajKorisnika():
    kraj = False
    while(not kraj):
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
                print("Korisnicko ime " + korisnickoIme + " već postoji u bazi podataka.")
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
        unos = input("Zelite li da nastavite? (DA/NE): ")
        unos = unos.lower()
        while(not(unos == "da" or unos == "ne")):
            unos = input("Zelite li da nastavite? (DA/NE): ")
            unos = unos.lower()
        if(unos == "ne"):
            kraj = True
        else:
            continue

def kolikoJeProdato():
    lista = []
    recnik = {}
    kraj = False
    fajl = open("Racuni.txt", "a")
    fajl.close()
    fajl = open("Racuni.txt", "r")
    for linija in fajl:
        naziv, cena, kolicina = linija[:-1].split("|")
        if(naziv != ""):
            lista.append(linija)
            recnik[naziv] = kolicina
    fajl.close()
    while(not kraj):
        prodato = 0
        if(not lista):
            print("Jos nije nista prodato.")
            break
        else:
            unos = input("Unesite naziv leka: ")
            if(len(unos) == 0):
                continue
            unos = unos.upper()
            if(unos not in recnik.keys()):
                print("Lek " + unos + " jos uvek niko nije kupio.")
            else:
                for linija in lista:
                    naziv, kolicina, cena = linija[:-1].split("|")
                    if(naziv == unos):
                        prodato = prodato + int(kolicina)
                print("Prodato kutija leka " + unos + ": " + str(prodato))
        x = input("Zelite li da nastavite? (DA/NE): ")
        x = x.lower()
        while(not(x == "da" or x == "ne")):
            x = input("Zelite li da nastavite? (DA/NE): ")
            x = x.lower()
        if(x == "da"):
            continue
        else:
            kraj = True

def obrisiKorisnika():
    kraj = False
    while(not kraj):
        listaImena = []
        listaPrezimena = []
        listaKorImena = []
        listaLozinki = []
        fajl = open("Podaci.txt", "r")
        for linija in fajl:
            ime, prezime, korIme, lozinka = linija[:-1].split("|")
            listaImena.append(ime)
            listaPrezimena.append(prezime)
            listaKorImena.append(korIme)
            listaLozinki.append(lozinka)
        fajl.close()
        if(not listaKorImena):
            print("Nije registrovan nijedan korisnik.")
            break
        while(True):
            korIme = input("Unesite korisnicko ime: ")
            if(len(korIme) == 0):
                continue
            elif(korIme not in listaKorImena):
                print("Korisnicko ime " + korIme + " ne postoji u bazi podataka.")
                print("Pokusajte ponovo.")
                continue
            else:
                break
        fajl = open("Podaci.txt", "w")
        fajl.close()
        i = 0
        fajl = open("Podaci.txt", "a")
        for linija in listaImena:
            if(korIme != listaKorImena[i]):
                fajl.write(listaImena[i] + "|" + listaPrezimena[i] + "|" + listaKorImena[i] + "|" + listaLozinki[i] + "\n")
            i = i + 1
        fajl.close()
        unos = input("Zelite li da nastavite? (DA/NE): ")
        unos = unos.lower()
        while(not(unos == "da" or unos == "ne")):
            unos = input("Zelite li da nastavite? (DA/NE): ")
            unos = unos.lower()
        if(unos == "ne"):
            kraj = True
        else:
            pass

def dodajLekove():
    nazivi = []
    cene = []
    namene = []
    kolicine = []
    lekovi = open("Lekovi.txt", "r")
    for linija in lekovi:
        naziv, cena, namena, kolicina = linija[:-1].split("|")
        nazivi.append(naziv)
        cene.append(cena)
        namene.append(namena)
        kolicine.append(kolicina)
    lekovi.close()
    while(True):
        while(True):
            naziv = str(input("Unesite naziv leka: "))
            naziv = naziv.upper()
            if(len(naziv) == 0):
                continue
            else:
                break
        if(naziv in nazivi):
            while(True):
                try:
                    brKom = int(input("Unesite broj kutija: "))
                    while(not(brKom > 0)):
                        brKom = int(input("Unesite broj kutija: "))
                    break
                except ValueError:
                    print("Greska. Niste uneli ceo broj.")
            j = 0
            for element in nazivi:
                if(element == naziv):
                    kolicine[j] = str(int(kolicine[j]) + brKom)
                j = j + 1
            lekovi = open("Lekovi.txt", "w")
            lekovi.close()
            c = 0
            lekovi = open("Lekovi.txt", "a")
            for x in nazivi:
                lekovi.write(nazivi[c] + "|" + cene[c] + "|" + namene[c] + "|" + kolicine[c] + "\n")
                c = c + 1
            lekovi.close()
        else:
            while(True):
                try:
                    cena = int(input("Unesite cenu leka: "))
                    while(not(cena > 0)):
                        cena = int(input("Unesite cenu leka: "))
                    break
                except ValueError:
                    print("Greska. Niste uneli ceo broj.")
            while(True):
                namena = str(input("Unesite namenu leka: "))
                if(len(namena) == 0):
                    continue
                else:
                    break
            while(True):
                try:
                    brKom = int(input("Unesite broj kutija: "))
                    while(not (brKom > 0)):
                        brKom = int(input("Unesite broj kutija: "))
                    break
                except ValueError:
                    print("Greska. Niste uneli ceo broj.")
            lekovi = open("Lekovi.txt", "a")
            lekovi.write(naziv + "|" + str(cena) + "|" + namena + "|" + str(brKom) + "\n")
            lekovi.close()
            nazivi.append(naziv)
            cene.append(str(cena))
            namene.append(namena)
            kolicine.append(str(brKom))
        unos = str(input("Zelite li da nastavite? (DA/NE): "))
        unos = unos.lower()
        while(not(unos == "da" or unos == "ne")):
            unos = str(input("Zelite li da nastavite? (DA/NE): "))
            unos = unos.lower()
        if(unos == "da"):
            continue
        else:
            break

def stanje():
    lekKolicina = {}
    lekovi = open("Lekovi.txt", "r")
    for linija in lekovi:
        naziv, cena, namena, kolicina = linija[:-1].split("|")
        lekKolicina[naziv] = kolicina
    lekovi.close()
    if(not lekKolicina):
        print("Baza lekova je prazna.")
    else:
        for naziv, kolicina in lekKolicina.items():
            print("Naziv leka: " + naziv + "\t" + "Kolicina: " + kolicina)

def admin():
    odjava = False
    while(not odjava):
        print("\nIzaberite jednu od opcija:")
        print("1. Unos lekova u bazu podataka")
        print("2. Dodaj novog korisnika")
        print("3. Obrisi korisnika")
        print("4. Stanje")
        print("5. Kolicina prodatih lekova")
        print("6. ODJAVA")
        while(True):
            try:
                unos = int(input("Unesite opciju: "))
                while(not(unos >= 1 and unos <= 6)):
                    unos = int(input("Pokusajte ponovo: "))
                break
            except ValueError:
                print("Greska. Niste uneli broj.")
        if(unos == 1):
            dodajLekove()
        elif(unos == 2):
            dodajKorisnika()
        elif(unos == 3):
            obrisiKorisnika()
        elif(unos == 4):
            stanje()
        elif(unos == 5):
            kolikoJeProdato()
        else:
            odjava = True
