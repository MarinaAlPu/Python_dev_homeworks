import json, os

DATA_SOURCE_STUDENTS = os.path.join('students.json')
DATA_SOURCE_PROFESSIONS = os.path.join('professions.json')

# no_student_string = "У нас нет такого студента"
# no_profession_string = "У нас нет такой профессии"


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


def get_student_by_pk(pk: int, DATA_SOURCE_STUDENTS: str) -> dict:
    """
    Получает словарь с данными студента по его pk
    """
    students_data_list = load_students(DATA_SOURCE_STUDENTS)
    for student in students_data_list:
        if student["pk"] == pk:
            return student


def get_profession_by_title(title: str, DATA_SOURCE_PROFESSIONS: str) -> dict:
    """
    Получает словарь с информацией о профессии по названию
    """
    professions_data_list = load_professions(DATA_SOURCE_PROFESSIONS)
    for profession in professions_data_list:
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
    student_data_dict = get_student_by_pk(student, DATA_SOURCE_STUDENTS)
    student_skills_list = student_data_dict["skills"]
    student_skills = set(student_skills_list)

    profession_data_dict = get_profession_by_title(profession, DATA_SOURCE_PROFESSIONS)
    profession_skills_list = profession_data_dict["skills"]
    profession_skills = set(profession_skills_list)

    skills_to_check_fitness = student_skills.intersection(profession_skills)
    skills_to_check_fitness_list = list(skills_to_check_fitness)

    profession_skills_quantity = len(profession_skills_list)
    skills_to_check_fitness_quantity = len(skills_to_check_fitness_list)
    fit_percent_int = int((skills_to_check_fitness_quantity / profession_skills_quantity) * 100)
    fit_percent = (f"{fit_percent_int}%")

    student_skills_lacks = list(profession_skills.difference(student_skills))

    check_fitness_dict = {}
    check_fitness_dict["has"] = student_skills_list
    check_fitness_dict["lacks"] = student_skills_lacks
    check_fitness_dict["fit_percent"] = fit_percent

    return check_fitness_dict
