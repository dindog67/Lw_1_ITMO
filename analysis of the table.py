from csv import reader
import os
import random
from xml.etree import ElementTree

YELLOW = '\u001b[93m'
RED = '\u001b[91m'
GREEN = '\u001b[92m'
BLUE = '\u001b[94m'
CYAN = '\u001b[96m'
RESET = '\u001b[0m'


os.system('cls')

def open_table():
    try:
        with open('books-en.csv', 'r') as csvfile:
            table = list(reader(csvfile, delimiter=';'))
            table = table[1:]
            return table

    except FileNotFoundError:
        print(f'{RED + 'File not found!' + RESET}')
        return 0



def search_quantity(table):
    count = 0
    for row in table:
        if len(row[1]) > 30:
            count += 1

    print(f'{YELLOW + 'Number of books with a title lenght greater than 30: ' + RESET + str(count) + ' things'}')


def search_index(line, string):
    string = string.lower()
    index = string.find(line.lower())
    return index


def search_author(table):
    author = input(f'{ YELLOW + "2)Enter the name of author who wrote a book between 1991 and 1995 years: " + RESET}')
    if author in ['0','']:
        return 0

    flag = 0
    duplicate = []
    for row in table:
        if row[3].isnumeric():
            if search_index(author, row[2]) != -1 and 1991 <= int(row[3]) <= 1995 :
                if row[1] not in duplicate:
                    print(f'{YELLOW + '·' + RESET}', row[1])
                duplicate.append(row[1])
                flag = 1

    if flag == 0:
        print(f'{RED + 'Error: Author not found' + RESET}')


def generator(table):
    index = list(range(len(table)))
    random.shuffle(index)
    row = table
    num = 1
    output = open('catalog.txt', 'a')
    max_author = 0
    max_name = 0
    for i in index:
        if row[i][3].isnumeric() and row[i][3] != 0:
            author = row[i][2]
            name = row[i][1]
            if len(str(name)) <= 50:
                if len(str(author)) > max_author:
                    max_author = len(str(author))
                if len(str(name)) > max_name:
                    max_name = len(str(name))

            num += 1
        if num == 21:
            break

    print(f'{YELLOW + '№'}\033[1;4H{YELLOW + 'Author' + RESET}\033[1;{max_author-4}H\
            {GREEN + 'Book' + RESET}\033[1;{max_name + max_author + 15}H{BLUE + 'Year' + RESET}')
    num_line = 1
    num = 0
    for i in index:
        if row[i][3].isnumeric() and row[i][3] != 0:
            author = row[i][2]
            name = row[i][1]
            date = row[i][3]
            if len(str(name)) <= 50 and len(str(author)) <= 50 and row[i][3] != '0':
                num_line += 1
                num += 1
                print(f'{YELLOW + str(num) + RESET}\033[{num_line};4H{str(author)}\033[{num_line};{max_author + 8}H{str(name)}\
                        \033[{num_line};{max_name + max_author + 15}H{str(date)}')
                output.write(f'{'book:' + str(name) + ' ' + 'author:' + str(author) + ' ' + 'date:' + str(date) + '\n' }')



        if num_line == 21:
            break


def xml():
    tree = ElementTree.parse('currency.xml')
    root = tree.getroot()
    print(f'{YELLOW + 'Withdrawal of currencies with a factor of 10 or 100:' + RESET}')

    num = -1
    for element in root.findall('Valute'):
        num += 1
        for child in element:
            if child.tag == 'Nominal' and (child.text == '10' or child.text == '100'):
                print(root[num][1].text)



def publisher(table):
    duplicate = []
    print(f'{YELLOW + 'Publisher:' + RESET}')

    for row in table:
            if row[4] not in duplicate and (str(row[4]).isnumeric() == False):
                print(f'{YELLOW + '·' + RESET}', row[4])
            duplicate.append(row[4])


def popular(table):
     data = sorted(open_table(), key = lambda x: (int(x[-2]), float(x[-1].replace(',', '.'))), reverse=True)
     print(f'{YELLOW + 'Popular books:' + RESET}')
     for i in range(20):
         print(f'{YELLOW + str(i+1) + ') ' + RESET + str(data[i][1])}')






while True:
    if open_table() == 0:
        break
    print(f'{YELLOW + 'Menu:' '\n' + BLUE + '1' + RESET + GREEN +'-List of popular books -Display 20 random books' + RESET +'\n'\
                                   + BLUE + '2' + RESET + GREEN +'-Search for a book by author' + RESET +'\n'\
                                   + BLUE + '3' + RESET + GREEN +'-List of popular books' + RESET +'\n'\
                                   + BLUE + '4' + RESET + GREEN +'-Withdrawal of currencies with a factor of 10 or 100' + RESET +'\n'\
                                   + BLUE + '5' + RESET + GREEN +'-List of publisher' + RESET +'\n'\
                                   + BLUE + '6' + RESET + GREEN +'-Number of books with a title lenght greater than 30 ' + RESET +'\n'\
                                   + BLUE + '0' + RESET + GREEN +'-Exit' + RESET +'\n'}')
    menu = input(f'{YELLOW + 'Select a menu item:' + RESET }')
    match menu:
        case '6':
            search_quantity(open_table())
        case '2':
            search_author(open_table())
        case '1':
            os.system('cls')
            generator(open_table())
        case '4':
            xml()
        case '5':
            publisher(open_table())
        case '3':
            popular(open_table())
        case '0':
            print(f'{BLUE + 'Goodbye!'}')
            break
        case _:
            print('No menu item, press Enter')

    print(f'{CYAN + '='*100}')








