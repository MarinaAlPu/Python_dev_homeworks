from utils import load_random_word

from basic_word_class import BasicWord
from player_class import Player

MIN_QUANTITY_OF_LETTERS = 3

# user_name = input("Ввведите имя игрока\n")

# print(f"Привет, {user_name}!")

player = Player("PLAYER")#"(user_name)
# print(player)

original_word = load_random_word().original_word
# quantity_of_valid_words = len(load_random_word().valid_words)

quantity_of_valid_words = load_random_word().count_valid_words()

print(f"Составьте {quantity_of_valid_words} слов из слова '{original_word}'\n"
    f"Слова должны быть не короче {MIN_QUANTITY_OF_LETTERS} букв\n"
    f"Чтобы закончить игру, угадайте все слова или напишите 'stop'\n"
    f"Поехали, ваше первое слово?")

for i in range(quantity_of_valid_words):

# Получить от пользователя слово
user_word = input()
used_words = []
# Выполнить проверки
## Если слово короче 3 букв – это неудачное слово
# Пользователь: мя
# Программа: слишком короткое слово
if len(user_word) < MIN_QUANTITY_OF_LETTERS:
    print("слишком короткое слово")

## Если слова нет в списке допустимых у BasicWord – это неудачное слово
# Пользователь: ъуъ
# Программа: неверно
# load_random_word().is_word_valid(user_word)
# print(load_random_word().valid_words)
# print(load_random_word().is_word_valid(user_word))

elif load_random_word().is_word_valid(user_word): # == True:
    print("неверно")

## Если слово уже было угадано пользователем (Player) – это неудачное слово
# Пользователь: руна
# Программа: уже использовано
elif user_word in used_words:
    print("уже использовано")

## Если слово stop или стоп, то игра прекращается
# Пользователь: стоп
# Программа: (выводит статистику, см шаг 6)
# Программа: Игра завершена, вы угадали 8 слов!
elif user_word in ["stop", "стоп"]:
    print("уже использовано")


# Если все проверки выше пройдены, то слово хорошее, его нужно добавить слово в список использованных слов класса Player и вывести оповещение об этом пользователю:
# Пользователь: руна
# Программа: верно
else:
    used_words = player.add_new_word(user_word)
    print("верно")



# Шаг 6
#Выведите количество угаданных слов. Информацию получите из экземпляра класса Player.
# Программа: Игра завершена, вы угадали 8 слов!




