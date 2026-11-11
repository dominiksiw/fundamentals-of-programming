
number = int(input('Enter number: '))  # Wczytuje liczbę, dla której powstanie tabliczka mnożenia.
for multiplier in range(1, 11):  # Ustawia mnożnik kolejno na 1, 2, aż do 10.
    print(f'{number} x {multiplier} = {number * multiplier}')  # Wyświetla jedno działanie oraz jego wynik.


input("Naciśnij ENTER, aby zakończyć...")
exit()