number = int(input("Podaj liczbe: "))
if number % 2 == 0:
    if number % 4 == 0:
        print("Podales liczbe parzysta ktora jest wielokrotnoscia liczby 4")
    else:
        print("Liczba jest parzysta")
else:
    print("Liczba nieparzysta")

number2 = int(input("Podaj liczbe do podzielenia: "))
number3 = int(input("Podaj dzielnik: "))
if number2 % number3 == 0:
    print("Liczba " + str(number2) + " dzieli sie parzyscie przez " + str(number3))
else:
    print("Liczba " + str(number2) + " dzieli sie nieparzyscie przez " + str(number3))
