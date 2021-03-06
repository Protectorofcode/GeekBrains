


# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

a = [1,2.5,True,"String",None]
for i in a:
    print(type(i))


# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

n = int(input("Введите размерность списка: "))
a_2 = []
for i in range(n):
    a_2.append(int(input("Введите элемент списка: ")))

i=0
for j in range(int(len(a_2)/2)):
    a_2[i], a_2[i+1] = a_2[i+1], a_2[i]
    i += 2

print(a_2)





# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

my_dict = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна",
           6: "Лето", 7: "Лето", 8: "Лето", 9: "Осень", 10: "Осень", 11: "Осень", 12: "Зима"}

n = int(input("Введите месяц в виде целого числа: "))

print(my_dict.get(n))



# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

str1 = input("Введите строку: ")
str_split = str1.split()

for ind, el in enumerate(str_split, 1):
    print(ind, el[:10])



# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением
# должен разместиться после них.

my_list = [7, 5, 3, 3, 2]
while True:
    n = int(input("Введите целое число: "))
    if n >= my_list[0]:
        my_list.insert(0,n)
    elif n <= my_list[len(my_list) - 1]:
        my_list.insert(len(my_list), n)
    else:
        r = len(my_list) - 1
        l = 0
        mid = int(r/2)
        while my_list[mid] != n and l <= r:
            if n > my_list[mid]:
                r = mid-1
            else:
                l = mid+1
                mid = int((r+l)/2)

        if my_list[mid] == n:
            my_list.insert(mid,n)
        else:
            my_list.insert(mid+1, n)

    print(my_list)




# 6. Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

goods = []
while input("Вы хотите добавить товар? да/нет: ") == 'да':
    number = int(input("Введите номер продукта: "))
    features = {}
    feature_key = input("Введите название товара: ")
    feature_price = input("Введите цену продукта: ")
    feature_number = input("Введите количество продукта: ")
    feature_kind = input("Введите единицу измерения количества продукта: ")
    features = {"название": feature_key, "цена": feature_price, "количество": feature_number,
                "ед.": feature_kind}
    goods.append(tuple([number, features]))
features = {}
#print(goods)

analytics = {}
for i in goods:
    for good_key, good_value in i[1].items():
        if good_key in analytics:
            analytics[good_key].append(good_value)
        else:
            analytics[good_key] = [good_value]

print(analytics)





