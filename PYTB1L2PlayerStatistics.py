import time
import os

repeat = "Y"
while repeat[0] not in ("N"):
    print("Welkom bij de ultimate character maker!")
    time.sleep(2)
    print(" ")
    print(" ")
    print("Vandaag krijg je een kans om jou eigen game character te maken!.")
    print(" ")
    time.sleep(1)
    naam = input("Kies een naam voor jou karakter: ")
    print("Oke, " + naam + "!")
    print(" ")
    print("Nu moet je een speciale kracht uitkiezen waar jou karakter zich op gaat foccusen")
    print("Je kunt kiezen uit: Sterk, Snelheid, Behendigheid, Geld")
    kracht = input("Kies hier jou speciale kracht: ")
    print(naam + "," + " jij koos: " + kracht)
    print(" ")
    time.sleep(2)
    print("Er is nog een 1 ding dat je moet kiezen!")
    print(" ")
    print("Wat voor wapen wilt u om mee te starten?")
    print("Je kunt kiezen uit: Pistol, Mini-Smg, Kapmes")
    wapen = input("Kies hier uw wapen: ")
    print(" ")
    print("Jij koos: " + wapen)
    print(" ")
    time.sleep(1)
    print("Aan het berekenen...")
    time.sleep(1)
    print("Uw karakter is klaar!")
    print("Hier komen de statestieken")
    time.sleep(1)
    print("Naam: " + naam)
    time.sleep(1)
    print("Kracht: " + kracht)
    time.sleep(1)
    print("Wapen: " + wapen)
    time.sleep(1)
    print("Levens: 3")
    time.sleep(1)
    print("Level: 1")
    time.sleep(1)
    print("Wanted: False")
    time.sleep(1)
    print("Owned vehicles: 0")
    time.sleep(1)
    print(" ")
    print("Uw bent klaar om te spelen!")
    repeat = input("Wilt u uw karakter opnieuw maken Y/N?: ")
print("Gemaakt door Tijmen SD1DB")



      

