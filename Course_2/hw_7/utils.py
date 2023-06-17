import json


def load_students():
    """
    Загружает список студентов из файла
    """
    with open('students.json') as students:
        students_data = students.read()
        students_data_list = json.loads(students_data)
        students_list = []
        for i in range(len(students_data_list)):
            students_list.append(students_data_list[i]["pk"])
        return students_data_list, students_list


def load_professions():
    """
    Загружает список профессий из файла
    """
    with open('professions.json') as professions:
        professions_data = professions.read()
        professions_data_list = json.loads(professions_data)
        professions_list = []
        for i in range(len(professions_data_list)):
            professions_list.append(professions_data_list[i]["title"])
        return professions_data_list, professions_list


def get_student_by_pk(pk):
    """
    Получает словарь с данными студента по его pk
    """
    with open('students.json') as students:
        students_data = students.read()
        students_data_list = json.loads(students_data)
        for i in range(len(students_data_list)):
            if pk == students_data_list[i]["pk"]:
                return students_data_list[i]


def get_profession_by_title(title):
    """
    Получает словарь с информацией о профессии по названию
    """
    with open('professions.json') as professions:
        professions_data = professions.read()
        professions_data_list = json.loads(professions_data)
        for i in range(len(professions_data_list)):
            if title.title() == professions_data_list[i]["title"]:
                return professions_data_list[i]


def check_fitness(student, profession):
    """
    Получив студента и профессию, возвращала бы словарь типа:
    {
    "has": ["Python", "Linux"], # есть у студента
    "lacks": ["Docker, SQL"], # не хватает у студента
    "fit_percent": 50 # пригодность студента
    }
    """
    student_data_dict = get_student_by_pk(student)
    student_skills_list = student_data_dict["skills"]
    student_skills = set(student_skills_list)

    profession_data_dict = get_profession_by_title(profession)
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


# Получить ввод номера студентао от пользователя
student_input = input("Введите номер студента\n")

# Проверить существование такого пользователя
students_data_list, students_list = load_students()
if int(student_input) in students_list:
    student_info = get_student_by_pk(int(student_input))
    student_name = student_info['full_name']
else:
    print("У нас нет такого студента")
    quit()


# Получить ввод названия профессии от пользователя
profession_input = input(f"Выберите специальность для оценки студента {student_name}\n")

# Проверить существование такой профессии
professions_data_list, professions_list = load_professions()
if profession_input.title() in professions_list:
    profession_info = get_profession_by_title(profession_input.title())
    check_fitness_dict = check_fitness(int(student_input), profession_input)
    print(f"Пригодность {check_fitness_dict['fit_percent']}\n"
          f"{student_name} знает {', '.join(check_fitness_dict['has'])}\n"
          f"{student_name} не знает {', '.join(check_fitness_dict['lacks'])}")
else:
    print("У нас нет такой специальности")
    quit()
