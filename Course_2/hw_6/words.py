import random

records = []
points_for_right_answer = 10
points = 0
number_of_games = 0
record = 0


def get_word_to_guess(words_file_name, points):
    """
    Выбирает первое слово из списка, перемешивает буквы и предлагает пользователю его отгадать
    """
    with open(words_file_name, 'r') as words_file:
        content = words_file.read().split("\n")

        for i_word in range(len(content)):
            word = content[i_word]
            i_word += 1

            # Получить слово из списка
            word_as_list = []
            for i_letter in range(len(word)):
                letter = word[i_letter]
                word_as_list.append(letter)
                i_letter += 1

            # Перемешать буквы в слове
            random.shuffle(word_as_list)

            # Предложить пользователю отгадать слово
            word_to_guess = ("".join(word_as_list))
            user_answer = input(f"Угадайте слово: {word_to_guess}\n")

            # Проверить правильность ответа пользователя
            if user_answer == word:
                print(f"Верно! Вы получаете {points_for_right_answer} очков.")
                points += points_for_right_answer
            else:
                print(f"Неверно! Верный ответ - {word}.")

    return points


def write_user_in_history(history_file_name, user_name, points):
    """
    Записывает рекорд пользователя в файл
    """
    with open(history_file_name, 'a', encoding='UTF-8') as history_file:
        history_file.write(f"\n{user_name} {points}")


def get_statistics(history_file_name):
    """
    выводит статистику из прошлых игр, с учетом последней игры
    """
    with open(history_file_name, encoding='UTF-8') as history_file:
        number_of_games = len(history_file.readlines())
        print(f"\nВсего игр сыграно: {number_of_games}")

    with open(history_file_name, encoding='UTF-8') as records_file:
        for records_data in records_file:
            name, record = records_data.rstrip("\n").split(" ")
            records.append(record)

        record_max = max(records)
        print(f"Максимальный рекорд: : {record_max}")


user_name = input("Введите ваше имя\n")

points_for_history = get_word_to_guess('words.txt', points)

write_user_in_history('history.txt', user_name, points_for_history)

get_statistics('history.txt')
