
phone = input("Enter phone number: ")  # Pobiera numer jako tekst, dzięki czemu nie gubi zer na początku.
formatted_phone = phone[0:3] + "-" + phone[3:6] + "-" + phone[6:9]  # Wycina trzy grupy cyfr i łączy je kreskami.
print(f"Phone number: {formatted_phone}")  # Wyświetla numer, np. 543-097-329.

input("Naciśnij ENTER, aby zakończyć...")
exit()
