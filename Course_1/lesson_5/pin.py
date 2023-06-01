"""
Функция должна возвращать True, если pin — это строка из 4 цифр, иначе — False.
"""


def check_pin(pin):
    if pin.isdigit() and len(pin) == 4:
        return True
    else:
        return False


# try:
#     assert check_pin("1234") == True
#     assert check_pin("123") == False
#     assert check_pin("a000") == False
#     assert check_pin("0000") == True
# except AssertionError:
#     print("Неверно, проверьте функцию на разных значениях")
# else:
#     print("Все хорошо, все работает")