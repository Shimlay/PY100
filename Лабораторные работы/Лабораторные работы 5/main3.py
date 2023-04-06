import random
import string


def get_random_password(length=8) -> str:
    ...  # TODO написать функцию генерации случайных паролей
    alphabet = string.ascii_letters + string.digits
    return ''.join(random.sample(alphabet, length))


print(get_random_password())
