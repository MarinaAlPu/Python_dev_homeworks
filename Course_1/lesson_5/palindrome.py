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


try:
    assert is_palindrome("level") == True
    assert is_palindrome("sagas") == True
    assert is_palindrome("hero") == False
    assert is_palindrome("drama") == False

except AssertionError:
    print("Неверно, проверьте функцию на разных значениях")

else:
    print("Все хорошо, все работает")
