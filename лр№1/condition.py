import os
import time

PIXEL = ' '
RED = '\u001b[101m'
GREEN = '\u001b[102m'
RESET = '\u001b[0m'


def condition_pilar():
    file = open('sequence.txt')
    number_more = [float(x) for x in file if 0 > float(x) > -5]
    file.seek(0)
    number_less = [float(x) for x in file if float(x) < -5]
    file.close()

    pilar_number_more = (len(number_more) / (len(number_more) + len(number_less))) * 100
    pilar_number_less = (len(number_less) / (len(number_more) + len(number_less))) * 100

    if pilar_number_more > pilar_number_less:
        print(str(round(pilar_number_more, 2)) + '%')

        k = 1
        n = int(pilar_number_less) // 5
        for num in range(1, int(pilar_number_more) // 5):
            print(f'\033[{num + 1};2H{RED + PIXEL * 2 + RESET}')
            time.sleep(0.1)
            k += 1

        while n > 0:
            print(f'\033[{k};9H{GREEN + PIXEL * 2 + RESET}')
            time.sleep(0.1)
            k -= 1
            n -= 1
        print(f'\033[{k};8H{round(pilar_number_less, 2)}%')


        print(f'\033[6;20H{RED + PIXEL * 2 + RESET}')
        k = 22
        red = ' - числа большие -5 и меньшие 0'
        for i in range(len(red)):
            print(f'\033[6;{k}H{red[i]}')
            time.sleep(0.1)
            k += 1

        print(f'\033[7;20H{GREEN + PIXEL * 2 + RESET}')
        k = 22
        green = ' - числа меньшие -5'
        for i in range(len(green)):
            print(f'\033[7;{k}H{green[i]}')
            time.sleep(0.1)
            k += 1


    print('\033[15;1H')


os.system('cls')
condition_pilar()
