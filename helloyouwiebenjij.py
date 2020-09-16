import time
from datetime import date


repeat = "ja"

today = date.today()

while repeat[0] not in ("nee"):
    
    print("Hello you, ik ben Tijmen")
    print("Wie ben jij?: ")
    naam = input()
    print("En je achternaam?: ")
    achternaam = input()
    print("Hello, " + naam + " " + achternaam)
    question = input("Wilt u de datum en tijd zien?: ")
    if question == "ja":
        time.sleep(1)
        print(today)
        print (time.strftime("%H:%M:%S"))
    else:
        print("Oke!")

    time.sleep(1)
    print("Wilt u het programma opnieuw uitvoeren?: ")
    repeat = input()
print("oke dan niet")
time.sleep(3)
raise SystemExit
