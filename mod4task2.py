import logging
logging.basicConfig(level=logging.INFO)

def add(a, b):
    logging.info("Dodaję {} i {}".format(a, b))
    return a + b

def subtract(a, b):
    logging.info("Odejmuję {1} od {0}".format(a, b))
    return a - b

def multiply(a, b):
    logging.info("Mnożę {} przez {}".format(a, b))
    return a * b

def divide(a, b):
    logging.info("Dzielę {} przez {}".format(a, b))
    return a / b

if __name__ == "__main__":

    choice = input("Podaj działanie, posługując się odpowiednią liczbą:\n a .. b = c\n 1 Dodawanie (+)\n 2 Odejmowanie (-)\n 3 Mnożenie (*)\n 4 Dzielenie (/)\n:")
    a = float(input("Podaj a: "))
    b = float(input("Podaj b: "))
    if choice == '1':
        print("WYNIK: ", add(a, b))
    elif choice == '2':
        print("WYNIK: ", subtract(a, b))
    elif choice == '3':
        print("WYNIK: ", multiply(a, b))
    elif choice == '4':
        print("WYNIK: ", divide(a, b))
    else:
        exit(1)
