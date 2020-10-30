import time
def countdown(t):
    while t > 0:
        print(t)
        t -= 1
        time.sleep(1)
    print("GELUKKIG NIEUWJAAR!")

print("HOEVEEL SECONDEN?:")
seconds = input()
while not seconds.isdigit():
    print("Vul iets geldigs in:")
    seconds = input()
seconds = int(seconds)
countdown(seconds)
