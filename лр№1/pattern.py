import time
import os

GREEN = '\u001b[102m'
RED = '\u001b[101m'
YELLOW = '\u001b[103m'
BLUE = '\u001b[104m'
MAGENTA = '\u001b[105m'
CYAN = '\u001b[106m'
WHITE = '\u001b[107m'
PIXEL = ' '
RESET = '\u001b[0m'
LENGHT = 60

def pattern():
    for i in range(1, LENGHT, 8):
        print(f'\033[5;{i}H{GREEN + PIXEL + RESET}')
        time.sleep(0.1)

        print(f'\033[4;{i + 1}H{RED + PIXEL + RESET}')
        time.sleep(0.1)
        print(f'\033[6;{i + 1}H{YELLOW + PIXEL + RESET}')
        time.sleep(0.1)

        print(f'\033[3;{i + 2}H{BLUE + PIXEL + RESET}')
        time.sleep(0.1)
        print(f'\033[7;{i + 2}H{MAGENTA + PIXEL + RESET}')
        time.sleep(0.1)

        print(f'\033[2;{i + 3}H{CYAN + PIXEL + RESET}')
        time.sleep(0.1)
        print(f'\033[8;{i + 3}H{WHITE + PIXEL + RESET}')
        time.sleep(0.1)

        print(f'\033[1;{i + 4}H{GREEN + PIXEL + RESET}')
        time.sleep(0.1)
        print(f'\033[9;{i + 4}H{RED + PIXEL + RESET}')
        time.sleep(0.1)


    for i in range(6, LENGHT, 8):
        print(f'\033[2;{i}H{YELLOW + PIXEL + RESET}')
        time.sleep(0.1)
        print(f'\033[8;{i}H{BLUE + PIXEL + RESET}')
        time.sleep(0.1)

        print(f'\033[3;{i + 1}H{MAGENTA + PIXEL + RESET}')
        time.sleep(0.1)
        print(f'\033[7;{i + 1}H{CYAN + PIXEL + RESET}')
        time.sleep(0.1)

        print(f'\033[4;{i + 2}H{WHITE + PIXEL + RESET}')
        time.sleep(0.1)
        print(f'\033[6;{i + 2}H{GREEN + PIXEL + RESET}')
        time.sleep(0.1)


    print('\033[12;1H')


os.system('cls')
pattern()





