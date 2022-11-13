#TODO написать функцию для получения списка уникальных целых чисел
from random import randint


def get_unique_list_numbers() -> list[int]:
    size = 15
    min_ = -10
    max_ = 10
    list_unique_num = []
    while len(list_unique_num) != size:
        rand_val = randint(min_, max_)
        if rand_val not in list_unique_num:
            list_unique_num.append(rand_val)
    return list_unique_num


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
