#Найти в матрице первый столбец, все элементы которого отрицательны, и среднее арифметическое этих элементов
import random

def main():
    n = int(input("Введите размер матрицы: "))
    matrix = [[random.randint(-10, 10) for _ in range(n)] for _ in range(n)]
    for row in matrix:
        print(row)
    print()
    for j in range(n):
        is_negative = True
        for i in range(n):
            if matrix[i][j] >= 0:
                is_negative = False
                break
        if is_negative:
            print("Столбец", j)
            break
    else:
        print("Нет отрицательных столбцов")

if __name__ == "__main__":
    main()
    

