WHITE = '\u001b[107m'
RED = '\u001b[101m'
PIXEL = '    '
RESET = '\u001b[0m'

#japan
def flag():
    hight = 11
    lenght = hight
    for i in range(hight - 1):
        if i < hight // 2 - 4:
            print(WHITE + PIXEL * lenght + RESET)
        elif i == hight // 2 or i == (hight // 2) - 1 or i == (hight // 2) + 1 or i == (hight // 2) - 2:
            print(WHITE + PIXEL * (lenght // 2 - 2) + RED + PIXEL * (lenght // 2) + WHITE + PIXEL * (lenght // 2 - 2) + RESET)
        elif i == (hight // 2) - 3 or i == (hight // 2) + 2:
            print(WHITE + PIXEL * (lenght // 2 - 1) + RED + PIXEL * (lenght // 2 - 2) + WHITE + PIXEL * (lenght // 2 - 1) + RESET)
        else:
            print(WHITE + PIXEL * lenght + RESET)

flag()
