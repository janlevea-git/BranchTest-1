# SANOMAT.PY-MODULIN TESTIT

# Modulien ja kirjastojen lataukset
import sanomat

# Testataan, että sanoman erotinmerkit tulevat oikein
def test_muodosta_sanoma():
    assert sanomat.muodosta_sanoma(3000, 4000, 5000, 0) == '3000|4000|5000|0|'

# Sama testi, mutta Janin funktiota käyttäen
def test_muodosta_sanoma2():
    assert sanomat.muodosta_sanoma2(3000, 4000, 5000, 0) == '3000|4000|5000|0|'