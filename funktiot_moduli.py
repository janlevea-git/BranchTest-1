# X-funktio tarkistaa onko kulma suora

def suorakulma(sivuA, sivuB, lavistaja):
    """Tarkistaa suorakulmaisuuden käyttäen Pythagoraan lausetta

    Args:
        sivuA (float): Ensimmäisen seinän pituus
        sivuB (float): Toisen seinän pituus
        lavistaja (float): Huoneen lävistäjän pituus

    Returns:
        float: Lävistäjän pituusvirhe 0 -> ei virhettä
    """
    # TODO: tee tähän virhe jos joku luvuista on 0 (Raise)
    try:
        A_nelio = sivuA * sivuA
        B_nelio = sivuB * sivuB
        l_nelio = lavistaja * lavistaja
        pitaisi_olla = A_nelio + B_nelio
        ero = l_nelio**0.5 - pitaisi_olla**0.5

    except:
        ero = 999
        print('Syötetty arvo on virheellinen')
    finally:    
        return ero

# Testataan, että toimii, poista tämä myöhemmin
if __name__ == "__main__":
    # Testi kulma on suora
    vastaus = suorakulma(3, 4, 5)
    print(vastaus)

    # Testi kulma ei ole suora
    vastaus = suorakulma(3, 4, 6)
    print(vastaus)