# MODULI MITTAUSSANOMIEN KÄSITTELYYN
#TODO: tee esimerkki siitä, miten rakennetaan sanoma

# Sanoma koostuu alkumerkistä <, datasta, loppumerkistä > ja varmistussummasta
# Varmistussumma lasketaan siten, että kirjainten ascii koodit
# lasketaan yhteen ja summasta otetaan jakojäännös modulo 127
# Sanoman sisältö koostuu kentistä: sivuA, sivuB, ristimitta ja virhe
# Erottimena kenttien välillä on pystyviiva |
# Pohdittavaksi: varmistussumma ennen vai jälkeen loppumerkin

# <3000|4007|5080|74.4|103>
#TODO: esimerkki, miten puretaan.
# Sanoman sisältämät tiedot tallennetaan avain-arvopareiksi
# Esim. {'seinä 1' : 2400, 'seinä 2' : 2500 ...}
# Tietojen oikeellisuus tarkistetaan laskemalla varmistussumma
# uudelleen ja vertaamalla sitä sanoman mukana tulleeseen

# Kirjastojen ja modulien lataukset

# Funktio, jolla muodostetaan sanoman sisältö
def muodosta_sanoma(seina1, seina2, ristimitta, virhe):
    """Muodostaa merkkijonon sanomarakennetta varten

    Args:
        seina1 (float): ensimmäisen seinän pituus mm
        seina2 (float): toisen seinän pituus mm
        ristimitta (float): seinien välinen ristimitta
        virhe (float): lasketun ja mitatun ristimitan välinen ero

    Returns:
        string: tiedot merkkijonoksi muutettuna, tietojen välissä |
    """
    merkkijono = str(seina1) + '|' + str(seina2) + '|' + str(ristimitta) + '|' + str(virhe) + '|'
    return merkkijono


def muodosta_sanoma2(seina1, seina2, ristimitta, virhe):
    """Muodostaa merkkijonon sanomarakennetta varten

    Args:
        seina1 (float): ensimmäisen seinän pituus mm
        seina2 (float): toisen seinän pituus mm
        ristimitta (float): seinien välinen ristimitta
        virhe (float): lasketun ja mitatun ristimitan välinen ero

    Returns:
        string: tiedot merkkijonoksi muutettuna, tietojen välissä |
    """
    merkkijono = f'{seina1}|{seina2}|{ristimitta}|{virhe}|'
    return merkkijono

def summaa_merkit(merkkijono):
    summa = 0
    for kirjain in merkkijono:
        numeroarvo = ord(kirjain)
        summa = summa + numeroarvo
    return summa

def laske_varmiste(summa):
    varmiste = summa % 127
    return varmiste

# TODO: Yhdistä kaikki yhteen sanomaan eli alku- ja loppumerkit sekä varmiste tekstinä

# TODO: Refaktoroi summaa_merkit() ja laske_varmiste() -funktiot yhdeksi funktioksi
# siten, että jakaja on funktion toisena argumenttina

if __name__ == "__main__":
    merkkijono = muodosta_sanoma(3000,4000,5003,3)
    print(merkkijono)
    summa = summaa_merkit(merkkijono)
    print('merkkien summa on:',summa)
    varmiste = laske_varmiste(summa)
    print('Modulo 127 varmiste on', varmiste)
        