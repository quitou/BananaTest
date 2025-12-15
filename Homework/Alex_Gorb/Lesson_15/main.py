import pymysql
import pymysql.cursors

"""
Все действия с базой данных из прошлого домашнего задания напишите с помощью Python.
При получении данных, распечатывайте эти данные.
"""

# Подключение к базе данных
db = pymysql.connect(
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    user='st4',
    password='your_aiven_password_here',
    database='st-onl',
    charset='utf8mb4'
)

cursor = db.cursor(pymysql.cursors.DictCursor)

try:
    # 1. Создаём студента
    cursor.execute(
        "INSERT INTO students (name, second_name) VALUES (%s, %s)",
        ('Hermione', 'Granger')
    )
    student_id = cursor.lastrowid
    db.commit()
    print(f"Создан студент с ID: {student_id}")

    # 2. Создаём группу и привязываем студента
    cursor.execute(
        "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)",
        ('Gryffindor', '1st of September', '30th of June')
    )
    group_id = cursor.lastrowid
    cursor.execute(
        "UPDATE students SET group_id = %s WHERE id = %s",
        (group_id, student_id)
    )
    db.commit()
    print(f"Создана группа с ID: {group_id}, студент привязан к группе")

    # 3. Вставляем предметы и получаем их ID
    subjects = [
        'Ancient Runes',
        'Arithmancy',
        'Potions',
        'Transfiguration',
        'Magical Law',
        'Defence Against the Dark Arts'
    ]

    insert_subject_query = "INSERT INTO subjets (title) VALUES (%s)"
    subject_ids = []
    for title in subjects:
        cursor.execute(insert_subject_query, (title,))
        subject_ids.append(cursor.lastrowid)
    db.commit()
    print(f"Созданы предметы с ID: {subject_ids}")

    # 4. Создаём занятия (lessons), привязывая к subject_id
    lessons_data = [
        ('Monday 10.00', subject_ids[0]),
        ('Tuesday 11.00', subject_ids[0]),
        ('Monday 11.00', subject_ids[1]),
        ('Friday 11.00', subject_ids[1]),
        ('Monday 12.00', subject_ids[2]),
        ('Sunday 10.00', subject_ids[2]),
        ('Monday 12.00', subject_ids[3]),
        ('Tuesday 12.00', subject_ids[3]),
        ('Tuesday 13.00', subject_ids[4]),
        ('Friday 12.00', subject_ids[4]),
        ('Monday 13.00', subject_ids[5]),
        ('Sunday 12.00', subject_ids[5]),
    ]

    cursor.executemany(
        "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)",
        lessons_data
    )
    db.commit()
    print("Созданы занятия")

    # 5. Добавляем книги для студента
    books = [
        ('Travovedenye', student_id),
        ('Zahita ot temnix iscustv', student_id),
        ('osnovi magic', student_id),
        ('history magic', student_id),
        ('arhimagia', student_id)
    ]

    cursor.executemany(
        "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)",
        books
    )
    db.commit()
    print("Добавлены книги")

    # 6. Добавляем оценки — по одной на каждое занятие
    # Получим ID всех созданных занятий (последние 12 записей)
    # Но лучше — вставить и сразу получить их ID. Однако, так как мы не сохраняли,
    # и если в таблице нет других записей, можно запросить:
    cursor.execute(
        "SELECT id FROM lessons WHERE subject_id IN %s ORDER BY id",
        (tuple(subject_ids),)
    )
    lesson_ids = [row['id'] for row in cursor.fetchall()]

    if len(lesson_ids) != 12:
        raise RuntimeError(f"Ожидалось 12 занятий, получено: {len(lesson_ids)}")

    # Генерируем оценки (Hermione почти всё на "Outstanding")
    marks_values = [
        'Outstanding', 'Outstanding',
        'Exceeds Expectations', 'Outstanding',
        'Exceeds Expectations', 'Outstanding',
        'Outstanding', 'Outstanding',
        'Exceeds Expectations', 'Outstanding',
        'Outstanding', 'Exceeds Expectations'
    ]

    marks_data = [
        (value, lesson_id, student_id)
        for value, lesson_id in zip(marks_values, lesson_ids)
    ]

    cursor.executemany(
        "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)",
        marks_data
    )
    db.commit()
    print("Добавлены оценки")

    # 7. Запросы на получение данных

    # Все оценки студента
    cursor.execute("SELECT * FROM marks WHERE student_id = %s", (student_id,))
    print("\nОценки студента:")
    print(cursor.fetchall())

    # Все книги студента
    cursor.execute("SELECT title FROM books WHERE taken_by_student_id = %s", (student_id,))
    print("\nКниги студента:")
    print(cursor.fetchall())

    # Полная информация через JOIN
    select_query = '''
    SELECT 
        students.name,
        students.second_name,
        `groups`.title AS group_name,
        books.title AS book_title,
        marks.value AS mark,
        lessons.title AS lesson_time,
        subjets.title AS subject_name
    FROM students
    JOIN `groups` ON students.group_id = groups.id
    JOIN books ON students.id = books.taken_by_student_id
    JOIN marks ON students.id = marks.student_id
    JOIN lessons ON marks.lesson_id = lessons.id
    JOIN subjets ON lessons.subject_id = subjets.id
    WHERE students.id = %s
    '''

    cursor.execute(select_query, (student_id,))
    results = cursor.fetchall()
    print("\nПолная информация о студенте:")
    for row in results:
        print(row)

except Exception as e:
    db.rollback()
    print(f"Произошла ошибка: {e}")
    raise
finally:
    cursor.close()
    db.close()
    print("\nСоединение с базой данных закрыто.")