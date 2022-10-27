a = input("Введите число: ")
even = 0
odd = 0
for i in a:
    if int(i) % 2 == 0:
        even += 1
    else:
        odd += 1
print("Четных: %d, Не четных: %d" % (even, odd))
