#Напишите программу, демонстрирующую работу try\except\finally

try:
    number = int(input("Введите число: "))
    print("Введенное число:", number)
except:
    print("Преобразование прошло неудачно")
finally:
    print("Блок try завершил выполнение")
print("Завершение программы")