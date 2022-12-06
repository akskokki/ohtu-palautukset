class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        self.joukko = []

    def kuuluu(self, n):
        return n in self.joukko

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.joukko.append(n)
            return True

        return False

    def poista(self, n):
        if n in self.joukko:
            self.joukko.remove(n)
            return True

        return False

    def mahtavuus(self):
        return len(self.joukko)

    def to_int_list(self):
        return self.joukko

    @staticmethod
    def yhdiste(joukko_a, joukko_b):
        uusi_joukko = IntJoukko()
        
        for n in joukko_a.joukko:
            uusi_joukko.lisaa(n)
        for n in joukko_b.joukko:
            uusi_joukko.lisaa(n)

        return uusi_joukko

    @staticmethod
    def leikkaus(joukko_a, joukko_b):
        uusi_joukko = IntJoukko()

        for n in joukko_a.joukko:
            if n in joukko_b.joukko:
                uusi_joukko.lisaa(n)

        return uusi_joukko

    @staticmethod
    def erotus(joukko_a, joukko_b):
        uusi_joukko = joukko_a
        
        for n in joukko_b.joukko:
            uusi_joukko.poista(n)

        return uusi_joukko

    def __str__(self):
        return str(self.joukko).replace("[", "{").replace("]", "}")
