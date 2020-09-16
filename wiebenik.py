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
    print(" ")
    print(" ")
    print("Ik ben een nieuwkomer op het Mediacollege Amsterdam.")
    print(" ")
    print("Er komen wat vragen over mij zodat je mij beter kan leren kennen veel succes!")
    print(" ")
    print("Ik ga je hier een kleine hint geven! mijn reistijd is 1,5 uur en ik woon in een dorp")
    print("Het dorp waar ik woon heet: ")
    print(" A: Opperdoes")
    print(" B: Berkhout")
    print(" C: Limmen")
    question = input("Ik woon in (Vul hier A, B of C in):  ")
    if question == "A":
        print("Correct!")
        print("Op naar de volgende ronde!")
    if question == "a":
        print("Correct!")
        print("Op naar de volgende ronde!")
        start_over -= 1
    if question == "B":
        print("Fout!")
        print("Probeer het nog een keer")
        print("wilt u het programma opnieuw uitvoeren?: ")
        repeat = input()
    if question == "b":
        print("Fout!")
        print("Probeer het nog een keer")
        print("wilt u het programma opnieuw uitvoeren?: ")
        repeat = input()
    if question == "C":
        print("Fout!")
        print("Dit dorpje ligt in Australie lol")
        print("wilt u het programma opnieuw uitvoeren?: ")
        repeat = input()
    if question == "c":
        print("Fout!")
        print("Dit dorpje ligt in Australie lol")
        print("wilt u het programma opnieuw uitvoeren?: ")
        repeat = input()
    print("Hier verder")
    print("wilt u het programma opnieuw uitvoeren?: ")
    repeat = input()
print("oke dan niet")
time.sleep(3)
raise SystemExit
