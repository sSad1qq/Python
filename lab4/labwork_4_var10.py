import string
import random
from timeit import default_timer


ALPHABET = string.ascii_lowercase + string.ascii_uppercase + string.digits


def replace_z(string):
    return string.replace('z', 'zet')


def create_string(n: int) -> str:
    res = ''
    for _ in range(n):
        res += random.choice(ALPHABET)
    return res

print(ALPHABET)
n = int(input("Введите кол-во символов в строке: "))
ur_string = create_string(n)
start_time = default_timer()
print(f'Исходная строка: {ur_string}')
print(f'Строка после замены: {replace_z(ur_string)}')
end_time = default_timer()
print(f"Время исполнения программы: {end_time - start_time} сек.")
