#Напишите функцию, которая будет принимать один аргумент. Если в
#функцию передаётся множество, то найти произведение всех его чисел.
#Если список, то удалить все нулевые элементы, найти произведение
#между первым и вторым положительными элементами.
#Число – определить количество разрядом.
#Строка – найти количество чисел в строке.
#Сделать проверку со всеми этими случаями

def func(a):
    if type(a) == set:
        pr = 1
        number = 0
        for i in a:
            if i.isdigit():
                number += 1
                pr *= int(i)
        if number == 0:
            print('В множестве нет чисел')
        elif number == 1:
            print('В множестве только одно число')
        else:
            print('Произведение всех чисел множества = ', pr)
    elif type(a) == list:
        i = 0
        buf = a.count('0')
        while i < buf:
            a.remove('0')
            i += 1
        print('Новый список без нулей: ', a)
        pr = 1
        number = 0
        for i in a:
            if i.isdigit() and int(i) > 0 and number < 2:
                pr *= int(i)
                number += 1
        if number < 2:
            print('В списке недостаточно таких чисел')
        else:
            print('Произведение между первым и вторым положительными элементами = ', pr)
    elif type(a) == int:
        counter = 0
        while a > 1:
            a /= 10
            counter += 1
        print('Количесво разрядов числа = ', counter)
    elif type(a) == str:
        kol = 0
        for i in a:
            if i.isdigit():
                kol += 1
        print('Количество чисел в строке = ', kol)


print('Что хотите ввести?\n'
      '1. Множество\n'
      '2. Список\n'
      '3. Число\n'
      '4. Строка\n'
      '0. Конец')
while 1:
    while 1:
        try:
            choise = int(input('Ваш выбор: '))
        except ValueError:
            print('Необходимо ввести число!')
        else:
            break
    if choise == 1:
        a = set(input('Введите множество: '))
        func(a)
    elif choise == 2:
        a = list(input('Введите список: '))
        func(a)
    elif choise == 3:
        while 1:
            try:
                a = int(input('Введите число: '))
            except ValueError:
                print('Необходимо ввести число!')
            else:
                break
        func(a)
    elif choise == 4:
        a = input('Введите строку: ')
        func(a)
    elif choise == 0:
        break
    else:
        print('Неверное значение!')