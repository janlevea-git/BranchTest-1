# SANOMAT.PY-MODULIN TESTIT

# Modulien ja kirjastojen lataukset
import sanomat



# TODO: luo testit lopuille funktioille

# ASCII-koodien summan testi
def test_summaa_merkit():
    assert sanomat.summaa_merkit('3000|4000|5003|3|') == 1138

# Testataan parannettu varmisteenlaskentafunktio
def test_muodosta_varmiste():
    merkit = '3000|4000|5003|3|'
    jakaja = 127
    assert sanomat.muodosta_varmiste(merkit, jakaja) == '122'

# Testataan yleiskäyttöinen sanomanmuodostusfunktio
def test_luo_sanoma():
    mitatut_arvot = [3000, 4000, 5003, 3]
    assert sanomat.luo_sanoma(mitatut_arvot, '<', '>', '|', 127) == '<3000|4000|5003|3|122>'

def test_pura_sanoma():
    assert sanomat.pura_sanoma('<3000|4000|5003|3|122>','<','>', '|',127) == [['3000', '4000', '5003', '3'], 0, 'Data OK']
    # TODO: tee loput testit missä näkyy virheilmoiukset ja koodit
