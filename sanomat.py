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
    """Laskee merkkijonon kirjainten ASCII-arvot yhteen

    Args:
        merkkijono (string): merkkijono, jonka kirjaimista summa lasketaan

    Returns:
        integer: kirjainten ASCII-koodien summa
    """
    summa = 0
    for kirjain in merkkijono:
        numeroarvo = ord(kirjain)
        summa = summa + numeroarvo
    return summa

def laske_varmiste(summa):
    """Laskee modulo 127 tarkisteen

    Args:
        summa (integer): luku, josta tarkiste lasketaan

    Returns:
        integer: jakojäännös 127:llä jaettaessa
    """
    varmiste = summa % 127
    return varmiste

def lopullinen_sanoma(sanoma, varmiste):
    """Koostaa lopullisen sanoman

    Args:
        sanoma (string): pituustiedot sisältävä merkkijono
        varmiste (integer): varmiste

    Returns:
        string: kokonainen sanoma, jossa on alku- ja loppumerkit mukana
    """
    varmiste_str = str(varmiste)
    sanoma = '<' + sanoma + varmiste_str + '>'
    return sanoma    

# TODO: Yhdistä kaikki yhteen sanomaan eli alku- ja loppumerkit sekä varmiste tekstinä

# TODO: Refaktoroi summaa_merkit() ja laske_varmiste() -funktiot yhdeksi funktioksi
# siten, että jakaja on funktion toisena argumenttina
def muodosta_varmiste(merkit, jakaja):
    """_summary_

    Args:
        merkit (_type_): _description_
        jakaja (_type_): _description_

    Returns:
        _type_: _description_
    """
    varmiste = ''
    return varmiste

if __name__ == "__main__":
    merkkijono = muodosta_sanoma(3000,4000,5003,3)
    print(merkkijono)
    summa = summaa_merkit(merkkijono)
    print('merkkien summa on:',summa)
    varmiste = laske_varmiste(summa)
    print('Modulo 127 varmiste on', varmiste)
    valmis_sanoma = lopullinen_sanoma(merkkijono, varmiste)
    print('Valmis sanoma näyttää tältä', valmis_sanoma)
        