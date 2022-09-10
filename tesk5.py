# Задайте число.Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так:
#  [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Введите число: '))


def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1)+fib(n-2)


set1 = [0]
set2 = []
for i in range(1, 10):
    set1.append(fib(i))
    set2.append(fib(i)*-1)
for i in range(len(set2)):
    if i%2==0:
        set2[i]= -set2[i]
set3 = set2[::-1]
print(set3+set1)

