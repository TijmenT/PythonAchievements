# Script gemaakt door Tijmen Terpstra SD1DB
# Script gemaakt door Tijmen Terpstra SD1DB
# Script gemaakt door Tijmen Terpstra SD1DB


import time

start_over = 1

#Tekst bij onderwerp

inleiding = "Mijn naam is Tijmen Terpstra, en ik ben slecht in rijmen."
school = "Als ik naar school ga moet ik eerst anderhalf uur reizen"
hobbys = "Mijn hobbys zijn Gamen en fitnessen. De games die ik meestal speel zijn CSGO en GTA V"
school2 = "Waarom heb ik voor deze opleiding gekozen?"
schoolanswer = "Ik heb voor deze opleiding gekozen omdat ik al heel lang bezig ben met de computer."
slot = "Dit was een klein beetje informatie van mij voor de Python opdracht."



#uitvoering


repeat = "ja"
while repeat[0] not in ("nee", "Nee","no","No"):
    
    print(" ")
    print(" ")
    print("Hallo!")
    time.sleep(1)
    print("Dit is een gedichtje over mij via Python")
    question = input("Heb je er zin in?: ")
    if question == "ja":
        print("Mooizo!")
    else:
        print("Jammer dat je er geen zin in hebt maar ik ga het alsnog vertellen.")
    
    time.sleep(1)
    print("Oke daar gaan we dan!")
    time.sleep(1)
    print(" ")
    time.sleep(1)
    print(inleiding)
    time.sleep(3)
    print(school)
    time.sleep(3)
    print(hobbys)
    time.sleep(3)
    print(school2)
    time.sleep(3)
    print(schoolanswer)
    time.sleep(3)
    print(slot)
    time.sleep(3)
    print(".")
    time.sleep(1)
    question = input("Wat vond u van dit gedicht op een schaal van 1/10?: ")
    if question == "10":
        print("Wouw een 10,")
        start_over -= 1
    else:
        print("Geen 10 maar alsnog,")
    print("Bedankt!")

    question = input("Wilt u het gedicht opnieuw lezen?: ")
    if question == "ja":
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
    else:
        print("Jammer, dit programma word afgesloten in 5 seconden.")
        time.sleep(0.5)
        print("5")
        time.sleep(1)
        print("4")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("0")
        time.sleep(1)
        print("Doei")
        time.sleep(0.5)
        raise SystemExit

                     
    time.sleep(1)
    repeat

# Script gemaakt door Tijmen Terpstra SD1DB
# Script gemaakt door Tijmen Terpstra SD1DB
# Script gemaakt door Tijmen Terpstra SD1DB
