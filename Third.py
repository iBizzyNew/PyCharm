import random
a = [random.randint(-123, 123) for _ in range(10)]
print(a)
print(max(a))
a.remove(max(a))
print(a)

def Summa(List):
    Sum = 0
    for i in range(1, len(List), 2):
        Sum += List[i]
    return Sum



