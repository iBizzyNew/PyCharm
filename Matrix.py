import random

def RandomMatrix():
    a = int(input('Введите количество строк: '))
    b = int(input('Введите количество столбцов: '))
    Matrix = [[random.randint(-100, 100) for _ in range(b)] for _ in range(a)]
    return Matrix

def PrintMatrix(Matrix):
    for i in Matrix:
        print(i)

def main():

        Matrix = RandomMatrix()
        PrintMatrix(Matrix)

        Matrix = RandomMatrix()
        PrintMatrix(Matrix)

if __name__ == '__main__':
    main()







