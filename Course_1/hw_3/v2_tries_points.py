'''
1. Программа здоровается и предлагает начать.
2. Если пользователь набрал `"ready"` — программа начинает задавать вопросы.
   Если нет – программа завершается.
3. Когда первый вопрос задан, приложение ждет ввод пользователя.
   Если ответ правильный, приложение говорит: `Ответ верный!`
   Если нет, говорит: `Неправильно. Правильный ответ: ______.`
4. Затем приложение задает следующий вопрос.
5. После ответа на  все вопросы приложение говорит:
`Вот и все! Вы ответили на ___ вопросов из ___ верно, это ____ процентов.`

Дорабатываем:
Если ответ правильный, приложение говорит: `Ответ верный!`
Если ответ неверный, приложение говорит: `Осталось попыток: 2, попробуйте еще раз!`
Если ответ опять неверный, говорит: `Осталось попыток: 1, попробуйте еще раз!`
Если еще раз вводится неправильный ответ, то приложение говорит: 
`Увы, но нет. Верный ответ: ____________`
За каждый ответ начисляются баллы.
Если с первой попытки введен правильный ответ — 3 балла, со второй — 2, с третьей — 1.
После ответа на все вопросы приложение говорит:
`Вот и все! Вы ответили на ___ вопросов из ___ верно, вы набрали ___ баллов.`
'''

# Списки вопросов и ответов
questions = ["My name ___ Vova.", "I ___ a coder.", "I live ___ Moscow.", "How much ___ the fish?",\
             "The sky ___ blue.", "I ___ a dog.", "My dog ___ many toys.", "My dog ___ grey.",\
             "His name ___ Charlie.", "I ___ snow.", "I ___ to sleep.", "What ___ your name?",\
             "The sun ___ shining.", "The weather ___ good.", "I ___ my homework.", "I ___ snowboard."] 
answers = ["is", "am", "in", "is", "is", "have", "has", "is", "is", "like", "like", "is", "is", "is", "do", "have"]

# Константы и переменные
POINTS_PER_ANSWER_1 = 3
POINTS_PER_ANSWER_2 = 2
POINTS_PER_ANSWER_3 = 1
tries_to_answer_left = 0
current_try = 0
correct_answers = 0
points_total = 0
last_digit_in_points_total = 0
percent_of_correct_answers = 0
last_digit_in_correct_answers = 0
morthy_answers = None
morthy_points = None
morthy_percents = None


# Поздароваться и предложить начать
user_input = input('Привет!\nПредлагаю проверить свои знания английского!\nНаберите "ready", чтобы начать! ')

if user_input != "ready":
    print('Кажется, вы не хотите играть. Очень жаль')
else:

# Запустить цикл с задаванием вопросов
    for index_of_question in range(len(questions)):
        print(f'\n{questions[index_of_question]} ')
        tries_to_answer_left = 3
        current_try = 0

# Запустить цикл с попытками
        while tries_to_answer_left > 0:
# Получить ответ пользователя
            user_answer = input()
            current_try += 1

# Если ответ верный
            if user_answer == answers[index_of_question]:
                print('Ответ верный!')
                correct_answers += 1
                if current_try == 1:
                    points_total += POINTS_PER_ANSWER_1
                elif current_try == 2:
                    points_total += POINTS_PER_ANSWER_2
                elif current_try == 3:
                    points_total += POINTS_PER_ANSWER_3
                break

# Если ответ неверный
            else:
# Уменьшить счётчик количества попыток
                tries_to_answer_left -= 1
                if tries_to_answer_left == 0:
                    print(f'Увы, но нет. Верный ответ: {answers[index_of_question]}')
                else:
# Вывести пользователю сообщение о количестве оставшихся попыток
                    print(f'Осталось попыток: {tries_to_answer_left}, попробуйте еще раз!')


# ПОДБОР КОРРЕКТНЫХ ОКОНЧАНИЙ
# Количество правильных ответов
    last_digit_in_correct_answers = correct_answers % 10

    if 11 <= correct_answers <= 19:
        morthy_answers = "вопросов"
    elif last_digit_in_correct_answers == 1:
        morthy_answers = "вопрос"
    elif last_digit_in_correct_answers in [2, 3, 4]:
        morthy_answers = "вопроса"
    else:
        morthy_answers = "вопросов"

# Количество набранных баллов
    last_digit_in_points_total = points_total % 10

    if 11 <= last_digit_in_points_total <= 19:
        morthy_points = "баллов"
    elif last_digit_in_points_total == 1:
        morthy_points = "балл"
    elif last_digit_in_points_total in [2, 3, 4]:
        morthy_points = "балла"
    else:
        morthy_points = "баллов"

# Процент правильных ответов
    percent_of_correct_answers = round((correct_answers / len(questions)) * 100)

    if 11 <= percent_of_correct_answers <= 19:
        morthy_percents = "процентов"
    elif percent_of_correct_answers == 1:
        morthy_percents = "процент"
    elif percent_of_correct_answers in [2, 3, 4]:
        morthy_percents = "процента"
    else:
        morthy_percents = "процентов"


# Финальный вывод 
    print(f"\nВот и все!\nВы ответили на {correct_answers} {morthy_answers} из {len(questions)} верно, вы набрали {points_total} {morthy_points}.\
          \nЭто {percent_of_correct_answers} {morthy_percents}")
