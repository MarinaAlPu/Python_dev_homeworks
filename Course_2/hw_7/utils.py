import functions
import os


DATA_SOURCE_STUDENTS = os.path.join('students.json')
DATA_SOURCE_PROFESSIONS = os.path.join('professions.json')


# Получить ввод номера студента от пользователя
student_input = int(input("Введите номер студента\n"))

# Проверить существование такого студента
students_list = functions.load_students(DATA_SOURCE_STUDENTS)
student_info = functions.get_student_by_pk(student_input, students_list)

if student_info is None:
    print("У нас нет такого студента")
    quit()

student_name = student_info["full_name"]


# Получить ввод названия профессии от пользователя
profession_input = input(f"Выберите специальность для оценки студента {student_name}\n").title()

# Проверить существование такой профессии
professions_list = functions.load_professions(DATA_SOURCE_PROFESSIONS)
profession_info = functions.get_profession_by_title(profession_input, professions_list)

if profession_info is None:
    print("У нас нет такой профессии")
    quit()

# Проверить пригодность студента для выбранной профессии
check_fitness_dict = functions.check_fitness(student_info, profession_info)

print(f"Пригодность {check_fitness_dict['fit_percent']}\n"
        f"{student_name} знает {', '.join(check_fitness_dict['has'])}\n"
        f"{student_name} не знает {', '.join(check_fitness_dict['lacks'])}")
