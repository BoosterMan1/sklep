import json
import inspect
import sys
import os


# magazyn = [
#     {
#         "id": 1,
#         "nazwa": "mleko",
#         "cena": 4.5,
#         "kategoria": "nabiał",
#         "ilosc": 10
#     },
#     {
#         "id": 2,
#         "nazwa": "sól",
#         "cena": 2.5,
#         "kategoria": "przyprawy",
#         "ilosc": 10
#     },
#     {
#         "id": 3,
#         "nazwa": "kawa",
#         "cena": 14.99,
#         "kategoria": "napoje",
#         "ilosc": 15
#     },
#     {
#         "id": 4,
#         "nazwa": "herbata",
#         "cena": 8.5,
#         "kategoria": "napoje",
#         "ilosc": 20
#     },
#     {
#         "id": 5,
#         "nazwa": "cukier",
#         "cena": 4.2,
#         "kategoria": "produkty sypkie",
#         "ilosc": 25
#     },
#     {
#         "id": 6,
#         "nazwa": "mąka pszenna",
#         "cena": 3.8,
#         "kategoria": "produkty sypkie",
#         "ilosc": 30
#     },
#     {
#         "id": 7,
#         "nazwa": "mąka ziemniaczana",
#         "cena": 5.2,
#         "kategoria": "produkty sypkie",
#         "ilosc": 12
#     },
#     {
#         "id": 8,
#         "nazwa": "ryż",
#         "cena": 6.5,
#         "kategoria": "produkty sypkie",
#         "ilosc": 18
#     },
#     {
#         "id": 9,
#         "nazwa": "kasza gryczana",
#         "cena": 7.4,
#         "kategoria": "produkty sypkie",
#         "ilosc": 14
#     },
#     {
#         "id": 10,
#         "nazwa": "makaron spaghetti",
#         "cena": 5.9,
#         "kategoria": "makarony",
#         "ilosc": 22
#     },
#     {
#         "id": 11,
#         "nazwa": "makaron penne",
#         "cena": 5.5,
#         "kategoria": "makarony",
#         "ilosc": 17
#     },
#     {
#         "id": 12,
#         "nazwa": "płatki owsiane",
#         "cena": 6.8,
#         "kategoria": "śniadaniowe",
#         "ilosc": 16
#     },
#     {
#         "id": 13,
#         "nazwa": "musli",
#         "cena": 11.5,
#         "kategoria": "śniadaniowe",
#         "ilosc": 9
#     },
#     {
#         "id": 14,
#         "nazwa": "jogurt naturalny",
#         "cena": 3.2,
#         "kategoria": "nabiał",
#         "ilosc": 24
#     },
#     {
#         "id": 15,
#         "nazwa": "jogurt truskawkowy",
#         "cena": 3.5,
#         "kategoria": "nabiał",
#         "ilosc": 19
#     },
#     {
#         "id": 16,
#         "nazwa": "ser żółty",
#         "cena": 18.9,
#         "kategoria": "nabiał",
#         "ilosc": 8
#     },
#     {
#         "id": 17,
#         "nazwa": "twarożek",
#         "cena": 5.8,
#         "kategoria": "nabiał",
#         "ilosc": 13
#     },
#     {
#         "id": 18,
#         "nazwa": "masło",
#         "cena": 8.99,
#         "kategoria": "nabiał",
#         "ilosc": 20
#     },
#     {
#         "id": 19,
#         "nazwa": "śmietana",
#         "cena": 4.7,
#         "kategoria": "nabiał",
#         "ilosc": 15
#     },
#     {
#         "id": 20,
#         "nazwa": "jajka",
#         "cena": 12.5,
#         "kategoria": "nabiał",
#         "ilosc": 18
#     },
#     {
#         "id": 21,
#         "nazwa": "chleb pszenny",
#         "cena": 5.5,
#         "kategoria": "pieczywo",
#         "ilosc": 14
#     },
#     {
#         "id": 22,
#         "nazwa": "chleb razowy",
#         "cena": 7.2,
#         "kategoria": "pieczywo",
#         "ilosc": 11
#     },
#     {
#         "id": 23,
#         "nazwa": "bułka",
#         "cena": 1.2,
#         "kategoria": "pieczywo",
#         "ilosc": 45
#     },
#     {
#         "id": 24,
#         "nazwa": "bagietka",
#         "cena": 4.5,
#         "kategoria": "pieczywo",
#         "ilosc": 16
#     },
#     {
#         "id": 25,
#         "nazwa": "rogalik",
#         "cena": 3.8,
#         "kategoria": "pieczywo",
#         "ilosc": 12
#     },
#     {
#         "id": 26,
#         "nazwa": "szynka",
#         "cena": 22.5,
#         "kategoria": "wędliny",
#         "ilosc": 7
#     },
#     {
#         "id": 27,
#         "nazwa": "kiełbasa",
#         "cena": 19.9,
#         "kategoria": "wędliny",
#         "ilosc": 9
#     },
#     {
#         "id": 28,
#         "nazwa": "parówki",
#         "cena": 12.8,
#         "kategoria": "wędliny",
#         "ilosc": 13
#     },
#     {
#         "id": 29,
#         "nazwa": "salami",
#         "cena": 24.5,
#         "kategoria": "wędliny",
#         "ilosc": 6
#     },
#     {
#         "id": 30,
#         "nazwa": "pierś z kurczaka",
#         "cena": 23.9,
#         "kategoria": "mięso",
#         "ilosc": 8
#     },
#     {
#         "id": 31,
#         "nazwa": "wołowina",
#         "cena": 42.5,
#         "kategoria": "mięso",
#         "ilosc": 5
#     },
#     {
#         "id": 32,
#         "nazwa": "schab",
#         "cena": 25.9,
#         "kategoria": "mięso",
#         "ilosc": 7
#     },
#     {
#         "id": 33,
#         "nazwa": "mielone mięso",
#         "cena": 19.5,
#         "kategoria": "mięso",
#         "ilosc": 10
#     },
#     {
#         "id": 34,
#         "nazwa": "łosoś",
#         "cena": 39.9,
#         "kategoria": "ryby",
#         "ilosc": 6
#     },
#     {
#         "id": 35,
#         "nazwa": "makrela",
#         "cena": 17.5,
#         "kategoria": "ryby",
#         "ilosc": 8
#     },
#     {
#         "id": 36,
#         "nazwa": "tuńczyk",
#         "cena": 9.9,
#         "kategoria": "ryby",
#         "ilosc": 14
#     },
#     {
#         "id": 37,
#         "nazwa": "marchew",
#         "cena": 3.9,
#         "kategoria": "warzywa",
#         "ilosc": 25
#     },
#     {
#         "id": 38,
#         "nazwa": "ziemniaki",
#         "cena": 4.5,
#         "kategoria": "warzywa",
#         "ilosc": 30
#     },
#     {
#         "id": 39,
#         "nazwa": "cebula",
#         "cena": 3.5,
#         "kategoria": "warzywa",
#         "ilosc": 28
#     },
#     {
#         "id": 40,
#         "nazwa": "pomidor",
#         "cena": 8.9,
#         "kategoria": "warzywa",
#         "ilosc": 20
#     },
#     {
#         "id": 41,
#         "nazwa": "ogórek",
#         "cena": 6.9,
#         "kategoria": "warzywa",
#         "ilosc": 18
#     },
#     {
#         "id": 42,
#         "nazwa": "papryka czerwona",
#         "cena": 9.5,
#         "kategoria": "warzywa",
#         "ilosc": 16
#     },
#     {
#         "id": 43,
#         "nazwa": "brokuł",
#         "cena": 7.5,
#         "kategoria": "warzywa",
#         "ilosc": 10
#     },
#     {
#         "id": 44,
#         "nazwa": "jabłka",
#         "cena": 5.9,
#         "kategoria": "owoce",
#         "ilosc": 24
#     },
#     {
#         "id": 45,
#         "nazwa": "banany",
#         "cena": 6.5,
#         "kategoria": "owoce",
#         "ilosc": 22
#     },
#     {
#         "id": 46,
#         "nazwa": "pomarańcze",
#         "cena": 7.9,
#         "kategoria": "owoce",
#         "ilosc": 18
#     },
#     {
#         "id": 47,
#         "nazwa": "mandarynki",
#         "cena": 8.5,
#         "kategoria": "owoce",
#         "ilosc": 15
#     },
#     {
#         "id": 48,
#         "nazwa": "gruszki",
#         "cena": 9.2,
#         "kategoria": "owoce",
#         "ilosc": 13
#     },
#     {
#         "id": 49,
#         "nazwa": "winogrona",
#         "cena": 12.9,
#         "kategoria": "owoce",
#         "ilosc": 11
#     },
#     {
#         "id": 50,
#         "nazwa": "truskawki",
#         "cena": 14.5,
#         "kategoria": "owoce",
#         "ilosc": 8
#     },
#     {
#         "id": 51,
#         "nazwa": "borówki",
#         "cena": 16.9,
#         "kategoria": "owoce",
#         "ilosc": 7
#     },
#     {
#         "id": 52,
#         "nazwa": "sok pomarańczowy",
#         "cena": 7.5,
#         "kategoria": "napoje",
#         "ilosc": 20
#     },
#     {
#         "id": 53,
#         "nazwa": "sok jabłkowy",
#         "cena": 6.9,
#         "kategoria": "napoje",
#         "ilosc": 18
#     },
#     {
#         "id": 54,
#         "nazwa": "woda mineralna",
#         "cena": 2.5,
#         "kategoria": "napoje",
#         "ilosc": 50
#     },
#     {
#         "id": 55,
#         "nazwa": "woda gazowana",
#         "cena": 2.3,
#         "kategoria": "napoje",
#         "ilosc": 42
#     },
#     {
#         "id": 56,
#         "nazwa": "cola",
#         "cena": 7.5,
#         "kategoria": "napoje",
#         "ilosc": 25
#     },
#     {
#         "id": 57,
#         "nazwa": "lemoniada",
#         "cena": 6.5,
#         "kategoria": "napoje",
#         "ilosc": 14
#     },
#     {
#         "id": 58,
#         "nazwa": "kakao",
#         "cena": 9.8,
#         "kategoria": "napoje",
#         "ilosc": 12
#     },
#     {
#         "id": 59,
#         "nazwa": "pieprz",
#         "cena": 4.5,
#         "kategoria": "przyprawy",
#         "ilosc": 20
#     },
#     {
#         "id": 60,
#         "nazwa": "papryka słodka",
#         "cena": 3.9,
#         "kategoria": "przyprawy",
#         "ilosc": 17
#     },
#     {
#         "id": 61,
#         "nazwa": "curry",
#         "cena": 5.5,
#         "kategoria": "przyprawy",
#         "ilosc": 11
#     },
#     {
#         "id": 62,
#         "nazwa": "bazylia",
#         "cena": 4.2,
#         "kategoria": "przyprawy",
#         "ilosc": 13
#     },
#     {
#         "id": 63,
#         "nazwa": "oregano",
#         "cena": 4.2,
#         "kategoria": "przyprawy",
#         "ilosc": 15
#     },
#     {
#         "id": 64,
#         "nazwa": "cynamon",
#         "cena": 5.8,
#         "kategoria": "przyprawy",
#         "ilosc": 9
#     },
#     {
#         "id": 65,
#         "nazwa": "czosnek",
#         "cena": 3.5,
#         "kategoria": "warzywa",
#         "ilosc": 20
#     },
#     {
#         "id": 66,
#         "nazwa": "ketchup",
#         "cena": 7.9,
#         "kategoria": "sosy",
#         "ilosc": 16
#     },
#     {
#         "id": 67,
#         "nazwa": "majonez",
#         "cena": 9.5,
#         "kategoria": "sosy",
#         "ilosc": 12
#     },
#     {
#         "id": 68,
#         "nazwa": "musztarda",
#         "cena": 5.5,
#         "kategoria": "sosy",
#         "ilosc": 14
#     },
#     {
#         "id": 69,
#         "nazwa": "sos czosnkowy",
#         "cena": 8.5,
#         "kategoria": "sosy",
#         "ilosc": 9
#     },
#     {
#         "id": 70,
#         "nazwa": "czekolada mleczna",
#         "cena": 6.5,
#         "kategoria": "słodycze",
#         "ilosc": 20
#     },
#     {
#         "id": 71,
#         "nazwa": "czekolada gorzka",
#         "cena": 7.5,
#         "kategoria": "słodycze",
#         "ilosc": 15
#     },
#     {
#         "id": 72,
#         "nazwa": "baton",
#         "cena": 3.5,
#         "kategoria": "słodycze",
#         "ilosc": 35
#     },
#     {
#         "id": 73,
#         "nazwa": "żelki",
#         "cena": 5.9,
#         "kategoria": "słodycze",
#         "ilosc": 18
#     },
#     {
#         "id": 74,
#         "nazwa": "ciastka czekoladowe",
#         "cena": 7.9,
#         "kategoria": "słodycze",
#         "ilosc": 14
#     },
#     {
#         "id": 75,
#         "nazwa": "chipsy",
#         "cena": 8.5,
#         "kategoria": "przekąski",
#         "ilosc": 21
#     },
#     {
#         "id": 76,
#         "nazwa": "paluszki",
#         "cena": 4.9,
#         "kategoria": "przekąski",
#         "ilosc": 25
#     },
#     {
#         "id": 77,
#         "nazwa": "orzeszki ziemne",
#         "cena": 7.5,
#         "kategoria": "przekąski",
#         "ilosc": 16
#     },
#     {
#         "id": 78,
#         "nazwa": "popcorn",
#         "cena": 5.5,
#         "kategoria": "przekąski",
#         "ilosc": 13
#     },
#     {
#         "id": 79,
#         "nazwa": "krakersy",
#         "cena": 6.5,
#         "kategoria": "przekąski",
#         "ilosc": 17
#     },
#     {
#         "id": 80,
#         "nazwa": "dżem truskawkowy",
#         "cena": 9.5,
#         "kategoria": "przetwory",
#         "ilosc": 12
#     },
#     {
#         "id": 81,
#         "nazwa": "dżem malinowy",
#         "cena": 10.5,
#         "kategoria": "przetwory",
#         "ilosc": 8
#     },
#     {
#         "id": 82,
#         "nazwa": "miód",
#         "cena": 18.5,
#         "kategoria": "przetwory",
#         "ilosc": 7
#     },
#     {
#         "id": 83,
#         "nazwa": "ogórki konserwowe",
#         "cena": 8.9,
#         "kategoria": "przetwory",
#         "ilosc": 10
#     },
#     {
#         "id": 84,
#         "nazwa": "kukurydza konserwowa",
#         "cena": 5.9,
#         "kategoria": "konserwy",
#         "ilosc": 15
#     },
#     {
#         "id": 85,
#         "nazwa": "fasola konserwowa",
#         "cena": 5.5,
#         "kategoria": "konserwy",
#         "ilosc": 13
#     },
#     {
#         "id": 86,
#         "nazwa": "groszek konserwowy",
#         "cena": 5.2,
#         "kategoria": "konserwy",
#         "ilosc": 14
#     },
#     {
#         "id": 87,
#         "nazwa": "tuńczyk w puszce",
#         "cena": 8.9,
#         "kategoria": "konserwy",
#         "ilosc": 11
#     },
#     {
#         "id": 88,
#         "nazwa": "papier toaletowy",
#         "cena": 18.9,
#         "kategoria": "higiena",
#         "ilosc": 20
#     },
#     {
#         "id": 89,
#         "nazwa": "ręczniki papierowe",
#         "cena": 9.9,
#         "kategoria": "higiena",
#         "ilosc": 18
#     },
#     {
#         "id": 90,
#         "nazwa": "mydło",
#         "cena": 4.5,
#         "kategoria": "higiena",
#         "ilosc": 25
#     },
#     {
#         "id": 91,
#         "nazwa": "szampon",
#         "cena": 12.5,
#         "kategoria": "higiena",
#         "ilosc": 14
#     },
#     {
#         "id": 92,
#         "nazwa": "pasta do zębów",
#         "cena": 9.5,
#         "kategoria": "higiena",
#         "ilosc": 17
#     },
#     {
#         "id": 93,
#         "nazwa": "płyn do naczyń",
#         "cena": 8.5,
#         "kategoria": "chemia",
#         "ilosc": 16
#     },
#     {
#         "id": 94,
#         "nazwa": "proszek do prania",
#         "cena": 24.9,
#         "kategoria": "chemia",
#         "ilosc": 9
#     },
#     {
#         "id": 95,
#         "nazwa": "płyn do szyb",
#         "cena": 7.9,
#         "kategoria": "chemia",
#         "ilosc": 11
#     },
#     {
#         "id": 96,
#         "nazwa": "gąbki kuchenne",
#         "cena": 5.5,
#         "kategoria": "chemia",
#         "ilosc": 22
#     },
#     {
#         "id": 97,
#         "nazwa": "worki na śmieci",
#         "cena": 8.9,
#         "kategoria": "domowe",
#         "ilosc": 19
#     },
#     {
#         "id": 98,
#         "nazwa": "folia aluminiowa",
#         "cena": 6.5,
#         "kategoria": "domowe",
#         "ilosc": 12
#     },
#     {
#         "id": 99,
#         "nazwa": "papier do pieczenia",
#         "cena": 5.9,
#         "kategoria": "domowe",
#         "ilosc": 14
#     },
#     {
#         "id": 100,
#         "nazwa": "baterie AA",
#         "cena": 12.9,
#         "kategoria": "elektronika",
#         "ilosc": 10
#     },
#     {
#         "id": 101,
#         "nazwa": "żarówka LED",
#         "cena": 15.5,
#         "kategoria": "elektronika",
#         "ilosc": 8
#     },
#     {
#         "id": 102,
#         "nazwa": "Fiolka z dżumą płucną",
#         "cena": 37000,
#         "kategoria": "ciekawa kategoria",
#         "ilosc": 53
#     },
#     {
#         "id": 103,
#         "nazwa": "Wścieklizna w strzykawce",
#         "cena": 40000,
#         "kategoria": "ciekawa kategoria",
#         "ilosc": 11
#     },
#     {
#         "id": 104,
#         "nazwa": "Lampa konfiskowana dżinowi",
#         "cena": 37000,
#         "kategoria": "ciekawa kategoria",
#         "ilosc": 1
#     },
#     {
#         "id": 105,
#         "nazwa": "Robotyczna replika córki Elona Muska",
#         "cena": 67000,
#         "kategoria": "ciekawa kategoria",
#         "ilosc": 80
#     },
#     {
#         "id": 106,
#         "nazwa": "Rakieta atomowa RS-28",
#         "cena": 100000000,
#         "kategoria": "ciekawa kategoria",
#         "ilosc": 4
#     },
#     {
#         "id": 107,
#         "nazwa": "Przyrodzenie Adolfa Hitlera",
#         "cena": 70000,
#         "kategoria": "ciekawa kategoria",
#         "ilosc": 1
#     },
#     {
#         "id": 108,
#         "nazwa": "Lewe jądro Adolfa Hitlera",
#         "cena": 15000,
#         "kategoria": "ciekawa kategoria",
#         "ilosc": 1
#     },
#     {
#         "id": 109,
#         "nazwa": "Prawe jądro Adolfa Hitlera",
#         "cena": 16000,
#         "kategoria": "ciekawa kategoria",
#         "ilosc": 1
#     },
#     {
#         "id": 110,
#         "nazwa": "Niezidentyfikowana broń biologiczna",
#         "cena": 1000000,
#         "kategoria": "ciekawa kategoria",
#         "ilosc": 1
#     },
#     {
#         "id": 111,
#         "nazwa": "Największy koszmar Karola Nawrockiego",
#         "cena": 7640.99,
#         "kategoria": "ciekawa kategoria",
#         "ilosc": 3
#     },
#     {
#         "id": 112,
#         "nazwa": "Czarna dziura",
#         "cena": 4,
#         "kategoria": "ciekawa kategoria",
#         "ilosc": 19
#     },
#     {
#         "id": 113,
#         "nazwa": "Universumsuntergangswaffe",
#         "cena": 8735000000,
#         "kategoria": "piekło i apokalipsa",
#         "ilosc": 1
#     },
#     {
#         "id": 114,
#         "nazwa": "Palec szatana",
#         "cena": 666000000,
#         "kategoria": "piekło i apokalipsa",
#         "ilosc": 20
#     },
#     {
#         "id": 115,
#         "nazwa": "Izraelska międzyplanetarna rakieta przeciwcywilna (Elimunuje całą ludność cywilną na planecie)",
#         "cena": 35090000000,
#         "kategoria": "piekło i apokalipsa",
#         "ilosc": 67
#     }
# ]



# Tu należy podać ścieżkę do swojego magazynu, lub odkomentować listę magazyn powyżej
sciezkaDoMagazynu = "twoja ścieżka"

saldoFirmy = 0.0

with open(sciezkaDoMagazynu, "r", encoding="utf-8") as plik:
    magazyn = json.load(plik)


class Produkt:
    def __init__(self, nazwa, cena, kategoria):
        self.nazwa = nazwa
        self.cena = cena
        self.kategoria = kategoria

def zapisz():
    dane_do_zapisu = [
    {"nazwa": p["nazwa"], "cena": p["cena"], "kategoria": p["kategoria"], "ilosc": p["ilosc"]}
    for p in magazyn
    ]
    with open(sciezkaDoMagazynu, "w", encoding="utf-8") as plik:
        json.dump(dane_do_zapisu, plik, ensure_ascii=False, indent=4)

    sciezka = os.path.abspath("magazyn.json")
    print(f'Zapisano do pliku "magazyn.json", ścieżka: "{sciezka}"')

def odczytaj():
    with open(sciezkaDoMagazynu, "r", encoding="utf-8") as plik:
        magazyn = json.load(plik)

    sciezka = os.path.abspath("magazyn.json")
    print(f"Pomyślnie wczytano z pliku {sciezka}.\nLiczba przedmiotów: {len(magazyn)}")

def pokazFunkcje():
    plik = sys.modules[__name__]
    print("Dostępne komendy:\n")

    for nazwa, obiekt in inspect.getmembers(plik, inspect.isfunction):
        if nazwa != "pokazFunkcje":
            print(f"> {nazwa}")


def lista():
    try:
        najwiekszaCena = 0
        for produkt in magazyn:
            if produkt["cena"] > najwiekszaCena:
                najwiekszaCena = produkt["cena"]

        print(f"Koszt najdroższego produktu: {najwiekszaCena}zł")
        maxCena = input('Wprowadź budżet bądź naciśnij "ENTER"\n')
        if maxCena == "":
            maxCena = float(najwiekszaCena)
        else:
            maxCena = float(maxCena)
        print(f"Wprowadzony budżet: {maxCena}zł")
        print("\n")

        print("Nasze kategorie:\n")
        kategorie = []
        licznik = 0
        for produkt in magazyn:
            kategoria = produkt["kategoria"]
            if kategoria in kategorie:
                continue
            licznik += 1
            kategorie.append(kategoria)
            print(f"> {licznik}. {kategoria}")

        wybranaKategoria = input('Wybierz numer kategorii, lub naciśnij "ENTER"\n')
        if wybranaKategoria == "":
            kategoria = "brak"
        else:
            wybranaKategoria = int(wybranaKategoria) - 1
            kategoria = kategorie[wybranaKategoria]
            print(f"Wybrano kategorię: {kategoria}")

        for produkt in magazyn:
            if produkt["ilosc"] == 0:
                continue
            elif produkt["cena"] > maxCena:
                continue
            elif produkt["kategoria"].replace(" ", "").lower() == kategoria.replace(" ", "").lower() or kategoria.replace(" ", "").lower() == "brak":
                print(f'\nProdukt: {produkt["nazwa"]}\nCena: {produkt["cena"]}zł\nID: {produkt["id"]}\nIlość: {produkt["ilosc"]}\n')

    except ValueError:
        print("Błąd typu danych.")


def kup(saldo):
    while True:
        print('Jaki produkt chcesz kupić? \nWyświetl listę -> "lista"\nZakończ kupno -> "stop"\nKup produkt -> "(Nazwa produktu/ID produktu)"')
        komenda = input("\n>").strip().lower().replace(" ", "")

        if komenda == "lista":
            lista()
        elif komenda == "stop":
            break
        elif komenda.isdigit():
            idKup = int(komenda)
            znaleziono = False
            for p in magazyn:
                if p["id"] == idKup and p["ilosc"] == 0:
                    print(f'\nNiestety nie ma już: {p["nazwa"]}\n')
                    znaleziono = True
                    break
                elif p["id"] == idKup:
                    znaleziono = True
                    cena = p["cena"]
                    saldo += cena
                    p["ilosc"] -= 1
                    print(f'\nKupiłeś {p["nazwa"]}.\n')
                    break
            if not znaleziono:
                print("\nNie znaleziono produktu, sprawdź pisownię.\n")
        else:
            nazwa = komenda
            znaleziono = False
            for p in magazyn:
                if p["nazwa"].lower().replace(" ", "") == nazwa and p["ilosc"] == 0:
                    print(f'Niestety nie ma już: {p["nazwa"]}')
                    break
                elif p["nazwa"].lower().replace(" ", "") == nazwa:
                    znaleziono = True
                    cena = p["cena"]
                    saldo += cena
                    p["ilosc"] -= 1
                    print(f'\nKupiłeś {p["nazwa"]}.\n')
                    break

            if not znaleziono:
                print("Nie znaleziono produktu, sprawdź pisownię.")

    return saldo


def saldo():
    print(f"Saldo firmy: {saldoFirmy}zł")


print("\n\n\n\n\n====== WITAJ W WIELKIM SKLEPIE JAKUBA SASINA! ======")
print("Wszystkie produkty kupujesz na własną odpowiedzialność\nFirma Sasin Inc. nie ponosi odpowiedzialności za ewentualne zakrztuszenia, omdlenia,\nzatrucie pokarmowe, akty terroryzmu bądź katastrofy biologiczne.")
print("\nDziękujemy za współpracę, miłych zakupów!\n")

while True:
    pokazFunkcje()
    print('Wprowadź komendę. ("stop" by zakończyć)')
    komenda = input("\n> ").lower()

    if komenda == "lista":
        lista()
    elif komenda == "kup":
        saldoFirmy = kup(saldoFirmy)
    elif komenda == "zapisz":
        zapisz()
    elif komenda == "odczytaj":
        odczytaj()
    elif komenda == "stop":
        break
    elif komenda == "saldo":
        saldo()
    else:
        print(f'Nie rozpoznano komendy "{komenda}"')

# wyswietlenie menu -
# 1 Wszystkie produkty
# 2 Dostępne produkty tylko bez tych których ilość to 0 / dla chętnych checkbox obok innych funkcji
# 3 Wyszukaj produkty - użyć z lower
# 4 Produkty do podanej ceny - może być niedostępny ale spełnia warunek ceny
# 5 Kup produkt - user wpisze nazwę i jeśli istnieje i jego ilość > 0 to jego liczba zmniejszy się o 1
# stan == 0 to print produkt niedostępny, print nie znaleziono produktu jeśli nazwa niepoprawna, podaj produkt: input, monit: kupiono mleko, pozostało sztuk x
# 0 Zakończ program - w pęprli dopóki użytkownik nie wybierze zera
# jeśli inna cyfra komunikat że wybrano zła opcję
# int, float, bool, for, while, if, elif, else, break, continue, input, lower, try/except
# LEPIEJ UŻYĆ KLASY!

# chcę aby jeszcze była zmienna odpowiadająca za portfel firmy, i jeżeli kupię produkt to doda się do niej cena produktu
