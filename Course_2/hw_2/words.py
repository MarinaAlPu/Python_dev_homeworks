import random


points_for_right_answer = 10
points = 0
number_of_games = 0


def get_word_to_guess(words_file_name, points):
    """
    Выбирает первое слово из списка, перемешивает буквы и предлагает пользователю его отгадать.
    """
    with open(words_file_name, 'r') as words_file:
        content = words_file.read().split("\n")
        # print(f"Содержимое документа words.txt: {content}")

        for i_word in range(len(content)):
            word = content[i_word]
            # print(f"Слово номер {i_word} в документе: words.txt {word}")
            i_word += 1

            # сделать из слова список букв
            word_as_list = []
            for i_letter in range(len(word)):
                # print(f"Длина слова: {len(word)}")
                letter = word[i_letter]
                # print(f"Буква {letter} из слова {word}")
                word_as_list.append(letter)
                # print(f"Список из букв по порядку {word_as_list}")
                i_letter += 1
            # print(f"Финальный список из букв по порядку {word_as_list}")

            # перемешать буквы в слове - написать такую функцию
            random.shuffle(word_as_list)
            # print(f"В слове {word} перемешали буквы и получилось {word_as_list}")

            # Предложить пользователю отгадать слово
            word_to_guess = ("".join(word_as_list))
            user_answer = input(f"Угадайте слово: {word_to_guess} ")

            # Проверить слово
            if user_answer == word:
                print(f"Верно! Вы получаете {points_for_right_answer} очков.")
                points += points_for_right_answer
                # print(f"Суммарное количество очков: {points}.")
            else:
                print(f"Неверно! Верный ответ - {word}.")
                # print(f"Суммарное количество очков: {points}.")
    return points


def write_user_in_history(history_file_name, user_name, points):
    """
    Записывает рекорд пользователя в файл.
    """
    with open(history_file_name, 'a', encoding='UTF-8') as history_file:
        history_file.write(f"\n{user_name} {points}")


def get_statistics(history_file_name):
    """
    выводит статистику из прошлых игр, с учетом последней игры.
    """
    with open(history_file_name, encoding='UTF-8') as history_file:
        # content_history = history_file.read()
        """
        После прочтения файла в строке 65 , указатель устанавливается на его конец и дальше ему читать уже нечего.
        Попробуй использовать seek(0) чтобы перевести указатель на начало файла
        """
        # print(f"Содержимое документа history.txt:\n{content_history}")
        # games_list = history_file.readlines()
        number_of_games = len(history_file.readlines())
        # print(f"Список строк: {games_list}")
        print(f"Всего игр сыграно: {number_of_games}")

    with open(history_file_name, encoding='UTF-8') as records_file:
        record = 0
        for data in records_file:
            pass


user_name = input("Введите ваше имя\n")

points_for_history = get_word_to_guess('words.txt', points)

write_user_in_history('history.txt', user_name, points_for_history)

get_statistics('history.txt')

# Вывести статистику из прошлых игр с учётом этой игры
# Всего игр сыграно: 27
# Максимальный рекорд: 200

# with open('history.txt', encoding='UTF-8') as history_file:

#     content_history = history_file.read()
#     print(f"Содержимое документа history.txt:\n{content_history}")
#     games_list = history_file.readlines()
#     number_of_games = len(history_file.readlines())
#     print(f"Список строк: {games_list}")
#     print(f"Всего игр сыграно: {number_of_games}")




    # content_history_1 = history_file.read().split("\n")
    # print(f"Содержимое документа history.txt в виде списка:\n{content_history_1}")
    #
    # for users_data in history_file:
    #     name, user_points = users_data.rstrip("\n").split(" ")
    #     print(f"Игрок {name} набрал {user_points} очков")


