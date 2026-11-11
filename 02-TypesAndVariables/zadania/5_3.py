
a = float(input("a="))  # Pobiera pierwszy bok i zamienia wpisany tekst na liczbę.
b = float(input("b="))  # Pobiera drugi bok jako liczbę, również z częścią ułamkową.
c = float(input("c="))  # Pobiera trzeci bok jako liczbę.
volume = a * b * c  # Mnoży trzy wymiary, otrzymując objętość.
surface_area = 2 * (a * b + a * c + b * c)  # Dodaje pola trzech różnych ścian i mnoży przez 2.
print(f"The volume of the cuboid is {volume}")  # Wyświetla obliczoną objętość.
print(f"The surface area of the cuboid is {surface_area}")  # Wyświetla całkowite pole powierzchni.

input("Naciśnij ENTER, aby zakończyć...")
exit()
