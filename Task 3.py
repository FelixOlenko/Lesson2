#3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму

num = int(input())

list = []
for i in range(1, num + 1):
    res = 1 + 1/i ** i
    print(res)

    