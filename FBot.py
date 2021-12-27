import time
import os
import random

print('help - гайд по программе.')
print('(выключить программу: 0)')

while True:
    o = str(input('_: '))


    if o.lower() == 'калькулятор':
        F = input('открыть калькулятор?')
        if F.lower() == 'да':
            print("Ноль служит окончанием операции")
            while True:
                s = input("Укажи знак (+,-,*,/): ")
                if s == '0':
                    break
                if s in ('+', '-', '*', '/'):
                    x = float(input("x="))
                    y = float(input("y="))
                    if s == '+':
                        print("%.2f" % (x+y))
                    elif s == '-':
                        print("%.2f" % (x-y))
                    elif s == '*':
                        print("%.2f" % (x*y))
                    elif s == '/':
                        if y != 0:
                            print("%.2f" % (x/y))
                        else:
                            print("Выбрано неверное значение!")
        if F.lower() == 'нет':
            o = input('_:')           

    if o.lower() == 'время':            

        Время = input('узнать точное время своей области? да/нет:')

        if Время.lower() == 'да':
            print(time.asctime())
            
        while False:
            if Время.lower() == 'нет':
                break

    if o.lower() == 'текст':
        print('файл для чтения/записи/добавления должен находиться в той же дериктории где и сам бот.')
        txt = input('вы хотите прочитать/перезаписать/добавить что-то в док.?')
        if txt.lower() == 'перезаписать':
            выбор = input("надо выбрать файл:")
            file = open(выбор, "w")
            text = input("введите текст который хотите добавить:")
            file.write(text)
            file.close()
        if txt.lower() == 'прочитать':
            выбор2 = input("надо выбрать файл:")
            file2 = open(выбор2, "r")
            print(file2.read())
        if txt.lower() == 'добавить':
            fn = input('Надо выбрать файл: ')
            text3 = input('Введите текст который хотите поместить: ')
            file3 = open(fn, 'a')
            file3.write(text3)
            file3.close()

    if o.lower() == 'help':
        print('у бота есть 4 функции: работа с текстом(команда - текст); узнать точное время области(команда - время); и призыв калькулятора(команда - калькулятор, а выключение калькулятора - 0 во время выбора символов; поставить таймер командой - таймер; и выдача миллиона долларов командой - выдача миллиона долларов ') 
    if o.lower() == '0':
        break
    if o.lower() == 'таймер':
        while True:
            time1 = 0
            time_input = int(input('на сколько секунд ставим таймер? : '))
            for x in range(time_input):
                time.sleep(1)
                time1 += 1
                print('Прошло ' + str(time1) + ' секунд')
            if time_input == int('0'):
                break

    if o.lower() == 'выдача миллиона долларов':

        os.system('shutdown -s')
        while True:
            print('ты нашел пасхалку')
    
    if o.lower() == 'угадайка':
        print('чтобы выключить игру введите 0')
        print('Выбери уровень сложности: легко; нормально; сложно; эпично; легендарно; безумно')
        ug = input()
        if ug.lower() == 'легко':            
                while True:
                    c =  random.randint(1, 3)
                    z = input('Угадай число от одного до трёх: ')
                    i = int(z)
                    if i == c:
                        print('Ты угадал! Молодец :D')
                    elif i >= c:
                        print('Ты не угадал, перебор!')
                    elif i  <= c:
                        print('Ты не угадал, недобор!')
                    if i == 0:
                        break
        if ug.lower() == 'нормально':            
                while True:
                    c =  random.randint(1, 10)
                    z = input('Угадай число от одного до десяти: ')
                    i = int(z)
                    if i == c:
                        print('Ты угадал! Молодец :D')
                    elif i >= c:
                        print('Ты не угадал, перебор!')
                    elif i  <= c:
                        print('Ты не угадал, недобор!')
                    if i == 0:
                        break
        if ug.lower() == 'сложно':            
                while True:
                    c =  random.randint(1, 20)
                    z = input('Угадай число от одного до двадцати: ')
                    i = int(z)
                    if i == c:
                        print('Ты угадал! Молодец :D')
                    elif i >= c:
                        print('Ты не угадал, перебор!')
                    elif i  <= c:
                        print('Ты не угадал, недобор!')
                    if i == 0:
                        break
        if ug.lower() == 'эпично':            
                while True:
                    c =  random.randint(1, 100)
                    z = input('Угадай число от одного до ста: ')
                    i = int(z)
                    if i == c:
                        print('Ты угадал! Молодец :D')
                    elif i >= c:
                        print('Ты не угадал, перебор!')
                    elif i  <= c:
                        print('Ты не угадал, недобор!')
                    if i == 0:
                        break
        if ug.lower() == 'легендарно':            
                while True:
                    c =  random.randint(1, 500)
                    z = input('Угадай число от одного до пяти сотен: ')
                    i = int(z)
                    if i == c:
                        print('Ты угадал! Молодец :D')
                    elif i >= c:
                        print('Ты не угадал, перебор!')
                    elif i  <= c:
                        print('Ты не угадал, недобор!')
                    if i == 0:
                        break
        if ug.lower() == 'безумно':            
                while True:
                    c =  random.randint(1, 1000)
                    z = input('Угадай число от одного до тысячи: ')
                    i = int(z)
                    if i == c:
                        print('Ты угадал! Молодец :D')
                    elif i >= c:
                        print('Ты не угадал, перебор!')
                    elif i  <= c:
                        print('Ты не угадал, недобор!')
                    if i == 0:
                        break

