# PÄÄOHJELMA

# KIRJASTOJEN JA MODULIEN LATAUS

# Otetaan käyttöön Windows-äänikirjasto (pythonin sisäänrakennettu kirjasto)
import winsound

# Otetaan käyttöön oma funktiomoduli
import funktiot_moduli

# Otetaan käyttöön oma kysymysmoduli
import kysymys

def select_case(sanakirja, avain, oletus):
    """Muiden ohjelmointikielten Select-Case-rakennetta vastaava funktio

    Args:
        sanakirja (dict): Avain-arvo-parit
        avain (any): hakuavain
        oletus (any): arvo, jos hakuavainta ei löydy

    Returns:
        any: Hakuavainta vastaava arvo tai oletus, mikäli hakuavainta ei löytynyt
    """
    arvo = sanakirja.get(avain, oletus)
    return arvo
 
# Varsinainen pääohjelma alkaa tästä
huoneraja_arvot = {'MH':30, 'K':20, 'KPH':5, 'WC':5, 'OH':20}

# Lista mittaustuloksita, tyhjä ennen silmukkaa
mittaustulokset = []

# Ikuinen silmukka
while True:
    seina1 = kysymys.kysy_liukuluku('Anna ensimmäisen seinän pituus (mm)')
    seina2 = kysymys.kysy_liukuluku('Anna toisen seinän pituus (mm)')
    lavistaja = kysymys.kysy_liukuluku('Anna huoneen ristimitta (mm)')
    
    # Kysytään huonetyyppi
    huone = input('Mikä huone? ').upper()
    mittaustulokset.append(seina1)
    mittaustulokset.append(seina2)
    mittaustulokset.append(lavistaja)

    # Haetaan raja-arvo sanakirjasta, oletus 50 mm
    raja_arvo = select_case(huoneraja_arvot, huone, 50)
    # Ilmoitetaan ero ja suurin sallittu poikkeama#
    ero = funktiot_moduli.suorakulma(seina1, seina2, lavistaja)
    print('Ero suoraankulmaan oli', ero, 'suurin sallittu on', raja_arvo)
    

    # Kysytään käyttäjältä haluaako jatkaa
    lopetetaan = input('Paina L, jos haluat lopettaa: ').upper()

    if lopetetaan == 'L':
        break

# Ohjelman suoritus päättyy

# Kysytään mittaajan ja työmaan tiedot
# tyomaa = input('Minkä tyyppinen työmaa oli (kerrostalo, rivitalo tai OK-talo): ').lower()

# Ilmoitetaan montako senttiä mittauksessa saa olla virhettä IF-rakenteen avulla

# if tyomaa == 'kerrostalo':
#   print('Maksimivirhe saa olla 10 mm')
# elif tyomaa == 'rivitalo':
#     print('Maksimivirhe saa olla 20 mm')
# else:
#   print('Maksimivirhe saa olla 50 mm')





print('Maksimiero', huone, 'on', raja_arvo, 'mm')

mittauksia = len(mittaustulokset)
print('Kiitos tästä päivästä, teit', mittauksia, 'mittausta')

# Tulostetaan ruudulle kaikki mittaustulokset
print('Päivän mittaukset alla:')
for mittaus in mittaustulokset:
    print(mittaus)
 