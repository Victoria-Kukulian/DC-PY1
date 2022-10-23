def get_count_char(str_):
    # TODO посчитать количество каждой буквы в строке в аргументе str_
    dict_ = {}
    new_str = str_.lower()
    for letter in new_str:
        if letter in dict_:
            dict_[letter] += 1
        elif letter.isalpha():
            dict_[letter] = 1
    return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

def get_percents(dict_):
    new_dict = {}
    for key in dict_:
        new_dict[key] = round(dict_[key] * 100 / sum(dict_.values()), 2)
    return new_dict
