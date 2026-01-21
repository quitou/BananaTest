import csv
import os
import dotenv
import pymysql
import pymysql.cursors

dotenv.load_dotenv()
''' TODO:
В папке /homework/eugene_okulik/Lesson_19/hw_data
лежит csv файл. Файл никуда не копируйте и не переносите.
Прочитайте этот файл с помощью модуля csv и проверьте есть ли те данные,
которые там перечислены, в нашей базе данных.'''

current_path = os.path.dirname(__file__)
root_path = os.path.dirname(os.path.dirname(current_path))
file_path = os.path.join(root_path, 'eugene_okulik', 'Lesson_19', 'hw_data', 'db_data.csv')


with open(file_path, newline='') as data_csv_file:
    file_data = csv.DictReader(data_csv_file)
    data = []
    for row in file_data:
        data.append(row)

print(data)


'''
При подключении к базе данных не прописывайте данные подключения в коде,
а воспользуйтесь подходом .env c такими переменными:
DB_USER,
DB_PASSW,
DB_HOST,
DB_PORT,
DB_NAME.
Я на своем компе уже настроил этим переменные, так что, если все сделаем одинаковые названия,
будет работать всё универсально'''

db = pymysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')

)

cursor = db.cursor(pymysql.cursors.DictCursor)

'''
    В результате сравнения, если обнаружится, что каких-то данных, которые есть в файле, нет в базе данных,
    распечатайте строки csv файла, данные из которых не были найдены.
    '''

for line in data:
    fname = line['name']
    lname = line['second_name']
    group = line['group_title']
    book = line['book_title']
    subject = line['subject_title']
    lesson = line['lesson_title']
    grade = line['mark_value']

    name_chek_query = "SELECT * FROM students WHERE name = %s and second_name = %s"
    cursor.execute(name_chek_query, (fname,lname))
    name_request = cursor.fetchall()
    try:
        student_name = name_request[0]['name']
        student_lname = name_request[0]['second_name']
    except IndexError:
        print(f' Not found: {fname}, {lname} in BD!')
        continue

    group_chek_query = "SELECT * FROM groups WHERE id = %s"
    user_group_id = name_request[0]['group_id']
    cursor.execute(group_chek_query, [user_group_id])
    group_request = cursor.fetchall()
    try:
        group_name = group_request[0]['title']
    except IndexError:
        print(f' Not found:  {group} in BD!')
        continue

    book_chek_query = "SELECT * FROM book WHERE title = %s and taken_by_student_id = %s"
    student_id = name_request[0]['id']
    cursor.execute(book_chek_query,(book, student_id))
    book_request = cursor.fetchall()
    try:
        book_name = book_request[0]['book_title']
    except IndexError:
        print(f' Not found:  {book} in BD!')
        continue

    subject_chek_query = "SELECT * FROM subjects WHERE subject_title = %s"
    cursor.execute(subject_chek_query, (subject))
    subject_request = cursor.fetchall()
    try:
        subject_name = subject_request[0]['subject_title']
    except IndexError:
        print(f' Not found:  {subject} in BD!')
        continue

    lesson_chek_query = "SELECT * FROM lesson WHERE title = %s and subject_id = %s"
    subject_id = subject_request[0]['id']
    cursor.execute(lesson_chek_query, (lesson, subject_id))
    lesson_request = cursor.fetchall()
    try:
        lesson_name = lesson_request[0]['lesson_title']
    except IndexError:
        print(f' Not found:  {lesson} in BD!')
        continue

    grade_chek_query = "SELECT * FROM marks WHERE value = %s and lesson_id = %s and student_id = %s"
    student_id = name_request[0]['id']
    lesson_id = lesson_request[0]['id']
    cursor.execute(grade_chek_query, (grade,lesson_id, student_id))
    grade_request = cursor.fetchall()
    try:
        grade_name = grade_request[0]['value']
    except IndexError:
        print(f' Not found:  {grade} in BD!')
        continue

