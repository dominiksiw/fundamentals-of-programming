

cm = 170  # Zapisuje przykładowy wzrost w centymetrach.
total_inches = cm / 2.54  # Zamienia cały wzrost z centymetrów na cale.
feet = int(total_inches // 12)  # Dzieli przez 12 w dół i zapisuje liczbę pełnych stóp jako liczbę całkowitą.
inches = total_inches % 12  # Oblicza pozostałe cale po odjęciu wszystkich pełnych stóp.
print(f'I am {cm}cm tall, i.e. {feet} feet and {inches:.2f} inches')  # Wyświetla centymetry, pełne stopy i pozostałe cale z dwiema cyframi po kropce.

input("Naciśnij ENTER, aby zakończyć...")
exit()