import os
import time

WHITE = '\u001b[97m'
MAGENTA = '\u001b[105m'
PIXEL = ' '
RESET = '\u001b[0m'
BLUE = '\u001b[94m'
YELLOW = '\u001b[93m'

X_0 = 1
Y_0 = 19

ordinate = 18
abscissae = 40


def graph():
    print(f'\033[1;3H↑')
    print(f'\033[1;4Hy')

    for num in range(ordinate, 0, -1):
        print(BLUE + str(num))
    for y in range(4, ordinate + 4):
        print(f'\033[{y - 2};{X_0 + 2}H{WHITE + '|' + RESET}')


    for num in range(3, abscissae - 4, 3):
        print(f'\033[{Y_0 + 2};{num + 3}H{BLUE + str(num // 3) + RESET}', end = '')
    for x in range(3, abscissae,3):
        print(f'\033[{Y_0 + 1};{x}H{WHITE + '‾' + RESET}', end = '')


    print(f'\033[{Y_0 + 1};{abscissae - 1}H→')
    print(f'\033[{Y_0 + 1};{abscissae}Hx')

    position_x = [x for x in range(21, -1, -1)]

    k_int = -1
    for y in range(ordinate):
        k_int += 1
        print(f'\033[{y + 2};{position_x[k_int]}H{MAGENTA + PIXEL + RESET}')
        time.sleep(0.1)

    print(f'\033[2;15H{YELLOW + 'y'}')
    time.sleep(0.2)
    print(f'\033[2;16H=')
    time.sleep(0.2)
    print(f'\033[2;17H3')
    time.sleep(0.2)
    print(f'\033[2;18Hx')
    time.sleep(0.2)


    print('\033[20;1H')

os.system('cls')
graph()
