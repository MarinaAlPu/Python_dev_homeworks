from functions import *


# Получить ввод номера студентао от пользователя
student_input = int(input("Введите номер студента\n"))

# Проверить существование такого пользователя
students_list = load_students(DATA_SOURCE_STUDENTS)
print(students_list, '\n', type(students_list))

for i in range(len(students_list)):
    if students_list[i]["pk"] == student_input:
        student_info = get_student_by_pk(student_input, DATA_SOURCE_STUDENTS)
        student_name = student_info["full_name"]
    # else:
    #     print("У нас нет такого студента")
    #     quit()

#
# for student in students_list:
#     if student_input in student["pk"]:
#         student_info = get_student_by_pk(student_input, DATA_SOURCE_STUDENTS)
#         print(student_info)
#         student_name = student_info["full_name"]
#         # break
#     else:
#         print(f"если нет студента: student_input, type(student_input)")
#         print("У нас нет такого студента")
#         quit()


# Получить ввод названия профессии от пользователя
profession_input = input(f"Выберите специальность для оценки студента {student_name}\n").title()

# Проверить существование такой профессии
professions_list = load_professions(DATA_SOURCE_PROFESSIONS)
print(professions_list, '\n', type(professions_list))

for i in range(len(professions_list)):
    if professions_list[i]["title"] == profession_input:
        profession_info = get_profession_by_title(profession_input, DATA_SOURCE_PROFESSIONS)
        print(profession_info, type(profession_info))

#
# for profession in professions_list:
#     if profession["title"] == profession_input:
#         profession_info = get_profession_by_title(profession_input, DATA_SOURCE_PROFESSIONS)
#         print(profession_info, type(profession_info))


        check_fitness_dict = check_fitness(student_input, profession_input)
        print(f"Пригодность {check_fitness_dict['fit_percent']}\n"
              f"{student_name} знает {', '.join(check_fitness_dict['has'])}\n"
              f"{student_name} не знает {', '.join(check_fitness_dict['lacks'])}")
        # break
    # else:
    #     print(profession["title"])
    #     print(profession_input.title())
    #     print("У нас нет такой специальности")
    #     # quit()
