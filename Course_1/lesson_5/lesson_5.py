# def check_pin(pin):
#     if pin.isdigit() and len(pin) == 4:
#         return True
#     else:
#         return False


# try:
#     assert check_pin("1234") == True
#     assert check_pin("123") == False
#     assert check_pin("a000") == False
#     assert check_pin("0000") == True
# except AssertionError:
#     print("Неверно, проверьте функцию на разных значениях")
# else:
#     print("Все хорошо, все работает")

#####################

"""
Чтобы проверить, является ли строка палиндромом, уберите из нее пробелы,
приведите к нижнему регистру, затем проверьте,
что инвертированная строка (reversed_str = str[::-1]) равна оригинальной строке. Например:
level — True
sagas — True
hero — False
drama — False
"""


def is_palindrome(word):
    print(word)
    string = word.replace(" ", "")
    print(string)
    string = string.lower()
    print(string)

    reversed_str = string[::-1]
    print(reversed_str)

    if string == reversed_str:
        return True
    else:
        return False



# try:
#     assert is_palindrome("level") == True
#     assert is_palindrome("sagas") == True
#     assert is_palindrome("hero") == False
#     assert is_palindrome("drama") == False

# except AssertionError:
#     print("Неверно, проверьте функцию на разных значениях")

# else:
#     print("Все хорошо, все работает")

# ####################


"""
принимает целое число от 2 до 5 и возвращает оценку. Например:
2 — Плохо
3 — Удовлетворительн
4 — Хорошо
5 — Отлично
Другое — Ошибка
"""


# def get_grade(grade):
#     if isinstance(grade, int):
#         if grade == 2:
#             return "Плохо"
#         elif grade == 3:
#             return "Удовлетворительно"
#         elif grade == 4:
#             return "Хорошо"
#         elif grade == 5:
#             return "Отлично"
#         else:
#             return "Ошибка"


# try:
#     assert get_grade(2) == "Плохо"
#     assert get_grade(3) == "Удовлетворительно"
#     assert get_grade(4) == "Хорошо"
#     assert get_grade(5) == "Отлично"
#     assert get_grade("") == "Ошибка"
# except AssertionError:
#     print("Неверно, проверьте функцию на разных значениях")
# else:
#     print("Все хорошо, все работает")

#########################

from pin import check_pin

print("Введите ваш ПИН-код")

user_input = input()

# pin_code = check_pin(user_input)


if check_pin(user_input):
    print("Такой ПИН-код подходит")
else:
    print("Такой ПИН-код НЕ подходит")
