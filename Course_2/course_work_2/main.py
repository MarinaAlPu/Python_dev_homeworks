from utils import load_random_word

# from basic_word_class import BasicWord
from player_class import Player

MIN_QUANTITY_OF_LETTERS = 3
i = 0
used_words = []

# user_name = input("Ввведите имя игрока\n")

# print(f"Привет, {user_name}!")

player = Player("PLAYER")#"(user_name)
# print(player)


original_word_and_subwords = load_random_word()
print(original_word_and_subwords)

original_word = original_word_and_subwords.original_word
print(original_word)

# quantity_of_valid_words_1 = len(original_word_and_subwords.valid_words)
# print(quantity_of_valid_words_1)

quantity_of_valid_words = original_word_and_subwords.count_valid_words()
print(quantity_of_valid_words)

print(f"Составьте {quantity_of_valid_words} слов из слова '{original_word}'\n"
    f"Слова должны быть не короче {MIN_QUANTITY_OF_LETTERS} букв\n"
    f"Чтобы закончить игру, угадайте все слова или напишите 'stop'/'стоп'\n"
    f"Поехали, ваше первое слово?")


while player.count_used_words() < quantity_of_valid_words:
# for i in range(quantity_of_valid_words):
    # Получить от пользователя слово
    user_word = input()

    # Выполнить проверки
# ## Если слово stop или стоп, прекратить игра
# # Пользователь: стоп
# # Программа: (выводит статистику, см шаг 6)
# # Программа: Игра завершена, вы угадали 8 слов!
    if user_word in ["stop", "стоп"]:
        print(f"Игра завершена, вы угадали {player.count_used_words()} слов!")
        quit()

    ## Если слово короче 3 букв – это неудачное слово
    elif len(user_word) < MIN_QUANTITY_OF_LETTERS:
        print("слишком короткое слово")

    # ## Если слова нет в списке допустимых у BasicWord – это неудачное слово
    elif original_word_and_subwords.is_word_valid(user_word) != True:
        # print(original_word)
        # print()
        print("неверно")

    # ## Если слово уже было угадано пользователем (Player) – это неудачное слово
    elif user_word in used_words:
        print("уже использовано")

    # # Если все проверки пройдены, добавить слово в список использованных слов класса Player и вывести оповещение об этом пользователю
    else:
        used_words = player.add_new_word(user_word)
        print(used_words)
        print("верно")
    i += 1


# Шаг 6
#Вывести количество угаданных слов. Информацию получите из экземпляра класса Player.
print(f"Игра завершена, вы угадали {player.count_used_words()} слов!")

quit()
