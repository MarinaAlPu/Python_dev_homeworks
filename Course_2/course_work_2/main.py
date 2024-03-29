from utils import load_random_word

from player_class import Player


MIN_QUANTITY_OF_LETTERS = 3


# Пролучить имя игрока
user_name = input("Ввведите имя игрока\n")

print(f"Привет, {user_name}!")

# Пролучить экземпляр класса Player
player = Player(user_name)

# Пролучить данные для игры
original_word_and_subwords = load_random_word()
original_word = original_word_and_subwords.original_word
quantity_of_valid_words = original_word_and_subwords.count_valid_words()


print(f"Составьте {quantity_of_valid_words} слов из слова '{original_word}'\n"
    f"Слова должны быть не короче {MIN_QUANTITY_OF_LETTERS} букв\n"
    f"Чтобы закончить игру, угадайте все слова или напишите 'stop'/'стоп'\n"
    f"Поехали, ваше первое слово?")


while player.count_used_words() < quantity_of_valid_words:
    # Получить от пользователя слово
    user_word = input()

    # Выполнить проверки
    # Если слово stop или стоп, прекратить игру и вывести статистику
    if user_word in ["stop", "стоп"]:
        break

    # Если слово короче 3 букв
    elif len(user_word) < MIN_QUANTITY_OF_LETTERS:
        print("слишком короткое слово")

    # Если слова нет в списке допустимых
    elif original_word_and_subwords.is_word_valid(user_word) is False:
        print("неверно")

    # Если слово уже было угадано пользователем
    elif player.is_new_word_used(user_word):
        print("уже использовано")

    # Если все проверки пройдены, добавить слово в список использованных слов класса Player и вывести оповещение об этом пользователю
    else:
        player.add_new_word(user_word)
        print("верно")


# Вывести количество угаданных слов
print(f"Игра завершена, вы угадали {player.count_used_words()} слов!")
