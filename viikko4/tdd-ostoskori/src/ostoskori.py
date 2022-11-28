from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostokset = dict()

    def tavaroita_korissa(self):
        return len(self.ostokset.keys())

    def hinta(self):
        hinta = 0
        for ostos in list(self.ostokset.values()):
            hinta += ostos.hinta()
        return hinta

    def lisaa_tuote(self, lisattava: Tuote):
        if not lisattava.nimi in self.ostokset:
            self.ostokset[lisattava.nimi] = Ostos(lisattava)
        else:
            self.ostokset[lisattava.nimi].muuta_lukumaaraa(1)
        pass

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        pass
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
