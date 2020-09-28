import logging
import re
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

def input_number(txt):
    while True:
        number = input("Podaj {}: ".format(txt))
        # if not pattern.fullmatch(number):
        #     print("NaN")
        # else:
        #     return float(number)
        try:
            float(number)
        except:
            print("NaN")
        else:
            return float(number)



if __name__ == "__main__":

    # pattern = re.compile(r'((-)?\d+(\.\d+)?)|(\.\d+)|((-)?\d+e(-)?\d+)')

    while True:
        choice = input("Podaj działanie, posługując się odpowiednią liczbą:\n a .. b = c\n 1 Dodawanie (+)\n 2 Odejmowanie (-)\n 3 Mnożenie (*)\n 4 Dzielenie (/)\n 0 Zakończ\n:")
        if choice == '0':
            break
        elif choice in ['1', '2', '3', '4']:
            # a = float(input("Podaj a: "))
            # b = float(input("Podaj b: "))
            a = input_number('a')
            b = input_number('b')
            if choice == '1':
                print("WYNIK: ", add(a, b))
            elif choice == '2':
                print("WYNIK: ", subtract(a, b))
            elif choice == '3':
                print("WYNIK: ", multiply(a, b))
            elif choice == '4':
                print("WYNIK: ", divide(a, b))
            print("\n")
        else:
            print("Niepoprawna opcja")
