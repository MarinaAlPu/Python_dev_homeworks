# Переменные, константы
WORDS = 5

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

words = {}
answers = {}
right_answered_words = []
wrong_answered_words = []

user_input = None # или user_input = ""
edited_user_input = None # или user_input = ""
letter_unneeded = "ё"
letter_needed = "е"
dict_name = "words"
correct = "Правильно отвечены слова: "
incorrect = "Неправильно отвечены слова: "
amount_right_answered_words = 0

# words = words_easy
# print(words_easy)
# print(words)

# Получить у пользователя уровень сложности
print("Выберите уровень сложности: легкий, средний, сложный.\n")
user_input = input().lower()

if letter_unneeded in user_input:
    edited_user_input = user_input.replace(letter_unneeded, letter_needed)

# Положить в словарь words один из словарей в зависимости полученного от пользователя уровня сложности
for level_en, level_ru in levels_for_select.items():
        if edited_user_input == level_ru:
            words = (f"{dict_name}_{level_en}")
            print(f"\nСловарь с учётом уровня сложности:\n{words}")
            print(f"Тут я хочу напечатать весь словарь {words}")
            print(words) # а словарь не печатается, печатается только название словаря, потому что words - это str
            break
        else:
            pass
            # user_input = input("\nТакого уровня не существует.\nВыберите уровень сложности из следующих: лёгкий, средний, сложный.\n").lower()


user_input = input(f"\nВыбран уровень сложности {level_ru}, мы предложим {WORDS} слов, подберите перевод.\nНажмите Enter.")


# Запустить цикл по пяти словам из словаря words
for word, translation in words_easy.items(): # заменить words_easy на words когда разберусь как в words положить словарь words_easy
# Получить у пользователя ответ
    user_input = input(f"{word}, {len(word)} букв, начинается на {translation[0]}: ")
    print(user_input)
    if user_input.lower() == translation:
# Записать результат в answers
        answers[word] = True
        print(f"Верно, {word.title()} — это {translation}.")
    else:
        answers[word] = False
        print(f"Неверно, {word.title()} — это {translation}.")

print("\nПечатаю словарь с ответами")
print(answers)


# Когда слова закончились, вывести в зависимости от результата правильно и неправильно отвеченные слова
for key, value in answers.items():
        if value == True:
            right_answered_words.append(key)
        else:
            wrong_answered_words.append(key)

print(f"\n{correct}:")#{right_answered_words}
# print(right_answered_words)

for i in range(len(right_answered_words)):
    print(right_answered_words[i])


print(f"\n{incorrect}:")#{wrong_answered_words}
# print(wrong_answered_words)

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
        print(f"Ваш ранг: {level}.")
