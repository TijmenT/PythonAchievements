varA = 5
varB = 10

if ( varA >= 5 ):
    print("varA staat gelijk aan 5")
else:
    print("variable staat niet gelijk")

if ( varA == varB ) :
    print("varA staat gelijk aan")
elif ( varA < varB ) :
    print("varA is kleiner dan varB")
elif ( varA == 50 ) :
    pass #doe niks
else:
    print("Dan is varA groter dan varB")

if ( False ):
    print("Doe dit")

varW = False
varX = True
varY = True
varZ = True

# (varW == True and varX == True or varY == True and varZ == True
if ( varW and varX or varY and varZ ):
    print("Print dit")
# ( False       True        True
if ( varW and (varX or varY) and varZ ):
    print("Print mij ook")




print("Einde programma")

