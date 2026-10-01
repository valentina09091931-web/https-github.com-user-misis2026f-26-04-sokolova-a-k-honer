while True:
    print('Выберите уровень:')
    level = input()
    if 1 <= int(level) <= 5 or int(level) == 10:
        if int(level) == 1:
            print('Введите строку')
            a = input()
            print('Выберите способ преобразования:')
            print('1 - в верхний регистр, 2 - в нижний, 3 - все, кроме первой буквы в нижний')
            c = input()
            if int(c) == 1:
                print(a.upper())
            elif int(c) == 2:
                print(a.lower())
            elif int(c) == 3:
                a1=a[1:]
                print(a[0]+a1.lower())
        elif int(level) == 2:
            print('Введите строку')
            a = input()
            print('Выберите действие:')
            print('1 - найти каким по счету "круто"')
            print('2 - заменить "круто" на любое слово')
            print('3 - посчитать буквы "о"')
            c2 = input()
            if int(c2) == 1:
                print(a.find('круто'))
            elif int(c2) == 2:
                print('Введите слово, на которое нужно заменить слово "круто"')
                word = input()
                a = a.replace('круто', word)
                print(a)
            elif int(c2) == 3:
                print(a.count('о'))
        elif int(level) == 3:
            print('Введите строку, которую Вы хотите "распилить" или "соединить" ')
            a = input()
            print('Выберите действие:')
            print('1 - пилим, 2 - пилим и соединяем')
            c3 = input()
            if int(c3) == 1:
                print('Введите символ, который является разделителем:')
                symb = input()
                spisok = a.split(symb)
                print(spisok)
            elif int(c3) == 2:
                print('Введите символ, который является разделителем сейчас:')
                symb = input()
                a = a.split(symb)
                print('Введите новый разделитель')
                symb2 = input()
                a = symb2.join(a)
                print(a)
        elif int(level) == 4:
            print('Введите строку')
            a = input()
            print('Выберите действие:')
            print('1 - проверить, является ли строка числом или строкой')
            print('2 - откинуть часть строки')
            c4 = input()
            if int(c4) == 1:
                if int(a)==a:
                    print('Строка является числом')
                elif str(a)==a:
                    print('Строка является словом')
                else:
                    print('Строка смешанного типа')
        elif int(level) == 5:
            print('Введите строку ')
            a = input()
            print('Выберите действие:')
            print('1 - разделить строку по пробелам на отдельные слова')
            print('2 - разделить строку по нижнему подчерк на отдельные слова')
            print('3 - разделить строку по пробелам на отдельные слова и поочередно поменять регистр')
            c3 = input()
            if int(c3) == 1:
                a1=a.split()
                for r in a1:
                    print(r)
            if int(c3) == 2:
                a1=a.split('_')
                for r in a1:
                    print(r)
            if int(c3) == 3:
                a1=a.split()
                for r in range(0,len(a1)):
                    if r%2==0:
                        print(a1[r].upper())
                    if r%2==1:
                        print(a1[r].lower())
        break
