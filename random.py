#stappenplan
# 1. Een willekeurig nummer van 1 t/m 10 maken.
# 2. De speler voert een nummer tussen 1 en 10 in.
# 3. De speler moet daarna raden of het volgende getal hoger of lager wordt.
# 4. Er moet een volgend getal gegenereed worden.
# 5. De speler moet weten of ze gewonnen heeft.

import time
import random

willekeur = random.randrange(1, 10)

print("Welkom bij dit hoger of lager spelletje!")

spelers = input("Met hoeveel spelers wilt u dit spel spelen? 2/4 spelers: ")
if spelers == "2":
    speler1 = input("Speler 1 voer naam in: ")
    print(" ")
    time.sleep(1)
    speler2 = input("Speler 2 voer naam in: ")
    print("Hallo, " + speler1 + " en " + speler2)
    print(" ")
    time.sleep(1)
    print("Het spel gaat als volgt: Er komt een getal en " + speler1 + " moet raden of het volgende getal hoger of lager wordt")
    print("Info: 1 voor hoger, 2 voor lager")
    time.sleep(3)
    print(" ")
    print("Oke daar gaan we!" + " " + speler1 + " " + "Kiest nu als eerst een getal!")
    startgetal = input("Speler 1 kies een start getal tussen 1/10: ")
    getal = input("Wordt het getal hoger(1) of lager(2)?: ")
    if getal >= startgetal:
        print("Goedzo")
