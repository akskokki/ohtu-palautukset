from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostokset_dict = dict()

    def tavaroita_korissa(self):
        tavaroita = 0
        for ostos in self.ostokset_dict.values():
            tavaroita += ostos.lukumaara()
        return tavaroita

    def hinta(self):
        hinta = 0
        for ostos in self.ostokset_dict.values():
            hinta += ostos.hinta()
        return hinta

    def lisaa_tuote(self, lisattava: Tuote):
        if not lisattava.nimi in self.ostokset_dict:
            self.ostokset_dict[lisattava.nimi] = Ostos(lisattava)
        else:
            self.ostokset_dict[lisattava.nimi].muuta_lukumaaraa(1)
        pass

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return list(self.ostokset_dict.values())