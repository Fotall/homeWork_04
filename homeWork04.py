# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке
# возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

n = int(input('Введите кол-во элементов первого множества: '))
m = int(input('Введите кол-во элементов второго множества: '))
import random
first_str = [chr(random.randint(48, 57)) for _ in range(n)]
second_str = [chr(random.randint(48, 57)) for _ in range(m)]
print(*first_str)
print(*second_str)
count_dict = {}
for letter in first_str:
    for letter_2 in second_str:
        if letter == letter_2:
            if letter not in count_dict:
                count_dict[letter] = 1
            else:
                count_dict[letter] += 1
#print(count_dict)
sorted_count_dict = sorted(count_dict.items(), key = lambda x: x[0])
dict(sorted_count_dict)
print(*sorted_count_dict)

# задача 2 про кусты
n = int(input())
arr = list()
for i in range(n):
    x = int(input())
    arr.append(x)
arr_count = list()
for i in range(len(arr) - 1):
    arr_count.append(arr[i - 1] + arr[i] + arr[i + 1])
arr_count.append(arr[-2] + arr[-1] + arr[0])
print(max(arr_count))