# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


list1 = [2, 3, 4, 5, 6]
n = len(list1)
list2 = []
k=int(len(list1)/2+len(list1)%2)
len(list2)==k
for i in range(k):
    list2.append((list1[i]*list1[n-1-i]))
print(list2)
