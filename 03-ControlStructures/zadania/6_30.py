
for row in range(1, 8):  # Ustawia pierwszą liczbę wiersza kolejno na 1, 2, aż do 7.
    for number in range(row, 50, 7):  # Wybiera liczby danego wiersza, zwiększając każdą następną o 7.
        print(number, end=' ')  # Wyświetla jedną liczbę i spację bez kończenia wiersza.
    print()  # Przechodzi do nowego wiersza po wypisaniu jego siedmiu liczb.


input("Naciśnij ENTER, aby zakończyć...")
exit()