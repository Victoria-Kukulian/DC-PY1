from random import randint

def get_unique_list_numbers(start = -10, stop = 10, count = 15) -> list[int]:
    list_ = []
    if stop - start < count:
        raise ValueError("Размер списка превышает диапазон!")
    while len(list_) < count:
        new_number = randint(start, stop)
        if new_number not in list_:
            list_.append(new_number)
    return list_

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
