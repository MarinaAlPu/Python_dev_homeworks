import os
from random import shuffle

from data_questions.questions_manager import load_data, get_statistics


DATA_SOURCE_QUESTIONS = os.path.join("data_questions/questions.json")


questions_list = load_data(DATA_SOURCE_QUESTIONS)
shuffle(questions_list)
print(questions_list)
# print(type(questions_list))

print("Игра начинается!")

# Получить ответ пользователя, прокомментировать ответ, записать ответ в соответствующее поле экземпляра класса Question
for question in questions_list:
    user_answer = input(f"{question.build_question}\n")
    question.user_answer = user_answer # в поле user_answer записываем ответ пользователя
    print(question.build_feedback(), "\n")

# Получить статистику
print(get_statistics(questions_list))
