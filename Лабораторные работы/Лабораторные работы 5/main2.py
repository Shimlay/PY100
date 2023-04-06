import random


def get_unique_list_numbers() -> list[int]:
    ...  # TODO написать функцию для получения списка уникальных целых чисел
    random_list = []
    while len(random_list) < 15:
        random_number = random.randint(-10, 10)
        if random_number not in random_list:
            random_list.append(random_number)
    return random_list


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

