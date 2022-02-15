# MODULI MITTAUSSANOMIEN KÄSITTELYYN
#

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
# Funktio saa parametrina mitat, jakajan ja erotinmerkin, alkumerkin ja loppumerkin

# Alla runko funktiosta, jollaisena tilaaja sen haluaa:
def luo_sanoma(arvot, alkumerkki, loppumerkki, erotin, jakaja):
    """ Muodostaa sanoman, joka koostuu alkumerkistä, arvoista, varmistussummasta \n
    ja loppumerkistä. Arvojen välillä on haluttu erotinmerkki

    Args:
        arvot (list): sanomaan sisällöksi halutut arvot
        alkumerkki (string): merkki, jolla ilmaistaan sanoman alku
        loppumerkki (string): merkki, jolla ilmaistaan sanoman päättyminen
        erotin (string): arvojen välille tuleva välimerkki
        jakaja (int): jakojäännöksen laskennassa käytettävä jakaja

    Returns:
        string: Valmis sanoma 
    """
    sanoma = ''
    return sanoma

# Muodostetaan merkeistä varmiste valittua jakajaa käyttäen
def muodosta_varmiste(merkit, jakaja):
    return str(summaa_merkit(merkit) % jakaja)


if __name__ == "__main__":

    # Testataan sanoman muodostamista
    merkkijono = muodosta_sanoma(3000,4000,5003,3)
    print(merkkijono)
    summa = summaa_merkit(merkkijono)
    print('merkkien summa on:',summa)
    varmiste = laske_varmiste(summa)
    print('Modulo 127 varmiste on', varmiste)
    valmis_sanoma = lopullinen_sanoma(merkkijono, varmiste)
    print('Valmis sanoma näyttää tältä', valmis_sanoma)
        
    # Testataan sanoman purkamista
    sanoman_pituus = len(valmis_sanoma) # lasketaan sanoman kokonaispituus
    ilman_merkkeja = valmis_sanoma[1:sanoman_pituus -1] # sanoma ilman alku- ja loppumerkkejä 
    print('sanoma ilman alku- ja loppumerkkiä on', ilman_merkkeja)
    paloteltu_sanoma = ilman_merkkeja.split('|') # pilkotaan |-merkistä listaksi
    print('arvot listamuodossa ovat:', paloteltu_sanoma)

    listan_pituus = len(paloteltu_sanoma)
    print('listassa on', listan_pituus, 'jäsentä')
    alkuperainen_tarkiste = paloteltu_sanoma[listan_pituus - 1] # sanoman mukana tullut tarkiste
    ilman_varmistetta = paloteltu_sanoma[0:listan_pituus - 1] # listan jäsenet ilman varmistussummaa

    # Rakennetaan mitat sisältävä merkkijono uudelleen
    uudelleen_str = ''
    for jasen in ilman_varmistetta:
        uudelleen_str = uudelleen_str + jasen + '|'
    print('alkuperäinen tarkiste on', alkuperainen_tarkiste)
    print(uudelleen_str)
    # Verrataan alkuperäista ja uudelleenlaskettua tarkistetta, jos sama sanoma OK
    uudelleenlaskettu_tarkiste = muodosta_varmiste(uudelleen_str, 127)
    print('uudelleen laskettuna se on', uudelleenlaskettu_tarkiste)
    if (alkuperainen_tarkiste) == muodosta_varmiste(uudelleen_str, 127):
        print('Sanoma vahingoittumaton, varmiste tarkistettu')

    else:
        print('Sanoma muuttunut tiedonsiirrossa!')
        
    # TODO: Rakenna purkutestin perusteella funktio ja tee sille testi
    # TODO: Refaktoroi koodia
    """ 
    [13.49] Sergey Vasilyev
    paloteltu_sanoma = valmis_sanoma[1:len(valmis_sanoma)-1].split('|')

    [13.53] Verneri Lähteenoja
    [1:-1] tekee ton ilman len()

    [14.53] Verneri Lähteenoja
    ilman_varmistetta = f"{'|'.join(paloteltu_sanoma[0:-1])}|"

    [14.54] Sergey Vasilyev
    Verneri Lähteenojailman_varmistetta = f"{'|'.join(paloteltu_sanoma[0:-1])}|"hyvä ratkaisu 





    """