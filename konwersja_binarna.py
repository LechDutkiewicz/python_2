def dziesietna_na_binarna(liczba):
    """Zamienia liczbę dziesiętną (np. 10) na binarną (np. '1010')."""

    # Obsługujemy zero osobno, bo pętla poniżej by się nie wykonała
    if liczba == 0:
        return "0"

    bity = []  # tutaj będziemy zbierać kolejne bity (0 lub 1)

    # Dzielimy liczbę przez 2 i zbieramy reszty – to właśnie są bity
    while liczba > 0:
        reszta = liczba % 2      # reszta z dzielenia przez 2 to kolejny bit
        bity.append(str(reszta)) # dodajemy bit do listy
        liczba = liczba // 2     # całkowite dzielenie przez 2

    # Bity zebraliśmy od najmniej znaczącego – odwracamy kolejność
    bity.reverse()

    return "".join(bity)  # łączymy listę w jeden napis, np. ['1','0','1'] -> "101"


def binarna_na_dziesietna(napis_binarny):
    """Zamienia liczbę binarną jako tekst (np. '1010') na dziesiętną (np. 10)."""

    wynik = 0
    potega = 0  # zaczynamy od potęgi 2^0 = 1, idąc od prawej strony

    # Odczytujemy bity od prawej do lewej
    for bit in reversed(napis_binarny):
        if bit == "1":
            wynik += 2 ** potega  # dodajemy odpowiednią potęgę dwójki
        potega += 1               # przechodzimy do następnej potęgi

    return wynik


# --- Testowanie ---

print("=== Dziesiętna → Binarna ===")
liczby = [0, 1, 5, 10, 42, 255]
for n in liczby:
    print(f"{n:>3} dziesiętnie  =  {dziesietna_na_binarna(n)} binarnie")

print()
print("=== Binarna → Dziesiętna ===")
kody = ["0", "1", "101", "1010", "101010", "11111111"]
for k in kody:
    print(f"{k:>8} binarnie  =  {binarna_na_dziesietna(k)} dziesiętnie")
