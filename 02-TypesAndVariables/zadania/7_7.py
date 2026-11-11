

import random  # Udostępnia funkcje służące do losowania liczb.
for i in range(5):  # Powtarza wcięte instrukcje 5 razy; i przyjmuje kolejno wartości od 0 do 4.
    random_number = random.randint(5, 10)  # Losuje liczbę całkowitą od 5 do 10, włącznie z obiema granicami.
    print(random_number)  # Wyświetla wylosowaną liczbę w osobnym wierszu.

    input("Naciśnij ENTER, aby zakończyć...")
exit()
