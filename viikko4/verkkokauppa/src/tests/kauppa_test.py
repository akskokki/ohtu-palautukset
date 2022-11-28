import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()

        self.viitegeneraattori_mock = Mock()
        self.viitenumero = 42
        self.viitegeneraattori_mock.uusi.return_value = self.viitenumero

        self.varasto_mock = Mock()

        self.asiakas_nimi = "pekka"
        self.asiakas_tilinumero = "12345"

        self.kauppa_tilinumero = "33333-44455"

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 10
            if tuote_id == 3:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "voi", 3)
            if tuote_id == 3:
                return Tuote(3, "leipä", 10)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)


    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu(self.asiakas_nimi, self.asiakas_tilinumero)

        self.pankki_mock.tilisiirto.assert_called()

    def test_tilisiirto_kutsutaan_oikeilla_arvoilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu(self.asiakas_nimi, self.asiakas_tilinumero)

        self.pankki_mock.tilisiirto.assert_called_with(self.asiakas_nimi, self.viitenumero, self.asiakas_tilinumero, self.kauppa_tilinumero, 5)
    
    def test_tilimaksu_toimii_kahdella_eri_tuotteella(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu(self.asiakas_nimi, self.asiakas_tilinumero)

        self.pankki_mock.tilisiirto.assert_called_with(self.asiakas_nimi, self.viitenumero, self.asiakas_tilinumero, self.kauppa_tilinumero, 8)
    
    def test_tilimaksu_toimii_kahdella_samalla_tuotteella(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu(self.asiakas_nimi, self.asiakas_tilinumero)

        self.pankki_mock.tilisiirto.assert_called_with(self.asiakas_nimi, self.viitenumero, self.asiakas_tilinumero, self.kauppa_tilinumero, 10)
    
    def test_tilimaksu_toimii_kun_ostoskoriin_lisatty_tuote_joka_on_loppu(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu(self.asiakas_nimi, self.asiakas_tilinumero)

        self.pankki_mock.tilisiirto.assert_called_with(self.asiakas_nimi, self.viitenumero, self.asiakas_tilinumero, self.kauppa_tilinumero, 5)
 