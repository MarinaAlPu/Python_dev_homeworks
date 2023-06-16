import json


def load_students():
    """
    Загружает список студентов из файла
    """
    with open('students.json') as students:
        students_data = students.read()
        students_data_list = json.loads(students_data)
        # print(students_data_list)

        students_list = []
        for i in range(len(students_data_list)):
            students_list.append(students_data_list[i]["pk"])
        # print(students_list)

        return students_data_list, students_list

# students_data_list, students_list = load_students()
# print(students_list)
# print(students_list[0])

def load_professions():
    """
    Загружает список профессий из файла
    """
    with open('professions.json') as professions:
        professions_data = professions.read()
        professions_data_list = json.loads(professions_data)
        # print(professions_data_list)

        professions_list = []
        for i in range(len(professions_data_list)):
            professions_list.append(professions_data_list[i]["title"])
        # print(professions_list)

        return professions_data_list, professions_list


def get_student_by_pk(pk):
    """
    Получает словарь с данными студента по его pk
    """
    # Вычитать из файла json и преобразовать в список
    with open('students.json') as students:
        students_data = students.read()
        students_data_list = json.loads(students_data)
        # print(students_data_list)
        # print(type(students_data_list))
        # По индексу в диапазоне, зависящем от длины списка, вычислить словарь с данными студента, чей pk был введён
        for i in range(len(students_data_list)):
            # print(type(students_data_list[i]))
            # Вернуть словарь с данными нужного студента
            if pk == students_data_list[i]["pk"]:
                # print(students_data_list[i])
                return students_data_list[i]


def get_profession_by_title(title):
    """
    Получает словарь с информацией о профессии по названию
    """

    with open('professions.json') as professions:
        professions_data = professions.read()
        professions_data_list = json.loads(professions_data)
        # print(type(professions_data_list))
        # print(professions_data_list)
        for i in range(len(professions_data_list)):
            if title.title() == professions_data_list[i]["title"]:
                # print(professions_data_list[i]["title"])
                return professions_data_list[i]


def check_fitness(student, profession):
    """
    Получив студента и профессию, возвращала бы словарь типа:
    {
    "has": ["Python", "Linux"], # есть у студента
    "lacks": ["Docker, SQL"], # не хватает у студента
    "fit_percent": 50 # пригодность студента
    }

    Эта функция должна использовать методы множеств
    """
    # По номеру студента получить словарь с данными студента
    student_data_dict = get_student_by_pk(student)
    print(f"Печатаю словарь с данными студента {student_data_dict}")

    # По номеру студента получить список скиллов студента
    student_skills_list = student_data_dict["skills"]

    # Преобразовать список в множество
    student_skills = set(student_skills_list)

    # По названию профессии получить словарь с данными профессии
    profession_data_dict = get_profession_by_title(profession)

    # По названию профессии получить список скиллов профессии
    profession_skills_list = profession_data_dict["skills"]

    # Преобразовать список в множество
    profession_skills = set(profession_skills_list)

    # Найти пересечение множеств скиллов студента и скиллов професии
    skills_to_check_fitness = student_skills.intersection(profession_skills)

    # Получить процент пригодности студента для профессии - какой процент от необходимых скиллов есть у студента
    ## Посчитать количество скиллов студента - НЕ НАДО

    ## Посчитать количество скиллов профессии
    profession_skills_quantity = len(profession_skills_list)

    ## Преобразовать множество пересекающихся скиллов в список
    skills_to_check_fitness_list = list(skills_to_check_fitness)

    ## Посчитать количество пересекающихся скиллов
    skills_to_check_fitness_quantity = len(skills_to_check_fitness_list)

    ## Посчитать долю пересекающихся скиллов от количества скиллов профессии
    fit_percent_int = int((skills_to_check_fitness_quantity / profession_skills_quantity) * 100)
    fit_percent = (f"{fit_percent_int}%")

    ## Посчитать количество скиллов профессии, которых нет у студента
    student_skills_lacks = list(profession_skills.difference(student_skills))
    print("Список скиллов, которых не хватает студенту:")
    print(student_skills_lacks)

    # Записать данные в словарь по форме:
    # {
    # "has": ["Python", "Linux"], # есть у студента
    # "lacks": ["Docker, SQL"], # не хватает у студента
    # "fit_percent": 50 # пригодность студента
    # }
    check_fitness_dict = {}
    check_fitness_dict["has"] = student_skills_list
    check_fitness_dict["lacks"] = student_skills_lacks
    check_fitness_dict["fit_percent"] = fit_percent

    # Вернуть полученный словарь
    return check_fitness_dict



# Получить ввод pk пользователя
student_input = input("Введите номер студента\n")

# Проверить существование такого пользователя
students_data_list, students_list = load_students()
print(students_data_list)
print(students_list)
# print(students_list[0])

# Если такой студент есть – выведите информацию о пользователе
if int(student_input) in students_list:
    print("This is a table")
    student_info = get_student_by_pk(int(student_input))
    print(student_info)
    student_name = student_info['full_name']

# Если такого студента нет - завершитесь
else:
    print("У нас нет такого студента")
    quit()


# Получить ввод title профессии
profession_input = input(f"Выберите специальность для оценки студента {student_name}\n")

# Проверить существование такой профессии
professions_data_list, professions_list = load_professions()
print(professions_data_list)
print(professions_list)
# print(professions_list[0])

# Если такая специальность есть – получите соответствие с помощью  check_fitness
if profession_input.title() in professions_list:
    print("London is the capital of Great Britain")
    profession_info = get_profession_by_title(profession_input.title())
    print(profession_info)

    check_fitness_dict = check_fitness(int(student_input), profession_input)
    print(f"Печатаю словарь с проверками {check_fitness_dict}")

    # Пригодность 50 %
    # Программа: Jane Snake знает Python, Linux
    # Программа: Jane Snake не знает Docker, SQL

    print(f"Пригодность {check_fitness_dict['fit_percent']} %\n"
          f"{student_name} знает {check_fitness_dict['has']}\n"
          f"{student_name} не знает {check_fitness_dict['lacks']}")


# Если такой специальности нет - завершитесь
else:
    print("У нас нет такой специальности")
    quit()







