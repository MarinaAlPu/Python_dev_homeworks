import json


def load_students(DATA_SOURCE_STUDENTS: str) -> list:
    """
    Загружает список карточек студентов из файла
    """
    students = open(DATA_SOURCE_STUDENTS)
    students_data = json.load(students)
    return students_data


def load_professions(DATA_SOURCE_PROFESSIONS: str) -> list:
    """
    Загружает список карточек профессий из файла
    """
    professions = open(DATA_SOURCE_PROFESSIONS)
    professions_data = json.load(professions)
    return professions_data


def get_student_by_pk(pk: int, students_list: list) -> dict:
    """
    Получает словарь с данными студента по его pk
    """
    for student in students_list:
        if student["pk"] == pk:
            return student


def get_profession_by_title(title: str, professions_list: list) -> dict:
    """
    Получает словарь с информацией о профессии по названию
    """
    for profession in professions_list:
        if profession["title"] == title.title():
            return profession


def check_fitness(student: dict, profession: dict) -> dict:
    """
    Получив студента и профессию, возвращала бы словарь типа:
    {
    "has": ["Python", "Linux"], # есть у студента
    "lacks": ["Docker, SQL"], # не хватает у студента
    "fit_percent": 50 # пригодность студента
    }
    """
    student_skills_list = student["skills"]
    student_skills = set(student_skills_list)

    profession_skills_list = profession["skills"]
    profession_skills = set(profession_skills_list)

    skills_to_check_fitness = student_skills.intersection(profession_skills)
    skills_to_check_fitness_list = list(skills_to_check_fitness)

    profession_skills_quantity = len(profession_skills_list)
    skills_to_check_fitness_quantity = len(skills_to_check_fitness_list)
    fit_percent_int = int(
        (skills_to_check_fitness_quantity / profession_skills_quantity) * 100
        )
    fit_percent = f"{fit_percent_int}%"

    student_skills_lacks = list(profession_skills.difference(student_skills))

    check_fitness_dict = {}
    check_fitness_dict["has"] = student_skills_list
    check_fitness_dict["lacks"] = student_skills_lacks
    check_fitness_dict["fit_percent"] = fit_percent

    return check_fitness_dict
