#Info
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y



print("Kies een optie: 1.optellen, 2.aftrekken, 3.vermenigvuldigen, 4.gedeelddoor")

while True:
    keuze = input("Maak een keuze tussen die cijfers: ")

    if keuze in ('1', '2', '3', '4'):
        num1 = float(input("Eerste nummer: "))
        num2 = float(input("Tweede nummer: "))

        if keuze == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif keuze == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif keuze == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif keuze == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Geen nummer")
