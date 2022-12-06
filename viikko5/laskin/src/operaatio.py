class Summa:
    def __init__(self, sovelluslogiikka, _lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self._lue_syote = _lue_syote
    
    def suorita(self):
        self.arvo = int(self._lue_syote())
        self.sovelluslogiikka.plus(self.arvo)

class Erotus:
    def __init__(self, sovelluslogiikka, _lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self._lue_syote = _lue_syote
    
    def suorita(self):
        self.arvo = int(self._lue_syote())
        self.sovelluslogiikka.miinus(self.arvo)

class Nollaus:
    def __init__(self, sovelluslogiikka, _lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self._lue_syote = _lue_syote
    
    def suorita(self):
        self.sovelluslogiikka.nollaa()

class Kumoa:
    def __init__(self, sovelluslogiikka, _lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self._lue_syote = _lue_syote
    
    def suorita(self):
        self.sovelluslogiikka.kumoa()