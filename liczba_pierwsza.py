def czy_pierwsza(liczba):
    """Sprawdza, czy podana liczba jest pierwsza."""

    # Liczby mniejsze niż 2 nie są pierwsze (np. 0, 1, liczby ujemne)
    if liczba < 2:
        return False

    # Sprawdzamy, czy liczba dzieli się przez którąś z liczb od 2 do liczba-1
    # Wystarczy sprawdzać tylko do pierwiastka z liczby, ale pętla do liczba
    # jest prostsza i też poprawna
    for dzielnik in range(2, liczba):
        if liczba % dzielnik == 0:
            # Znaleziono dzielnik – liczba NIE jest pierwsza
            return False

    # Żaden dzielnik nie został znaleziony – liczba JEST pierwsza
    return True


# --- Testowanie funkcji ---

liczby_do_sprawdzenia = [1, 2, 3, 4, 10, 13, 17, 20, 97]

for n in liczby_do_sprawdzenia:
    if czy_pierwsza(n):
        print(f"{n} jest liczbą pierwszą")
    else:
        print(f"{n} NIE jest liczbą pierwszą")
