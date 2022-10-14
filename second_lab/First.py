#ввести диапозон чисел и вывести простые числа в этом диапозоне
def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, n):
            if n % x == 0:
                return False
        return True

def main():
    start = int(input("Введите начало диапозона: "))
    end = int(input("Введите конец диапозона: "))
    for n in range(start, end + 1):
        if is_prime(n):
            print(n, end=" ")
    print()

if __name__ == "__main__":
    main()






