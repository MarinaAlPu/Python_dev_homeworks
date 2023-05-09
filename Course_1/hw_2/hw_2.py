number_of_questions = 3
correct_answers = 0
points_per_correct_answer = 10
points_scored = 0
percent_of_correct_answers = 0
last_digit_in_correct_answers = 0
morthy_answers = None
morthy_points = None

question_1 = "My name ___ Vova. "
answer_1 = "is"
question_2 = "I ___ a coder. "
answer_2 = "am"
question_3 = "I live ___ Moscow. "
answer_3 = "in"


user_name = input("Привет!\nПредлагаю проверить свои знания английского!\nРасскажи, как тебя зовут! ")

print(f"\nПривет, {user_name}, начинаем тренировку!\n")


user_answer_1 = input(question_1)

if user_answer_1 == answer_1:
    correct_answers += 1
    points_scored += points_per_correct_answer
    print(f"Ответ верный!\nВы получаете {points_per_correct_answer} баллов!")
else:
    print(f"Неправильно.\nПравильный ответ: {answer_1}")


user_answer_2 = input(question_2)

if user_answer_2 == answer_2:
    correct_answers += 1
    points_scored += points_per_correct_answer
    print(f"Ответ верный!\nВы получаете {points_per_correct_answer} баллов!")
else:
    print(f"Неправильно.\nПравильный ответ: {answer_2}")


user_answer_3 = input(question_3)

if user_answer_3 == answer_3:
    correct_answers += 1
    points_scored += points_per_correct_answer
    print(f"Ответ верный!\nВы получаете {points_per_correct_answer} баллов!")
else:
    print(f"Неправильно.\nПравильный ответ: {answer_3}")


fracture_of_correct_answers = correct_answers / number_of_questions

if 0 < fracture_of_correct_answers < 1:
    percent_of_correct_answers = round(((fracture_of_correct_answers) * 100), 2)
else:
    percent_of_correct_answers = int((fracture_of_correct_answers) * 100)

last_digit_in_correct_answers = correct_answers % 10

if last_digit_in_correct_answers == 1:
    morthy_answers = "вопрос"
elif last_digit_in_correct_answers == 2 or last_digit_in_correct_answers == 3:
    morthy_answers = "вопроса"


if type(percent_of_correct_answers) == float:
    morthy_percents = "процента"
else:
    morthy_percents = "процентов"


print(f"\nВот и все, {user_name}!\nВы ответили на {correct_answers} {morthy_answers} из {number_of_questions} верно.\
      \nВы заработали {points_scored} баллов.\nЭто {percent_of_correct_answers} {morthy_percents}")
