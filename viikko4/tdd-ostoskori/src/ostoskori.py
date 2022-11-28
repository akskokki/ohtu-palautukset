from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostokset = dict()

    def tavaroita_korissa(self):
        tavaroita = 0
        for ostos in self._ostokset.values():
            tavaroita += ostos.lukumaara()
        return tavaroita

    def hinta(self):
        hinta = 0
        for ostos in self._ostokset.values():
            hinta += ostos.hinta()
        return hinta

    def lisaa_tuote(self, lisattava: Tuote):
        if not lisattava.nimi in self._ostokset:
            self._ostokset[lisattava.nimi] = Ostos(lisattava)
        else:
            self._ostokset[lisattava.nimi].muuta_lukumaaraa(1)
        pass

    def poista_tuote(self, poistettava: Tuote):
        ostos = self._ostokset[poistettava.nimi]
        ostos.muuta_lukumaaraa(-1)

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return list(self._ostokset.values())