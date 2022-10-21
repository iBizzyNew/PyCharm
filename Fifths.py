import math

toys = {'Автомат': 'пластик', 'Мячик': 'каучук', 'Попрыгунчик': 'резина'}
toys1 = {'Автомат': 10, 'Мячик': 5, 'Попрыгунчик': 50}
toys2 = {'Автомат': 10, 'Мячик': 5, 'Попрыгунчик': 10}
choice = 50
list = ['Автомат', 'Мячик', 'Попрыгунчик']
print('1.  Просмотр описания: название – описание.')
print('2.  Просмотр цены: название – цена.')
print('3.  Просмотр количества: название – количество.')
print('4.  Всю информацию.')
print('5.  Покупка')
print('6.  Вызов меню.')
print('7.  До свидания')
while (choice != 7):
    choice = int(input('Ваш выбор: '))
    if choice == 6:
        print('1.  Просмотр описания: название – описание.')
        print('2.  Просмотр цены: название – цена.')
        print('3.  Просмотр количества: название – количество.')
        print('4.  Всю информацию.')
        print('5.  Покупка')
        print('6.  Вызов меню.')
        print('7.  До свидания')
    if choice == 4:
        for i in range(3):
            str = list[i]
            print()
            print(str, 'Материал', 'Цена', 'Кол-во')
            print('     ', toys[str], '  ', toys1[str], ' ', toys2[str])
            print()
    if choice == 1:
        str = input('Введите название товара: ')
        print('Состав: ', toys[str])
    if choice == 2:
        str = input('Введите название товара: ')
        print('Цена: ', toys1[str])
    if choice == 3:
        str = input('Введите название товара: ')
        print('Кол-во: ', toys2[str])
    if choice == 5:
        str = input('Введите название товара: ')
        print('На складе есть: ', toys2[str])
        k = int(input('Введите кол-во: '))
        if k > toys2[str]:
            print('На складе недостаточно товара')
            print('Желаете продолжить покупку?')
            print('1. Да')
            print('2. Нет')
            choice2 = int(input())
            if choice2 == 1:
                print('На складе есть: ', toys2[str])
                k = int(input('Введите кол-во: '))
                while (k > toys2[str]):
                    print('На складе есть: ', toys2[str])
                    k = int(input('Введите правильное кол-во: '))
                sum = 0
                sum = sum + k * toys1[str]
                print('Стоимость:', sum)
                print('Спасибо за покупку!')
                toys2[str] = toys2[str] - k
        else:
            sum = 0
            sum = sum + k * toys1[str]
            print('Стоимость:', sum)
            print('Спасибо за покупку!')
            toys2[str] = toys2[str] - k

def input_int(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return userInput
            break

