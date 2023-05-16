# Константы, переменные
WORDS = 5
LEVELS = ["легкий", "средний", "сложный"]

levels_for_select = {
    "easy": "легкий",
    "medium": "средний",
    "hard": "сложный",
}

words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}

words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}

words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}

levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично",
}

words_all = {
    "easy": words_easy,
    "medium": words_medium,
    "hard": words_hard,
}

words = {}
answers = {}
right_answered_words = []
wrong_answered_words = []

# user_try = 2
user_input = None
edited_user_input = None
letter_unneeded = "ё"
letter_needed = "е"
dict_name = "words"
correct = "Правильно отвечены слова:"
incorrect = "Неправильно отвечены слова:"
amount_right_answered_words = 0


levels_for_intro = ", ".join(LEVELS)

print(f"Выберите уровень сложности: {levels_for_intro}.\n")

# Получить у пользователя уровень сложности
user_input = input().lower()

# Проверить введённое значение на наличие буквы "ё" и заменить её на букву "е"
if letter_unneeded in user_input:
    edited_user_input = user_input.replace(letter_unneeded, letter_needed)
else:
    edited_user_input = user_input


# Положить в словарь words один из словарей в зависимости полученного от пользователя уровня сложности
for level_en, level_ru in levels_for_select.items():
    if edited_user_input == level_ru:
        words = words_all[level_en]
        # print(words)
        break
    else:
        pass
        # user_input = input(f"\nТакого уровня не существует.\nВыберите уровень сложности из следующих: {levels_for_intro}.\n").lower()


user_input = input(f"\nВыбран уровень сложности {edited_user_input}, мы предложим {WORDS} слов, подберите перевод.\nНажмите Enter.")


# Запустить цикл по пяти словам из словаря words
for word, translation in words.items():
# Получить у пользователя ответ
    user_input = input(f"{word}, {len(translation)} букв, начинается на {translation[0]}: ")
    # print(user_input)
    if user_input.lower() == translation:
# Записать результат в answers
        answers[word] = True
        print(f"Верно, {word.title()} — это {translation}.")
    else:
        answers[word] = False
        print(f"Неверно, {word.title()} — это {translation}.")


# print(f"\nПечатаю словарь с ответами {answers}")


# Когда слова закончились, вывести правильно и неправильно отвеченные слова
for key, value in answers.items():
        if value == True:
            right_answered_words.append(key)
        else:
            wrong_answered_words.append(key)


# Список правильно отвеченных слов
print(f"\n{correct}:")
for i in range(len(right_answered_words)):
    print(right_answered_words[i])


# Список неправильно отвеченных слов
print(f"\n{incorrect}:")
for i in range(len(wrong_answered_words)):
    print(wrong_answered_words[i])


# Посчитать количество правильно отгаданных слов, например, получив список ключей из answers
for value in answers.values():
    if value == True:
        amount_right_answered_words += 1

# amount_right_answered_words = len(right_answered_words)
# amount_right_answered_words = len(list(answers.keys()))
# print(amount_right_answered_words)


# Вывеcти ранг пользователя, используя в качестве ключа количество правильно отгаданных слов
for key, level in levels.items():
    if key == amount_right_answered_words:
        print(f"\nВаш ранг: {level}.")
