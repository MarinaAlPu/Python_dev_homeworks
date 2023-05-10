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

# Списки вопросов, ответов, слов и окончаний
questions = ["My name ___ Vova.", "I ___ a coder.", "I live ___ Moscow.", "How much ___ the fish?",\
             "The sky ___ blue.", "I ___ a dog.", "My dog ___ many toys.", "My dog ___ grey.",\
             "His name ___ Charlie.", "I ___ snow.", "I ___ to sleep.", "What ___ your name?",\
             "The sun ___ shining.", "The weather ___ good.", "I ___ my homework.", "I ___ snowboard."] 
answers = ["is", "am", "in", "is", "is", "have", "has", "is", "is", "like", "like", "is", "is", "is", "do", "have"]
words = ["вопрос", "балл", "процент"]
endinds = ["ов", "", "а", "ов"]
last_digits = []
quantity = []
morthy = []

# Переменные
POINTS_PER_ANSWER_1 = 3
POINTS_PER_ANSWER_2 = 2
POINTS_PER_ANSWER_3 = 1
tries_to_answer_left = 3
current_try = 0
correct_answers = 0
points_total = 0
last_digit_in_points_total = 0
percent_of_correct_answers = 0
last_digit_in_correct_answers = 0
morthy_answers = None
morthy_points = None
morthy_percents = None

# Программа здоровается и предлагает начать
user_input = input('Привет!\nПредлагаю проверить свои знания английского!\nНаберите "ready", чтобы начать! ')

if user_input != "ready":
    print('Кажется, вы не хотите играть. Очень жаль')
else:

# Мы задали вопрос
    for index_of_question in range(len(questions)):
        print(f'\n{questions[index_of_question]} ')
        tries_to_answer_left = 3
        current_try = 0
# и запустили цикл с попытками.
        while tries_to_answer_left > 0:
# Внутри него пользователь вводит слово.
            user_answer = input()
            current_try += 1

# Если оно верное - цикл с попытками прерывается брейк.
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

# Если неверное
            else:
# уменьшаем счетчик количества попыток
                tries_to_answer_left -= 1
                
# если осталось 0 попыток
                if tries_to_answer_left == 0:
                    print(f'Увы, но нет. Верный ответ: {answers[index_of_question]}')
                else:
# выводим пользователю сообщение, сколько у него попыток осталось
                    print(f'Осталось попыток: {tries_to_answer_left}, попробуйте еще раз!')


# ПОДБОР КОРРЕКТНЫХ ОКОНЧАНИЙ
# Правильные ответы
    quantity.append(correct_answers)
    last_digit_in_correct_answers = correct_answers % 10
    last_digits.append(last_digit_in_correct_answers)

# Набранные баллы
    quantity.append(points_total)
    last_digit_in_points_total = points_total % 10    
    last_digits.append(last_digit_in_points_total)

# Проценты правильных ответов
    percent_of_correct_answers = round((correct_answers / len(questions)) * 100)
    quantity.append(percent_of_correct_answers)
    last_digit_in_percent_of_correct_answers = percent_of_correct_answers % 10 
    last_digits.append(last_digit_in_percent_of_correct_answers)


for i in range(len(quantity)):
    if 11 <= quantity[i] <= 19:
        morthy.append(words[i] + endinds[0])
    elif last_digits[i] == 1:
        morthy.append(words[i] + endinds[1])
    elif last_digits[i] in [2, 3, 4]:
        morthy.append(words[i] + endinds[2])
    else:
        morthy.append(words[i] + endinds[3])


# Финальный вывод 
    print(f"\nВот и все!\nВы ответили на {correct_answers} {morthy[0]} из {len(questions)} верно, вы набрали {points_total} {morthy[1]}.\
        \nЭто {percent_of_correct_answers} {morthy[2]}")
