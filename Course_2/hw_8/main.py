from random import shuffle

from data_questions.questions_manager import load_data_json, get_statistics

if __name__ == "__main__":
    PATH = "https://www.jsonkeeper.com/b/3L7X"

    # Получить список вопросов
    questions_list = load_data_json(PATH)
    shuffle(questions_list)

    print("Игра начинается!\n")

    # Получить ответ пользователя, прокомментировать ответ, записать ответ в соответствующее поле экземпляра класса Question
    for question in questions_list:
        question_for_user = question.build_question()
        user_answer = input(f"{question_for_user}\n")
        question.user_answer = user_answer # в поле user_answer записываем ответ пользователя
        print(question.build_feedback(), "\n")

    # Получить статистику
    statistics = get_statistics(questions_list)
    print(statistics)
