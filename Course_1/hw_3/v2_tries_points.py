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
'''


questions = ["My name ___ Vova.", "I ___ a coder.", "I live ___ Moscow.", "How much ___ the fish?",\
             "The sky ___ blue.", "I ___ a dog.", "My dog ___ many toys.", "My dog ___ grey.",\
             "His name ___ Charlie.", "I ___ snow.", "I ___ to sleep.", "What ___ your name?",\
             "The sun ___ shining.", "The weather ___ good.", "I ___ my homework.", "I ___ snowboard."] 
answers = ["is", "am", "in", "is", "is", "have", "has", "is", "is", "like", "like", "is", "is", "is", "do", "have"]

correct_answers = 0
percent_of_correct_answers = 0
last_digit_in_correct_answers = 0
morthy_answers = None
morthy_points = None
morthy_percents = None


user_input = input('Привет!\nПредлагаю проверить свои знания английского!\nНаберите "ready", чтобы начать! ')

if user_input != "ready":
    print('Кажется, вы не хотите играть. Очень жаль')
else:
    for index_of_question in range(len(questions)):
        user_answer = input(f'{questions[index_of_question]} ')
        if user_answer != answers[index_of_question]:
            print(f'Неправильно. Правильный ответ: {answers[index_of_question]}')
        else:
            print('Ответ верный!')
            correct_answers += 1


    last_digit_in_correct_answers = correct_answers % 10

    if 11 <= correct_answers <= 19:
        morthy_answers = "вопросов"
    elif last_digit_in_correct_answers == 1:
        morthy_answers = "вопрос"
    elif last_digit_in_correct_answers in [2, 3, 4]:
        morthy_answers = "вопроса"
    else:
        morthy_answers = "вопросов"


    percent_of_correct_answers = round((correct_answers / len(questions)) * 100)

    if 11 <= percent_of_correct_answers <= 19:
        morthy_percents = "процентов"
    elif percent_of_correct_answers == 1:
        morthy_percents = "процент"
    elif percent_of_correct_answers in [2, 3, 4]:
        morthy_percents = "процента"
    else:
        morthy_percents = "процентов"


    print(f"\nВот и все!\nВы ответили на {correct_answers} {morthy_answers} из {len(questions)} верно.\
          \nЭто {percent_of_correct_answers} {morthy_percents}")
