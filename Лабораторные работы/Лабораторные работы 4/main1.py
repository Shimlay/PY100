main_str = """
        Данное предложение будет разбиваться на отдельные слова. 
        В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
        Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
    """


def get_count_char(str_):
    # TODO посчитать количество каждой буквы в строке в аргументе str_
    string = main_str.lower()
    char_dict = {}
    for char in string:
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict


def percent_chars(char_dict):
    total_chars = sum(char_dict.values())
    percent_dict = {}
    for char, count in char_dict.items():
        percent = (count / total_chars) * 100
        percent_dict[char] = percent
    return percent_dict


print(get_count_char(main_str))
