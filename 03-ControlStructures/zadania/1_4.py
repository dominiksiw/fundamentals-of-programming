
account_balance = 500  # Zapisuje dostępne środki z treści zadania.
total_payment = float(input('Enter total payment: '))  # Pobiera kwotę zakupów jako liczbę, również z częścią dziesiętną.
if total_payment <= account_balance:  # Sprawdza, czy kwota zakupów nie przekracza dostępnych środków.
    print('Payment completed')  # Potwierdza możliwość zapłaty.
else:  # Wybiera tę część, gdy zakupy kosztują więcej niż dostępne środki.
    print('No funds')  # Informuje o braku wystarczających środków.


input("Naciśnij ENTER, aby zakończyć...")
exit()