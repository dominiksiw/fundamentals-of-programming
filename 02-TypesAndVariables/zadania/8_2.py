

radius = float(input('Enter circle radius: '))  # Wczytuje promień koła jako liczbę, która może mieć część dziesiętną.
pi = 3.14  # Zapisuje przybliżenie liczby pi użyte w przykładach z ćwiczenia.
area = pi * radius ** 2  # Oblicza pole koła ze wzoru pi razy promień podniesiony do kwadratu.
circumference = 2 * pi * radius  # Oblicza obwód koła ze wzoru 2 razy pi razy promień.
print(f'Area: {area:.2f}')  # Wyświetla pole z dokładnie dwiema cyframi po kropce dziesiętnej.
print(f'Circumference: {circumference:.2f}')  # Wyświetla obwód z dokładnie dwiema cyframi po kropce dziesiętnej.

input("Naciśnij ENTER, aby zakończyć...")
exit()
