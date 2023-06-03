""" Moj pierwszy moduł - STATISTICA """

"""Funkcja obliczająca średnią z liczb"""

def srednia(dane):
    return sum(dane)/len(dane)

"""Oblicz wariancję dla liczb"""

def wariancja(dane):
    SumaKwadratowRoznic = 0
    SredniaLiczb = srednia(dane)
    for liczba in dane:
        SumaKwadratowRoznic += (liczba - SredniaLiczb)**2
    return SumaKwadratowRoznic/len(dane)

"""Opis naszych liczb"""

def oblicz(dane):
    wynik = {
        'suma': sum(dane),
        'najmniejsza liczba': min(dane),
        'najwieksza liczba': max(dane),
        'srednia': srednia(dane),
        'wariacja': wariancja(dane)
    }
    return wynik