import time
from datetime import date

start_over = 1

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
    question = input("Wilt u een rekensom uitvoeren?: ")
    if question == "ja":
        time.sleep(1)
        question = input("ja voor optellen, nee voor vermenigvuldigen: ")
        if question == "ja":
            print("Voor hier het eerste getal in: ")
            getala = input()
            print("Voer hier het tweede getal in: ")
            getalb = input()
            print("Uw getal is: " + 5+5)           
    time.sleep(1)
    print("Wilt u het programma opnieuw uitvoeren?: ")
    repeat = input()
print("oke dan niet")
time.sleep(3)
raise SystemExit
