def nwd(a, b):
    """Oblicza Największy Wspólny Dzielnik (NWD) dwóch liczb algorytmem Euklidesa."""

    # Algorytm Euklidesa działa tak:
    # Dopóki b nie wynosi 0, zastępujemy a przez b, a b przez resztę z dzielenia a przez b.
    # Kiedy b osiągnie 0, odpowiedź to a.

    while b != 0:
        reszta = a % b   # obliczamy resztę z dzielenia a przez b
        a = b            # a staje się poprzednim b
        b = reszta       # b staje się resztą

    # Kiedy b == 0, w zmiennej a mamy wynik – NWD
    return a


# --- Testowanie funkcji ---

pary = [
    (48, 18),
    (100, 75),
    (7, 13),    # liczby pierwsze – NWD wyniesie 1
    (0, 5),
    (12, 12),
]

for a, b in pary:
    wynik = nwd(a, b)
    print(f"NWD({a}, {b}) = {wynik}")
