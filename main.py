# Пересечение двух неупорядоченных наборов целых чисел

# Инструкция по использованию платформы



# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# На вход подается 2 числа через пробел: n m
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо


var1 = '5 5'
var2 = '10 20 30 40 50'
var3 = '10 20 30 40 50'

# Введите ваше решение ниже

new2 = var2.replace(",")

print(new2)
a = set(var2)
b = set(var3)



i = a.intersection(b)
f = sorted(i)
print(i)

print(*f)

# Решение от автора задачи
mol = [int(x) for x in var1.split()]
n = mol[0]
m = mol[1]
set_1 = set()
set_2 = set()
list_1 = list()
a = [int(x) for x in var2.split()]
k = set(a)
for i in k:
   set_1.add(i)
b = [int(x) for x in var3.split()]
k1 = set(b)
for i in k1:
   set_2.add(i)
lok = set_1 & set_2
kool = list(lok)
kool.sort()
for i in kool:
   print(i, end=' ')

