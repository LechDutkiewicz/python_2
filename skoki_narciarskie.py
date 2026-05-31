K_PUNKT = 120          # metry – próg referencyjny (duża skocznia)
BAZA_PUNKTOW = 60      # punkty za wylądowanie dokładnie na K-punkcie
PUNKTY_ZA_METR = 1.8   # punkty dodawane/odejmowane za każdy metr od K-punktu
PUNKTY_ZA_METR_WIATRU = 9.0  # punkty kompensaty za 1 m/s wiatru (duża skocznia)


def punkty_za_odleglosc(dlugosc):
    """Oblicza punkty za odległość skoku."""
    # Za każdy metr powyżej K-punktu dostajemy punkty, poniżej – tracimy
    return BAZA_PUNKTOW + (dlugosc - K_PUNKT) * PUNKTY_ZA_METR


def punkty_za_styl(oceny_sedziow):
    """Oblicza punkty za styl na podstawie 5 ocen sędziów (0–20 każda)."""
    # Odrzucamy najwyższą i najniższą ocenę, sumujemy pozostałe 3
    oceny_posortowane = sorted(oceny_sedziow)
    oceny_bez_skrajnych = oceny_posortowane[1:-1]  # wycinamy pierwszą i ostatnią
    return sum(oceny_bez_skrajnych)


def kompensata_wiatru(predkosc_wiatru):
    """
    Oblicza kompensatę punktową za wiatr.
    Wartość dodatnia = wiatr w twarz (przeszkadza) → dostajemy punkty.
    Wartość ujemna  = wiatr w plecy (pomaga)       → tracimy punkty.
    """
    return predkosc_wiatru * PUNKTY_ZA_METR_WIATRU


def oblicz_wynik(dlugosc, oceny_sedziow, predkosc_wiatru):
    """Oblicza łączny wynik skoku."""

    pkt_odleglosc = punkty_za_odleglosc(dlugosc)
    pkt_styl      = punkty_za_styl(oceny_sedziow)
    pkt_wiatr     = kompensata_wiatru(predkosc_wiatru)

    lacznie = pkt_odleglosc + pkt_styl + pkt_wiatr

    # Wyświetlamy szczegółowe podsumowanie
    print(f"  Odległość:        {dlugosc} m")
    print(f"  Oceny sędziów:    {oceny_sedziow}  →  po odrzuceniu skrajnych: {sorted(oceny_sedziow)[1:-1]}")
    print(f"  Wiatr:            {predkosc_wiatru:+.1f} m/s")
    print(f"  --------------------------")
    print(f"  Pkt za odległość: {pkt_odleglosc:.1f}")
    print(f"  Pkt za styl:      {pkt_styl:.1f}")
    print(f"  Kompensata wiatru:{pkt_wiatr:+.1f}")
    print(f"  ŁĄCZNIE:          {lacznie:.1f} pkt")

    return lacznie


# --- Testowanie – trzech zawodników ---

zawodnicy = [
    {"imie": "Adam Małysz",   "dlugosc": 135.0, "oceny": [18.0, 17.5, 18.5, 17.0, 18.0], "wiatr": -1.0},
    {"imie": "Kamil Stoch",   "dlugosc": 128.5, "oceny": [19.0, 18.5, 17.5, 19.5, 18.0], "wiatr":  0.5},
    {"imie": "Dawid Kubacki", "dlugosc": 118.0, "oceny": [16.5, 17.0, 16.0, 17.5, 16.5], "wiatr":  2.0},
]

for z in zawodnicy:
    print(f"\n{'='*45}")
    print(f"  Zawodnik: {z['imie']}")
    print(f"{'='*45}")
    oblicz_wynik(z["dlugosc"], z["oceny"], z["wiatr"])
