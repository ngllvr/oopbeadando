from abc import ABC, abstractmethod


class Szoba(ABC):
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

    @abstractmethod
    def leiras(self):
        pass


class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam, klima=False):
        super().__init__(ar=15000, szobaszam=szobaszam)
        self.klima = klima

    def leiras(self):
        return f"Egyágyas szoba {self.szobaszam}, klímával: {self.klima}, ára: {self.ar}."


class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam, erkely=False):
        super().__init__(ar=30000, szobaszam=szobaszam)
        self.erkely = erkely

    def leiras(self):
        return f"Kétágyas szoba {self.szobaszam}, erkéllyel: {self.erkely}, ára: {self.ar}."



egyagyas = EgyagyasSzoba(szobaszam=1492, klima=True)
print(egyagyas.leiras())

ketagyas = KetagyasSzoba(szobaszam=1331, erkely=True)
print(ketagyas.leiras())

class Szalloda:
    def __init__(self, nev, cim):
        self.nev = nev
        self.cim = cim
        self.szobak = []

    def szoba_hozzaadasa(self, szoba):
        self.szobak.append(szoba)

    def osszes_szoba_leiras(self):
        for szoba in self.szobak:
            print(szoba.leiras())

if __name__ == "__main__":

    szalloda = Szalloda(nev="Vicces Szálloda", cim="Király utca 12.")


    egyagyas = EgyagyasSzoba(szobaszam=1492, klima=True)
    ketagyas = KetagyasSzoba(szobaszam=1331, erkely=True)

    szalloda.szoba_hozzaadasa(egyagyas)
    szalloda.szoba_hozzaadasa(ketagyas)

    szalloda.osszes_szoba_leiras()


    class Foglalas:
        def __init__(self, szoba, datum):
            self.szoba = szoba
            self.datum = datum

        def __str__(self):
            return f"Foglalás a {self.szoba.szobaszam} számú szobára, dátum: {self.datum}"



    if __name__ == "__main__":

        foglalas = Foglalas(szoba=egyagyas, datum="2024-05-03")


        print(foglalas)

# Implementálás
from datetime import datetime


class Szalloda:
    def __init__(self, nev, cim):
        self.nev = nev
        self.cim = cim
        self.szobak = []

    def szoba_hozzaadasa(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                return szoba.foglalas(datum)
        return None


class Szoba:
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

    def foglalas(self, datum):
        # ha a dátum jelenlegi dátumnál későbbi, akkor a szoba árát adja vissza
        if datetime.strptime(datum, "%Y-%m-%d") >= datetime.now():
            return self.ar
        else:
            return 0


class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam, klima=False):
        super().__init__(ar=15000, szobaszam=szobaszam)
        self.klima = klima

    def leiras(self):
        return f"Egyágyas szoba {self.szobaszam}, klímával: {self.klima}, ára: {self.ar}."


class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam, erkely=False):
        super().__init__(ar=30000, szobaszam=szobaszam)
        self.erkely = erkely

    def leiras(self):
        return f"Kétágyas szoba {self.szobaszam}, erkéllyel: {self.erkely}, ára: {self.ar}."



if __name__ == "__main__":
    szalloda = Szalloda(nev="Vicces Szálloda", cim="Király utca 12")
    egyagyas = EgyagyasSzoba(szobaszam=1492, klima=True)
    ketagyas = KetagyasSzoba(szobaszam=1331, erkely=True)
    szalloda.szoba_hozzaadasa(egyagyas)
    szalloda.szoba_hozzaadasa(ketagyas)

    # foglalás és árának lekérdezése
    foglalas_ar = szalloda.foglalas(szobaszam=1331, datum="2024-05-03")
    print(f"A foglalás ára: {foglalas_ar}")

class Szalloda:
    def __init__(self, nev, cim):
        self.nev = nev
        self.cim = cim
        self.szobak = []

    def szoba_hozzaadasa(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                return szoba.foglalas(datum)
        return None

    def foglalas_lemondasa(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                return szoba.foglalas_lemondas(datum)
        return None


class Szalloda:
    def __init__(self, nev, cim):
        self.nev = nev
        self.cim = cim
        self.szobak = []

    def szoba_hozzaadasa(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                return szoba.foglalas(datum)
        return None

    def foglalas_lemondasa(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                return szoba.foglalas_lemondas(datum)
        return None

    def osszes_foglalas_listazasa(self):
        foglalasok = []
        for szoba in self.szobak:
            foglalasok.append((szoba.szobaszam, szoba.foglalas_datum))
        return foglalasok


class Szoba:
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam
        self.foglalas_datum = None

    def foglalas(self, datum):
        if datetime.strptime(datum, "%Y-%m-%d") >= datetime.now():
            self.foglalas_datum = datum
            return self.ar
        else:
            return 0

    def foglalas_lemondas(self, datum):
        self.foglalas_datum = None
        return "A foglalás sikeresen lemondva."


# Felhasználói interfész

from datetime import datetime


class Szalloda:
    def __init__(self, nev, cim):
        self.nev = nev
        self.cim = cim
        self.szobak = []

    def szoba_hozzaadasa(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                return szoba.foglalas(datum)
        return None

    def foglalas_lemondasa(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                return szoba.foglalas_lemondas(datum)
        return None

    def osszes_foglalas_listazasa(self):
        foglalasok = []
        for szoba in self.szobak:
            foglalasok.append((szoba.szobaszam, szoba.foglalas_datum))
        return foglalasok


class Szoba:
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam
        self.foglalas_datum = None

    def foglalas(self, datum):
        if datetime.strptime(datum, "%Y-%m-%d") >= datetime.now():
            self.foglalas_datum = datum
            return self.ar
        else:
            return 0

    def foglalas_lemondas(self, datum):
        self.foglalas_datum = None
        return "A foglalás sikeresen lemondva."


# Felhasználói interfész
def main():
    szalloda = Szalloda("Vicces Szálloda", "Király utca 12")
    szalloda.szoba_hozzaadasa(Szoba(15000, 1492))
    szalloda.szoba_hozzaadasa(Szoba(30000, 1331))

    while True:
        print("\nVálasszon a következő műveletek közül:")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("4. Kilépés")

        valasztas = input("Adja meg a választott művelet sorszámát: ")

        if valasztas == "1":
            szobaszam = input("Adja meg a foglalandó szoba sorszámát: ")
            datum = input("Adja meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
            ar = szalloda.foglalas(int(szobaszam), datum)
            if ar is not None:
                print(f"A foglalás sikeres. Az ára: {ar}")
            else:
                print("A foglalás sikertelen.")

        elif valasztas == "2":
            szobaszam = input("Adja meg a lemondandó foglalás szobaszámát: ")
            datum = input("Adja meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
            uzenet = szalloda.foglalas_lemondasa(int(szobaszam), datum)
            print(uzenet)

        elif valasztas == "3":
            foglalasok = szalloda.osszes_foglalas_listazasa()
            if foglalasok:
                print("A szálloda foglalásai:")
                for szobaszam, datum in foglalasok:
                    print(f"Szoba sorszám: {szobaszam}, Foglalás dátuma: {datum}")
            else:
                print("Nincsenek foglalások.")

        elif valasztas == "4":
            print("Kilépés...")
            break

        else:
            print("Érvénytelen választás. Kérem, válasszon újra.")


if __name__ == "__main__":
    main()

from datetime import datetime


class Szalloda:
    def __init__(self, nev, cim):
        self.nev = nev
        self.cim = cim
        self.szobak = []

    def szoba_hozzaadasa(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                return szoba.foglalas(datum)
        return None

    def foglalas_lemondasa(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                return szoba.foglalas_lemondas(datum)
        return None

    def osszes_foglalas_listazasa(self):
        foglalasok = []
        for szoba in self.szobak:
            foglalasok.append((szoba.szobaszam, szoba.foglalas_datum))
        return foglalasok


class Szoba:
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam
        self.foglalas_datum = None

    def foglalas(self, datum):
        if datetime.strptime(datum, "%Y-%m-%d") >= datetime.now():
            if not self.foglalt(datum):
                self.foglalas_datum = datum
                return self.ar
            else:
                print("A szoba ezen a dátumon már foglalt.")
                return 0
        else:
            print("Hibás dátum. Csak jövőbeli foglalások lehetségesek.")
            return 0

    def foglalas_lemondas(self, datum):
        self.foglalas_datum = None
        return "A foglalás sikeresen lemondva."

    def foglalt(self, datum):
        return self.foglalas_datum == datum


# Felhasználói interfész
def main():
    szalloda = Szalloda("Vicces Szálloda", "Király utca 12")
    szalloda.szoba_hozzaadasa(Szoba(15000, 1492))
    szalloda.szoba_hozzaadasa(Szoba(30000, 1331))

    while True:
        print("\nVálasszon a következő műveletek közül:")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("4. Kilépés")

        valasztas = input("Adja meg a választott művelet sorszámát: ")

        if valasztas == "1":
            szobaszam = input("Adja meg a foglalandó szoba sorszámát: ")
            datum = input("Adja meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
            ar = szalloda.foglalas(int(szobaszam), datum)
            if ar:
                print(f"A foglalás sikeres. Az ára: {ar}")
            else:
                print("A foglalás sikertelen.")

        elif valasztas == "2":
            szobaszam = input("Adja meg a lemondandó foglalás szobaszámát: ")
            datum = input("Adja meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
            uzenet = szalloda.foglalas_lemondasa(int(szobaszam), datum)
            print(uzenet)

        elif valasztas == "3":
            foglalasok = szalloda.osszes_foglalas_listazasa()
            if foglalasok:
                print("A szálloda foglalásai:")
                for szobaszam, datum in foglalasok:
                    print(f"Szoba sorszám: {szobaszam}, Foglalás dátuma: {datum}")
            else:
                print("Nincsenek foglalások.")

        elif valasztas == "4":
            print("Kilépés...")
            break

        else:
            print("Érvénytelen választás. Kérem, válasszon újra.")


if __name__ == "__main__":
    main()

class Szalloda:


    def foglalas_lemondasa(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam and szoba.foglalt(datum):
                return szoba.foglalas_lemondas(datum)
        return "A megadott szobaszámmal és dátummal nem található foglalás."

class Szoba:


    def foglalt(self, datum):
        return self.foglalas_datum == datum


def main():

    szalloda = Szalloda("Vicces Szálloda", "Király utca 12")


    szalloda.szoba_hozzaadasa(Szoba(15000, 1492))
    szalloda.szoba_hozzaadasa(Szoba(30000, 1331))
    szalloda.szoba_hozzaadasa(Szoba(20000, 1515))


    szalloda.szobak[0].foglalas("2024-05-10")
    szalloda.szobak[1].foglalas("2024-05-15")
    szalloda.szobak[1].foglalas("2024-05-18")
    szalloda.szobak[2].foglalas("2024-05-20")
    szalloda.szobak[2].foglalas("2024-05-22")

    while True:
        print("\nVálasszon a következő műveletek közül:")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("4. Kilépés")

        valasztas = input("Adja meg a választott művelet sorszámát: ")

        if valasztas == "1":
            szobaszam = input("Adja meg a foglalandó szoba sorszámát: ")
            datum = input("Adja meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
            ar = szalloda.foglalas(int(szobaszam), datum)
            if ar:
                print(f"A foglalás sikeres. Az ára: {ar}")
            else:
                print("A foglalás sikertelen.")

        elif valasztas == "2":
            szobaszam = input("Adja meg a lemondandó foglalás szobaszámát: ")
            datum = input("Adja meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
            uzenet = szalloda.foglalas_lemondasa(int(szobaszam), datum)
            print(uzenet)

        elif valasztas == "3":
            foglalasok = szalloda.osszes_foglalas_listazasa()
            if foglalasok:
                print("A szálloda foglalásai:")
                for szobaszam, datum in foglalasok:
                    print(f"Szoba sorszám: {szobaszam}, Foglalás dátuma: {datum}")
            else:
                print("Nincsenek foglalások.")

        elif valasztas == "4":
            print("Kilépés...")
            break

        else:
            print("Érvénytelen választás. Kérem, válasszon újra.")


if __name__ == "__main__":
    main()
