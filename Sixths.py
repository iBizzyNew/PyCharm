import random
a = tuple(random.randint(-200, 200) for _ in range(10))
print(a)
for i in range(len(a)):
    if a[i] > 0:
        print(sum(a[i+1:]))
        break



