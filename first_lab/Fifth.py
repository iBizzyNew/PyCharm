def ret(i):
    if i == 1:
        return 'Кольцо'
    elif i == 2:
        return 'Ожерелье'
    elif i == 3:
        return 'Серьги'
    elif i == 4:
        return 'Браслет'
    elif i == 5:
        return 'Бусы'
    else:
        return 1




my_dict = {'Кольцо': ['Сплав золота,серебра,палладия,никеля и меди', 1690, 5],
           'Ожерелье': ['Сплав серебра и меди, вставки из жемчуга', 278, 42],
           'Серьги': ['Розовое золото с вставками из фионита', 362, 61],
           'Браслет': ['Бронза(сплав меди и алюминия)', 135, 50],
           'Бусы': ['Янтарь, пластик, текстиль', 50, 108]}
sum = 0
while True:
    print('''    1. Описание материала изделия
    2. Цена изделия
    3. Количество оставшегося товара
    4. Просмотр всей информации
    5. Покупка
    6. До свидания''')
    ch = int(input('Ваш выбор: '))
    if ch != 6 and ch != 4 and ch in range(1, 6):
        print('1.Кольцо 2.Ожерелье 3.Серьги 4.Браслет 5.Бусы')
    if ch == 1:
        s = int(input('Ваш выбор: '))
        if ret(s) ==1 :
            print('Неверный выбор')
        else:
            print('Состав. ', ret(s), ':', my_dict[ret(s)][0])
    elif ch == 2:
        s = int(input('Ваш выбор: '))
        if ret(s) == 1:
            print('Неверный выбор')
        else:
            print('Цена. ', ret(s), ':', my_dict[ret(s)][1])
    elif ch == 3:
        s = int(input('Ваш выбор: '))
        if ret(s) == 1:
            print('Неверный выбор')
        else:
            print('Количество товара. ', ret(s), ':', my_dict[ret(s)][2])
    elif ch == 4:
        for i in my_dict:
            print(i, ':', my_dict[i])
    elif ch == 5:
        s = int(input('Что желаете приобрести? 0 — выход из покупок '))
        if ret(s) == 1:
            print('Неверный выбор')
        else:
            while s != 0:
                while ret(s) not in my_dict:
                    print('К сожалению, такого товара нет')
                    s = int(input('Что желаете приобрести? '))
                count = int(input('Введите желаемое количество: '))
                while count > my_dict[ret(s)][2]:
                    print('К сожалению, в данный момент такого количества товара нет')
                    count = int(input('Введите желаемое количество: '))
                price = count * my_dict[ret(s)][1]
                print('За', ret(s), 'Вы должны', price,'белорусских рубля(-ей)')
                my_dict[ret(s)][2] -= count
                break
    elif ch == 6:
        break
    else:
        print('Неверное значение')