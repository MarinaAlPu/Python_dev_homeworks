import json
import requests

from data_questions.questions_class import Question


def load_data(path) -> list:
    """Создаёт список экземпляров класса Question"""
    with open(path) as file:
        data = json.load(file)
        questions = []
        for q in data:
            question = Question(q["q"], q["d"], q["a"])
            questions.append(question)
        return questions

def load_data_json(path) -> list:
    """Загружает данные с сайта. Создаёт список экземпляров класса Question"""
    resp = requests.get(path)
    data = resp.json()

    questions = []
    for q in data:
        question = Question(q["q"], q["d"], q["a"])
        questions.append(question)
    return questions

def get_statistics(questions):
    """Выводит статистику"""
    points = 0
    count_answers = 0
    for question in questions:
        if question.is_correct():
            points += question.points
            count_answers += 1
    return f"Вот и всё!\nОтвечено {count_answers} вопроса из {len(questions)}\nНабрано баллов: {points}"
