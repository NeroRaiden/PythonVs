# # # Створіть функцію, яка приймає список, індекс початку сортування та індекс кінця сортування, і повертає список, у якому відсортовано лише ті елементи, які укладені між індексом початку сортування та індексом кінця сортування.

# # # У відповідь вернуть початковий список, але з відсортованою частиною!

# # # Зробити змінні для зручного виставлення індексів
# # # програма повинна тільки надрукувати список
# # # підпишіть коментарями як працює ваша функція
# # # довжина списку не більше 1000


# # # import random

# # # start_index = 0
# # # stop_index = 10

# # # random_list = [random.randint(0, 100) for i in range(15)]

# # # def sort_list(list, start_index, stop_index):
# # #     list[start_index:stop_index] = sorted(list[start_index:stop_index])
# # #     return list

# # # #tests
# # # print(random_list)
# # # print(sort_list(random_list, start_index, stop_index))
# # # # print(sort_list(random_list, 0, 5))


# # # a = [1,3,9,1,2,5,4,10,0]
# # # print(a[1:5])
# # # print(a[:2]+sorted(a[2:7])+a[7:])

# # # a[2:7] = sorted(a[2:7])
# # # print(a)



# # Given a dictionary of student grades, 
# # write a function that calculates the average grade for each student
# # and returns a dictionary that maps student names to 
# # their average grades.


# # grades = {
# #     'Alice': [100, 90, 80],
# #     'Bob': [60, 70, 80],
# #     'Charlie': [80, 80, 80],
# #     'Dave': [70, 70, 70],
# #     'Eve': [60, 60, 60],
# #     'Frank': [50, 50, 50],
# #     'Gina': [40, 40, 40],
# #     'Hannah': [30, 30, 30],
# #     'Igor': [20, 20, 20],
# #     'Jenny': [10, 10, 10]
# # Приклад:

# # average_grades = average_grades(grades)
# # print(average_grades)  # {'Alice': 90.0, 'Bob': 70.0, 'Charlie': 80.0}


# grades = {
#     'Alice': [100, 90, 80],
#     'Bob': [60, 70, 80],
#     'Charlie': [80, 80, 80],
#     'Dave': [70, 70, 70],
#     'Eve': [60, 60, 60],
#     'Frank': [50, 50, 50],
#     'Gina': [40, 90, 40],
#     'Hannah': [30, 50, 100],
#     'Igor': [20, 20, 20],
#     'Jenny': [10, 10, 10]
#     }

# # print(list(grades.items()))

# def average_grades(some_grad):
#     average_grades = {}
#     for name, grade in some_grad.items():
#         average_grades[name] = sum(grade) / len(grade)
#     return average_grades

# print(average_grades(grades))





# Создать текстовые файлы с вариантами ответов на типичные фразы и вопросы:
# К примеру^
# Привет
# Как дела?
# Какая погода за окном?
# Как тебя зовут?
# Сколько тебе дней?
# Который час?
# и тд..
# далее написать функционала для бота
# который позволит при получении такого вопроса 
# от пользователя рандомно извлечь из 
# нужного файла ответ и в сообщении ответить пользователю.

# Вариативность должна быть не менее 5и разных ответов на один вопрос!

folder_answers = 'lesson23/answers'


