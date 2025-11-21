from string import ascii_lowercase, ascii_uppercase, digits #английский алфавит
import random # с помощью этого модуля будем генерировать слуяайные строки
from timeit import default_timer # подсчет времени работы программы


ALPHABET = ascii_lowercase + ascii_uppercase + digits + 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮйцукенгшщзхъфывапролджэячсмитьбю' #алфавит для строк


# функция подсчета процента строчных букв в строке
def count_lowercase_in_percent(string: str) -> float:
    # делаем строку без пробелов, что не исказить результат
    string = "".join(char for char in string if char.isalpha())
    count_lowercase = 0
    for char in string:
        if char.islower():
            count_lowercase += 1

    percent_lowercase = (count_lowercase / len(string)) * 100

    return percent_lowercase


# функция для создания случайных строк из алфавита
def create_string(n: int) -> str:
    result = ''
    for i in range(n):
        result += random.choice(ALPHABET)
    return result


# функция проверяет какое задание надо выполнить
def choise_client(choise):
    if choise == '2': # проверка на время выполнения
        ur_string = create_string(int(input('Введите число символов в строке: ')))
        start_time = default_timer()
        print(f"Процент строчных букв в строке: {ur_string}")
        print(f"{count_lowercase_in_percent(ur_string)} %")
        end_time = default_timer()
        print(f"Время исполнения программы: {round(end_time - start_time, 5)} сек.")
    elif choise == '1': # проврека на работоспособность
        ur_string = str(input("Введите вашу строку: "))
        print(f"Процент строчных букв в строке: {ur_string}")
        print(f"{count_lowercase_in_percent(ur_string)} %")


choise = str(input("Введите: 1, если надо выполнить первое задание, 2, если надо выполнить второе задание: "))
choise_client(choise)
